#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu" at 09:43, 18/10/2021                                                               %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Nguyen_Thieu2                                  %
#       Github:     https://github.com/thieu1995                                                        %
# ------------------------------------------------------------------------------------------------------%

import time
import threading

start = time.perf_counter()


def do_something():
    print("Sleeping 1 second....")
    time.sleep(1)
    print("Done sleeping...")

threads = []
for _ in range(10):
    t = threading.Thread(target=do_something)  # Object
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} second(s)")
