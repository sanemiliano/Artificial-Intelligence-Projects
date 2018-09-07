
def factorial(num):
   if num != 0:
       return num * factorial(num-1)
   return 1

def sum(num1,num2):
   return num1 + num2


print(factorial(8))
print(sum(4,98))