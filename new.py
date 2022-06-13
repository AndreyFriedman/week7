import copy

import pandas as pd
import random
import numpy as np
from itertools import compress
import math

random.seed(1337)


def initialization(matrix):
    if (len(matrix) <= 1 or len(matrix[0]) <= 1):
        return
    solution2 = copy.deepcopy(matrix)

    for i in range(len(solution2) - 1):
        for j in range(len(solution2[0]) - 1):
            solution2[i + 1][j + 1] = "-"
    i = 0
    while i < len(solution2) - 1:
        x = random.randint(1, len(matrix[0]) - 1)

        solution2[i + 1][x] = "+"
        i = i + 1


    return solution2


def check(matrix, sol1, sol2, j, k):
    sum1 = 0
    sum2 = 0
    for i in range(len(matrix) - 1):
        if sol1[i + 1][k] == "+":
            sum1 = sum1 + int(matrix[i + 1][k])

    for i in range(len(matrix) - 1):
        if sol2[i + 1][j] == "+":
            sum2 = sum2 + int(matrix[i + 1][j])

    # print("######")
    # print(sum1)
    # print(sum2)

    if sum2 < sum1:
        return True, sum1, sum2

    if sum2 == sum1:
        subSum1 = subSum2 = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if sol1[i][j] == "+":
                    subSum1 = subSum1 + matrix[i][j]
                if sol2[i][j] == "+":
                    subSum2 = subSum2 + matrix[i][j]
        if subSum1 >= subSum2:
            return True, sum1, sum2

    return False, sum1, sum2


def simulator(matrix):
    if len(matrix) <= 1 or len(matrix[0]) <= 1:
        return
    sol1 = initialization(matrix)
    if len(matrix[0]) <= 2:
        return sol1
    temp = 10000

    for x in range(1000):
        i = random.randint(1, len(sol1) - 1)

        k = 0

        for z in range(len(sol1[0]) - 1):
            if sol1[i][z + 1] == "+":
                k = z + 1
                break
        j = random.randint(1, len(sol1[0]) - 1)
        while j == k:
            j = random.randint(1, len(sol1[0]) - 1)

        sol2 = copy.deepcopy(sol1)
        sol2[i][k] = "-"
        sol2[i][j] = "+"
        # print(i)
        # print(j)
        # print(k)
        # print(sol1)
        # print(sol2)

        c, old_cost, new_cost = check(matrix, sol1, sol2, j, k)

        b = (10000 - 0.1) / ((1000 - 1) * 10000 * 0.1)
        temp = temp / (1 + b * 0.1)
        p = math.e ** ((- new_cost - old_cost) / temp)

        if c is True and random.random() < p:
            sol1 = copy.deepcopy(sol2)

    return sol1


natun0 = [["", "M1", "M2", "M3", "M4"],
          ["J1", 14, 6, 8, 20],
          ["J2", 7, 4, 11, 20],
          ["J3", 3, 21, 5, 20],
          ["J4", 1, 1, 5, 20]]

natun1 = [["", "M1", "M2", "M3"],
          ["J1", 14, 6, 80],
          ["J2", 7, 4, 110],
          ["J3", 3, 21, 50]]

natun2 = [["", "M1", "M2"],
          ["J1", 14, 6],
          ["J2", 7, 4]]

natun3 = [["", "M1"],
          ["J1", 14]]

natun4 = [[""]]

natun5 = [["", "M1", "M2", "M3"],
          ["J1", 14, 60, 80],
          ["J2", 7, 40, 110],
          ["J3", 3, 210, 50]]

natun6 = [["", "M1"],
          ["J1", 14],
          ["J2", 7],
          ["J3", 3]]

natun7 = [["", "M1", "M2", "M3"],
          ["J1", 14, 6, 8]]

# print(initialization(natun0))
print(simulator(natun0))
