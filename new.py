import copy

import pandas as pd
import random
import numpy as np
from itertools import compress
import math


# random.seed(1337)

def initialization(matrix):
    if (len(matrix) <= 1 or len(matrix[0]) <= 1):
        return
    solution2 = copy.deepcopy(matrix)
    solution1 = copy.deepcopy(matrix)


    for i in range(len(solution2)-1):
        for j in range(len(solution2[0])-1):
            solution2[i+1][j+1] = "-"
    i = 0
    while i < len(solution2)-1:
        x = random.randint(1, len(matrix[0]) - 1)

        # if solution1[x][0] != "-1":
        solution2[i+1][x] = "+"
            # solution1[x][0] = "-1"
        i = i + 1

    print(solution2)

    return solution2
#
# def initialization(matrix):
#     if (len(matrix) <= 1 or len(matrix[0]) <= 1):
#         return
#     solution2 = copy.deepcopy(matrix)
#     solution1 = copy.deepcopy(matrix)
#     # random.seed(1337)
#
#     for j in range(len(solution2) - 2):
#         solution2.remove(solution2[len(solution2) - 1])
#     solution2[0].remove(solution2[0][0])
#     solution2[1].remove(solution2[1][0])
#     i = 0
#
#     while i < len(solution2[0]):
#         x = random.randint(1, len(matrix) - 1)
#         if solution1[x][0] != "-1":
#             solution2[1][i - 1] = "J" + str(x)
#             solution1[x][0] = "-1"
#             i = i + 1
#
#     print(solution2)
#     print("bapbap")
#
#     return solution2


def check(matrix,sol1, sol2, j, k):
    print("*****")
    print(matrix)
    print(sol1)
    print(sol2)
    print(j)
    print(k)
    print("*****")
    sum1 = 0
    sum2 = 0
    for i in range(len(matrix)-1):
        if sol1[i+1][k] == "+":
            print(matrix[i+1][k])
            sum1 = sum1 + int(matrix[i+1][k])

    for i in range(len(matrix)-1):
        if sol2[i+1][j] == "+":
            print(matrix[i+1][j])
            sum2 = sum2 + int(matrix[i+1][j])

    print("######")
    print(sum1)
    print(sum2)

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
                    print(subSum1)
                    print(subSum2)
        if subSum1 >= subSum2:

            return True, sum1, sum2

    return False, sum1, sum2
#
#7
# 3
# 6
# 4
# def check(matrix, mat1, mat2):
#     print("*****")
#     print(mat1)
#     print(mat2)
#     print("*****")
#     sum1 = 0
#     sum2 = 0
#     for i in range(len(mat1[0])):
#         m = matrix[0].index("M" + str(i + 1))
#         j = mat1[1][i]
#         j = j[1:]
#         bap = matrix[int(j)][i + 1]
#         sum1 = sum1 + int(bap)
#
#     for i in range(len(mat2[0])):
#         m = matrix[0].index("M" + str(i + 1))
#         j = mat2[1][i]
#         j = j[1:]
#         bap = matrix[int(j)][i + 1]
#         sum2 = sum2 + int(bap)
#
#     print("######")
#     print(sum1)
#     print(sum2)
#
#     if sum2 < sum1:
#         return True, sum1, sum2
#
#     return False, sum1, sum2


def simulator(matrix):
    if (len(matrix) <= 1 or len(matrix[0]) <= 1):
        return
    sol1 = initialization(matrix)
    if len(matrix[0]) <= 2:
        return sol1
    temp = 10000

    for x in range(1000):
        i = random.randint(1, len(sol1) - 1)

        k = 0

        for x in range(len(sol1[0])-1):
            if sol1[i][x+1] == "+":
                k = x+1
                break
        j = random.randint(1, len(sol1[0]) - 1)
        while j == k:
            j = random.randint(1, len(sol1[0]) - 1)
        # for x in range(len(sol1)-1):
        #     if sol1[j][x+1] == "+":
        #         index2 = x+1
        #         print(j)
        #         print(index2)
        #         print(")))")
        #         break
        sol2 = copy.deepcopy(sol1)
        sol2[i][k] = "-"
        sol2[i][j] = "+"
        # bap1 = sol1[i][index1]
        # bap2 = sol1[j][index2]
        # print("!!!!!!!!!!!!!!")
        # print(bap1)
        # print(bap2)
        # print("!!!!!!!!!!!!!!")
        # sol2[index1][i] = bap2
        # sol2[index2][j] = bap1
        print(i)
        print(j)
        print(k)
        print(sol1)
        print(sol2)

        c, old_cost, new_cost = check(matrix,sol1, sol2, j, k)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(c)
        print(old_cost)
        print(new_cost)
        b = (10000 - 0.1) / ((1000 - 1) * 10000 * 0.1)
        temp = temp / (1 + b * 0.1)
        p = math.e ** ((- new_cost - old_cost) / temp)

        if c is True and random.random() < p:
            sol1 = copy.deepcopy(sol2)
            print(sol1)

    return sol1


# solution 30
# initialization with 1337 seed ['J2', 'J4', 'J1', 'J3']
natun0 = [["", "M1", "M2", "M3", "M4"],
          ["J1", 14, 6, 8, 20],
          ["J2", 7, 4, 11, 20],
          ["J3", 3, 21, 5, 20],
          ["J4", 1, 1, 5, 20]]

# solution 15
# initialization with 1337 seed ['J2', 'J1', 'J3']
natun1 = [["", "M1", "M2", "M3"],
          ["J1", 14, 6, 80],
          ["J2", 7, 4, 110],
          ["J3", 3, 21, 50]]

# solution 13
# initialization with 1337 seed ['J1', 'J2']
natun2 = [["", "M1", "M2"],
          ["J1", 14, 6],
          ["J2", 7, 4]]

# solution 14
# initialization with 1337 seed ['J1']
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




# print(initialization(natun6))
print(simulator(natun0))
