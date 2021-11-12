#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu" at 09:51, 18/10/2021                                                               %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Nguyen_Thieu2                                  %
#       Github:     https://github.com/thieu1995                                                        %
# ------------------------------------------------------------------------------------------------------%

import time
import threading

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second(s)....")
    time.sleep(seconds)
    print("Done sleeping...")


threads = []
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5 ])  # Object
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} second(s)")
