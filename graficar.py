import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

os.system ("g++ JuanVelasquez_Ejercicio30.cpp")
os.system ("./a.out")

a = np.loadtxt("data.dat")

#Código adaptado de https://matplotlib.org/api/animation_api.html 
fig, axes = plt.subplots()
x = np.linspace(0.0,1.0,a.shape[1])
axes.grid()
plot, = plt.plot(x,a[0])

def inicial():
    axes.set_xlabel("Posicion[metros]")
    axes.set_ylabel("U")
    axes.set_xlim(0.0,1.0)
    axes.set_ylim(-0.05,0.05)
    return plot,

def refresca(i):
    plot.set_ydata(a[i])
    axes.set_title("Tiempo: " + str("{0:.2f}".format(2*i/(len(a[0])-1))) + " segundos")
    return plot,   
    
    
ani = animation.FuncAnimation(fig,refresca,frames = range(len(a[0])),init_func = inicial, blit = True, repeat = True)
ani.save("movie.gif",fps = 20)

