import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import random
from scipy.spatial import Delaunay

# Функция для генерации кадра
def update(ax):
    ax.clear()  # Очистка текущего окна

    # Генерация линии
    points = []
    for i in range(100):
        x = np.random.uniform(-100, 100)
        y = np.random.uniform(-100, 100)
        z = np.random.uniform(-100, 100)
        points.append([x, y, z])

    # Преобразование точек в NumPy массив 
    points = np.array(points)

    # Выполнить триангуляцию Делоне
    triangulation = Delaunay(points)

    # Постройте график треугольников
    for triangle in triangulation.simplices:
        ax.plot3D(points[triangle, 0], points[triangle, 1], points[triangle, 2], 'k-', linewidth=5)

# Запуск анимации
plt.ion()  # Включение интерактивного режима
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-150, 150)
ax.set_ylim(-150, 150)
ax.set_zlim(-150, 150)

for i in range(100):
    update(ax)
    plt.pause(0.1)  # Пауза между кадрами
    plt.draw()  # Отрисовка текущего кадра

plt.ioff()  # Выключение интерактивного режима
plt.show()  # Окончательный кадр
