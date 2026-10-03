from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FINAL = "--final" in sys.argv
errors: list[str] = []

required = [
    ROOT / "contracts/nullproof.py",
    ROOT / "contracts/absence_gate.py",
    ROOT / "README.md",
    ROOT / "SUBMISSION.md",
    ROOT / "DEPLOYMENT.md",
    ROOT / "BUILD_STATUS.md",
    ROOT / "docs/ARCHITECTURE.md",
    ROOT / "docs/INVARIANTS.md",
    ROOT / "docs/SECURITY.md",
    ROOT / "tests/test_nullproof.py",
    ROOT / "tests/test_source_invariants.py",
    ROOT / "tests/test_live_studionet.py",
    ROOT / "fixtures/registry_no_hit.txt",
    ROOT / "fixtures/registry_hit.txt",
    ROOT / "fixtures/registry_ambiguous.txt",
]

for p in required:
    if not p.exists():
        errors.append(f"missing required file: {p.relative_to(ROOT)}")

for p in [ROOT / "contracts/nullproof.py", ROOT / "contracts/absence_gate.py"]:
    if not p.exists():
        continue
    src = p.read_text(encoding="utf-8")
    try:
        ast.parse(src)
    except SyntaxError as exc:
        errors.append(f"syntax error in {p.name}: {exc}")
    if "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" not in src:
        errors.append(f"unexpected dependency pin in {p.name}")

core = (ROOT / "contracts/nullproof.py").read_text(encoding="utf-8") if (ROOT / "contracts/nullproof.py").exists() else ""
for marker in [
    "run_nondet_unsafe",
    "gl.nondet.web.get",
    "response_format=\"json\"",
    "min_optional_coverage",
    "SRC_UNAVAILABLE",
    "OBS_ABSENT",
    "OBS_PRESENT",
    "OBS_INDETERMINATE",
    "QUERY_PRESENT",
    "NULLPROOF_DEFINITION_V1",
    "NULLPROOF_OBSERVATION_V1",
    "is_absence_valid",
    "query already has terminal PRESENT evidence",
    "Store only consensus-critical material",
]:
    if marker not in core:
        errors.append(f"missing core marker: {marker}")

gate = (ROOT / "contracts/absence_gate.py").read_text(encoding="utf-8") if (ROOT / "contracts/absence_gate.py").exists() else ""
for marker in [
    "@gl.contract_interface",
    ".view().is_absence_valid",
    "expected_definition_hash must be 64 hex",
    "expected_observation_hash must be 64 hex",
    "action already consumed",
]:
    if marker not in gate:
        errors.append(f"missing gate marker: {marker}")

if (ROOT / "frontend").exists():
    errors.append("frontend directory present")

for p in ROOT.rglob("*"):
    if not p.is_file():
        continue
    rel = p.relative_to(ROOT)
    if p.name in {".env", "id_rsa", "id_ed25519"}:
        errors.append(f"sensitive file present: {rel}")
    if any(part in {".venv", "venv", "__pycache__", ".pytest_cache", "node_modules"} for part in rel.parts):
        errors.append(f"generated/cache directory present: {rel}")
    if p.suffix in {".pyc", ".pyo"}:
        errors.append(f"compiled artifact present: {rel}")

text = "\n".join(
    p.read_text(encoding="utf-8", errors="ignore")
    for p in ROOT.rglob("*")
    if p.is_file()
    and p.resolve() != Path(__file__).resolve()
    and p.resolve() != (ROOT / "scripts/pin_fixture_commit.py").resolve()
    and p.suffix in {".md", ".py", ".yaml", ".yml", ".txt"}
)
if "https://studio.genlayer.com/api" not in text:
    errors.append("stable Studionet RPC reference missing")
if "61999" not in text:
    errors.append("stable Studionet chain ID reference missing")
if "studio-dev.genlayer.com/api" in text or re.search(r"\b61997\b", text):
    errors.append("preview network reference found; stable Studionet only")

if FINAL:
    if "FIXTURE_COMMIT_PLACEHOLDER" in text:
        errors.append("fixture commit placeholder remains")
    dep = (ROOT / "DEPLOYMENT.md").read_text(encoding="utf-8")
    if "PENDING" in dep:
        errors.append("DEPLOYMENT.md still contains PENDING proof")

if errors:
    print("PREFLIGHT FAIL")
    for error in errors:
        print(" -", error)
    raise SystemExit(1)

print("PREFLIGHT PASS")
print(" - required repository files present")
print(" - contract Python parses")
print(" - stable dependency pin present")
print(" - bounded absence / terminal presence markers present")
print(" - typed consumer/replay markers present")
print(" - no frontend directory")
print(" - no obvious sensitive/generated artifacts")
print(" - stable Studionet / chain 61999 references present")
if not FINAL:
    print(" - handoff mode: fixture/deployment placeholders permitted")
