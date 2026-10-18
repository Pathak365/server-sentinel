
import json
from datetime import datetime, timezone
from pathlib import Path


class HistoryManager:
    def __init__(self, file_path="data/history.json"):
        self.file_path = Path(file_path)
        self.history = {}

        self.load()

    def add(self, metrics):
        timestamp = datetime.now(timezone.utc).isoformat()

        record = {
            "timestamp": timestamp,
            **metrics,
        }

        self.history[timestamp] = record
        return record

    def get_all(self):
        return list(self.history.values())

    def get_by_id(self, record_id):
        return self.history.get(record_id)

    def save(self):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(self.history, file, indent=4)

    def load(self):
        if not self.file_path.exists():
            return

        with self.file_path.open("r", encoding="utf-8") as file:
            self.history = json.load(file)
