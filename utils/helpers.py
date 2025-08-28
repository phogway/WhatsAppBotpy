# utils/helpers.py — вспомогательные функции

import re

def contains_untrusted_link(text: str, trusted_domains: list) -> bool:
    """Проверка на наличие ссылок вне доверенных доменов"""
    urls = re.findall(r'(https?://\S+)', text)
    for url in urls:
        if not any(domain in url for domain in trusted_domains):
            return True
    return False