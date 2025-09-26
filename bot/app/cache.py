from cachetools import TTLCache
from functools import wraps
from typing import Callable, Any, Coroutine


cache = TTLCache(maxsize=500, ttl=300)


def make_key(user_id: int, category: str):
    return f'{category}:{user_id}'


def cached(category: str, flush: bool = False):
    def decorator(func: Callable[..., Coroutine[Any, Any, Any]]):
        @wraps(func)
        async def wrapper(user_id: int, *args, **kwargs):
            key = make_key(user_id, category)
            if key in cache and not flush:
                return cache[key]
            data = await func(user_id, *args, **kwargs)
            cache[key] = data
            return data
        return wrapper
    return decorator