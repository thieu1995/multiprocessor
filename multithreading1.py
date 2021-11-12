#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu" at 09:39, 18/10/2021                                                               %
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


t1 = threading.Thread(target=do_something)      # Object 1
t2 = threading.Thread(target=do_something)      # Object 2

t1.start()
t2.start()

t1.join()
t2.join()       # Finished their code before print out line below

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} second(s)")
