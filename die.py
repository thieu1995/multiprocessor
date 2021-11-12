#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu" at 09:40, 27/10/2021                                                               %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Nguyen_Thieu2                                  %
#       Github:     https://github.com/thieu1995                                                        %
# ------------------------------------------------------------------------------------------------------%

import numpy as np
import concurrent.futures as parallel
import time

def fitness(solution):
    return np.sum(solution**2)

def create_solution():
    pos = np.random.uniform(0, 1, 5)
    fit = fitness(pos)
    return [pos, fit]

def create_population(size):
    pop = []
    with parallel.ProcessPoolExecutor() as executor:
        list_executors = [executor.submit(create_solution) for _ in range(size)]
        # This method yield the result everytime a thread finished their job.
        for f in parallel.as_completed(list_executors):
            pop.append(f.result())
    return pop


if __name__ == "__main__":
    pop = create_population(10)
    for agent in pop:
        print(agent[1])
