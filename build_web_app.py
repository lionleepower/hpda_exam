#!/usr/bin/env python3
"""
Build a local HTML study app from the master question bank.
"""

from __future__ import annotations

import csv
import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MASTER_FILE = ROOT / "data" / "processed" / "questions_master.csv"
TOPIC_NOTE_FILE = ROOT / "data" / "processed" / "topic_notes.csv"
OUTPUT_DIR = ROOT / "output" / "web_app"
OUTPUT_FILE = OUTPUT_DIR / "index.html"
VISUAL_HINT_KEYWORDS = [
    "plot",
    "plots",
    "figure",
    "figures",
    "diagram",
    "table",
    "tables",
    "shown below",
    "show below",
    "below illustrate",
    "illustrates",
    "illustrate",
    "the following data sample",
    "example data",
    "scatterplot",
    "scatterplots",
    "graph",
    "graphs",
    "chart",
    "charts",
]


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as csvfile:
        return list(csv.DictReader(csvfile))


def relative_asset_path(path_text: str) -> str:
    if not path_text.strip():
        return ""
    path = ROOT / path_text
    return os.path.relpath(path, OUTPUT_DIR)


def prepare_questions(rows: list[dict[str, str]], for_server: bool) -> list[dict[str, str]]:
    questions: list[dict[str, str]] = []
    for row in rows:
        questions.append(
            {
                "stable_id": row["stable_id"],
                "topic_id": row["topic_id"],
                "topic_group": row["topic_group"],
                "knowledge_point": row["knowledge_point"],
                "year": row["year"],
                "exam_time": row["exam_time"],
                "question_number": row["question_number"],
                "question_summary": row["question_summary"],
                "topic_priority": row["topic_priority"],
                "review_status": row["review_status"],
                "practice_count": row["practice_count"],
                "last_practiced": row["last_practiced"],
                "source_pdf": row["source_pdf"] if for_server else relative_asset_path(row["source_pdf"]),
                "source_page": row["source_page"],
                "source_image": row["source_image"] if for_server else relative_asset_path(row["source_image"]),
                "original_question_text": row["original_question_text"],
                "answer_notes": row["answer_notes"],
            }
        )
    return questions


