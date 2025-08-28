# Автоответчик
class AutoReply:
    def __init__(self, trigger="привет", response="Привет! 👋"):
        self.trigger = trigger
        self.response = response

    def process(self, message: str) -> str | None:
        if self.trigger.lower() in message.lower():
            return self.response
        return None