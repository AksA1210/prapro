# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 21:27:26 2024

@author: user
"""


import numpy as np
import time

start = time.time()

# Create a 1000x1000 random NumPy array
random_array = np.random.rand(1000, 1000)

end = time.time()

# Print the array
print(random_array)

# Measure how long the creation takes
duration = end - start
print("Time taken for creation : ",duration,"seconds")

# Convert the array into bytes
array_bytes = random_array.tobytes()
print(array_bytes)

# Recreate the array from the bytes
shape = random_array.shape
dtype = random_array.dtype
recreated_array = np.frombuffer(array_bytes, dtype=dtype).reshape(shape)
print(recreated_array)