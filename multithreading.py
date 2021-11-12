#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu" at 09:31, 18/10/2021                                                               %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Nguyen_Thieu2                                  %
#       Github:     https://github.com/thieu1995                                                        %
# ------------------------------------------------------------------------------------------------------%

## IO bound --> threading                   ==> Not parallel
## CPU bound --> multi-processing (cores)   ==> Parallel

## Thread: has problem with creating, destroying --> Fit for IO operators (read, write file)
##      + thread may slowdown your problem if using for computing.
## CPU bound: fit for computing, processing

import time

start = time.perf_counter()
start2 = time.time()

def do_something():
    print("Sleeping 1 second....")
    time.sleep(1)
    print("Done sleeping...")

do_something()
do_something()

finish = time.perf_counter()
finish2 = time.time()

print(f"Finished in {round(finish - start, 2)} second(s)")
print(f"Finished in {round(finish2 - start2, 2)} second(s)")
