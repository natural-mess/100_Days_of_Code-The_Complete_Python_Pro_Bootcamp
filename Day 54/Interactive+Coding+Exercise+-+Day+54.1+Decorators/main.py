import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(func):
    def wrapper_func():
        func()
        run_time = time.time() - current_time
        print(f"{func.__name__} run speed: {run_time}s")
    return wrapper_func

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()