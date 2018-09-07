
number = input("Por favor ingresa un numero\n")

count = 0;
det = 0

while(count < number.__len__()):
    if number[count] == "5":
        det = 1
        print("yes")
        break
    count += 1;

if det == 0:
    print("No")
