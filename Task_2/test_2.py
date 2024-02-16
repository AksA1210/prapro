import numpy as np
import time

def test_array_creation():
    start = time.time()
    random_array = np.random.rand(1000, 1000)
    end = time.time()
    assert random_array.shape == (1000, 1000)
    assert random_array is not None
    assert end - start < 1.0

def test_array_bytes_conversion():
    random_array = np.random.rand(1000, 1000)
    array_bytes = random_array.tobytes()
    assert array_bytes is not None
    assert len(array_bytes) > 0

def test_array_recreation():
    random_array = np.random.rand(1000, 1000)
    array_bytes = random_array.tobytes()
    shape = random_array.shape
    dtype = random_array.dtype
    recreated_array = np.frombuffer(array_bytes, dtype=dtype).reshape(shape)
    assert recreated_array.shape == random_array.shape
    assert np.array_equal(recreated_array, random_array)
