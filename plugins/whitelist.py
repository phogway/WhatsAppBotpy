# Белый список доверенных пользователей
class WhitelistPlugin:
    def __init__(self, allowed_users=None):
        if allowed_users is None:
            allowed_users = []
        self.allowed_users = allowed_users

    def check(self, user: str) -> bool:
        return user in self.allowed_users

    def process(self, sender: str, message: str) -> str | None:
        if not self.check(sender):
            return "🚫 Пользователь не в белом списке!"
        return None