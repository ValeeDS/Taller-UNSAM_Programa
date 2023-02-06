import numpy as np
import random

#INDIVIDUALES
def crear_album(figus_total):
    album=[]
    for i in range(0,figus_total,1):
        album.append(0)
    return album #Album vacío con 'figus_total' espacios

def hayAlguno(l,e):
    for i in range(0,len(l),1):
        if l[i] == e:
            return True #Verifica que 'e' esté en la lista 'l'
    return False

def comprar_una_figu(figus_total):
    figu=random.randint(1,figus_total)
    return figu #Figurita comprada aleatoria

def cuantas_figus(figus_total):
    album=crear_album(figus_total)
    suma=0
    while hayAlguno(album,0)==True:
        f=comprar_una_figu(figus_total)
        album[f-1]=1
        suma=suma+1
    return suma #Cuantas figuritas se necesitaron comprar para llenarlo"

def estimacion(n_repeticiones,figus_total):
    lista_resultados=[]
    for i in range(0,n_repeticiones,1):
        result=cuantas_figus(figus_total)
        lista_resultados.append(result)
    prom=np.mean(lista_resultados)
    print("Hay que comprar "+str(prom)+" para completar las "+str(figus_total)+" figuritas")
    return prom
    
n_repeticiones1=1000
figus_total1=6
n_repeticiones2=100
figus_total2=670
Ri1=estimacion(n_repeticiones1,figus_total1)
Ri2=estimacion(n_repeticiones1,figus_total2)

#PAQUETES
def generar_paquete(figus_total,figus_paquete):
    paquete=[]
    for i in range(0,figus_paquete,1):
        paquete.append(random.randint(1,figus_total))
    return paquete

def cuantos_paquetes(figus_total,figus_paquete):
    album=crear_album(figus_total)
    suma=0
    while hayAlguno(album,0)==True:
        p=generar_paquete(figus_total,figus_paquete)
        for i in range(0,figus_paquete,1):
            f=p.pop(0)
            album[f-1]=1
        suma=suma+1
    return suma #Igual a cuantas_figus
    
def estimacion_paquetes(n_repeticiones,figus_total,figus_paquete):
    lista_resultados=[]
    for i in range(0,n_repeticiones,1):
        result=cuantos_paquetes(figus_total,figus_paquete)
        lista_resultados.append(result)
    prom=np.mean(lista_resultados)
    print("Hay que comprar "+str(prom)+" paquetes para completar las "+str(figus_total))
    return prom
    
figus_total= 670
figus_paquete=5
n_repeticiones=100
Rp=estimacion_paquetes(n_repeticiones,figus_total,figus_paquete)

#OPTATIVO 1
def estimar_probabilidad(n_repeticiones,figus_total,figus_paquete,paquetes):
    lista_resultados=[]
    for i in range(0,n_repeticiones,1):
        favorables=cuantos_paquetes(figus_total,figus_paquete)
        if favorables<=paquetes:
            prob=favorables/paquetes
            lista_resultados.append(prob)
    prob=np.mean(lista_resultados)
    print("La probabilidad estimada es del "+str(prob))

paquetes=800
O1=estimar_probabilidad(n_repeticiones,figus_total,figus_paquete,paquetes)

#OPTATIVO 2
def estimar_para_probabilidad(n_repeticiones,figus_total,figus_paquetes,probabilidad):
    lista_resultados=[]
    for i in range(n_repeticiones):
        favorables=probabilidad*cuantos_paquetes(figus_total,figus_paquete)
        lista_resultados.append(favorables)
    prom=np.mean(lista_resultados)
    print("Hay que comprar "+str(prom)+" paquetes")
    return prom

probabilidad=0.90
Paquetes=estimar_para_probabilidad(n_repeticiones,figus_total,figus_paquete,probabilidad)

#OPTATIVO 3
def generar_paquete_unicos(figus_total,figus_paquete):
    paquete=[]
    while len(paquete)<figus_paquete:
        figu=random.randint(1,figus_total)
        if not hayAlguno(paquete,figu):
            paquete.append(figu)
    return paquete

paq=generar_paquete_unicos(figus_total,figus_paquete)

#Después lo que habría que hacer es reemplazar 'generar_paquete' por esta