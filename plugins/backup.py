# Бэкапы переписки
import json
import datetime

class BackupPlugin:
    def __init__(self, filename="chat_backup.json"):
        self.filename = filename
        self.data = []

    def save_message(self, sender: str, message: str):
        entry = {
            "time": str(datetime.datetime.now()),
            "sender": sender,
            "message": message
        }
        self.data.append(entry)
        self._save()

    def _save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def process(self, sender: str, message: str):
        self.save_message(sender, message)