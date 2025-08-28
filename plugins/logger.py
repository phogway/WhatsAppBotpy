# Логирование
import datetime

class LoggerPlugin:
    def __init__(self, logfile="whatsappbot.log"):
        self.logfile = logfile

    def log(self, message: str):
        with open(self.logfile, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.datetime.now()}] {message}\n")

    def process(self, message: str) -> None:
        self.log(f"Получено сообщение: {message}")