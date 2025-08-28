# WhatsAppBot

WhatsAppBot is an extensible Python library for building WhatsApp bots with ease.  
It provides a simple interface to interact with WhatsApp, handle messages, and integrate with other services.

## Features

- Easy setup and integration
- Message handling and response
- Extensible architecture for plugins and custom logic
- REST API support (via Flask)
- HTTP requests support (via Requests)

## Installation

```bash
pip install whatsappbot
```

Or install from source:

```bash
git clone https://github.com/yourusername/whatsappbot.git
cd whatsappbot
pip install .
```

## Usage

```python
from whatsappbot import WhatsAppBot

bot = WhatsAppBot(token="YOUR_TOKEN")

@bot.on_message
def handle_message(message):
    if message.text == "hello":
        bot.send_message(message.chat_id, "Hi there!")

bot.run()
```

## Requirements

- Python 3.7+
- Flask
- Requests

##