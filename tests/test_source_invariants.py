"""Static guards runnable without GenLayer runtime."""

from pathlib import Path

ROOT = Path(__file__).parents[1]
CORE = (ROOT / "contracts/nullproof.py").read_text(encoding="utf-8")
GATE = (ROOT / "contracts/absence_gate.py").read_text(encoding="utf-8")


def test_standalone_no_frontend_and_two_contracts():
    assert "class NullProof(gl.Contract)" in CORE
    assert "class AbsenceGate(gl.Contract)" in GATE
    assert not (ROOT / "frontend").exists()


def test_consensus_is_independent_refetch_not_shape_only():
    assert "run_nondet_unsafe" in CORE
    assert "gl.nondet.web.get" in CORE
    assert "gl.nondet.exec_prompt" in CORE
    assert CORE.count("gl.nondet.web.get(source[\"url\"])") == 2
    assert CORE.count("gl.nondet.exec_prompt(") == 2
    assert "material_source_payload(proposed) == material_source_payload(own)" in CORE


def test_absence_requires_coverage_not_just_no_keyword_hit():
    assert "sufficiently complete" in CORE
    assert "partial, paginated" in CORE
    assert "derive_observation_status" in CORE
    assert "min_optional_coverage" in CORE


def test_unavailable_and_oversize_fail_closed():
    assert "MAX_SOURCE_TEXT_BYTES" in CORE
    assert "SRC_UNAVAILABLE" in CORE
    assert "len(raw) == 0 or len(raw) > MAX_SOURCE_TEXT_BYTES" in CORE


def test_absence_is_freshness_bounded_and_presence_terminal():
    assert "expires_at" in CORE
    assert "QUERY_PRESENT" in CORE
    assert "query already has terminal PRESENT evidence" in CORE
    assert "if int(q.status) == QUERY_PRESENT" in CORE


def test_hash_domains_are_explicit():
    assert "NULLPROOF_DEFINITION_V1" in CORE
    assert "NULLPROOF_OBSERVATION_V1" in CORE


def test_persisted_source_material_excludes_unvalidated_notes_and_excerpts():
    marker = "Store only consensus-critical material"
    assert marker in CORE
    stored_block = CORE.split(marker, 1)[1].split("self.observations", 1)[0]
    assert '"note"' not in stored_block
    assert '"evidence_excerpt"' not in stored_block


def test_consumer_pins_both_hashes_and_rejects_replay():
    assert "@gl.contract_interface" in GATE
    assert ".view().is_absence_valid" in GATE
    assert "expected_definition_hash must be 64 hex" in GATE
    assert "expected_observation_hash must be 64 hex" in GATE
    assert "action already consumed" in GATE
