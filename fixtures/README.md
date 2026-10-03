# Immutable live fixtures

The final live integration must use raw GitHub URLs pinned to the exact source commit that contains these files.

Current source marker: `2d71ecba5a7f3aef7e8a7914b58e96a9b339aae5`

Fixtures:

- `registry_no_hit.txt` — complete bounded fixture with no qualifying Product X recall;
- `registry_hit.txt` — complete bounded fixture with an explicit qualifying Product X recall;
- `registry_ambiguous.txt` — deliberately incomplete/paginated representation that must not support absence.
