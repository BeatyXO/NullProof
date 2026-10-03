# Build status

This file records only checks actually performed before the final GenLayer-enabled handoff. It is not deployment proof.

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

## Still requires GenLayer-enabled finishing environment

- install/run exact current stable `genlayer-test` Direct Mode runtime;
- run current stable GenVM linter against both contracts;
- make only compatibility fixes exposed by those real tools;
- publish/deploy on stable Studionet chain 61999;
- execute real ABSENT and PRESENT live lifecycles;
- deploy and exercise AbsenceGate;
- record real finalized evidence in `DEPLOYMENT.md`;
- run final preflight after all evidence is populated.
