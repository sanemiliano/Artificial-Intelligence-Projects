
Contactos =  {"Emiliano":949851, "Luis":197875, "Sebastian":484965,"Alberto":494952,"Francisco":46548}

def printNames():
    print(Contactos.keys())

def addNewContact():
    nombre = input("Ingrese el nombre\n")
    numero = int(input("Ingrese el numero\n"))
    Contactos[nombre] = numero

def consultName():
    toCheck = input("Por favor ingrese el nombre\n")
    print(Contactos[toCheck])

def printMenu():
    print("1.- Imprimir Nombres en la Agenda")
    print("2. Consultar el teléfono de un contacto")
    print("3. Agregar un nuevo contacto")
    print("0. Salir")

opciones = 10
while opciones != 0:
    printMenu()
    opciones = int(input())
    if opciones == 1:
        printNames()
    if opciones == 2:
        consultName()
    if opciones == 3:
        addNewContact()



