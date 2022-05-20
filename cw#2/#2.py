from multiprocessing import Process
from random import randint
from time import time


def is_arr_sum_even() -> bool:
    arr = [randint(-10000, 10000) for i in range(10**6)]
    return sum(arr) % 2 == 0


def coherent():
    print('---Coherent---')
    start = time()
    for i in range(4):
        is_arr_sum_even()
    print(f'{time() - start} ns')


def multiproc():
    print('---Multiprocessing(4)---')
    start = time()
    processes = [Process(target=is_arr_sum_even) for i in range(4)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    print(f'{time() - start} ns')


def main():
    coherent()
    multiproc()


if __name__ == '__main__':
    main()