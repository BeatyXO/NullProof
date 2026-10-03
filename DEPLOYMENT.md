# Deployment evidence

Network target: **stable Studionet / chain 61999**  
RPC: `https://studio.genlayer.com/api`  
Explorer: `https://explorer-studio.genlayer.com`

Canonical source repository: https://github.com/BeatyXO/NullProof.git

Canonical source commit: `b648b62e71aa511af54a230dfb83d4ae27726cf4`

Immutable fixture commit: `2d71ecba5a7f3aef7e8a7914b58e96a9b339aae5`; all three raw fixture URLs returned HTTP 200.

The deployments and lifecycle transactions below were submitted by the authorized unlocked signer `0x7876E9F76F32925c212528D57BC9DfE5E34bCC07` and finalized on stable Studionet.

## Canonical deployments

- NullProof address: `0x3325FFEEc92603d6EB7CEdaEC3c087b8a8BC8936`
- NullProof deploy tx: `0xadf1788ee812fa20d3cb67237c29d598d5e9332fcb14efa175ea377cbe1120a9`
- NullProof deployment finalized status: finalized
- AbsenceGate address: `0xa2ad9305FE0DECd9221Bb1DE0e310011eA946a35`
- AbsenceGate deploy tx: `0x0c86638ce44bf7b9d27dcfcf8016dda3d4d92ffa6f9d9336160f593d835810fe`
- AbsenceGate deployment finalized status: finalized
- AbsenceGate NullProof target: `0x3325FFEEc92603d6EB7CEdaEC3c087b8a8BC8936`

## ABSENT lifecycle

- ABSENT query ID: `1`
- ABSENT query creation tx: `0xfe6f61fdc43d84a6ceb0ba00e3f97b13fc90f85c2e5560bbe4a98cea778e7bc1`
- ABSENT definition hash: `e99c6d75d8452f652f0c5091c79f31d0f7e8edfdc541ce63b8fa6bf19427fe95`
- ABSENT observation ID: `1`
- ABSENT observation tx: `0xf3d465ec7c1b219add29154c1c9a8b65fcf95e3e96656d0dd14778ee0f45a66f`
- ABSENT observation hash: `23111fd3567a7765a66352aff93e24bfd24f6a1757fcce68876e4a4aede8d1cc`
- ABSENT observed_at: `1791044025`
- ABSENT expires_at: `1791047625`
- ABSENT source status: NO_HIT
- ABSENT aggregate status: ABSENT
- fresh certificate validation: true

The ABSENT source is the immutable `registry_no_hit.txt` fixture. The certificate was valid at consume time and then became invalid when the later PRESENT observation terminalized the query state.

At final verification, `get_observation(1, 1)` still reports the original ABSENT hash and unexpired timestamp. The gate reports the action consumed, while `is_absence_valid(1, 1, ...)` returns false after the PRESENT terminal observation, as designed.

## Consumer proof

- successful AbsenceGate consume tx: `0x4ebce0f1bf72f0204c9e1ffa1d5422c42a799c1c982ca9dbd7b8140ce92f0696`
- successful action hash: `3196d3a345b312288874879570ec6fed2e5a652fdfec75e77185d886ebbe151d`
- AbsenceGate consumed result: true
- wrong-definition rejection evidence: read-only simulation rejected with `NullProof absence certificate not currently valid`; no transaction submitted
- wrong-observation rejection evidence: read-only simulation rejected with `NullProof absence certificate not currently valid`; no transaction submitted
- replay rejection evidence: read-only simulation rejected with `action already consumed`; no transaction submitted

## PRESENT lifecycle

- PRESENT query ID: `2`
- PRESENT query creation tx: `0x0e55d0ce1b696ed9708706d66f4cdfffe907333fde995083e1ff338b80b3723c`
- PRESENT definition hash: `4d7f44c34bd3c733807d21308cfb361da2e463be6256cb9ddb5dc2d80d8cb359`
- PRESENT observation ID: `1`
- PRESENT observation tx: `0x3adb0fe611589b897027c08c78f5917f9ed5c50f427b2a72b9de65ce534ddd7b`
- PRESENT observation hash: `efb156e3ef989687ab14b7b0ce46b70107618924b11c6a5b1e5a5b6420a708fc`
- PRESENT source status: HIT
- PRESENT aggregate status: PRESENT
- PRESENT terminal-state evidence: query status code 2, observation ID 1, matching hash
- terminal PRESENT observation ID: `1`
- terminal PRESENT observation hash: `efb156e3ef989687ab14b7b0ce46b70107618924b11c6a5b1e5a5b6420a708fc`
- repeated-observe rejection evidence: read-only simulation rejected; terminal-state guard confirmed
- gate rejection for PRESENT evidence: read-only simulation rejected with `NullProof absence certificate not currently valid`; no transaction submitted

## Verification

- `python scripts/preflight.py`: PASS
- `python scripts/preflight.py --final`: PASS after this evidence was recorded
- `python -m compileall contracts scripts tests`: PASS
- NullProof GenVM lint: PASS; 3 checks, 6 contract methods validated
- AbsenceGate GenVM lint: PASS; 3 checks, 2 contract methods validated
- `gltest -q --tb=short -p no:cacheprovider`: 30 passed, 1 live-only test skipped
- GitHub Actions run 37135221928: success for documentation/preflight commit `d690fd708e2c4ced2bfd4c2998936dd8afc14220`
- raw fixture URL checks: HTTP 200 for `registry_no_hit.txt`, `registry_hit.txt`, and `registry_ambiguous.txt` at immutable fixture commit `2d71ecba5a7f3aef7e8a7914b58e96a9b339aae5`
- stable Studionet network check: alias `studionet`, chain ID `61999`, RPC `https://studio.genlayer.com/api`
