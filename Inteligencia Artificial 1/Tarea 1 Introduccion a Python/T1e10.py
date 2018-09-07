
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0 ,item)

    def dequeue(self):
        return self.items.pop()

def printMenu():
    print("1. Imprimir Queue\n2. Agregar un elemento\n3. Eliminar un elemento\n0. Salir")

def printQueue():
    for x in myQueue.items:
        print(str(x))

def addElement(aux):
    myQueue.enqueue(aux)

def deleteElement():
    myQueue.dequeue()


myQueue = Queue()

opciones = 10
while opciones != 0:
    printMenu()
    opciones = int(input())
    if opciones == 1:
        printQueue()
    if opciones == 2:
        aux = input("Agregue su elemento\n")
        addElement(aux)
    if opciones == 3:
        print("Se elimnira el primer elemento agregado\n")
        deleteElement()
