import numpy as np
import random

def crear_tablero(filas,columnas):
    t=np.repeat(" ",(filas+2)*(columnas+2)).reshape(filas+2,columnas+2)
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

#valle=crear_tablero(3,4)

#coordenadas de animales
#filas=[1,2,2,3,1]
#columnas=[3,1,3,1,1]
#animal=['A','A','A','A','L']

#for i in range(len(animal)):
#    valle[(filas[i],columnas[i])]=animal[i]

