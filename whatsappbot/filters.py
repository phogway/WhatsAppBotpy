class F:
    def __init__(self, func):
        self.func = func

    def __eq__(self, other):
        return F(lambda m: self.func(m) == other)

    def __call__(self, message):
        return self.func(message)

    @staticmethod
    def text(message):
        return getattr(message, "text", "")

    @staticmethod
    def contains(substring):
        return F(lambda m: substring in getattr(m, "text", ""))