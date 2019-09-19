import pickle

from metrohash import MetroHash128

try:
    from numpy import ndarray
except ImportError:
    class ndarray: pass

try:
    from torch import Tensor
except ImportError:
    class Tensor: pass


class Hasher(MetroHash128):
    def write(self, data):
        self.update(data)
        return len(data)


class HashPickler(pickle.Pickler):
    @staticmethod
    def numpy_id(obj):
        return (
            obj.dtype.name,
            obj.shape,
            '{:.2e}'.format(obj.mean()),
            '{:.2e}'.format(obj.std()),
        )

    def persistent_id(self, obj):
        if isinstance(obj, ndarray):
            return self.numpy_id(obj)
        elif isinstance(obj, Tensor):
            return self.numpy_id(obj.numpy())
        else:
            return None


def ext_hash(data):
    hasher = Hasher()
    HashPickler(hasher).dump(data)
    return hasher.hexdigest()
