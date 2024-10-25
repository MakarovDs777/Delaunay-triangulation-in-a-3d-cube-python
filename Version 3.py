import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d
from skimage import measure
import os
from scipy.spatial import Delaunay

def generate_points(shape, num_points):
    points = []
    for _ in range(num_points):
        x = np.random.randint(0, shape[0])
        y = np.random.randint(0, shape[1])
        z = np.random.randint(0, shape[2])
        points.append([x, y, z])
    return np.array(points)

def generate_cube_field(shape):
    array = np.ones(shape, dtype=float)
    # Удаляем все 6 сторон куба
    for x in range(shape[0]):
        for y in range(shape[1]):
            for z in range(shape[2]):
                if x == 0 or x == shape[0] - 1 or y == 0 or y == shape[1] - 1 or z == 0 or z == shape[2] - 1:
                    array[x, y, z] = 0.0
    return array

# Параметры
shape = (64, 64, 64)  # Размеры 3D массива
num_points = 100  # Количество точек

# Генерация точек
points = generate_points(shape, num_points)

# Выполнить триангуляцию Делоне
triangulation = Delaunay(points)

# Генерация 3D-поля с кубом
cube_field = generate_cube_field(shape)

# Создание изосурфейса
verts, faces, _, _ = measure.marching_cubes(cube_field, level=0.5)

# Создание изосурфейса из точек триангуляции Делоне
verts_delone = points[triangulation.simplices].mean(axis=1)
faces_delone = triangulation.simplices

# Сохранение изосурфейса в OBJ файл
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
filename = os.path.join(desktop_path, "delone.obj")
with open(filename, "w") as f:
    for j, vert in enumerate(verts_delone):
        f.write(f"v {vert[0]} {vert[1]} {vert[2]}\n")
    for face in faces_delone:
        f.write(f"f {face[0]+1} {face[1]+1} {face[2]+1}\n")
print(f"Model saved as {filename}")

# Визуализация
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for triangle in triangulation.simplices:
    ax.plot3D(points[triangle, 0], points[triangle, 1], points[triangle, 2], 'k-', linewidth=5)

# Рисуем треугольники
for face in faces_delone:
    v1 = points[face[0]]
    v2 = points[face[1]]
    v3 = points[face[2]]
    vertices = [v1, v2, v3, v1]
    ax.add_collection3d(art3d.Poly3DCollection([vertices], alpha=0.5, color='r'))

plt.show()
