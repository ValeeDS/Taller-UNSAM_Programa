#%% Ejercicio

import numpy as np
import random
visualizacion=__import__('Actividad 6 - Visualizacion')

def crear_tablero(f,c):
    t=np.repeat(" ",(f+2)*(c+2)).reshape(f+2,c+2)
    for i in range(t.shape[0]):
        t[(i,0)]="M"
        t[(i,t.shape[1]-1)]="M"
    for j in range(t.shape[1]):
        t[(0,j)]="M"
        t[(t.shape[0]-1,j)]="M"
    return t

def vecinos_de(t,coord):
    i=coord[0]
    j=coord[1]
    vecinos=[]
    posiciones=[(i-1,j-1),(i-1,j),(i-1,j+1),(i,j+1),(i+1,j+1),(i+1,j),(i+1,j-1),(i,j-1)]
    for p in range(len(posiciones)):
        if not t[posiciones[p]]=="M":
            vecinos.append(posiciones[p])
    return vecinos

def buscar_adyacente(tablero,coord,objetivo):
    vecinos=vecinos_de(tablero,coord)
    adyacentes=[]
    for i in range(len(vecinos)):
        if tablero[vecinos[i]]==objetivo:
            adyacentes.append(vecinos[i])
    if adyacentes==[]:
        return adyacentes
    else:
        adyacente=adyacentes.pop(0)
        return adyacente

def mover(tablero,coord):
    vacia=buscar_adyacente(tablero,coord," ")
    animal=tablero[coord]
    if not animal==" ":
        if not vacia==[]:
            tablero[coord]=" "
            tablero[vacia]=animal
    return tablero
        
def alimentar(tablero,coord):
    if tablero[coord]=="L":
        antilope=buscar_adyacente(tablero,coord,"A")
        if not antilope==[]:
            tablero[coord]=" "
            tablero[antilope]="L"
    return tablero

def reproducir(tablero,coord):
    animal=tablero[coord]
    if not animal==" ":
        pareja=buscar_adyacente(tablero,coord,animal)
        if not pareja==[]:
            vacia=buscar_adyacente(tablero,coord," ")
            if not vacia==[]:
                tablero[vacia]=animal
    return tablero

def fase_mover(tablero):
    for i in range(1,tablero.shape[0]-1):
        for j in range(1,tablero.shape[1]-1):
            mover(tablero,(i,j))
    print(tablero)
    return tablero

def fase_alimentacion(tablero):
    for i in range(1,tablero.shape[0]-1):
        for j in range(1,tablero.shape[1]-1):
            alimentar(tablero,(i,j))
    print(tablero)
    return tablero
 
def fase_reproduccion(tablero):
    for i in range(1,tablero.shape[0]-1):
        for j in range(1,tablero.shape[1]-1):
            reproducir(tablero,(i,j))
    print(tablero)
    return tablero

def evolucionar(tablero):
    fase_alimentacion(tablero)
    print(tablero)
    fase_reproduccion(tablero)
    print(tablero)
    fase_mover(tablero)
    print(tablero)
    return tablero

def evolucionar_en_el_tiempo(tablero,k):
    for i in range(k):
        evolucionar(tablero)
    return tablero

def mezclar_celdas(tablero):
    celdas=[]
    for i in range(1,tablero.shape[0]-1):
        for j in range(1,tablero.shape[1]-1):
            celdas.append((i,j))
    random.shuffle(celdas)
    return celdas

def generar_tablero_azar(filas,columnas,n_antilopes,n_leones):
    tablero=crear_tablero(filas,columnas)
    celdas=mezclar_celdas(tablero)
    for i in range(n_antilopes):
        tablero[celdas.pop(0)]="A"
    for i in range(n_leones):
        tablero[celdas.pop(0)]="L"
    return tablero

#%% "OPTATIVOS"
    
import csv
import matplotlib.pyplot as plt

#OPTATIVO
def cuantos_de_cada(tablero):
    antilopes=0
    leones=0
    for i in range(tablero.shape[0]):
        for j in range(tablero.shape[1]):
            if tablero[(i,j)]=="L":
                leones=leones+1
            elif tablero[(i,j)]=="A":
                antilopes=antilopes+1
    res=[antilopes,leones]
    return res

