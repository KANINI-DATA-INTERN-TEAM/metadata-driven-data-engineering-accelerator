"""Azure ADLS Gen2 target contract placeholder.

Runnable Azure deployment is outside the initial MVP unless the team explicitly expands scope.
"""

from .base_adapter import StorageAdapter


class AzureAdapter(StorageAdapter):
    def write_bronze(self, table_name: str, records: list[dict], metadata: dict) -> None:
        raise NotImplementedError("Azure adapter implementation is a follow-on.")

    def read_silver(self, table_name: str):
        raise NotImplementedError("Azure adapter implementation is a follow-on.")

    def write_silver(self, table_name: str, records, mode: str, metadata: dict) -> None:
        raise NotImplementedError("Azure adapter implementation is a follow-on.")

    def write_rejects(self, table_name: str, records: list[dict], metadata: dict) -> None:
        raise NotImplementedError("Azure adapter implementation is a follow-on.")

    def write_audit(self, record: dict) -> None:
        raise NotImplementedError("Azure adapter implementation is a follow-on.")
