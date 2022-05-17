from pickle import TRUE
import random


# ----  Ejercicios ---- 

#Ejercicio 1

#Fin ejercicio 1


def mostrarmenu():

    print("****MENU****")
    print("1.Guardar asignatura" )
    print("2.Borrar asignatura")
    print("3.Ver nota media")
    print("4.Ver todas las asignaturas")
    print("5.Salir")
    bandera=True

    while bandera==True:
        try:
            opc=int(input("¿Qué opción desea?:"))
            bandera=False
        except:
            print("Esa opción no es válida")
            bandera=True
    if opc==5:
        print("Adiosito...")
    return opc


#Programa principal



#Ejercicio 3

def opci1(asignaturas):
    materia = input("Añade la asignatura: ")
    asignaturas.append(materia)
    




#Ejercicio 4

def opci2(asignaturas):
    borrar=input("Asignatura que desea borrar")
    asignaturas.remove(borrar)


#Ejercicio 2


opc = mostrarmenu()
asignaturas=[]
while (opc >= 1) and (opc < 5):
    if opc == 1:
        opci1(asignaturas)
    elif opc == 2:
        print("2.Borrar asignatura")
    elif opc == 3:
        print("3.Ver Nota media")
    elif opc == 4:
        print("4.Ver asignaturas")

    opc = mostrarmenu()


#Ejercicio 5

def numRandom():
    numrand = []
    numnotas = int(input("¿Cuántas notas vas a introducir?: "))
    num = 0

    for i in range(0, numnotas):
        num = random.randint(0, 10)
        numrand.append(num)
    
    return numrand
#Ejercicio6

def opcion3():
    numAle = numRandom()
    total = 0
    contador = 0

    for i in numAle:
        total = total + i
        contador = contador + 1
    
    media = total / contador
    
    return media

#Ejercicio 7

def opci(asignaturas):
    print("********* Asignaturas matriculadas *********")
    contador = 0

    for i in asignaturas:
        contador = contador + 1
    
    for i in range(0, contador):
        print(i+1, ".", asignaturas[i])
    
    print("*** Fin asignaturas matriculadas ***")
