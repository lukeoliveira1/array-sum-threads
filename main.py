import threading
import time
import matplotlib.pyplot as plt

from functions import create_array, split_array, threading_sum_array

n = [4, 8, 16, 32]
size = [1000, 10000, 100000, 1000000]

###############################################

times_threads_full_array_reference = []

for i in range(4):
    start_time = time.time()

    array = create_array(size[i])
    parts = split_array(array, n[i])
    result_thread = threading_sum_array(parts, n[i])

    end_time = time.time()

    times_threads_full_array_reference.append(end_time - start_time)

################################################

times_threads_part_reference_manual_sum = []

for i in range(4):
    threads_list = list()
    threads_sum_list = list()

    global array2
    array2 = create_array(size[i])
    n_threads = n[i]

    k, r = divmod(len(array2), n_threads)

    def threading_sum_array(start, end):

        def sum_part(array_part):
            total_sum = 0
            for i in array_part:
                total_sum += i
            threads_sum_list.append(total_sum)

        thread = threading.Thread(target=sum_part, args=(array2[start:end],))
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

    times_threads_part_reference_manual_sum.append(time_end - time_start)

#############################################################

times_threads_part_reference_sum = []

for i in range(4):

    threads_list = list()
    threads_sum_list = list()

    global array3
    array3 = create_array(size[i])
    n_threads = n[i]

    k, r = divmod(len(array3), n_threads)

    def threading_sum_array(start, end):

        def sum_part(array_part):
            part_sum = sum(array_part)
            threads_sum_list.append(part_sum)

        thread = threading.Thread(target=sum_part, args=(array3[start:end],))
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

    times_threads_part_reference_sum.append(time_end - time_start)

############################################################

plt.plot(
    size,
    times_threads_full_array_reference,
    marker="o",
    label="With Full Array Reference",
)
plt.plot(
    size,
    times_threads_part_reference_manual_sum,
    marker="o",
    label="With Part Array Reference And Manual Sum Array",
)
plt.plot(
    size,
    times_threads_part_reference_sum,
    marker="o",
    label="With Part Array Reference And Sum Array",
)
plt.xlabel("Array Size")
plt.ylabel("Time (s)")
plt.xscale("log")
plt.xticks(size, size)
plt.title("Comparison of Execution Time - List Sum Threads ")
plt.legend()
plt.grid(True)
plt.show()
