#!/usr/bin/env python3
"""
Serve the browser study app and sync changes back to questions_master.csv.
"""

from __future__ import annotations

import argparse
import csv
import json
import socket
import threading
import webbrowser
from datetime import datetime
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from build_web_app import ROOT, MASTER_FILE, build_server_html


def load_questions() -> tuple[list[str], list[dict[str, str]]]:
    with MASTER_FILE.open("r", encoding="utf-8", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return reader.fieldnames or [], list(reader)


def save_questions(fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with MASTER_FILE.open("w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def update_question(payload: dict[str, str]) -> dict[str, str] | None:
    stable_id = str(payload.get("stable_id", "")).strip()
    if not stable_id:
        return None

    fieldnames, rows = load_questions()
    target = None
    for row in rows:
        if row["stable_id"] == stable_id:
            target = row
            break

    if target is None:
        return None

    last_practiced_supplied = "last_practiced" in payload

    for key in ("review_status", "answer_notes", "practice_count", "last_practiced"):
        if key in payload and payload[key] is not None:
            target[key] = str(payload[key])

    if not last_practiced_supplied and not target["last_practiced"].strip():
        target["last_practiced"] = datetime.now().strftime("%Y-%m-%d %H:%M")

    save_questions(fieldnames, rows)
    return target


class StudyHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self) -> None:
        if self.path in ("/", "/index.html"):
            html = build_server_html().encode("utf-8")
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(html)))
            self.end_headers()
            self.wfile.write(html)
            return
        super().do_GET()

    def do_POST(self) -> None:
        if self.path != "/api/update":
            self.send_error(HTTPStatus.NOT_FOUND, "Unknown endpoint")
            return

        content_length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(content_length)
        try:
            payload = json.loads(body.decode("utf-8"))
        except json.JSONDecodeError:
            self.send_error(HTTPStatus.BAD_REQUEST, "Invalid JSON")
            return

        updated = update_question(payload)
        if updated is None:
            self.send_error(HTTPStatus.NOT_FOUND, "Question not found")
            return

        response = json.dumps({"ok": True, "question": updated}, ensure_ascii=False).encode("utf-8")
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def log_message(self, format: str, *args) -> None:
        return


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Serve the HPDA browser study app")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind to")
    parser.add_argument("--port", type=int, default=8000, help="Port to serve on")
    parser.add_argument("--no-open", action="store_true", help="Do not auto-open the browser")
    return parser.parse_args()


def port_is_available(host: str, port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            sock.bind((host, port))
        except OSError:
            return False
    return True


def choose_port(host: str, requested_port: int) -> int:
    candidates = [requested_port]
    candidates.extend(range(requested_port + 1, requested_port + 11))
    for fallback in (8765, 8766, 8888, 9000):
        if fallback not in candidates:
            candidates.append(fallback)

    for port in candidates:
        if port_is_available(host, port):
            return port

    raise OSError("Could not find an available local port for the study server.")


def open_browser_later(url: str) -> None:
    try:
        webbrowser.open(url)
    except Exception:
        pass


def main() -> None:
    args = parse_args()
    selected_port = choose_port(args.host, args.port)
    server = ThreadingHTTPServer((args.host, selected_port), StudyHandler)
    url = f"http://{args.host}:{selected_port}"
    print(f"Serving study app on {url}")
    print(f"CSV sync target: {MASTER_FILE}")
    if selected_port != args.port:
        print(f"Requested port {args.port} was unavailable, so the server switched to {selected_port}.")
    if not args.no_open:
        threading.Timer(0.8, open_browser_later, args=[url]).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping study server.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
