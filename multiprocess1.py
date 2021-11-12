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
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    p1.start()
    p2.start()

    ## Asynchronous (Khong dong bo)

    finish = time.perf_counter()

    print(f"Finished in {round(finish - start, 2)} second(s)")

    ## This case: Start process but not finished it yet. Then process the above line immediatly
