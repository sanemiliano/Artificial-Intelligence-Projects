import random

numbers = []

b = 5
cont = 0

while b <= 1000:
    numbers.append(b)
    b += 5
    cont += 1

Matrix = [[0 for x in range(4)] for y in range(2)]

numbers2 = [1 for x in range(10)]

print("Columnas: 2")
print("Filas: 4")

print("Elementos en V: 5")

numbers3 = [[0 for x in range(4)] for y in range(5)]

for x in range(5):
    for y in range(4):
        numbers3[x][y] = random.randint(1,100)
        
