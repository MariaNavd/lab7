import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

x = np.linspace(0, 2, 100)

def fun(y, x):
    y1, y2 = y
    dydx = [y2, -y2 + 4 * y1 + x * np.exp(-x)]
    return dydx

def drawPhasePortrait(deltaX1, deltaX2, startX1, stopX1, startX2, stopX2):
    plt.axis([startX1, stopX1, startX2, stopX2])
    for y1 in np.arange(startX1, stopX1, deltaX1):
        for y2 in np.arange(startX2, stopX2, deltaX2):
            y0 = [y1, y2]
            sol = odeint(fun, y0, x)
            plt.plot(sol[:, 0], sol[:, 1], 'b')
    plt.xlabel('x')
    plt.grid()

a = np.loadtxt('result.txt')

plt.figure()

plt.subplot(121)
plt.plot(a[:, 0], a[:, 1], 'g', label = 'y')
plt.legend(loc = 'best')
plt.xlabel('x')
plt.grid()

plt.subplot(122)
plt.plot(a[:, 0], a[:, 2], 'r', label = 'y\'')
plt.legend(loc = 'best')
plt.xlabel('x')
plt.grid()
plt.show()

plt.figure()
plt.title('Phase portrait')
drawPhasePortrait(1.5, 1.5, -10, 10, -10, 10)
plt.show()