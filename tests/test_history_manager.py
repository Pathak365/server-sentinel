
from app.services.history_manager import HistoryManager


def test_add_record_creates_timestamped_history():
    manager = HistoryManager(file_path="data/test_history.json")

    record = manager.add({
        "cpu_uses": 25.0,
        "memory_uses": 50.0,
        "disk_uses": 60.0,
    })

    assert "timestamp" in record
    assert record["cpu_uses"] == 25.0


def test_save_and_load_history(tmp_path):
    file_path = tmp_path / "history.json"

    manager = HistoryManager(file_path=str(file_path))

    manager.add({
        "cpu_uses": 25.0,
        "memory_uses": 50.0,
        "disk_uses": 60.0,
    })

    manager.save()

    restored_manager = HistoryManager(file_path=str(file_path))

    records = restored_manager.get_all()

    assert len(records) == 1
    assert records[0]["cpu_uses"] == 25.0


def test_get_by_id_returns_record():
    manager = HistoryManager(file_path="data/test_history_lookup.json")

    record = manager.add({
        "cpu_uses": 30.0,
        "memory_uses": 40.0,
        "disk_uses": 50.0,
    })

    assert manager.get_by_id(record["timestamp"]) == record
