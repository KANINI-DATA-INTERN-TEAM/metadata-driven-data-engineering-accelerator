"""Starter interface for Silver type casting, validation, and quarantine routing."""


def split_valid_and_rejected(records: list[dict], required_columns: list[str]) -> tuple[list[dict], list[dict]]:
    """Split records based on required fields; rejected records include a reason.

    This is a minimal starter rule, not the complete metadata-driven quality engine.
    """
    accepted, rejected = [], []
    for record in records:
        missing = [column for column in required_columns if record.get(column) in (None, "")]
        if missing:
            rejected.append({**record, "_reject_reason": f"Missing required fields: {', '.join(missing)}"})
        else:
            accepted.append(record)
    return accepted, rejected
