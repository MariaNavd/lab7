import matplotlib.pyplot as plt
import numpy as np

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

plt.figure()
plt.title('Phase trajectory')
plt.plot(a[:, 1], a[:, 2], 'b')
plt.grid()
