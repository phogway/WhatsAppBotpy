class Router:
    def __init__(self):
        self.handlers = []

    def message(self, filter_func):
        def decorator(func):
            self.handlers.append((filter_func, func))
            return func
        return decorator

    def resolve(self, message):
        for filter_func, handler in self.handlers:
            if filter_func(message):
                return handler
        return None