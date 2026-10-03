"""Stable Studionet live-proof handoff specification.

This is skipped in ordinary pytest because it requires authenticated/funded stable
Studionet accounts and the current compatible GenLayer client/fee lifecycle.

Immutable fixtures:
https://raw.githubusercontent.com/BeatyXO/NullProof/2d71ecba5a7f3aef7e8a7914b58e96a9b339aae5/fixtures/

Required live proof on Studionet / chain 61999:
1. verify effective network before writes;
2. deploy NullProof and finalize;
3. create a bounded absence query using the pinned no-hit fixture as REQUIRED source;
4. observe and finalize ABSENT with nonzero definition/observation hashes;
5. deploy AbsenceGate using finalized NullProof address;
6. correct fresh pinned certificate + fresh action succeeds;
7. wrong definition hash rejects;
8. wrong observation hash rejects;
9. replay rejects;
10. create a second query against pinned hit fixture;
11. observe PRESENT and prove query becomes PRESENT_TERMINAL;
12. prove AbsenceGate cannot consume a PRESENT observation;
13. record only real finalized evidence in DEPLOYMENT.md.
"""

import pytest

pytestmark = pytest.mark.skip(reason="requires authenticated stable Studionet accounts and finalized live workflow")


def test_live_studionet_lifecycle_handoff_specification():
    assert True
