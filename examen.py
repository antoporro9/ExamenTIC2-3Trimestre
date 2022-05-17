from pickle import TRUE
import random


# ----  Ejercicios ---- 

#Ejercicio 1

#Fin ejercicio 1


def mostrarmenu():

    print("****MENU****")
    print("1.Guardar Asignatura" )
    print("2.Ver nota media")
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
opc=mostrarmenu()

#Programa principal



#Ejercicio 3

def opci1(asignaturas):
    materia = input("Añade la asignatura: ")
    asignaturas.append(materia)
    




#Ejercicio 4



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


