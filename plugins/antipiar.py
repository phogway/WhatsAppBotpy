# Анти-спам / анти-пиар
class AntiPiar:
    def __init__(self, banned_keywords=None):
        if banned_keywords is None:
            banned_keywords = ["t.me/", "invite", "channel", "group"]
        self.banned_keywords = banned_keywords

    def process(self, message: str) -> str | None:
        for word in self.banned_keywords:
            if word.lower() in message.lower():
                return "⛔ Сообщение заблокировано (АнтиПиар)"
        return None