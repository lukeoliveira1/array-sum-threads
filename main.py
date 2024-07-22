import time
import matplotlib.pyplot as plt

from functions import (
    split_array,
    threading_sum_array,
    create_array,
    trivial_split_array_and_sum,
)


n = [4, 8, 16, 32]
size = [1000, 10000, 100000, 1000000]

# n = input("How many threads do you want: ")
# size = int(input("What size of array do you want: ")

times_threading = []

for i in range(4):
    start_time = time.time()

    array = create_array(size[i])
    parts = split_array(array, n[i])
    result_thread = threading_sum_array(parts, n[i])

    end_time = time.time()

    times_threading.append(end_time - start_time)


times_trivial = []

for i in range(4):
    start_time = time.time()

    array = create_array(size[i])
    result_trivial = trivial_split_array_and_sum(array, n[i])

    end_time = time.time()

    times_trivial.append(end_time - start_time)


plt.plot(size, times_threading, marker="o", label="Threading Sum Array")
plt.plot(size, times_trivial, marker="o", label="Trivial Sum Array")
plt.xlabel("Tamanho do Array")
plt.ylabel("Tempo (segundos)")
plt.title("Comparação do Tempo de Execução")
plt.legend()
plt.grid(True)
plt.show()
