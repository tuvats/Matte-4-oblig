import numpy as np
import matplotlib.pyplot as plt

#Definerer problemet som skal løses

a = 110
lengde = 50 #mm
tid = 4 #sekunder
noder = 30

#Initiering

h = lengde/noder
y = lengde/noder
k = min(h**2/(4*a), y**2/(4*a))
t_noder = int(tid/k)

u = np.zeros((noder, noder)) + 20 #Stangen starter på 20 grader

#Randkrav

u[0, :] = 100
u[-1, :] = 100

#Visualisering

fig, axis = plt.subplots()
pcm = axis.pcolormesh(u, cmap = plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)

#Lager simulering

counter = 0

while counter < tid :
    w = u.copy() #Lager kopi for å ikke endre u

    for i in range(1, noder - 1):
        for j in range(1, noder -1):

            dd_ux = (w[i+1, j] - 2*w[i, j] + w[i-1, j])/h**2 #Andrederiverte av x
            dd_uy = (w[i, j+1] - 2*w[i, j] + w[i, j-1])/y**2 #Andrederiverte av y
            u[i, j] = k * a * (dd_ux + dd_uy) + w[i, j]

    counter += k
    print("t: {:.3f} [s], Gjennomsnittlig temperatur: {:.2f} grader Celsius".format(counter, np.average(u)))

    #Oppdaterer plot

    pcm.set_array(u)
    axis.set_title("Distribusjon ved t: {:.3f} [s].".format(counter))
    plt.pause(0.01)

plt.show()


