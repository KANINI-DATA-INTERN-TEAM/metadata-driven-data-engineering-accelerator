"""Starter interface for dynamic CSV/JSON ingestion.

Implementation owner: Vaibhav Masal.
Keep this module independent of Fabric-specific APIs where practical.
"""

from pathlib import Path
import csv
import json


def read_source(path: str | Path, source_format: str) -> list[dict]:
    """Read a CSV or JSON source into a list of dictionaries."""
    source_path = Path(path)
    if source_format == "csv":
        with source_path.open(newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    if source_format == "json":
        with source_path.open(encoding="utf-8") as file:
            payload = json.load(file)
        if not isinstance(payload, list) or not all(isinstance(row, dict) for row in payload):
            raise ValueError("JSON source must contain a list of objects.")
        return payload
    raise ValueError(f"Unsupported source format: {source_format}")
