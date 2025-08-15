import time

def timer(fnc):
    def wrapper(*args, **kwargs):
        start = time.time()
        fnc(*args, **kwargs)
        end = time.time()
        print("Function took {:.2f} seconds".format(end-start))
    
    return wrapper

@timer
def sleep_fnc(s):
    time.sleep(s)

@timer
def sleep_double(s):
    time.sleep(s * 2)

sleep_fnc(3)
sleep_double(2)