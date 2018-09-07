num = int(input("Por favor ingresa un numero\n"))


def Find5(number):
    if(number % 10 == 5):
        return 1
    else:
        if(number > 10):
            return 0 + Find5(int(number / 10))
        else:
            return 0


print(Find5(num))