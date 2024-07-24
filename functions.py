import random
import threading


def create_array(size):
    return [random.randint(1, 1000) for _ in range(size)]


def split_array(array, n_threads):
    list_parts = []
    k, r = divmod(len(array), n_threads)  # size of each part

    start = 0
    for i in range(n_threads):
        end = start + k + (1 if i < r else 0)
        array_part = array[start:end]
        list_parts.append(array_part)
        start = end

    return list_parts


def threading_sum_array(array_parts, n_threads):
    threads_sum_list = list()

    def sum_part(array_part, thread_id):
        part_sum = sum(array_part)
        threads_sum_list.append(part_sum)

    threads_list = list()

    for i in range(n_threads):
        thread = threading.Thread(target=sum_part, args=(array_parts[i], i + 1))
        threads_list.append(thread)
        thread.start()

    for thread in threads_list:
        thread.join()

    return sum(threads_sum_list)
