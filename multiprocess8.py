#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu" at 11:35, 18/10/2021                                                               %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Nguyen_Thieu2                                  %
#       Github:     https://github.com/thieu1995                                                        %
# ------------------------------------------------------------------------------------------------------%

import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second....")
    time.sleep(seconds)
    return f"Done sleeping...{seconds}"


if __name__ == '__main__':

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [2, 6, 3, 1, 5]
        results = executor.map(do_something, secs)

        for result in results:
            print(result)

    finish = time.perf_counter()

    print(f"Finished in {round(finish - start, 2)} second(s)")
