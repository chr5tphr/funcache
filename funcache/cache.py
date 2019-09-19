import pickle
import os

from .hashing import ext_hash

def cache(default_cache='.__cache__'):
    def decorator(func):
        def wrapper(*args, _cache=default_cache, **kwargs):
            if _cache is not None:
                os.makedirs(_cache, exist_ok=True)
                hash_hex = ext_hash((func.__name__, args, kwargs))
                fname = os.path.join(_cache, hash_hex)
                if os.path.exists(fname):
                    with open(fname, 'rb') as fp:
                        result = pickle.load(fp)
                else:
                    result = func(*args, **kwargs)
                    with open(fname, 'wb') as fp:
                        pickle.dump(result, fp)
                return result
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator
