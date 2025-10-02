import time
import threading
import multiprocessing

def sleep_fnc(sec=1.1):
    print("inside sleep fnc")
    time.sleep(sec)
    print("finished sleep")

def compute_fnc():
    print("inside compute fnc")
    for x in range(1000000):
        _ = pow (x, 10)
    print("compute finished")

if __name__ == "__main__":
    # threading with sleep
    t1 = time.perf_counter()
    thread_list = [threading.Thread(target=sleep_fnc) for _ in range(5)]
    for th in thread_list:
        th.start()
    for th in thread_list:
        th.join()
    t2 = time.perf_counter()
    print("Threads (sleep):", round(t2 - t1, 2))

    # sequential sleep
    t1 = time.perf_counter()
    for _ in range(5):
        sleep_fnc()
    t2 = time.perf_counter()
    print("Sequential (sleep):", round(t2 - t1, 2))

    # multiprocessing with compute
    t1 = time.perf_counter()
    process_list = [multiprocessing.Process(target=compute_fnc) for _ in range(5)]
    for p in process_list:
        p.start()
    for p in process_list:
        p.join()
    t2 = time.perf_counter()
    print("Multiprocessing (compute):", round(t2 - t1, 2))

    # compute sequencial
    t1 = time.perf_counter()
    for _ in range(5):
        compute_fnc()
    t2 = time.perf_counter()
    print("Sequential (compute):", round(t2 - t1, 2))