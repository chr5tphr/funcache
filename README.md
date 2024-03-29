# Funcache
Caching function outputs by hashing inputs using MetroHash.

## Example
```python
from timeit import timeit
from shutil import rmtree

import numpy as np
from funcache import cache

cache_path = '/tmp/__democache__'

# default path to store cache can be set like the following:
@cache(cache_path)
def linear(data, weight, bias):
    return data @ weight + bias

for size in [1024, 2048, 4096, 8192]:
    data = np.zeros((size, size))
    weight = np.zeros((size, size))
    bias = np.zeros((size,))

    # the original, uncached function can be accessed as linear.__wrapped__
    dtime_u = timeit(
        lambda: linear.__wrapped__(data, weight, bias),
        number=1
    )

    # caching path can also be set using the keyword argument '_cache',
    # and disabled by setting it to None
    dtime_1 = timeit(
        lambda: linear(data, weight, bias, _cache=cache_path),
        number=1
    )

    dtime_2 = timeit(lambda: linear(data, weight, bias), number=1)

    print("Size: {}".format(size))
    print("    Uncached: {:.3f}s".format(dtime_u))
    print("    Cached 1: {:.3f}s".format(dtime_1))
    print("    Cached 2: {:.3f}s".format(dtime_2))

rmtree(cache_path)
```
