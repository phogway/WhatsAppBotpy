class State:
    _storage = {}

    async def set_state(self, chat_id, state):
        self._storage[chat_id] = {"state": state, "data": {}}

    async def update_data(self, chat_id, **kwargs):
        if chat_id in self._storage:
            self._storage[chat_id]["data"].update(kwargs)

    async def get_data(self, chat_id):
        return self._storage.get(chat_id, {}).get("data", {})

    async def finish(self, chat_id):
        if chat_id in self._storage:
            del self._storage[chat_id]