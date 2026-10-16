"""Audit event model and lightweight logger starter."""

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import json
import logging


@dataclass
class AuditRecord:
    run_id: str
    table_name: str
    status: str
    input_count: int = 0
    accepted_count: int = 0
    rejected_count: int = 0
    started_at: str = ""
    completed_at: str = ""
    error_message: str | None = None


def create_audit_record(run_id: str, table_name: str, status: str = "STARTED") -> AuditRecord:
    now = datetime.now(timezone.utc).isoformat()
    return AuditRecord(run_id=run_id, table_name=table_name, status=status, started_at=now)


def serialize_audit_record(record: AuditRecord) -> str:
    """Serialize an audit record to JSON for local logging or adapter persistence."""
    return json.dumps(asdict(record), sort_keys=True)


def log_audit_record(record: AuditRecord, logger: logging.Logger | None = None) -> None:
    """Log an audit record; persistent storage is intentionally adapter-owned."""
    (logger or logging.getLogger(__name__)).info("%s", serialize_audit_record(record))
