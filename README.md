# Funcache
Caching function outputs by hashing inputs using MetroHash.

## Example
```python
from timeit import timeit

import numpy as np
from funcache import cache

@cache("__cache__")
def linear(data, weight, bias):
    return data @ weight + bias

data = np.random.normal(size=1 << 64)
weight = np.random.normal(size=1 << 64)
bias = 5

dtime = timeit(lambda: linear(data, weight, bias), number=1)
print("First execution time: {:.2f}".format(dtime))

dtime = timeit(lambda: linear(data, weight, bias))
print("Second execution time: {:.2f}".format(dtime))
```