def prepare_topic_notes(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    notes: dict[str, list[str]] = {}
    for row in rows:
        notes.setdefault(row["topic_id"], []).append(row["note_text"])
    return notes


def render_html(questions: list[dict[str, str]], topic_notes: dict[str, list[str]], server_mode: bool) -> str:
    questions_json = json.dumps(questions, ensure_ascii=False)
    topic_notes_json = json.dumps(topic_notes, ensure_ascii=False)
    server_mode_json = "true" if server_mode else "false"

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>HPDA Final Exam Study App</title>
  <style>
    :root {{
      --bg: #f6f2e8;
      --panel: #fffaf1;
      --panel-strong: #fffdf8;
      --ink: #1f1b16;
      --muted: #6f6558;
      --line: #ddd2c2;
      --accent: #0e7490;
      --done: #2f855a;
      --review: #b83280;
      --shadow: 0 16px 40px rgba(48, 37, 24, 0.08);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      background:
        radial-gradient(circle at top left, rgba(14,116,144,0.12), transparent 28%),
        linear-gradient(180deg, #f3ede1 0%, var(--bg) 100%);
      color: var(--ink);
    }}
    .page {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 24px;
      display: grid;
      grid-template-columns: 360px minmax(0, 1fr);
      gap: 24px;
    }}
    .panel {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 20px;
      box-shadow: var(--shadow);
    }}
    .sidebar {{
      padding: 22px;
      position: sticky;
      top: 20px;
      align-self: start;
    }}
    .content {{
      padding: 22px;
      background: var(--panel-strong);
    }}
    h1 {{ margin: 0 0 10px; font-size: 2rem; line-height: 1.1; }}
    h2, h3 {{ margin: 0 0 12px; }}
    .lede {{ margin: 0 0 20px; color: var(--muted); line-height: 1.5; }}
    .grid {{ display: grid; gap: 14px; }}
    .field label {{ display: block; margin-bottom: 6px; font-size: 0.95rem; font-weight: 700; }}
    select, input, textarea, button {{ font: inherit; }}
    select, input[type="number"], textarea {{
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 10px 12px;
      background: white;
      color: var(--ink);
    }}
    textarea {{ min-height: 120px; resize: vertical; line-height: 1.45; }}
    .checkboxes {{ display: grid; gap: 8px; }}
    .checkboxes label {{ display: flex; gap: 10px; align-items: center; font-weight: 500; margin: 0; }}
    .buttons, .footer-actions, .nav-buttons {{ display: flex; flex-wrap: wrap; gap: 10px; }}
    button {{
      border: 0;
      border-radius: 999px;
      padding: 10px 16px;
      cursor: pointer;
      background: #ece2d2;
      color: var(--ink);
    }}
    button.primary {{ background: var(--accent); color: white; }}
    button.review {{ background: #f7d1ea; color: #7c2157; }}
    button.done {{ background: #d7f3df; color: #1f6a41; }}
    .stats {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin-bottom: 18px;
    }}
    .stat {{
      border: 1px solid var(--line);
      border-radius: 16px;
      padding: 12px;
      background: #fff;
    }}
    .stat .value {{ display: block; font-size: 1.5rem; font-weight: 700; }}
    .pill {{
      display: inline-flex;
      align-items: center;
      border-radius: 999px;
      padding: 6px 10px;
      font-size: 0.9rem;
      margin-right: 8px;
      margin-bottom: 8px;
    }}
    .pill.priority-high {{ background: #ffe4cf; color: #8a3b12; }}
    .pill.priority-medium {{ background: #ede7d5; color: #685e51; }}
    .pill.priority-low {{ background: #e6efe7; color: #3a6842; }}
    .pill.status-new {{ background: #e6f2f5; color: #0f5f73; }}
    .pill.status-review {{ background: #f8d8eb; color: #89245b; }}
    .pill.status-done {{ background: #daf4df; color: #266643; }}
    .question-text, .summary-box {{
      border: 1px solid var(--line);
      border-radius: 16px;
      padding: 16px;
      background: white;
      line-height: 1.6;
      white-space: pre-wrap;
    }}
    .summary-box {{ background: #fff7ea; }}
    .visual-warning {{
      border: 1px solid #efc48b;
      border-radius: 16px;
      padding: 14px 16px;
      background: #fff1db;
      color: #8a4b10;
      line-height: 1.5;
      margin-bottom: 16px;
    }}
    .topic-notes {{
      border-left: 4px solid var(--accent);
      padding-left: 14px;
      color: var(--muted);
      margin: 0 0 18px;
    }}
    .image-wrap {{
      margin-top: 18px;
      border: 1px solid var(--line);
      border-radius: 18px;
      padding: 14px;
      background: white;
    }}
    .image-wrap img {{ width: 100%; height: auto; border-radius: 12px; display: block; background: #f4efe7; }}
    .meta {{ margin-top: 12px; color: var(--muted); line-height: 1.5; }}
    .topbar {{ display: flex; justify-content: space-between; align-items: flex-start; gap: 16px; margin-bottom: 18px; }}
    .empty {{
      padding: 28px;
      border: 1px dashed var(--line);
      border-radius: 18px;
      color: var(--muted);
      background: white;
    }}
    .muted {{ color: var(--muted); }}
    #save-feedback {{ min-height: 24px; margin-top: 10px; color: var(--muted); }}
    .hidden {{ display: none; }}
    @media (max-width: 980px) {{
      .page {{ grid-template-columns: 1fr; }}
      .sidebar {{ position: static; }}
      .stats {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <div class="page">
    <aside class="panel sidebar">
      <h1>HPDA Study App</h1>
      <p class="lede" id="mode-lede"></p>
      <div class="grid">
        <div class="field">
          <label for="topic-filter">Topic</label>
          <select id="topic-filter"></select>
        </div>
        <div class="field">
          <label for="year-filter">Year</label>
          <select id="year-filter"></select>
        </div>
        <div class="field">
          <label for="status-filter">Status</label>
          <select id="status-filter">
            <option value="all">All</option>
            <option value="new">New</option>
            <option value="review">Review</option>
            <option value="done">Done</option>
          </select>
        </div>
        <div class="field">
          <label for="priority-filter">Priority</label>
          <select id="priority-filter">
            <option value="all">All</option>
            <option value="high">High</option>
            <option value="medium">Medium</option>
            <option value="low">Low</option>
          </select>
        </div>
        <div class="field">
          <label for="question-limit">Session Size</label>
          <input id="question-limit" type="number" min="0" value="0">
        </div>
        <div class="checkboxes">
          <label><input id="shuffle-filter" type="checkbox" checked> Shuffle session</label>
          <label><input id="show-image-toggle" type="checkbox" checked> Show image inline</label>
        </div>
        <div class="buttons">
          <button id="start-session" class="primary">Start Session</button>
          <button id="random-question">Random Question</button>
        </div>
        <div id="local-actions" class="footer-actions">
          <button id="export-progress">Export Browser Progress</button>
          <button id="import-progress">Import Browser Progress</button>
          <button id="reset-progress">Reset Browser Progress</button>
          <input id="import-file" type="file" accept="application/json" hidden>
        </div>
      </div>
    </aside>
    <main class="panel content">
      <div class="topbar">
        <div>
          <h2 id="session-title">No session loaded</h2>
          <p id="session-subtitle" class="muted">Pick filters on the left and start a session.</p>
        </div>
        <div class="nav-buttons">
          <button id="prev-question">Previous</button>
          <button id="next-question">Next</button>
        </div>
      </div>
      <div class="stats">
        <div class="stat"><span class="value" id="stat-total">0</span><span>Questions In Session</span></div>
        <div class="stat"><span class="value" id="stat-review">0</span><span>Marked Review</span></div>
        <div class="stat"><span class="value" id="stat-done">0</span><span>Marked Done</span></div>
      </div>
      <div id="question-container" class="empty">No question loaded yet.</div>
      <div id="save-feedback"></div>
    </main>
  </div>

  <script>
    const SERVER_MODE = {server_mode_json};
    const QUESTIONS = {questions_json};
    const TOPIC_NOTES = {topic_notes_json};
    const STORAGE_KEY = "hpda-study-app-progress-v1";
    const VISUAL_HINT_KEYWORDS = {json.dumps(VISUAL_HINT_KEYWORDS)};

    const state = {{ progress: {{}}, session: [], currentIndex: 0 }};

    function setFeedback(message) {{
      document.getElementById("save-feedback").textContent = message;
    }}

    function loadProgress() {{
      if (SERVER_MODE) {{
        state.progress = {{}};
        return;
      }}
      try {{
        state.progress = JSON.parse(localStorage.getItem(STORAGE_KEY) || "{{}}");
      }} catch (_err) {{
        state.progress = {{}};
      }}
    }}

    function saveProgress() {{
      if (!SERVER_MODE) {{
        localStorage.setItem(STORAGE_KEY, JSON.stringify(state.progress));
      }}
    }}

    function mergedQuestion(question) {{
      if (SERVER_MODE) return question;
      const saved = state.progress[question.stable_id] || {{}};
      return {{
        ...question,
        review_status: saved.review_status || question.review_status || "new",
        answer_notes: saved.answer_notes ?? question.answer_notes ?? "",
        practice_count: saved.practice_count ?? question.practice_count ?? "0",
        last_practiced: saved.last_practiced ?? question.last_practiced ?? ""
      }};
    }}

    async function updateQuestion(question, patch) {{
      if (SERVER_MODE) {{
        const response = await fetch("/api/update", {{
          method: "POST",
          headers: {{ "Content-Type": "application/json" }},
          body: JSON.stringify({{ stable_id: question.stable_id, ...patch }})
        }});
        if (!response.ok) {{
          setFeedback("Could not save changes to questions_master.csv");
          return;
        }}
        const updated = await response.json();
        const index = QUESTIONS.findIndex((item) => item.stable_id === question.stable_id);
        if (index >= 0) {{
          QUESTIONS[index] = updated.question;
          state.session = state.session.map((item) => item.stable_id === updated.question.stable_id ? updated.question : item);
        }}
        setFeedback(`Saved to CSV at ${{updated.question.last_practiced || "now"}}`);
        renderCurrentQuestion();
        return;
      }}

      const current = state.progress[question.stable_id] || {{}};
      state.progress[question.stable_id] = {{ ...current, ...patch }};
      saveProgress();
      setFeedback("Saved in browser local storage");
      renderCurrentQuestion();
    }}

    function uniqueValues(key) {{
      return [...new Set(QUESTIONS.map((item) => item[key]).filter(Boolean))];
    }}

    function optionHtml(value, label) {{
      return `<option value="${{value}}">${{label}}</option>`;
    }}

    function buildFilters() {{
      document.getElementById("mode-lede").textContent = SERVER_MODE
        ? "This page is running through the local study server. Status and notes are saved straight back to questions_master.csv."
        : "This page is running as a standalone local file. Progress is stored in your browser only.";
      document.getElementById("local-actions").classList.toggle("hidden", SERVER_MODE);

      const topicSelect = document.getElementById("topic-filter");
      const yearSelect = document.getElementById("year-filter");
      topicSelect.innerHTML = optionHtml("all", "All topics") +
        uniqueValues("topic_group").map((topic) => optionHtml(topic, topic)).join("");
      yearSelect.innerHTML = optionHtml("all", "All years") +
        uniqueValues("year").sort().map((year) => optionHtml(year, year)).join("");
    }}

    function filteredQuestions() {{
      const topic = document.getElementById("topic-filter").value;
      const year = document.getElementById("year-filter").value;
      const status = document.getElementById("status-filter").value;
      const priority = document.getElementById("priority-filter").value;

      return QUESTIONS.filter((question) => {{
        const merged = mergedQuestion(question);
        if (topic !== "all" && question.topic_group !== topic) return false;
        if (year !== "all" && question.year !== year) return false;
        if (status !== "all" && merged.review_status !== status) return false;
        if (priority !== "all" && question.topic_priority !== priority) return false;
        return true;
      }});
    }}

    function shuffleInPlace(items) {{
      for (let i = items.length - 1; i > 0; i -= 1) {{
        const j = Math.floor(Math.random() * (i + 1));
        [items[i], items[j]] = [items[j], items[i]];
      }}
    }}

    function buildSession(useRandomSingle = false) {{
      let questions = filteredQuestions();
      if (!questions.length) {{
        state.session = [];
        state.currentIndex = 0;
        renderCurrentQuestion();
        return;
      }}
      questions = [...questions];
      if (document.getElementById("shuffle-filter").checked || useRandomSingle) {{
        shuffleInPlace(questions);
      }}
      const limitValue = Number(document.getElementById("question-limit").value || "0");
      if (useRandomSingle) {{
        questions = questions.slice(0, 1);
      }} else if (limitValue > 0) {{
        questions = questions.slice(0, limitValue);
      }}
      state.session = questions;
      state.currentIndex = 0;
      setFeedback("");
      renderCurrentQuestion();
    }}

    function currentQuestion() {{
      if (!state.session.length) return null;
      return mergedQuestion(state.session[state.currentIndex]);
    }}

    function renderStats() {{
      const mergedSession = state.session.map(mergedQuestion);
      document.getElementById("stat-total").textContent = String(mergedSession.length);
      document.getElementById("stat-review").textContent = String(mergedSession.filter((q) => q.review_status === "review").length);
      document.getElementById("stat-done").textContent = String(mergedSession.filter((q) => q.review_status === "done").length);
    }}

    function escapeHtml(text) {{
      return String(text)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;");
    }}

    function noteList(topicId) {{
      const notes = TOPIC_NOTES[topicId] || [];
      if (!notes.length) return "";
      return `<div class="topic-notes">${{notes.map((note) => `<div>${{escapeHtml(note)}}</div>`).join("")}}</div>`;
    }}

    function questionNeedsVisualReference(question) {{
      const text = [
        question.knowledge_point || "",
        question.question_summary || "",
        question.original_question_text || ""
      ].join(" ").toLowerCase();
      return VISUAL_HINT_KEYWORDS.some((keyword) => text.includes(keyword));
    }}

    function renderCurrentQuestion() {{
      renderStats();
      const title = document.getElementById("session-title");
      const subtitle = document.getElementById("session-subtitle");
      const container = document.getElementById("question-container");
      const showImage = document.getElementById("show-image-toggle").checked;
      const question = currentQuestion();

      if (!question) {{
        title.textContent = "No session loaded";
        subtitle.textContent = "Pick filters on the left and start a session.";
        container.className = "empty";
        container.innerHTML = "No question loaded yet.";
        return;
      }}

      title.textContent = question.topic_group;
      subtitle.textContent = `Question ${{state.currentIndex + 1}} of ${{state.session.length}}`;
      container.className = "";

      const imageHtml = showImage && question.source_image
        ? `<div class="image-wrap">
            <img src="${{question.source_image}}" alt="Question source image">
            <div class="meta">
              <div>Source image: <a href="${{question.source_image}}" target="_blank" rel="noreferrer">${{question.source_image}}</a></div>
              <div>Source PDF: <a href="${{question.source_pdf}}" target="_blank" rel="noreferrer">${{question.source_pdf}}</a> (page ${{question.source_page || "?"}})</div>
            </div>
          </div>`
        : "";

      const visualWarningHtml = questionNeedsVisualReference(question)
        ? `<div class="visual-warning">
            This question depends on figures, tables, or page layout. Use the source image as the primary reference, and treat extracted text as a helper view.
          </div>`
        : "";

      container.innerHTML = `
        <div class="buttons" style="margin-bottom: 14px;">
          <span class="pill priority-${{question.topic_priority}}">Priority: ${{question.topic_priority}}</span>
          <span class="pill status-${{question.review_status || "new"}}">Status: ${{question.review_status || "new"}}</span>
          <span class="pill status-new">Year: ${{question.year}}</span>
          <span class="pill status-new">Question: ${{question.question_number}}</span>
        </div>
        ${{noteList(question.topic_id)}}
        <h3>${{escapeHtml(question.knowledge_point)}}</h3>
        <div class="summary-box">${{escapeHtml(question.question_summary)}}</div>
        <div style="height: 16px;"></div>
        ${{visualWarningHtml}}
        ${{imageHtml}}
        <div style="height: 18px;"></div>
        <h3>Original Question</h3>
        <div class="question-text">${{escapeHtml(question.original_question_text || "No original question text available.")}}</div>
        <div style="height: 18px;"></div>
        <div class="buttons">
          <button data-status="new">Mark New</button>
          <button data-status="review" class="review">Mark Review</button>
          <button data-status="done" class="done">Mark Done</button>
        </div>
        <div style="height: 18px;"></div>
        <h3>Notes</h3>
        <textarea id="notes-input" placeholder="Write answer notes or reminders here...">${{escapeHtml(question.answer_notes || "")}}</textarea>
        <div class="buttons" style="margin-top: 12px;">
          <button id="save-notes" class="primary">Save Notes</button>
        </div>
        <div class="meta" style="margin-top: 12px;">
          <div>Practice count: ${{question.practice_count || "0"}}</div>
          <div>Last practiced: ${{question.last_practiced || "not yet"}}</div>
          <div>Stable id: ${{question.stable_id}}</div>
        </div>
      `;

      for (const button of container.querySelectorAll("[data-status]")) {{
        button.addEventListener("click", async () => {{
          const now = new Date().toISOString().slice(0, 16).replace("T", " ");
          const oldCount = Number(question.practice_count || "0");
          await updateQuestion(question, {{
            review_status: button.dataset.status,
            practice_count: String(oldCount + 1),
            last_practiced: now
          }});
        }});
      }}

      document.getElementById("save-notes").addEventListener("click", async () => {{
        const notes = document.getElementById("notes-input").value;
        await updateQuestion(question, {{ answer_notes: notes }});
      }});
    }}

    function moveQuestion(offset) {{
      if (!state.session.length) return;
      state.currentIndex = (state.currentIndex + offset + state.session.length) % state.session.length;
      setFeedback("");
      renderCurrentQuestion();
    }}

    function exportProgress() {{
      const blob = new Blob([JSON.stringify(state.progress, null, 2)], {{ type: "application/json" }});
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;
      link.download = "hpda-browser-progress.json";
      link.click();
      URL.revokeObjectURL(url);
    }}

    function importProgress(file) {{
      const reader = new FileReader();
      reader.onload = () => {{
        try {{
          state.progress = JSON.parse(String(reader.result));
          saveProgress();
          setFeedback("Imported browser progress");
          renderCurrentQuestion();
        }} catch (_err) {{
          alert("Could not import progress JSON.");
        }}
      }};
      reader.readAsText(file, "utf-8");
    }}

    document.getElementById("start-session").addEventListener("click", () => buildSession(false));
    document.getElementById("random-question").addEventListener("click", () => buildSession(true));
    document.getElementById("prev-question").addEventListener("click", () => moveQuestion(-1));
    document.getElementById("next-question").addEventListener("click", () => moveQuestion(1));
    document.getElementById("show-image-toggle").addEventListener("change", renderCurrentQuestion);
    document.getElementById("export-progress").addEventListener("click", exportProgress);
    document.getElementById("import-progress").addEventListener("click", () => document.getElementById("import-file").click());
    document.getElementById("import-file").addEventListener("change", (event) => {{
      const file = event.target.files && event.target.files[0];
      if (file) importProgress(file);
    }});
    document.getElementById("reset-progress").addEventListener("click", () => {{
      if (!confirm("Reset browser-only progress for this study page?")) return;
      state.progress = {{}};
      saveProgress();
      setFeedback("Reset browser progress");
      renderCurrentQuestion();
    }});

    loadProgress();
    buildFilters();
    renderCurrentQuestion();
  </script>
</body>
</html>
"""


def build_static_html() -> str:
    question_rows = load_csv_rows(MASTER_FILE)
    note_rows = load_csv_rows(TOPIC_NOTE_FILE)
    return render_html(
        prepare_questions(question_rows, for_server=False),
        prepare_topic_notes(note_rows),
        server_mode=False,
    )


def build_server_html() -> str:
    question_rows = load_csv_rows(MASTER_FILE)
    note_rows = load_csv_rows(TOPIC_NOTE_FILE)
    return render_html(
        prepare_questions(question_rows, for_server=True),
        prepare_topic_notes(note_rows),
        server_mode=True,
    )


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(build_static_html(), encoding="utf-8")
    print(f"Built local web app: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
