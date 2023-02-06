import predpresa
import csv
import matplotlib.pyplot as plt
import numpy as np
import random

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
        predpresa.evolucionar(tablero)
        total=cuantos_de_cada(tablero)
        individuos.append(total)
    return individuos


tablero=predpresa.generar_tablero_azar(6,5,4,6)
evolucion_especies=registrar_evolucion(tablero,3)
with open("predpres.csv","w",newline="") as csvfile:
    csv_writer=csv.writer(csvfile)
    csv_writer.writerow(["antilopes","leones"])
    csv_writer.writerows(evolucion_especies)

valores=np.loadtxt('predpres.csv',delimiter=',',skiprows=1)
plt.ylabel('Cantidad de Individuos')
plt.xlabel('Ciclo')
plt.plot(valores[:,0],label='antilopes')
plt.plot(valores[:,1],label='leones')
plt.legend()

#OPTATIVO+
def buscar_adyacente_aleatoria(tablero,i,j,objetivo):
    vecinos=predpresa.vecinos_de(tablero,(i,j))
    adyacentes=[]
    for i in range(len(vecinos)):
        if tablero[vecinos[i]]==objetivo:
            adyacentes.append(vecinos[i])
    r=random.randint(0,len(adyacentes))
    if not adyacentes==[]:
        posible=adyacentes[r]
        return posible
    else:
        return adyacentes

def mover(tablero,coord):
    vacia=buscar_adyacente_aleatoria(tablero,coord," ")
    animal=tablero[coord]
    if not animal==" ":
        if not vacia==[]:
            tablero[coord]=" "
            tablero[vacia]=animal
    return tablero
        
def alimentar(tablero,coord):
    if tablero[coord]=="L":
        antilope=buscar_adyacente_aleatoria(tablero,coord,"A")
        if not antilope==[]:
            tablero[coord]=" "
            tablero[antilope]="L"
    return tablero

def reproducir(tablero,coord):
    animal=tablero[coord]
    if not animal==" ":
        pareja=buscar_adyacente_aleatoria(tablero,coord,animal)
        if not pareja==[]:
            vacia=buscar_adyacente_aleatoria(tablero,coord," ")
            if not vacia==[]:
                tablero[vacia]=animal
    return tablero

#OPTATIVO++
def crear_tablero_toroide(filas,columnas):
    t=np.repeat(" ",(filas)*(columnas)).reshape(filas,columnas)
    return t

def vecinos_de(t,coord):
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

tablero=crear_tablero_toroide(5,6)
vecinos=vecinos_de(tablero,(5,6))
print(vecinos)
