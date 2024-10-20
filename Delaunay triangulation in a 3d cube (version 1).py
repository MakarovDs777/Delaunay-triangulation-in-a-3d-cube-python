import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import Delaunay

# Генерация случайной функции с двумя переменными
def generate_function():
    functions = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
    return random.choice(functions)

# Генерация фрактала
def generate_fractal(x, y, z, depth):
    if depth == 0:
        return np.array([x, y, z])
    else:
        x1 = x + np.random.uniform(-1, 1)
        y1 = y + np.random.uniform(-1, 1)
        z1 = z + np.random.uniform(-1, 1)
        return np.array([x1, y1, z1]) + generate_fractal(x1, y1, z1, depth - 1)

# Генерация полостей и самоподобия
def generate_cavity(x, y, z, depth):
    if depth == 0:
        return np.array([x, y, z])
    else:
        x1 = x + np.random.uniform(-1, 1)
        y1 = y + np.random.uniform(-1, 1)
        z1 = z + np.random.uniform(-1, 1)
        return np.array([x1, y1, z1]) + generate_cavity(x1, y1, z1, depth - 1)

# Генерация трехмерного пространства
def generate_space():
    x = np.random.uniform(-10, 10)
    y = np.random.uniform(-10, 10)
    z = np.random.uniform(-10, 10)
    depth = np.random.randint(1, 10)
    return generate_fractal(x, y, z, depth)

# Визуализация пространства
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Создание трехмерных точек
points = np.zeros((100, 3))
for i in range(100):
    x, y, z = generate_space()
    points[i, :] = [x, y, z]

# Выполнить триангуляцию Делоне
triangulation = Delaunay(points)

# Нарисуйте точки и треугольники
ax.scatter(points[:, 0], points[:, 1], points[:, 2])
for triangle in triangulation.simplices:
    ax.plot3D(points[triangle, 0], points[triangle, 1], points[triangle, 2], 'k-')

plt.show()
