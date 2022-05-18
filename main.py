import pandas as pd
from string import ascii_lowercase
import random
import numpy as np
from itertools import compress
import math

resource = [random.choice(ascii_lowercase) + random.choice(ascii_lowercase) + random.choice(ascii_lowercase) + str(_)
            for _ in range(100)]
project = [random.choice(ascii_lowercase) + random.choice(ascii_lowercase) +
           str(_) for _ in range(50)]

bicycle = ["Tire", "Seat", "Chain", "Tube", "Brakes"]
car = ["Engine", "Tire", "Brakes", "Exhaust", "Seat", "Airbag", "Seatbelt"]

random.seed(1337)
supplier = pd.DataFrame({
    "name": resource,
    "bicycle": random.choices(bicycle, k=100),
    "car": random.choices(car, k=100)
})

factory = pd.DataFrame({
    "project": project,
    "bicycle": random.choices(bicycle, k=50),
    "car": random.choices(car, k=50)
})

print(supplier.head())
print(factory.head())
print("------------------")


def schedule_display(sol):
    sup = []
    fuc = []
    supitem = []
    fucitem = []
    slots = []
    for i in range(len(factory)): slots += [i, i]

    for i in range(len(sol)):
        x = int(sol[i])
        sup.append(supplier.name[i])
        pr = factory.project[slots[x]]
        fuc.append(pr)
        supitem.append(list(supplier.iloc[i, 1:]))
        pr_bool = factory.project == pr
        pr_ind = list(compress(range(len(pr_bool)), pr_bool))
        fucitem.append(list(factory.iloc[pr_ind, 1:].values[0]))
        del slots[x]

    res_proj = pd.DataFrame({"Supplier": sup, "Factory": fuc, "Sup_Item": supitem, "Fac_Needs": fucitem})

    return res_proj.sort_values("Factory")


def cost_func(sol):
    cost = 0
    slots = []
    for i in range(len(factory)): slots += [i, i]

    for i in range(len(sol)):
        x = int(sol[i])
        proj = np.array(factory.iloc[slots[x], 1:])
        res = np.array(supplier.iloc[i, 1:])
        cost += sum(res != proj)

        del slots[x]

    return cost


def simulator(solu):
    step = 3
    cool = 0.99
    temp = 10000
    current_sol = [float(random.randint(solu[i][0], solu[i][1])) for i in range(len(solu))]
    while temp > 0.1:
        i = random.randint(0, len(solu) - 1)

        direction = random.randint(- step, step)

        new_sol = current_sol[:]
        new_sol[i] += direction
        if new_sol[i] < solu[i][0]:
            new_sol[i] = solu[i][0]
        elif new_sol[i] > solu[i][1]:
            new_sol[i] = solu[i][1]

        current_cost = cost_func(current_sol)
        new_cost = cost_func(new_sol)
        p = math.e ** ((- new_cost - current_cost) / temp)

        if new_cost < current_cost or random.random() < p:
            current_sol = new_sol

        temp = temp * cool
    return current_sol


solution = [(0, (len(factory) * 2) - i - 1) for i in range(0, len(factory) * 2)]

schedule = simulator(solution)

schedule_df = schedule_display(schedule)
print(schedule_df.head(20))
