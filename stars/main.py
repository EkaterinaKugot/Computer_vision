import numpy as np
from scipy.ndimage import label, binary_erosion

image = np.load(f"stars.npy")
cross = np.array([[1, 0, 0, 0, 1],[0, 1, 0, 1, 0],[0, 0, 1, 0, 0],[0, 1, 0, 1, 0],[1, 0, 0, 0, 1]])
plus = np.array([[0, 0, 1, 0, 0],[0, 0, 1, 0, 0],[1, 1, 1, 1, 1],[0, 0, 1, 0, 0],[0, 0, 1, 0, 0]])

struct = [cross, plus]

for i in range(2):
    img = binary_erosion(image, struct[i])
    img, count = label(img)
    if i == 0:
        print(f"Crosses: {count}")
    else:
        print(f"Pluses: {count}")