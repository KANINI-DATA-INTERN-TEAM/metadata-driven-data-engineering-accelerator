"""Load and validate JSON table metadata."""

import json
from pathlib import Path
from jsonschema import validate


def load_config(config_path: str | Path, schema_path: str | Path) -> dict:
    """Read a JSON configuration file and validate it against the JSON Schema."""
    with Path(config_path).open(encoding="utf-8") as file:
        config = json.load(file)
    with Path(schema_path).open(encoding="utf-8") as file:
        schema = json.load(file)
    validate(instance=config, schema=schema)
    return config
