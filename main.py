from whatsappbot import WhatsAppBot, Router
from plugins import my_plugin, another_plugin

bot = WhatsAppBot(phone_number="+1234567890")
router = Router()

my_plugin.setup(router)
another_plugin.setup(router)

bot.include_router(router)
bot.run_polling()