
import time

from app.utils.cache import TTLCache


def test_cache_returns_stored_value():
    cache = TTLCache(ttl_seconds=5)

    cache.set("cpu", 45.0)

    assert cache.get("cpu") == 45.0


def test_cache_expires_after_ttl():
    cache = TTLCache(ttl_seconds=0.1)

    cache.set("cpu", 45.0)
    time.sleep(0.2)

    assert cache.get("cpu") is None


def test_cache_returns_none_for_missing_key():
    cache = TTLCache()

    assert cache.get("missing") is None
