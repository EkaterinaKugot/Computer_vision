import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label

figures = []

image = np.load(f"out/h_0.npy")
labeled = label(image)

for k in range(1, np.max(labeled)+1):
    tmp = np.where(labeled == k)
    figures.append([[int(tmp[0].mean())], [int(tmp[1].mean())]]) #x, y

for n in range(1, 100):
    image = np.load(f"out/h_{n}.npy")
    labeled = label(image)
    for k in range(1, np.max(labeled)+1): 
        find_coords = False
        tmp = np.where(labeled == k)
        for x, y in zip(*tmp):
            for fig in figures: 
                if x == fig[0][-1] and y == fig[1][-1]:
                    fig[0].append(int(tmp[0].mean()))
                    fig[1].append(int(tmp[1].mean()))
                    find_coords = True
                    break
            if find_coords:
                break

for k in range(len(figures)):
    plt.plot(figures[k][0], figures[k][1], label=f"{k+1} figure")
plt.legend()
plt.show()



    

