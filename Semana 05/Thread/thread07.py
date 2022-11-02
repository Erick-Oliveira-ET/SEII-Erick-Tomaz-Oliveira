import time
import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second(s) ...")
    time.sleep(seconds)
    return f"Done Sleeping...after {seconds} second(s)"


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 3, 2, 1]
    results = executor.map(do_something, secs)  # return all in order of execution

    for result in results:
        print(result)

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} seconds(s)")
