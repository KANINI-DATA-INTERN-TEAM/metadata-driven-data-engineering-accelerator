"""Storage adapter contract scaffold.

The core engine should depend on this interface, not on a specific cloud platform.
"""

from abc import ABC, abstractmethod


class StorageAdapter(ABC):
    @abstractmethod
    def write_bronze(self, table_name: str, records: list[dict], metadata: dict) -> None:
        """Persist raw records plus technical lineage."""
        raise NotImplementedError

    @abstractmethod
    def read_silver(self, table_name: str):
        """Read the current Silver target/history."""
        raise NotImplementedError

    @abstractmethod
    def write_silver(self, table_name: str, records, mode: str, metadata: dict) -> None:
        """Persist accepted Silver records using the requested load mode."""
        raise NotImplementedError

    @abstractmethod
    def write_rejects(self, table_name: str, records: list[dict], metadata: dict) -> None:
        """Persist quarantined/rejected records."""
        raise NotImplementedError

    @abstractmethod
    def write_audit(self, record: dict) -> None:
        """Persist run audit information."""
        raise NotImplementedError
