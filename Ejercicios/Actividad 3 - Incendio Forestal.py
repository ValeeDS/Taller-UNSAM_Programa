import random
import numpy as np
import matplotlib.pyplot as plt

def generar_bosque(n):
    bosque=[]
    for i in range(0,n,1):
        bosque.append(0)
    return bosque

def brotes(bosque,p):
    for i in range(len(bosque)):
        b=random.random()
        if b < p:
            bosque[i]=1
    return bosque

def cuantos(bosque,tipo_celda):
    c=0
    for i in range(len(bosque)):
        if bosque[i] == tipo_celda:
            c=c+1
    return c

def rayos(bosque,f):
    for i in range(len(bosque)):
        r=random.random()
        if r < f and bosque[i]==1:
            bosque[i]=-1
    return bosque

def propagacion(bosque):
    for i in range(1,len(bosque)-1,1):
        if bosque[i]==-1:
            if bosque[i+1]==1:
                bosque[i+1]=-1
            if bosque[i-1]==1:
                bosque[i-1]=-1
    for i in range(len(bosque)-1,0,-1):
        if bosque[i]==-1:
            if bosque[i-1]==1:
                bosque[i-1]=-1
    if bosque[0]==-1 and bosque[1]==1:
        bosque[1]=-1
    if bosque[len(bosque)-1]==-1 and bosque[len(bosque)-2]==1:
        bosque[len(bosque)-2]=-1
    return bosque

def limpieza(bosque):
    for i in range(0,len(bosque),1):
        if bosque[i]==-1:
            bosque[i]=0
    return bosque

def ciclo(n_rep,n,p,f):
    bosque=generar_bosque(n)
    vivos=[]
    for t in range(1,n_rep+1,1):
        brotes(bosque,p)
        rayos(bosque,f)
        propagacion(bosque)
        limpieza(bosque)
        v=cuantos(bosque,1)
        vivos.append(v)
    return vivos

def variar_p(n_rep,n,f):
    prob=np.arange(0.00,1.00,0.01)
    promedios=[]
    for i in range(0,len(prob),1):
        p=prob[i]
        vivos=ciclo(n_rep,n,p,f)
        prom=np.mean(vivos)
        promedios.append(prom)
    return promedios
    
def dinamica_evolutiva(n,f,n_rep):
    bosque=generar_bosque(n)
    vivos=[]
    for t in range(1,n_rep+1,1):
        pes=[]
        b=random.random()
        for i in range(0,len(bosque),1):
            p=random.random()
            pes.append(p)
            if b < p:
                bosque[i]=1
        rayos(bosque,f)
        propagacion(bosque)
        if bosque[i]==1:
            pes[i]=pes[i]+0.05
        elif bosque[i]==-1:
            pes[i]=pes[i]-0.05
        limpieza(bosque)
        v=cuantos(bosque,1)
        vivos.append(v)
    return vivos

def grafico_dinamicasimple(n,f,n_rep):
    años=[]
    vivos=[]
    for i in range(1,n_rep+1,1):
        años.append(i)
    vivos=variar_p(n_rep,n,f)
    plt.title("Dinámica simple")
    plt.xlabel("Años")
    plt.ylabel("Árboles vivos")
    plt.plot(años,vivos)
    plt.show()
    
def grafico_dinamicaevolutiva(n,f,n_rep):
    años=[]
    vivos=[]
    for i in range(1,n_rep+1,1):
        años.append(i)
    vivos=dinamica_evolutiva(n,f,n_rep)
    plt.title("Dinámica evolutiva")
    plt.xlabel("Años")
    plt.ylabel("Árboles vivos")
    plt.plot(años,vivos)
    plt.show()
   
n=100
f=0.1
n_rep=100

grafico_dinamicasimple(n,f,n_rep)
grafico_dinamicaevolutiva(n,f,n_rep)