def registrar_evolucion(tablero,k):
    individuos=[]
    for i in range(k):
        evolucionar(tablero)
        total=cuantos_de_cada(tablero)
        individuos.append(total)
    return individuos

def evolucion_grafico(tablero,k):
    evolucion_especies=registrar_evolucion(tablero,k)
    with open("Actividad 6 - Predpres.csv","w",newline="") as csvfile:
        csv_writer=csv.writer(csvfile)
        csv_writer.writerow(["antilopes","leones"])
        csv_writer.writerows(evolucion_especies)
    valores=np.loadtxt('Actividad 6 - Predpres.csv',delimiter=',',skiprows=1)
    plt.ylabel('Cantidad de Individuos')
    plt.xlabel('Ciclo')
    plt.plot(valores[:,0],label='antilopes')
    plt.plot(valores[:,1],label='leones')
    plt.legend()

#OPTATIVO+
def buscar_adyacente_aleatoria(tablero,coord,objetivo):
    i=coord[0]
    j=coord[1]
    vecinos=vecinos_de(tablero,(i,j))
    adyacentes=[]
    for i in range(len(vecinos)):
        if tablero[vecinos[i]]==objetivo:
            adyacentes.append(vecinos[i])
    if adyacentes==[]:
        return adyacentes
    else:
        posible=random.choice(adyacentes)
        return posible

def mover_aleatoria(tablero,coord):
    vacia=buscar_adyacente_aleatoria(tablero,coord," ")
    animal=tablero[coord]
    if not animal==" ":
        if not vacia==[]:
            tablero[coord]=" "
            tablero[vacia]=animal
    return tablero
        
def alimentar_aleatoria(tablero,coord):
    if tablero[coord]=="L":
        antilope=buscar_adyacente_aleatoria(tablero,coord,"A")
        if not antilope==[]:
            tablero[coord]=" "
            tablero[antilope]="L"
    return tablero

def reproducir_aleatoria(tablero,coord):
    animal=tablero[coord]
    if not animal==" ":
        pareja=buscar_adyacente_aleatoria(tablero,coord,animal)
        if not pareja==[]:
            vacia=buscar_adyacente_aleatoria(tablero,coord," ")
            if not vacia==[]:
                tablero[vacia]=animal
    return tablero

def evolucionar_en_el_tiempo_aleatoria(tablero,k):
    for i in range(k):
        for i in range(1,tablero.shape[0]-1):
            for j in range(1,tablero.shape[1]-1):
                alimentar_aleatoria(tablero,(i,j))
        print(tablero)
        for i in range(1,tablero.shape[0]-1):
            for j in range(1,tablero.shape[1]-1):
                reproducir_aleatoria(tablero,(i,j))
        print(tablero)
        for i in range(1,tablero.shape[0]-1):
            for j in range(1,tablero.shape[1]-1):
                mover_aleatoria(tablero,(i,j))
        print(tablero)
    return tablero

#OPTATIVO++
def crear_tablero_toroide(filas,columnas):
    t=np.repeat(" ",(filas)*(columnas)).reshape(filas,columnas)
    return t

def vecinos_de_toroide(t,coord):
    i=coord[0]
    j=coord[1]
    a=i-1
    b=i+1
    c=j-1
    d=j+1
    if i==0:
        a=t.shape[0]
    if i==t.shape[0]:
        b=0
    if j==0:
        c=t.shape[1]
    if j==t.shape[1]:
        d=0
    posiciones=[(a,c),(a,j),(a,d),(i,d),(b,d),(b,j),(b,c),(i,c)]
    return posiciones

#%%
    
visualizacion.simular(8,6,5,2,10) #Visualización gráfica de la evolución
#Matriz de 8x6 con 5 antílopes y 2 leones, evolución para 10 años
visualizacion.simular(6,6,7,5,5)

evolucion_grafico(generar_tablero_azar(4,6,6,3),4) #Optativo

evolucionar_en_el_tiempo_aleatoria(generar_tablero_azar(5,4,4,2),6) #Optativo+

print(vecinos_de(crear_tablero_toroide(5,6),(5,6))) #Optativo++