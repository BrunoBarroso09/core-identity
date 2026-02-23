import uuid
from UUID.identifier import Identifier

def test_uuid4_is_string():
    result = Identifier.v4()
    assert isinstance(result, str)

def test_uuid4_format_valido():
    result = Identifier.v4()
    uuid.UUID(result, version=4)

def test_uuid4_hex():
    result = Identifier.hex()
    assert "-" not in result

def test_uuid5_deterministic():
    id1 = Identifier.v5("user@email.com")
    id2 = Identifier.v5("user@email.com")
    assert id1 == id2

def test_uuid_v5_inputs_different():
    id1 = Identifier.v5("user1@email.com")
    id2 = Identifier.v5("user2@email.com")
    assert id1 != id2