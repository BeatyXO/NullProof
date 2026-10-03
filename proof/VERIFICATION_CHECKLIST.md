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
- [x] immutable public fixtures pinned to `2d71ecba5a7f3aef7e8a7914b58e96a9b339aae5`
- [x] canonical repository published at `https://github.com/BeatyXO/NullProof.git`
- [x] all pinned raw fixture URLs return HTTP 200
- [x] GitHub Actions run 37133510537 succeeded for contract-source commit `b648b62e71aa511af54a230dfb83d4ae27726cf4`

## GenLayer-enabled finishing environment

- [x] `python scripts/preflight.py`
- [x] `python -m compileall contracts scripts tests`
- [x] `genvm-lint check contracts/nullproof.py`
- [x] `genvm-lint check contracts/absence_gate.py`
- [x] Direct Mode: 30 passed, 1 live-only test skipped
- [x] GitHub Actions green
- [x] verify effective `studionet`, chain 61999
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
- [ ] `DEPLOYMENT.md` contains finalized live proof
- [ ] `python scripts/preflight.py --final` passes against populated evidence
- [ ] final git status clean and remote inspected after live evidence commit
