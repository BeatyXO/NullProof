# Deployment evidence

Network target: **stable Studionet / chain 61999**  
RPC: `https://studio.genlayer.com/api`  
Explorer: `https://explorer-studio.genlayer.com`

Canonical source repository: https://github.com/BeatyXO/NullProof.git

Canonical source commit: `b648b62e71aa511af54a230dfb83d4ae27726cf4`

Immutable fixture commit: `2d71ecba5a7f3aef7e8a7914b58e96a9b339aae5`; all three raw fixture URLs returned HTTP 200.

Live evidence status: awaiting a NullProof-authorized funded Studionet signer; no live contract writes have been submitted.

## Canonical deployments

- NullProof address: unrecorded
- NullProof deploy tx: unrecorded
- NullProof deployment finalized status: unrecorded
- AbsenceGate address: unrecorded
- AbsenceGate deploy tx: unrecorded
- AbsenceGate deployment finalized status: unrecorded
- AbsenceGate NullProof target: unrecorded

## ABSENT lifecycle

- ABSENT query ID: unrecorded
- ABSENT query creation tx: unrecorded
- ABSENT definition hash: unrecorded
- ABSENT observation ID: unrecorded
- ABSENT observation tx: unrecorded
- ABSENT observation hash: unrecorded
- ABSENT observed_at: unrecorded
- ABSENT expires_at: unrecorded
- fresh certificate validation: unrecorded

## Consumer proof

- successful AbsenceGate consume tx: unrecorded
- wrong-definition rejection evidence: unrecorded
- wrong-observation rejection evidence: unrecorded
- replay rejection evidence: unrecorded

## PRESENT lifecycle

- PRESENT query ID: unrecorded
- PRESENT query creation tx: unrecorded
- PRESENT definition hash: unrecorded
- PRESENT observation ID: unrecorded
- PRESENT observation tx: unrecorded
- PRESENT observation hash: unrecorded
- PRESENT terminal-state evidence: unrecorded
- repeated-observe rejection evidence: unrecorded
- gate rejection for PRESENT evidence: unrecorded

## Verification

- `python scripts/preflight.py`: PASS
- `python scripts/preflight.py --final`: BLOCKED until the required live evidence fields below are populated and validated
- `python -m compileall contracts scripts tests`: PASS
- NullProof GenVM lint: PASS, 3 checks; 6 contract methods validated
- AbsenceGate GenVM lint: PASS, 3 checks; 2 contract methods validated
- `gltest -q --tb=short -p no:cacheprovider`: 30 passed, 1 live-only test skipped
- GitHub Actions run 37133510537: success at canonical source commit `b648b62e71aa511af54a230dfb83d4ae27726cf4`
- raw fixture URL checks: HTTP 200 for `registry_no_hit.txt`, `registry_hit.txt`, and `registry_ambiguous.txt` at immutable fixture commit `2d71ecba5a7f3aef7e8a7914b58e96a9b339aae5`
- stable Studionet network check: alias `studionet`, chain ID `61999`, RPC `https://studio.genlayer.com/api`
