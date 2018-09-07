
Matrix = [[0 or x in range(3)] for y in range(3)f]
V = [1,2,3,4,5,6,7,8,9]

cont = 1

for x in range(3):
    for y in range(3):
        Matrix[x][y] = cont
        cont += 1

print(Matrix[0][1])

for x in range(3):
    print(Matrix[x][1])

for x in range(3):
    print(Matrix[2][x])

sum = 0
for x in range(9):
    sum += V[x]
    print(V[x])

min = 100000

for x in range(9):
    if V[x] < min:
        min = V[x]

maxF2 = 0
maxF3 = 0
maxF1 = 0

maxC1 = 0
maxC2 = 0
maxC3 = 0

for x in range(3):
    for y in range(3):
        if x == 0:
            if maxF1 < Matrix[x][y]:
                maxF1 = Matrix[x][y]
        if x == 1:
            if maxF2 < Matrix[x][y]:
                maxF2 = Matrix[x][y]
        if x == 2:
            if maxF3 < Matrix[x][y]:
                maxF3 = Matrix[x][y]
        if y == 0:
            if maxC1 < Matrix[x][y]:
                maxC1 = Matrix[x][y]
        if y == 1:
            if maxC2 < Matrix[x][y]:
                maxC2 = Matrix[x][y]
        if y == 2:
            if maxC3 < Matrix[x][y]:
                maxC3 = Matrix[x][y]


print ("Minimo de V",min)
print("Promedio de V",sum/9)

print("Maximo de columna 1 ",maxC1)
print("Maximo de columna 2 ",maxC2)
print("Maximo de columna 3 ",maxC3)

print("Maximo de fila 1 ",maxF1)
print("Maximo de fila 2 ",maxF2)
print("Maximo de fila 3 ",maxF3)








