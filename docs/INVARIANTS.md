# Protocol invariants

1. A query contains at least one REQUIRED source.
2. Query definition is immutable after creation.
3. Source IDs are normalized, bounded, and unique.
4. Source URLs are exact HTTPS URLs and cannot point to the blocked local/private IPv4 surface.
5. Source scope text is bounded and immutable.
6. `min_optional_coverage` never exceeds the number of OPTIONAL sources.
7. TTL is bounded between 60 seconds and 7 days.
8. External fetch failure can never become `NO_HIT`.
9. Empty source content can never become `NO_HIT`.
10. Oversized source content can never be truncated and then treated as complete negative evidence.
11. The model cannot declare `UNAVAILABLE`.
12. `HIT` requires affirmative source-grounded material.
13. `NO_HIT` requires both no qualifying hit and sufficient completeness for declared source scope.
14. Partial/paginated/uncertain source representations resolve to `AMBIGUOUS`, not absence.
15. Validators independently re-fetch and re-evaluate sources.
16. Consensus-critical material is limited to source ID, source mode, and source status.
17. Any consensus-backed `HIT` makes aggregate status `PRESENT`.
18. Every REQUIRED source must be `NO_HIT` before aggregate `ABSENT` is possible.
19. Any `AMBIGUOUS` source prevents `ABSENT`.
20. OPTIONAL `UNAVAILABLE` can be tolerated only when frozen optional negative-coverage threshold is still met.
21. Observations are append-only and monotonically numbered per query.
22. `ABSENT` observations have deterministic expiry timestamps.
23. Expired observations can never satisfy `is_absence_valid`.
24. Definition-hash mismatch can never satisfy `is_absence_valid`.
25. Observation-hash mismatch can never satisfy `is_absence_valid`.
26. A later finalized `PRESENT` immediately invalidates every prior absence certificate.
27. `PRESENT` is terminal for the existential query.
28. Terminal queries cannot be observed again.
29. Consumer contracts pin both definition and observation hashes.
30. `AbsenceGate` rejects replayed action hashes.
31. No frontend is part of this primitive.
