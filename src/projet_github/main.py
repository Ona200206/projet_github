"""blablabla"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf
from matplotlib.animation import FuncAnimation


# Initialisation des grandeurs numériques
D = 1
Temps = 0.3
NTemps = 4000
dt = Temps/NTemps
t=np.linspace(0,Temps, NTemps)
L = 10
NX=400
dx = L/(NX-1)
x = np.linspace(-400, 400, NX)

### MAIN PROGRAM ###

# Initialisation
xlim=10
T = 0.5*D*(erf(xlim-x)-erf(-xlim-x))

# Initialisation des variables pour le calcul
Theta = T[:,np.newaxis]
MD = np.zeros((NX))


# Résolution de l'équation de diffusion
for n in range(0,NTemps) :

    MD[1:-1] = dt * D * (T[:-2] - 2 * T[1:-1] + T[2:]) / (dx**2)
    T += MD

    Theta = np.concatenate([Theta, T[:,np.newaxis]], axis = 1)


fig1 = plt.figure(figsize=(8,6))
# Préparation pour l'animation
def animate(i):
    plt.clf()
    Y = Theta[:,i]
    plt.plot(x, Y, color = plt.get_cmap('viridis')(float(10*i)/NTemps))
    plt.xlim(-100, 100)
    plt.ylim(0,1)
    plt.title(f"Nombre d'itérations : {i}")
    plt.xlabel("x (u.a.)")
    plt.ylabel("T (u.a.)")
    plt.grid(True)

anim = FuncAnimation(fig1, animate, frames = 2000, interval=1)
plt.show()