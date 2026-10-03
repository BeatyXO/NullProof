# Submission summary

**Title:** NullProof — Bounded Proof-of-Absence Certificates

NullProof is a reusable GenLayer primitive for certifying that no qualifying record was found within a frozen authoritative source surface — without pretending to prove universal non-existence. A query commits to the existential subject, relevance rule, exact HTTPS sources, REQUIRED/OPTIONAL coverage policy, and certificate TTL. Validators independently fetch and semantically inspect every frozen source. A negative source result is valid only when the representation is sufficiently complete for its declared scope; partial, ambiguous, failed, empty, or oversized evidence cannot become absence. Deterministic logic aggregates source statuses into PRESENT, ABSENT, or INDETERMINATE. ABSENT certificates expire. Any later consensus-backed PRESENT result is terminal and immediately invalidates every earlier absence certificate. `AbsenceGate` proves another Intelligent Contract can enforce a fresh pinned certificate and reject replay.

No frontend is part of this submission.
