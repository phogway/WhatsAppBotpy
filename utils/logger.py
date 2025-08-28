# utils/logger.py — отдельный модуль для логов

import logging

def setup_logger(level="INFO"):
    logger = logging.getLogger("WhatsAppBotPro")
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))

    if not logger.handlers:
        handler = logging.StreamHandler()
        fmt = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
        handler.setFormatter(fmt)
        logger.addHandler(handler)

    return logger