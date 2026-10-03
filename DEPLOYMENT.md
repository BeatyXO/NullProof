# Deployment evidence

Network target: **stable Studionet / chain 61999**  
RPC: `https://studio.genlayer.com/api`  
Explorer: `https://explorer-studio.genlayer.com`

This repository never invents deployment evidence. No live deployment or transaction has been performed in the current environment, so no addresses, transaction IDs, query hashes, or finalized-state claims are recorded below.

## Canonical deployments

- NullProof address: not produced
- NullProof deploy tx: not produced
- AbsenceGate address: not produced
- AbsenceGate deploy tx: not produced
- canonical source commit on GitHub: not produced; the configured Git credential was denied write access

## ABSENT lifecycle

- absence query ID / creation tx / definition hash: not produced
- absence observation ID / tx / hash: not produced
- observed_at / expires_at: not produced
- fresh certificate validation: not performed

## Consumer proof

- successful AbsenceGate consume tx: not produced
- wrong-definition-hash rejection: not performed
- wrong-observation-hash rejection: not performed
- replay rejection: not performed

## PRESENT lifecycle

- present query ID / creation tx / definition hash: not produced
- present observation ID / tx / hash: not produced
- terminal-state evidence: not produced
- repeated-observation rejection: not performed
- gate rejection for non-ABSENT observation: not performed

## Verification

- `python scripts/preflight.py` and `python scripts/preflight.py --final`: PASS
- `python -m compileall contracts scripts tests`: PASS
- NullProof GenVM lint: PASS, 3 checks; 6 contract methods validated
- AbsenceGate GenVM lint: PASS, 3 checks; 2 contract methods validated
- `gltest -q --tb=short -p no:cacheprovider`: 30 passed, 1 live-only test skipped
- live stable Studionet lifecycle: not performed; no deployment evidence is claimed

The Git remote rejected writes from the configured GitHub identity (`Ifem1`) with HTTP 403. A GitHub identity with write access is required to publish the source and pin immutable fixture URLs to the pushed source commit. Live deployment also requires an authenticated funded Studionet account and verification of chain ID 61999 before any write.
