from pathlib import Path
import re
import sys

if len(sys.argv) != 2 or not re.fullmatch(r"[0-9a-fA-F]{40}", sys.argv[1]):
    raise SystemExit("usage: python scripts/pin_fixture_commit.py <40-char-commit-sha>")

root = Path(__file__).resolve().parents[1]
sha = sys.argv[1].lower()
changed = 0
for p in [root / "fixtures/README.md", root / "tests/test_live_studionet.py"]:
    text = p.read_text(encoding="utf-8")
    updated = text.replace("FIXTURE_COMMIT_PLACEHOLDER", sha)
    if updated != text:
        p.write_text(updated, encoding="utf-8")
        changed += 1
print(f"pinned {changed} file(s) to {sha}")
