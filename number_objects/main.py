import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
from scipy.ndimage import binary_erosion

image = np.load("ps.npy.txt")

mask1 = np.array([[1, 1, 1],[1, 1, 1],[1, 1, 1]])
mask2 = np.array([[0, 0, 0, 0],
                  [1, 0, 0, 1],
                  [1, 0, 0, 1],
                  [1, 1, 1, 1]]) #ушки вверх

mask3 = np.array([[1, 1, 1, 1],
                  [1, 0, 0, 1],
                  [1, 0, 0, 1],
                  [0, 0, 0, 0]]) #ушки вниз

mask4 = np.array([[1, 1, 1, 0],
                  [1, 0, 0, 0],
                  [1, 0, 0, 0],
                  [1, 1, 1, 0]]) #ушки вправо

mask5 = np.array([[0, 1, 1, 1],
                  [0, 0, 0, 1],
                  [0, 0, 0, 1],
                  [0, 1, 1, 1]]) #ушки влево

struct = [mask1, mask2, mask3, mask4, mask5]
name = ["Прямоугольники", "Ушки вверх", "Ушки вниз", "Ушки вправо", "Ушки влево"]

labeled = label(image)
total_number = np.max(labeled)
print("Всего:", total_number)

rect = 0
for i in range(5):
    img = binary_erosion(image, struct[i])
    labeled = label(img)
    number = np.max(labeled)
    if rect != 0:
        print(f"{name[i]}: {number-rect}")
        continue
    rect = number
    print(f"{name[i]}: {rect}")
