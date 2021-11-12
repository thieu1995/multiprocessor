#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu" at 11:35, 18/10/2021                                                               %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Nguyen_Thieu2                                  %
#       Github:     https://github.com/thieu1995                                                        %
# ------------------------------------------------------------------------------------------------------%

import multiprocessing
import time

start = time.perf_counter()


def do_something():
    print("Sleeping 1 second....")
    time.sleep(1)
    print("Done sleeping...")


if __name__ == '__main__':

    list_processors = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something)
        p.start()
        list_processors.append(p)

    for p in list_processors:
        p.join()

    finish = time.perf_counter()

    print(f"Finished in {round(finish - start, 2)} second(s)")
