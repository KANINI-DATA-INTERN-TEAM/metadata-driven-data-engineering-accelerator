from src.core.bronze_ingestion import read_source


def test_read_customers_csv(project_root):
    rows = read_source(project_root / "sample_data/batch_1/customers.csv", "csv")
    assert len(rows) == 3
    assert rows[0]["customer_id"] == "101"


def test_read_orders_json(project_root):
    rows = read_source(project_root / "sample_data/batch_1/orders.json", "json")
    assert len(rows) == 2
    assert rows[0]["order_id"] == 5001
