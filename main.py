from peluquería import *
import numpy as np
import random as rn
arreglo_cita = np.array([])
ciclo = True
def ingresar_cita(arreglo_cita):
    cita = peluqueria()
    c = False
    while c == False:
        c = cita.setCodigo_ate(input("Ingrese Codigo de atencion: "))
    c = False
    while c == False:
        c = cita.setDescr(input("Ingrese descripcion de atencion: "))
    c = False
    while c == False:
        c = cita.setNombre(input("Ingrese nombre: "))
    cita.fecha = input("Ingrese fecha de atencion: ")
    c = False

    while c == False:
        try:
            c = cita.setCosto(int(input("Ingrese costo de atencion: ")))
        except:
            print("Formato invalida, ingrese solo numeros")
    return np.append(arreglo_cita, cita)





def buscar_cita(arreglo_cita):
    codigo = input("Ingrese codigo de atencion: ")
    flag = True
    for cita in arreglo_cita:
        if codigo == cita.codigo_ate:
            flag = True
            print("Datos de la cita")
            print(f"codigo de atencion: {cita.codigo_ate}")
            print(f"Fecha de atencion: {cita.fecha}")
            print(f"Nombre cliente : {cita.nombre}")
            print(f"Descripcion de atencion: {cita.descr}")
            print(f"Costo: ${cita.costo}")


            if cita.costo >= 45000:
                print(f"Acceso a masaje facial: Si")
                prop = rn.randint(100,1000)
                print(f"Propina: {prop}")
            else:
                print("Acceso a masaje facial: No")
            break
    if flag == False:
        print("Cita no existe")


total=0
def lista(arreglo_cita):
    codigo = input("Ingrese codigo de atencion: ")

    for cita in arreglo_cita:
        if codigo == cita.codigo_ate:

            print("Datos de la cita")
            print(f"codigo de atencion:\t {cita.codigo_ate}")
            print(f"Fecha de atencion: \t {cita.fecha}")
            print(f"Nombre cliente : \t {cita.nombre}")
            print(f"Costo: \t ${cita.costo}")
            print(f"Descripcion de atencion: {cita.descr}")
            if cita.costo >= 20000:
                prop = rn.randint(100,1000)
                print(f"Propina: {prop}")
                total = cita.costo+ prop
                print(f"total \t ${total} ")
            break




def salir():
    print("Autor: Allan v1,  Adios")
    return False
while ciclo:
    print("Peluqueria “Mechas Locas”  ")
    print("1) pedir hora de atencion")
    print("2) Buscar hora de atencion")
    print("3) Imprimir atencion")
    print("4) Salir")
    try:
        op = int(input("Seleccione una opcion (1-4): "))
        match op:
            case 1:
                arreglo_cita=ingresar_cita(arreglo_cita)
            case 2:
                buscar_cita(arreglo_cita)
            case 3:
                lista(arreglo_cita)
            case 4:
                ciclo = salir()
            case _:
                print("Opcion invalida, seleccione (1-4)")
    except BaseException as error:
        print("Opcion invalida, seleccione (1-4)")
        print(f"{error}")