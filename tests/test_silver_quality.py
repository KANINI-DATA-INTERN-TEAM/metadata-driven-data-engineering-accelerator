from src.core.silver_quality import split_valid_and_rejected


def test_required_fields_route_invalid_rows_to_rejects():
    rows = [
        {"customer_id": 101, "customer_name": "Asha"},
        {"customer_id": 102, "customer_name": ""},
    ]
    accepted, rejected = split_valid_and_rejected(rows, ["customer_id", "customer_name"])
    assert len(accepted) == 1
    assert len(rejected) == 1
    assert "_reject_reason" in rejected[0]
