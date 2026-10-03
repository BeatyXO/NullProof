# Verification checklist

## Implemented before GenLayer runtime handoff

- [x] standalone primitive / no frontend
- [x] exact frozen HTTPS sources
- [x] at least one REQUIRED source
- [x] optional coverage threshold
- [x] source-size bound without negative-result truncation
- [x] independent validator re-fetch/re-evaluation
- [x] deterministic aggregate status
- [x] expiring ABSENT certificate
- [x] terminal PRESENT state
- [x] old ABSENT invalid after later PRESENT
- [x] append-only observation IDs
- [x] definition + observation hash pinning
- [x] typed consumer and replay defense
- [x] immutable public fixtures

## GenLayer-enabled finishing environment

- [ ] `python scripts/preflight.py`
- [ ] `python -m compileall contracts scripts tests`
- [ ] `genvm-lint check contracts/nullproof.py`
- [ ] `genvm-lint check contracts/absence_gate.py`
- [ ] all Direct Mode tests pass without weakening assertions
- [ ] GitHub Actions green
- [ ] verify effective `studionet`, chain 61999
- [ ] finalized NullProof deployment
- [ ] ABSENT live query finalized
- [ ] fresh ABSENT certificate verified
- [ ] finalized AbsenceGate deployment
- [ ] correct pinned gate action succeeds
- [ ] wrong definition hash rejected
- [ ] wrong observation hash rejected
- [ ] replay rejected
- [ ] PRESENT live query finalized
- [ ] PRESENT query becomes terminal
- [ ] gate rejects non-ABSENT observation
- [ ] `DEPLOYMENT.md` contains only real proof
- [ ] `python scripts/preflight.py --final`
- [ ] final git status clean and remote inspected
