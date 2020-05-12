from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt
import numpy as np

def fun(x, y):
    return np.vstack((y[1], -y[1] + 4 * y[0] + x * np.exp(-x)))

def bc(ya, yb):
    return np.array([ya[0], ya[1]])

x = np.linspace(0, 2, 10)
y = np.zeros((2, x.size))
sol = solve_bvp(fun, bc, x, y)

a = np.loadtxt("result.txt")

plt.figure()

plt.subplot(211)
y_plot = sol.sol(a[:, 0])[0]
plt.plot(a[:, 0], y_plot, 'g', label = 'y - scipy solution')
plt.plot(a[:, 0], a[:, 1], 'r', label = 'y - gotten solution')
plt.legend(loc = 'best')
plt.xlabel('x')
plt.grid()

plt.subplot(212)
plt.plot(a[:, 0], y_plot - a[:, 1], 'b', label = 'y_scipy - y_gotten')
plt.legend(loc = 'best')
plt.xlabel('x')
plt.grid()

plt.figure()

plt.subplot(211)
y_plot = sol.sol(a[:, 0])[1]
plt.plot(a[:, 0], y_plot, 'g', label = 'y\' - scipy solution')
plt.plot(a[:, 0], a[:, 2], 'r', label = 'y\' - gotten solution')
plt.legend(loc = 'best')
plt.xlabel('x')
plt.grid()

plt.subplot(212)
plt.plot(a[:, 0], y_plot - a[:, 2], 'b', label = 'y\'_scipy - y\'_gotten')
plt.legend(loc = 'best')
plt.xlabel('x')
plt.grid()
plt.show()