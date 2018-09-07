
def getSize(Mystring):
   return Mystring.__len__()

def isPalindrome(Mystring):
    end = Mystring.__len__() - 1
    begin = 0
    while(begin <= end):
        if Mystring[begin] != Mystring[end]:
            print("No es palidroma")
            break
        begin += 1
        end -= 1
        if begin > end:
            print("Es palindroma")

def print3Times(cadena):
    print(cadena,cadena,cadena)

cadena = input("Ingrese un palabra\n")

print(getSize(cadena))
isPalindrome(cadena)
print3Times(cadena)