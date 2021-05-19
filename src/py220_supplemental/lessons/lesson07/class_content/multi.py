from multiprocessing import Pool
import functools
import time


def time_me(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Ran {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


def fibo(n):
    if n <= 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)


@time_me
def calc_for_serial(one_range):
    results = []
    for num in one_range:
        results.append([fibo(i) for i in range(num)])
    return results


@time_me
def calc_for_parallel(one_range):
    results = [fibo(i) for i in range(one_range)]
    return results


@time_me
def do_parallel(runs):
    size = len(runs)
    # results = []
    with Pool(size) as p:
        [results] = [p.map(calc_for_parallel, runs)]
    return results


@time_me
def do_serial(runs):
    results = []
    results.append(calc_for_serial(runs))
    [results] = results
    return results


@time_me
def main():
    ranges = ((10, 12, 5, 7, 4, 3, 2), (35, 30, 25, 40), (40, 38, 42))
    parallel = []
    serial = []
    for number_set in ranges:
        parallel.append(do_parallel(number_set))
        serial.append(do_serial(number_set))


if __name__ == "__main__":
    main()
