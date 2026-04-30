#!/usr/bin/env python3
"""
Run the full question-bank rebuild pipeline in order.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent

STEPS = [
    ("Extract PDF pages", "extract_papers.py"),
    ("Parse summary file", "parse_question_summary.py"),
    ("Link questions to source pages", "auto_link_source_images.py"),
    ("Populate original question text", "populate_original_question_text.py"),
]


def main() -> None:
    for index, (label, script_name) in enumerate(STEPS, start=1):
        print(f"[{index}/{len(STEPS)}] {label}: {script_name}")
        result = subprocess.run([sys.executable, str(ROOT / script_name)], cwd=ROOT)
        if result.returncode != 0:
            raise SystemExit(result.returncode)

    print("\nQuestion bank rebuild complete.")


if __name__ == "__main__":
    main()
