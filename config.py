# config.py — глобальные настройки

class Config:
    def __init__(self):
        # Основное
        self.BOT_NAME = "WhatsAppBotPro"
        self.VERSION = "1.0.0"

        # Логирование
        self.LOG_LEVEL = "INFO"

        # Доверенные ссылки (для антиспама/антипиара)
        self.TRUSTED_DOMAINS = [
            "youtube.com",
            "t.me",
            "github.com"
        ]

        # Настройки антиспама
        self.ANTI_SPAM_LIMIT = 5  # сообщений в минуту