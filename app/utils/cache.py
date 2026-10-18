
import time


class TTLCache:
    def __init__(self, ttl_seconds=5):
        self.ttl_seconds = ttl_seconds
        self.cache = {}

    def get(self, key):
        item = self.cache.get(key)

        if item is None:
            return None

        value, expires_at = item

        if time.monotonic() >= expires_at:
            del self.cache[key]
            return None

        return value

    def set(self, key, value):
        expires_at = time.monotonic() + self.ttl_seconds
        self.cache[key] = (value, expires_at)
