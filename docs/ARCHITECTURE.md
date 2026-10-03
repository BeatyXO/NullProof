# Architecture

## Product boundary

NullProof is a reusable **bounded absence certificate** primitive. It is not a crawler, search engine, truth oracle, or claim of universal non-existence.

A query asks whether a qualifying existential record is present inside an explicitly frozen evidence surface.

## Query definition

A query freezes:

- title;
- existential subject;
- semantic relevance rule;
- exact source list;
- for each source: stable ID, HTTPS URL, REQUIRED/OPTIONAL mode, declared coverage scope;
- minimum OPTIONAL `NO_HIT` coverage;
- absence-certificate TTL.

The canonical `definition_hash` uses the domain `NULLPROOF_DEFINITION_V1`.

At least one source must be REQUIRED.

## Source safety

Source URLs are exact and immutable. The contract rejects:

- non-HTTPS URLs;
- credential-bearing authorities;
- localhost;
- common private/link-local IPv4 ranges.

This narrows source substitution and SSRF-style surfaces. It is not intended as a general-purpose URL security library.

## Nondeterministic boundary

For each source, leader and validators independently:

1. GET the exact URL;
2. treat non-2xx, empty, or oversized representations as deterministic `UNAVAILABLE`;
3. ask the model to classify the fetched representation as `HIT`, `NO_HIT`, or `AMBIGUOUS`;
4. require a non-empty `HIT` excerpt that occurs in the fetched representation;
5. force `AMBIGUOUS` when a proposed `NO_HIT` conflicts with explicit pagination or partial-result markers;
6. require the model to treat fetched text as untrusted data;
7. derive the material source row.

A model cannot declare `UNAVAILABLE`; that state belongs to the fetch/bounds layer.

## Consensus material

The contract validates exact source ordering/coverage and compares only:

```text
source_id
source mode
source status
```

This avoids requiring byte-identical dynamic web responses or identical LLM prose. It does not make arbitrary sources complete by assumption: source scopes must describe an authoritative bounded surface, and subtle or silent transport truncation remains outside the contract's ability to detect unless the source exposes an explicit completeness signal.

Leader notes, excerpts, and source digests are not persisted as consensus-backed evidence.

## Deterministic aggregate

### PRESENT

Any `HIT` => `PRESENT`.

### ABSENT

Every REQUIRED source must be `NO_HIT`.

No source may be `AMBIGUOUS` or `HIT`.

The count of OPTIONAL sources with `NO_HIT` must meet `min_optional_coverage`.

### INDETERMINATE

Every remaining combination, including:

- required source unavailable;
- any source ambiguous;
- insufficient optional negative coverage.

## Append-only observations

Each observation receives:

- monotonic observation ID;
- deterministic transaction timestamp;
- expiry timestamp;
- aggregate status;
- canonical material source matrix;
- `observation_hash` under `NULLPROOF_OBSERVATION_V1`.

Observation history is append-only.

## Freshness and terminal presence

`ABSENT` is temporary and certificate-scoped.

`PRESENT` is terminal because the query asks whether a qualifying record has ever been found within the frozen existential surface. Once found and finalized, later disappearance must not revive absence.

Thus:

- prior `ABSENT` remains independently addressable historically;
- `is_absence_valid` immediately returns false after terminal presence;
- no new observations are accepted after terminal presence.

## Consumer

`AbsenceGate` pins:

- query ID;
- observation ID;
- exact definition hash;
- exact observation hash;
- unique action hash.

It performs a typed synchronous view call to NullProof and records action hashes to reject replay.
