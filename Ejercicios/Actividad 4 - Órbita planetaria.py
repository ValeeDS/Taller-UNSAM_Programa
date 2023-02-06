import matplotlib.pyplot as plt
import numpy as np
import imageio

def coord_tierra(lista_x,lista_y,i):
    x=lista_x[i]
    y=lista_y[i]
    pos_tierra=[x,y]
    return pos_tierra

def calcula_delta(sol,pos_tierra):
    d=[]
    for i in range(2):
        di=sol[i]-pos_tierra[i]
        d.append(di)
    return d

def calcula_distancia(sol,pos_tierra):
    delta=calcula_delta(sol,pos_tierra)
    d=np.sqrt((delta[0])**2+(delta[1])**2)
    return d

def calcula_aceleracion(sol,pos_tierra):
    G=6.693e-11
    M=1.98e30
    delta=calcula_delta(sol,pos_tierra)
    dist=calcula_distancia(sol,pos_tierra)
    a=[]
    for i in range(2):
        Ai=(G*M/(dist**2))*(delta[i]/dist)
        a.append(Ai)
    return a

def realiza_Verlet(ayer,hoy,aceleracion_actual,dt):
    mañana=[]
    for i in range(2):
        ip=2*hoy[i]-ayer[i]+(aceleracion_actual[i]*(dt**2))
        mañana.append(ip)
    return mañana

def primeros_dias(lista_x,lista_y,sol):
    for i in range(2):
        pos_tierra=coord_tierra(lista_x,lista_y,i)
        aceleracion=calcula_aceleracion(sol,pos_tierra)
        lista_Ax.append(aceleracion[0])
        lista_Ay.append(aceleracion[1])
    
def ciclo_verlet(lista_x,lista_y,sol,dt,tiempo_total):
    primeros_dias(lista_x,lista_y,sol)
    for i in range (1, tiempo_total-1):
        hoy=coord_tierra(lista_x,lista_y,i)
        ayer=coord_tierra(lista_x,lista_y,i-1)
        aceleracion=calcula_aceleracion(sol,hoy)
        mañana=realiza_Verlet(ayer,hoy,aceleracion,dt)
        lista_x.append(mañana[0])
        lista_y.append(mañana[1])
        lista_Ax.append(aceleracion[0])
        lista_Ay.append(aceleracion[1])
        dias.append(i+1)

def hacer_foto(lista_x,lista_y,sol,dia):
    plt.clf()
    plt.plot(lista_x,lista_y,'grey')
    plt.plot(sol[0],sol[1],'yo',ms=20)
    plt.plot(lista_x[dia],lista_y[dia],'bo',ms=10)
    
def hacer_video(lista_x,lista_y,sol,nombre_video):
    lista_fotos=[]
    for i in range(len(lista_x)):
        if i%2==0:
            hacer_foto(lista_x,lista_y,sol,i)
            plt.savefig("Actividad 4 - "+nombre_video+'.png')
            lista_fotos.append(imageio.imread("Actividad 4 - "+nombre_video+'.png'))
        print(str(i)+" de "+str(len(lista_x))+" fotos guardadas")
    imageio.mimsave("Actividad 4 - "+nombre_video+'.mp4',lista_fotos)
    print('Video guardado')
    
def hacer_foto_ac(lista_x,lista_y,lista_Ax,lista_Ay,sol,dia):
    S=[sol[0],sol[1]]
    T=[lista_x[dia],lista_y[dia]]
    A=[lista_Ax[dia],lista_Ay[dia]]
    plt.clf()
    plt.plot(lista_x,lista_y,'grey')
    plt.plot(S[0],S[1],'yo',ms=20)
    plt.plot(T[0],T[1],'bo',ms=10)
    plt.arrow(T[0],T[1],A[0]*10**12.5,A[1]*10**12.5,width=10**9.5,color='g')
    
def hacer_video_ac(lista_x,lista_y,lista_Ax,lista_Ay,sol,nombre_video_ac):
    lista_fotos=[]
    for i in range(len(lista_x)):
        if i%2==0:
            hacer_foto_ac(lista_x,lista_y,lista_Ax,lista_Ay,sol,i)
            plt.savefig("Actividad 4 - "+nombre_video_ac+'.png')
            lista_fotos.append(imageio.imread("Actividad 4 - "+nombre_video_ac+'.png'))
        print(str(i)+" de "+str(len(lista_x))+" fotos guardadas")
    imageio.mimsave("Actividad 4 - "+nombre_video_ac+'.mp4',lista_fotos)
    print('Video guardado')

def grafico_distancia(dias,lista_x,lista_y,sol):
    dist=[]
    for i in range(len(dias)):
        T=coord_tierra(lista_x,lista_y,i)
        d=calcula_distancia(sol,T)
        dist.append(d)
    plt.title("Distancia vs días")
    plt.xlabel("Días")
    plt.ylabel("Distancia [m]")
    plt.plot(dias,dist)
    plt.show()
    
def calculo_velocidad(lista_x,lista_y,dt,dia):
    if not dia==0:
        hoy=coord_tierra(lista_x,lista_y,dia)
        ayer=coord_tierra(lista_x,lista_y,dia-1)
        d=calcula_distancia(hoy,ayer)
        v=d/dt
        return v

def grafico_velocidad(dias,lista_x,lista_y,dt):
    veloc=[]
    for i in range(len(dias)):
        v=calculo_velocidad(lista_x,lista_y,dt,i)
        veloc.append(v)
    plt.title("Velocidad vs días")
    plt.xlabel("Días")
    plt.ylabel("Velocidad [m/s]")
    plt.plot(dias,veloc)
    plt.show()

lista_x=[-147095000000.0,-147095000000.0] #lista de posiciones en x de la Tierra
lista_y=[0.0,2617920000.0] #lista de posiciones en y de la Tierra
lista_Ax=[]
lista_Ay=[]
sol=[0.0,0.0]
dt=60*60*24 #un día en segundos
tiempo_total=400 #cantidad de días al finalizar
dias=[0,1] #cantidad de dias iniciales

ciclo_verlet(lista_x,lista_y,sol,dt,tiempo_total)
grafico_distancia(dias,lista_x,lista_y,sol)
grafico_velocidad(dias,lista_x,lista_y,dt)

nombre_video="Prueba"
hacer_video(lista_x,lista_y,sol,nombre_video)
nombre_video_aceleracion="Prueba aceleración"
hacer_video_ac(lista_x,lista_y,lista_Ax,lista_Ay,sol,nombre_video_aceleracion)

#OPCIONAL 1
def grafico_conjunto(dias,lista_x,lista_y,sol,dt):
    veloc=[]
    dist=[]
    for i in range(len(dias)):
        v=calculo_velocidad(lista_x,lista_y,dt,i)
        veloc.append(v)
        T=coord_tierra(lista_x,lista_y,i)
        d=calcula_distancia(sol,T)
        dist.append(d)
    for i in range(len(dist)):
        dist[i]=dist[i]/(10**6.7)
    plt.title("Velocidad y Distancia vs días")
    plt.xlabel("Días")
    plt.ylabel("Velocidad [m/s](b) y Distancia [m](g)")
    plt.plot(dias,veloc,'b')
    plt.plot(dias,dist,'g')
    plt.show()

grafico_conjunto(dias,lista_x,lista_y,sol,dt)