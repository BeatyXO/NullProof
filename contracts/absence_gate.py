# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
"""Typed NullProof consumer that enforces a fresh absence certificate once per action."""

from genlayer import *

ZERO_ADDRESS = "0x" + ("0" * 40)


@gl.contract_interface
class INullProof:
    class View:
        def is_absence_valid(
            self,
            query_id: u256,
            observation_id: u32,
            expected_definition_hash: str,
            expected_observation_hash: str,
        ) -> bool: ...

    class Write:
        pass


class AbsenceConsumed(gl.Event):
    def __init__(self, action_hash: str, query_id: u256, observation_id: u32, /, **blob): ...


def valid_hash(value: str) -> bool:
    s = str(value).lower().strip()
    return len(s) == 64 and all(c in "0123456789abcdef" for c in s)


class AbsenceGate(gl.Contract):
    nullproof: Address
    consumed: TreeMap[str, bool]

    def __init__(self, nullproof: Address):
        if str(nullproof).lower() == ZERO_ADDRESS:
            raise gl.vm.UserError("NullProof address cannot be zero")
        self.nullproof = nullproof

    @gl.public.write
    def consume(
        self,
        query_id: u256,
        observation_id: u32,
        expected_definition_hash: str,
        expected_observation_hash: str,
        action_hash: str,
    ) -> bool:
        definition_hash = str(expected_definition_hash).lower().strip()
        observation_hash = str(expected_observation_hash).lower().strip()
        action = str(action_hash).lower().strip()
        if not valid_hash(definition_hash):
            raise gl.vm.UserError("expected_definition_hash must be 64 hex")
        if not valid_hash(observation_hash):
            raise gl.vm.UserError("expected_observation_hash must be 64 hex")
        if not valid_hash(action):
            raise gl.vm.UserError("action_hash must be 64 hex")
        if self.consumed.get(action, False):
            raise gl.vm.UserError("action already consumed")

        valid = INullProof(self.nullproof).view().is_absence_valid(
            query_id,
            observation_id,
            definition_hash,
            observation_hash,
        )
        if not valid:
            raise gl.vm.UserError("NullProof absence certificate not currently valid")

        self.consumed[action] = True
        AbsenceConsumed(
            action,
            query_id,
            observation_id,
            definition_hash=definition_hash,
            observation_hash=observation_hash,
        ).emit()
        return True

    @gl.public.view
    def is_consumed(self, action_hash: str) -> bool:
        action = str(action_hash).lower().strip()
        if not valid_hash(action):
            return False
        return self.consumed.get(action, False)
