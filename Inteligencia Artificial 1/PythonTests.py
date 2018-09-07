import random

M1 = [[random.randint(0,100) for x in range(2)] for y in range(3)]
M2 = [[random.randint(0,100) for x in range(2)] for y in range(3)]

V1 = [random.randint(0,100) for x in range(4)]
V2 = [random.randint(0,100) for x in range(4)]

numbers3 = [[0 for x in range(4)] for y in range(5)]

for x in range(5):
    for y in range(4):
        numbers3[x][y] = random.randint(1,100)

