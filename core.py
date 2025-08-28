# core.py — ядро библиотеки

import logging
from .config import Config
from .utils.logger import setup_logger

class WhatsAppBotPro:
    def __init__(self, config: Config = None):
        self.config = config or Config()
        self.logger = setup_logger(self.config.LOG_LEVEL)
        self.plugins = []
        self.blocked_users = set()

    def load_plugin(self, plugin):
        """Загрузить плагин (объект с методом handle_message)."""
        if plugin not in self.plugins:
            self.plugins.append(plugin)
            self.logger.info(f"[PLUGIN] {plugin.__class__.__name__} подключён")

    def block_user(self, user_id: str):
        """Блокировка пользователя."""
        self.blocked_users.add(user_id)
        self.logger.warning(f"[BLOCK] Пользователь {user_id} заблокирован!")

    def is_blocked(self, user_id: str) -> bool:
        return user_id in self.blocked_users

    async def handle_message(self, user_id: str, message: str) -> str:
        """Главная обработка сообщений"""
        if self.is_blocked(user_id):
            return "[BLOCKED] У вас нет доступа!"

        response = None
        for plugin in self.plugins:
            try:
                response = await plugin.handle_message(user_id, message)
                if response:
                    break
            except Exception as e:
                self.logger.error(f"[PLUGIN ERROR] {plugin.__class__.__name__}: {e}")
        return response or "[NO RESPONSE]"