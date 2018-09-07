from scipy.optimize import linprog

Aub = [[1,0],[0,1],[1,1],[0,-1],[-1,0]]
Bub = [8,10,9,0,0]
C = [600,800]
Aeq = [[40,50]]
Beq = 400


result = linprog(C,Aub,Bub,Aeq,Beq)

print(result)


