# whatsappbot/plugins/__init__.py

"""
Плагины для WhatsAppBot
"""

from .autoreply import AutoReply
from .antipiar import AntiPiar
from .logger import LoggerPlugin
from .backup import BackupPlugin
from .whitelist import WhitelistPlugin

__all__ = [
    "AutoReply",
    "AntiPiar",
    "LoggerPlugin",
    "BackupPlugin",
    "WhitelistPlugin"
]