import uuid
from typing import Final

class UUID:

    # Centralize service to generate unique identifiers
    #Ensures ID consistency across all microservices in the ecosystem..

    NAMESPACE: Final = uuid.NAMESPACE_OID

    #Generate random unique identifier using UUID4
    @staticmethod
    def v4() -> str:
        return str(uuid.uuid4())

    #Generate random unique identifier using UUID4 hexadecimal
    @staticmethod
    def hex() -> str:
        return str(uuid.uuid4().hex)

    #Generate random unique identifier using UUID5
    @staticmethod
    def v5(identifier: str) -> str:
        my_namespace = uuid.NAMESPACE_OID
        return str(uuid.uuid5(my_namespace, identifier))