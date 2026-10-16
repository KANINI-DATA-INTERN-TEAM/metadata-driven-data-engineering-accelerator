import pytest
from jsonschema import ValidationError

from src.core.config_parser import load_config


def test_customer_config_matches_schema(project_root):
    config = load_config(
        project_root / "configs/tables/customers_master.json",
        project_root / "configs/config_schema.json",
    )
    assert config["table_name"] == "customers"
    assert config["load_mode"] == "scd2"


def test_invalid_config_fails_validation(tmp_path, project_root):
    bad_config = tmp_path / "bad.json"
    bad_config.write_text('{"table_name": "missing-required-fields"}', encoding="utf-8")
    with pytest.raises(ValidationError):
        load_config(bad_config, project_root / "configs/config_schema.json")
