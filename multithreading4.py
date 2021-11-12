#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu" at 09:55, 18/10/2021                                                               %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Nguyen_Thieu2                                  %
#       Github:     https://github.com/thieu1995                                                        %
# ------------------------------------------------------------------------------------------------------%

import time
import concurrent.futures           # Simple and easy way to use multithreading (not handy craft)

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second(s)....")
    time.sleep(seconds)
    return "Done sleeping..."

# Use futures better with context block to avoid error which can happen
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit to schedule function, the future object can check result, status (running, finishing)
    f1 = executor.submit(do_something, 1.5)         # Futures object
    f2 = executor.submit(do_something, 1.5)

    # Run the result method, it will wait around until the function is completed
    print(f1.result())
    print(f2.result())


# threads = []
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])  # Object
#     t.start()
#     threads.append(t)
# for thread in threads:
#     thread.join()

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} second(s)")
