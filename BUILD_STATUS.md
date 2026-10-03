# Build status

Canonical repository: https://github.com/BeatyXO/NullProof.git

Verified contract-source commit: `b648b62e71aa511af54a230dfb83d4ae27726cf4`

GitHub Actions run [37135221928](https://github.com/BeatyXO/NullProof/actions/runs/37135221928): **success** for the preflight and documentation update. Final lifecycle evidence is recorded in [DEPLOYMENT.md](DEPLOYMENT.md).

This file records checks actually performed. It is not deployment proof.

## Implemented here

- bounded immutable query definitions;
- exact HTTPS source freezing;
- REQUIRED / OPTIONAL source policy;
- optional negative-coverage threshold;
- public/private URL sanity guard;
- independent validator re-fetch and semantic re-evaluation;
- fail-closed unavailable/empty/oversized handling;
- completeness-aware `NO_HIT` semantics;
- prompt-injection boundary;
- deterministic PRESENT / ABSENT / INDETERMINATE aggregation;
- append-only observation history;
- deterministic certificate freshness;
- terminal PRESENT invalidation of old absence certificates;
- canonical domain-separated hashes;
- typed `AbsenceGate` consumer with dual hash pinning and replay protection;
- Direct Mode/adversarial test suite;
- static guards, preflight, CI, fixtures, architecture/security docs.

## Runtime compatibility verified

- Updated `gltest.config.yaml` to the current `networks` and `paths` schema.
- Kept `gl.nondet.web.get` and `gl.nondet.exec_prompt` visibly inside both leader and validator callbacks so current `genvm-linter` can verify the equivalence-principle boundary.
- Passed source sequences to the current storage descriptor rather than calling the non-instantiable `DynArray` constructor.
- Passed event blob fields to event constructors; the current runtime's `.emit()` accepts no keyword arguments.
- Required HIT excerpts to occur in fetched text and deterministically downgraded NO_HIT to AMBIGUOUS for explicit pagination/partial-result markers.
- Reused one deployed contract per Direct Mode test because current Direct Mode permits one contract class per VM context.
- Pinned the tested harness tools to `genlayer-test==0.29.2` and `genvm-linter==0.11.0`; CI warms Direct Mode's runner cache from the linter's downloaded GenVM bundle.

## Checks performed

- `python scripts/preflight.py`: PASS.
- `python -m compileall contracts scripts tests`: PASS.
- `genvm-lint check contracts/nullproof.py`: PASS; 3 checks, contract validation passed (6 methods).
- `genvm-lint check contracts/absence_gate.py`: PASS; 3 checks, contract validation passed (2 methods).
- `gltest -q --tb=short -p no:cacheprovider`: PASS; 30 tests passed and the live Studionet handoff test was skipped.
- GitHub Actions run 37135221928: completed successfully for preflight and documentation commit `d690fd708e2c4ced2bfd4c2998936dd8afc14220`.
- Raw GitHub URLs for all three fixture files at commit `2d71ecba5a7f3aef7e8a7914b58e96a9b339aae5`: HTTP 200.
- NullProof and AbsenceGate deployed and finalized on stable Studionet (chain 61999); complete evidence is in `DEPLOYMENT.md`.
- ABSENT lifecycle finalized; certificate was accepted by AbsenceGate, and replay, wrong-definition, and wrong-observation simulations rejected.
- PRESENT lifecycle finalized; query entered `PRESENT_TERMINAL`, repeat observation rejected, and AbsenceGate rejected PRESENT evidence.

## Deployment and lifecycle evidence

Both contract deployments and the ABSENT and PRESENT lifecycle proofs are finalized on stable Studionet. The authorized unlocked signer was `0x7876E9F76F32925c212528D57BC9DfE5E34bCC07`. See `DEPLOYMENT.md` for transaction hashes, query/observation hashes, timestamps, and negative simulation results.
