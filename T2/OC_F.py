import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from celluloid import Camera



def fourier_onda_cuadrada(x,n):
    m = 2*n-1
    f = (4/np.pi)*(1/m)*np.sin(m*np.pi*x/L)
    return f
fig = plt.figure()
camera = Camera(fig)

L = np.pi
ciclos = 1
x = np.linspace(-0.0000001,2*ciclos*L,1000)

f = 0
n = 1
n_t = 20

while n <= n_t:
    f += fourier_onda_cuadrada(x,n)
    plt.plot(x,f)
    camera.snap()
    n += 1


plt.plot(x,signal.square(x),color='k')
animation = camera.animate()
animation.save('onda_cuadrada.gif', writer = 'pillow', fps = 10)
plt.legend()
plt.show()