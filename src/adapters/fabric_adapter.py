"""Microsoft Fabric adapter placeholder.

Implement using the team's agreed Fabric Lakehouse/Delta conventions.
Do not import Fabric-only libraries in unit-testable core modules.
"""

from .base_adapter import StorageAdapter


class FabricAdapter(StorageAdapter):
    def write_bronze(self, table_name: str, records: list[dict], metadata: dict) -> None:
        raise NotImplementedError("Implement in the Fabric runtime.")

    def read_silver(self, table_name: str):
        raise NotImplementedError("Implement in the Fabric runtime.")

    def write_silver(self, table_name: str, records, mode: str, metadata: dict) -> None:
        raise NotImplementedError("Implement in the Fabric runtime.")

    def write_rejects(self, table_name: str, records: list[dict], metadata: dict) -> None:
        raise NotImplementedError("Implement in the Fabric runtime.")

    def write_audit(self, record: dict) -> None:
        raise NotImplementedError("Implement in the Fabric runtime.")
