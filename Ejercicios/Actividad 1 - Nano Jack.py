import random

def generar_mazo(n):
    mazo=[]
    j=1
    while j<=n:
        for i in range(4): #Un mazo tiene 4 palos
            for c in range(13): #Cada palo tiene cartas del 1 al 13
                mazo.append(c+1)
        j=j+1
    random.shuffle(mazo)
    return mazo

def jugar(m): #Quita las cartas del mazo y suma sus valores
    cartas=[]
    suma=0
    while not suma>=21:
        if m==[]:
            suma=suma+0
        else:
            c=m.pop(0)
            suma=suma+int(c)
            cartas.append(c)
    return suma

def jugar_varios(m,j):
    sumas=[]
    for i in range(j):
        suma=jugar(m)
        sumas.append(suma)
    return sumas

n=6 #Representa el número de mazos y de jugadores
m=generar_mazo(n)
sumas=jugar_varios(m,n)

def ver_quien_gano(resultados): #OPTATIVO 1
    lista_ganadores=[]
    for i in range(len(resultados)):
        if resultados[i]==21:
            lista_ganadores.append(1)
        else:
            lista_ganadores.append(0)
    return lista_ganadores

ganadores=ver_quien_gano(sumas)

def experimentar(rep,n,m): #OPTATIVO 2
    veces_ganadas=[]
    for i in range(n): #Agrego ceros a la lista para después sumar
        veces_ganadas.append(0)
    for i in range(rep):
        lista_ganadores=ver_quien_gano(jugar_varios(m,n))
        for j in range(len(lista_ganadores)):
            if lista_ganadores[j]==1:
                veces_ganadas[j]=veces_ganadas[j]+1        
    return veces_ganadas

veces_ganadas=experimentar(3,5,generar_mazo(5))