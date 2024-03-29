import time
import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second(s) ...")
    time.sleep(seconds)
    return "Done Sleeping..."


with concurrent.futures.ProcessPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1)
    print(f1.result())
    f2 = executor.submit(do_something, 1)
    print(f2.result())

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} seconds(s)")
