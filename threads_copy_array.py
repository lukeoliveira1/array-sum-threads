import time

from functions import create_array, split_array, threading_sum_array

# Passing the full array reference

# n = input("How many threads do you want: ")
# size = int(input("What size of array do you want: ")

n_threads = 32

times_threading = []

start_time = time.time()

array = create_array(1000000)
parts = split_array(array, n_threads)
result = threading_sum_array(parts, n_threads)

end_time = time.time()


print("Result: ", result)
print("Time: ", end_time - start_time, "s")
