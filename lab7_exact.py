import matplotlib.pyplot as plt
import numpy as np

def y(arg):
    c1 = (9 - np.sqrt(17)) / 32 / np.sqrt(17)
    c2 = -(9 + np.sqrt(17)) / 32 / np.sqrt(17)
    return c1 * np.exp((-0.5 + np.sqrt(17) / 2) * arg) + c2 * np.exp((-0.5 - np.sqrt(17) / 2) * arg) + (-0.25 * arg + 1 / 16) * np.exp(-arg)

def y_x(arg):
    c1 = (9 - np.sqrt(17)) / 32 / np.sqrt(17)
    c2 = -(9 + np.sqrt(17)) / 32 / np.sqrt(17)
    return (-0.5 + np.sqrt(17) / 2) * c1 * np.exp((-0.5 + np.sqrt(17) / 2) * arg) + (-0.5 - np.sqrt(17) / 2) * c2 * np.exp((-0.5 - np.sqrt(17) / 2) * arg) + (0.25 * arg - 5 / 16) * np.exp(-arg)
    
    
a = np.loadtxt("result.txt")

arg = np.linspace(0, 2, 100)

plt.suptitle('Exact solution comparison')

plt.subplot(121)
plt.plot(a[:, 0], a[:, 1], 'g', label = 'y - exact solution')
plt.plot(arg, y(arg), 'r', label = 'y - gotten solution')
plt.legend(loc = 'best')
plt.xlabel('x')
plt.grid()

plt.subplot(122)
plt.plot(a[:, 0], a[:, 2], 'g', label = 'y\' - exact solution')
plt.plot(arg, y_x(arg), 'r', label = 'y\' - gotten solution')
plt.legend(loc = 'best')
plt.xlabel('x')
plt.grid()