import numpy as np
import matplotlib.pyplot as plt
import os

os.system ("g++ JuanVelasquez_Ejercicio30.cpp")
os.system ("./a.out")

a = np.loadtxt("data.dat")

x = np.linspace(0.0,1.0,a.shape[1])

plt.figure()
plt.plot(x,a[0,:])
plt.plot(x,a[1,:])
plt.xlabel("Posicion[metros]")
plt.ylabel("U")
plt.savefig("grafica.png")

