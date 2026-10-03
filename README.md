# NullProof

**Freshness-aware, source-bounded proof-of-absence for GenLayer.**

NullProof is a standalone reusable Intelligent Contract primitive for a question ordinary on-chain systems handle poorly:

> Within this explicitly declared authoritative search surface, under this relevance rule, was any qualifying record found?

NullProof never claims universal non-existence. A query freezes the subject, relevance rule, exact HTTPS sources, source coverage policy, and certificate TTL. GenLayer validators independently fetch and evaluate those sources. Deterministic contract logic derives only one of:

- `PRESENT`
- `ABSENT`
- `INDETERMINATE`

There is **no frontend** in this repository.

## Why this is different from a normal oracle

A weak absence oracle asks an LLM: “Does X exist?”

NullProof instead makes absence conditional on a bounded evidence universe:

1. exact source URLs are frozen in the query definition;
2. every source declares what surface it is supposed to represent;
3. sources are `REQUIRED` or `OPTIONAL`;
4. the query freezes how many optional sources must actually support a negative finding;
5. validators independently fetch and classify every source;
6. a source may return `NO_HIT` only if its fetched representation appears sufficiently complete for its declared scope;
7. unavailable, oversized, partial, paginated, or semantically uncertain evidence cannot prove absence;
8. deterministic logic aggregates per-source results;
9. `ABSENT` certificates expire after a frozen TTL;
10. any later consensus-backed `PRESENT` result is terminal for that existential query and instantly invalidates all earlier absence certificates.

## Per-source states

The consensus-critical source vocabulary is:

- `HIT` — affirmative source-grounded qualifying material exists;
- `NO_HIT` — no qualifying material exists **and** the fetched representation is sufficiently complete for the declared source scope;
- `AMBIGUOUS` — source is reachable but cannot safely support either a hit or negative finding;
- `UNAVAILABLE` — source could not be safely observed, including non-success response, empty response, or response exceeding the bounded source size.

The LLM may produce only `HIT`, `NO_HIT`, or `AMBIGUOUS`. `UNAVAILABLE` is produced deterministically from fetch failure/bounds, not by model discretion.

## Deterministic aggregation

`PRESENT` is decisive if **any** frozen source has a consensus-backed `HIT`.

`ABSENT` requires:

- every `REQUIRED` source = `NO_HIT`;
- no source = `HIT` or `AMBIGUOUS`;
- at least `min_optional_coverage` OPTIONAL sources = `NO_HIT`.

OPTIONAL sources may be unavailable only when the frozen optional-coverage threshold is still satisfied.

Everything else is `INDETERMINATE`.

## Terminal presence

The query is existential. Once a qualifying record has been consensus-confirmed, deleting or hiding it later must not resurrect absence.

Therefore:

```text
ACTIVE + PRESENT observation -> PRESENT_TERMINAL
```

After terminal presence:

- no further observations are accepted;
- all earlier `ABSENT` certificates become invalid immediately, even if their TTL has not expired.

## Freshness

An `ABSENT` observation is a time-bounded certificate, not a permanent fact.

Each query freezes `ttl_seconds` between 60 seconds and 7 days. An absence certificate is valid only while:

- the query definition hash matches;
- the exact observation hash matches;
- observation status is `ABSENT`;
- certificate has not expired;
- the query has not since reached terminal `PRESENT`.

## Consensus boundary

Validators independently:

1. fetch the same exact frozen URL;
2. reject failed/empty/oversized representations from negative coverage;
3. semantically evaluate the source against the same subject, relevance rule, and declared source scope;
4. derive the per-source material status.

Consensus compares only stable material fields:

`(source_id, REQUIRED|OPTIONAL mode, source status)`

Model notes, excerpts, and raw source digests are deliberately **not** persisted as if they were consensus-backed evidence. The frozen URL and material status are the protocol evidence surface.

## Consumer composability

`contracts/absence_gate.py` demonstrates a second Intelligent Contract enforcing a fresh NullProof certificate through a typed IC-to-IC read:

```python
is_absence_valid(
    query_id,
    observation_id,
    expected_definition_hash,
    expected_observation_hash,
)
```

The consumer pins both definition and observation hashes and rejects replayed action hashes.

## Security properties

The implementation explicitly addresses:

- universal-nonexistence overclaiming;
- source substitution;
- SSRF-style localhost/private IPv4 source surfaces;
- missing required sources;
- incomplete/paginated evidence;
- oversized evidence pretending to be complete after truncation;
- model-invented `UNAVAILABLE`;
- malformed/unknown model statuses;
- prompt injection inside fetched source text;
- leader/validator web divergence;
- fresh-certificate expiry;
- old absence surviving a later confirmed hit;
- consumer hash mismatch;
- downstream action replay.

## Privacy / content warning

Source URLs and query text are stored on-chain and should be treated as public. Do not place credentials, secrets, private URLs, personal tokens, or confidential information in query definitions.

## Stable network target

- network: `studionet`
- chain ID: `61999`
- RPC: `https://studio.genlayer.com/api`
- explorer: `https://explorer-studio.genlayer.com`

Current official GenLayer documentation lists Studionet at chain ID 61999. Keep this project on the stable target.

## Repository layout

- `contracts/nullproof.py` — reusable absence primitive
- `contracts/absence_gate.py` — typed consumer/replay example
- `tests/test_nullproof.py` — Direct Mode/adversarial coverage
- `tests/test_source_invariants.py` — static guards runnable without GenLayer runtime
- `tests/test_live_studionet.py` — final live-proof specification
- `fixtures/` — immutable public live fixtures
- `docs/` — architecture, invariants, security model
- `scripts/preflight.py` — handoff/final gate
- `scripts/pin_fixture_commit.py` — immutable fixture pinning
- `DEPLOYMENT.md` — only real deployment proof belongs here

## Local checks

```bash
python -m pip install -r requirements-test.txt
python scripts/preflight.py
python -m compileall contracts scripts tests
genvm-lint check contracts/nullproof.py
genvm-lint check contracts/absence_gate.py
pytest -q
```

Final submission gate:

```bash
python scripts/preflight.py --final
```

The final gate verifies immutable fixture pinning, rejects unresolved live-proof language, and requires well-formed deployment addresses, transaction hashes, lifecycle IDs, observation hashes, timestamps, and rejection evidence. It remains blocked until real finalized Studionet evidence is recorded.
