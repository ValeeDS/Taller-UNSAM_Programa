import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def crear_tablero(n):
    t=np.repeat(0,(n+2)*(n+2)).reshape(n+2,n+2)
    for i in range(t.shape[1]):
        t[(i,0)]=-1
        t[(i,t.shape[1]-1)]=-1
    for j in range(t.shape[0]):
        t[(0,j)]=-1
        t[(t.shape[1]-1,j)]=-1
    return t

def es_borde(tablero,coord):
    if tablero[coord]==-1:
        return True
    else:
        return False

def tirar_copo(tablero,coord):
    if not es_borde(tablero,coord)==True:
        tablero[coord]=tablero[coord]+1
    return tablero

def vecino_de(tablero,coord):
    if not es_borde(tablero,coord)==True:
        vecinos=[]
        i=coord[0]
        j=coord[1]
        if not es_borde(tablero,(i+1,j)):
            vecinos.append((i+1,j))
        if not es_borde(tablero,(i-1,j)):
            vecinos.append((i-1,j))
        if not es_borde(tablero,(i,j+1)):
            vecinos.append((i,j+1))
        if not es_borde(tablero,(i,j-1)):
            vecinos.append((i,j-1))
    return vecinos

def desbordar_posicion(tablero,coord):
    if tablero[coord]>=4:
        tablero[coord]=0
        vecinos=vecino_de(tablero,coord)
        for i in range(len(vecinos)):
            tirar_copo(tablero,vecinos[i])
    return tablero

def hay_que_desbordar(tablero):
    for i in range(tablero.shape[0]):
        for j in range(tablero.shape[1]):
            if tablero[(i,j)]>=4:
                return True
    else:
        return False

def desbordar_nieve(tablero):
    for i in range(tablero.shape[0]):
        for j in range(tablero.shape[1]):
            desbordar_posicion(tablero,(i,j))
    return tablero

def estabilizar(tablero):
     while (hay_que_desbordar(tablero)):
         desbordar_nieve(tablero)

def paso(tablero):
    i=int(tablero.shape[0]/2)
    j=int(tablero.shape[1]/2)
    coord=(i,j)
    tirar_copo(tablero,coord)
    estabilizar(tablero)
    return tablero

def crear_animacion(tablero,cant_iteraciones,animacion):
    ims=[]
    fig=plt.figure()
    for i in range(cant_iteraciones):
        paso(tablero)
        im=plt.imshow(tablero,animated=True)
        ims.append([im])
    print(tablero)
    ani=animation.ArtistAnimation(fig,ims,interval=50,blit=True,repeat_delay=400)
    print("Listo para guardar animación")
    ani.save("Actividad 5 - "+animacion+'.mp4')
    plt.show()

n=7 #Posiciones utilizables
cant_iteraciones=100 #100 copos añadidos a los tableros iniciales

t1=crear_tablero(n) #Tablero con todas las posiciones vacías inicialmente
crear_animacion(t1,cant_iteraciones,"Tablero 1")

#OPTATIVO
def crear_tablero_aleatorio(n,cant_copos): #Definición de funcion para OPTATIVO
    tablero=crear_tablero(n)
    for c in range(cant_copos):
        i=random.randint(0,tablero.shape[0]-1)
        j=random.randint(0,tablero.shape[1]-1)
        coord=(i,j)
        tirar_copo(tablero,coord)
    estabilizar(tablero)
    return tablero    

cant_copos=20 #copos arrojados en posiciones aleatorias
t2=crear_tablero_aleatorio(n,cant_copos) #Tablero aleatoriamente ocupado inicialmente - OPTATIVO
crear_animacion(t2,cant_iteraciones,"Tablero 2") #OPTATIVO

#OPTATIVO+
def tirar_copo_aleatorio(tablero):
    i=random.randint(0,tablero.shape[0]-1)
    j=random.randint(0,tablero.shape[1]-1)
    coord=(i,j)
    if not es_borde(tablero,coord)==True:
        tablero[coord]=tablero[coord]+1
    return tablero

def paso_aleatorio(tablero):
    tirar_copo_aleatorio(tablero)
    estabilizar(tablero)
    return tablero

def crear_animacion_aleatorio(tablero,cant_iteraciones,animacion):
    ims=[]
    fig=plt.figure()
    for i in range(cant_iteraciones):
        paso_aleatorio(tablero)
        im=plt.imshow(tablero,animated=True)
        ims.append([im])
    print(tablero)
    ani=animation.ArtistAnimation(fig,ims,interval=50,blit=True,repeat_delay=400)
    print("Listo para guardar animación")
    ani.save("Actividad 5 - "+animacion+'.mp4')
    plt.show()

t3=crear_tablero(n)
crear_animacion_aleatorio(t3,cant_iteraciones,"Tablero 3")