import threading
import time

from functions import create_array

# Passing a part of the array reference


threads_list = list()
threads_sum_list = list()

global array
array = create_array(1000000)
n_threads = 32

k, r = divmod(len(array), n_threads)


def threading_sum_array(start, end):

    def sum_part(array_part):
        part_sum = sum(array_part)
        threads_sum_list.append(part_sum)

    thread = threading.Thread(target=sum_part, args=(array[start:end],))
    threads_list.append(thread)
    thread.start()


time_start = time.time()

start = 0
for i in range(n_threads):
    end = start + k + (1 if i < r else 0)
    thread = threading_sum_array(start, end)
    start = end

for thread in threads_list:
    thread.join()

result = sum(threads_sum_list)

time_end = time.time()

print("Result: ", result)
print("Time: ", time_end - time_start, "s")
