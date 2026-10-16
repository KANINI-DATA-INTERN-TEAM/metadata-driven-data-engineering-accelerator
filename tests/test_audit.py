import json
from src.core.audit_logger import create_audit_record, serialize_audit_record


def test_audit_record_serializes_expected_fields():
    record = create_audit_record("run-001", "customers")
    payload = json.loads(serialize_audit_record(record))
    assert payload["run_id"] == "run-001"
    assert payload["table_name"] == "customers"
    assert payload["status"] == "STARTED"
    assert payload["input_count"] == 0
