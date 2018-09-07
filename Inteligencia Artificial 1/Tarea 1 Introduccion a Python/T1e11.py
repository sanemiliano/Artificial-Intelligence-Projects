
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0 ,item)

    def pop(self):
        return self.items.pop(0)

def printMenu():
    print("1. Imprimir Stack\n2. Agregar un elemento\n3. Eliminar un elemento\n0. Salir")

def printStack():
    for x in myStack.items:
        print(str(x))

def addElement(aux):
    myStack.push(aux)

def deleteElement():
    myStack.pop()


myStack = Stack()

opciones = 10
while opciones != 0:
    printMenu()
    opciones = int(input())
    if opciones == 1:
        printStack()
    if opciones == 2:
        aux = input("Agregue su elemento\n")
        addElement(aux)
    if opciones == 3:
        print("Se elimnira el primer elemento agregado\n")
        deleteElement()
