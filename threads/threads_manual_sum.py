import random
import threading
import time


def create_array(size):
    return [random.randint(1, 1000) for _ in range(size)]


# usando um array global e compartilhando os "pedaços" dele
# usando a iteração nas threads para somar

################

threads_list = list()
threads_sum_list = list()

global array
array = create_array(1000000)
n_threads = 32

k, r = divmod(len(array), n_threads)


def threading_sum_array(start, end):

    def sum_part(array_part):
        total_sum = 0
        for i in array_part:
            total_sum += i
        threads_sum_list.append(total_sum)

    # print('aaaaaa: ', array[start:end])
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

print("Resultado: ", result)
print("Tempo: ", time_end - time_start, "s")
