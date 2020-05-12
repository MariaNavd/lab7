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

plt.figure()

plt.subplot(211)
plt.plot(a[:, 0], a[:, 1], 'g', label = 'y - gotten solution')
plt.plot(a[:, 0], y(a[:, 0]), 'r', label = 'y - exact solution')
plt.legend(loc = 'best')
plt.xlabel('x')
plt.grid()

plt.subplot(212)
plt.plot(a[:, 0], y(a[:, 0]) - a[:, 1], 'b', label = 'y_exact - y_gotten')
plt.legend(loc = 'best')
plt.xlabel('x')
plt.grid()

plt.figure()

plt.subplot(211)
plt.plot(a[:, 0], a[:, 2], 'g', label = 'y\' - gotten solution')
plt.plot(a[:, 0], y_x(a[:, 0]), 'r', label = 'y\' - exact solution')
plt.legend(loc = 'best')
plt.xlabel('x')
plt.grid()

plt.subplot(212)
plt.plot(a[:, 0], y_x(a[:, 0]) - a[:, 2], 'b', label = 'y\'_exact - y\'_gotten')
plt.legend(loc = 'best')
plt.xlabel('x')
plt.grid()