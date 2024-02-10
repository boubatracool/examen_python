import numpy as np
import matplotlib.pyplot as plt

debut = 0
fin = 1
nbr_points = 5432

list_x = np.linspace(debut, fin, 100)
list_y = [0.5 + x ** 5 for x in list_x]
plt.plot(list_x, list_y, color='red')
plt.xlim(0, 1)
plt.ylim(0, 1.6)
plt.xlabel('x')
plt.ylabel('y')

list_x = np.random.uniform(debut, fin, nbr_points)
list_y = np.random.uniform(0, fin ** 5, nbr_points)

for x, y in zip(list_x, list_y):
    if y > x ** 5 + 0.5:
        plt.plot(x, y, 'b+', markersize=3)
    else:
        plt.plot(x, y, 'go', markersize=3)

plt.grid(True)
plt.legend()
plt.show()
