import uuid
from UUID.identifier import UUID

def test_uuid4_is_string():
    result = UUID.v4()
    assert isinstance(result, str)

def test_uuid4_format_valido():
    result = UUID.v4()
    uuid.UUID(result, version=4)

def test_uuid4_hex():
    result = UUID.hex()
    assert "-" not in result

def test_uuid5_deterministic():
    id1 = UUID.v5("user@email.com")
    id2 = UUID.v5("user@email.com")
    assert id1 == id2

def test_uuid_v5_inputs_different():
    id1 = UUID.v5("user1@email.com")
    id2 = UUID.v5("user2@email.com")
    assert id1 != id2