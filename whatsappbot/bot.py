import asyncio

class WhatsAppBot:
    def __init__(self, phone_number=None, session_path=None):
        self.phone_number = phone_number
        self.session_path = session_path
        self.routers = []
        self.middlewares = []

    def include_router(self, router):
        self.routers.append(router)

    def middleware(self, func):
        self.middlewares.append(func)
        return func

    async def _process_middlewares(self, message, handler):
        async def call(index):
            if index < len(self.middlewares):
                return await self.middlewares[index](message, lambda m: call(index + 1))
            return await handler(message)
        return await call(0)

    async def _handle_message(self, message):
        for router in self.routers:
            handler = router.resolve(message)
            if handler:
                await self._process_middlewares(message, handler)
                break

    def run_polling(self):
        print(f"Polling started for {self.phone_number} (stub). Press Ctrl+C to stop.")
        try:
            while True:
                text = input("You: ")
                message = type("Message", (), {"text": text, "chat_id": self.phone_number})()
                asyncio.run(self._handle_message(message))
        except KeyboardInterrupt:
            print("Stopped.")