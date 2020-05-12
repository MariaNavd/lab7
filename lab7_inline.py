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

x_plot = np.linspace(0, 2, 100)

a = np.loadtxt("result.txt")  

plt.suptitle('SciPy solution comparison')

plt.subplot(121)
y_plot = sol.sol(x_plot)[0]
plt.plot(x_plot, y_plot, 'b', label = 'y - scipy solution')
plt.plot(a[:, 0], a[:, 1], 'r', label = 'y - gotten solution')
plt.legend(loc = 'best')
plt.xlabel('x')
plt.grid()

plt.subplot(122)
y_plot = sol.sol(x_plot)[1]
plt.plot(x_plot, y_plot, 'b', label = 'y\' - scipy solution')
plt.plot(a[:, 0], a[:, 2], 'r', label = 'y\' - gotten solution')
plt.legend(loc = 'best')
plt.xlabel('x')
plt.grid()
plt.show()