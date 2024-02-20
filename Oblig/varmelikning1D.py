import numpy as np
import matplotlib.pyplot as plt

#Definerer problemet som skal løses

a = 110
lengde = 50 #mm
tid = 4 #sekunder
noder = 20

#Initiering

h = lengde/noder
k = 0.5 * h**2 / a
t_noder = int(tid/k)

u = np.zeros(noder) + 20 #Stanger starter på 20 grader

#Randkrav

u[0] = 100
u[-1] = 100

#Visualisering

fig, axis = plt.subplots()
pcm = axis.pcolormesh([u], cmap = plt.cm.rainbow, vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)
axis.set_ylim([-2, 3])
#Lager simulering

counter = 0

while counter < tid :
    w = u.copy() #Lager kopi for å ikke endre u

    for i in range(1, noder - 1):
        u[i] = k * a * (w[i-1] - 2 * w[i] + w[i+1])/h**2 + w[i]

    counter += k
    print("t: {:.3f} [s], Gjennomsnittlig temperatur: {:.2f} grader Celsius".format(counter, np.average(u)))

    #Oppdaterer plot

    pcm.set_array([u])
    axis.set_title("Distribusjon ved t: {:.3f} [s].".format(counter))
    plt.pause(0.01)

plt.show()