import numpy as np
import matplotlib.pyplot as plt

def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1

size = 100
image = np.zeros((size, size, 3), dtype="uint8")
image2 = image.copy()
assert image.shape[0] == image.shape[1]
assert image2.shape[0] == image2.shape[1]

color1 = [255, 128, 0] #оранжевый
color2 = [0, 128, 255] #голубой

for i, v in enumerate(np.linspace(0, 1, image.shape[0])):
    r = lerp(color1[0], color2[0], v)
    g = lerp(color1[1], color2[1], v)
    b = lerp(color1[2], color2[2], v)   
    image[i, :, :] = [r, g, b] 

for i in range(0, size):
    for j in range(0, size):
        v = (i + j) / (size * 2)
        r = int(lerp(color2[0], color1[0], v))
        g = int(lerp(color2[1], color1[1], v))
        b = int(lerp(color2[2], color1[2], v))
        image2[i, j, :] = [r, g, b]

plt.figure(figsize=(11, 5))
plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(image2)
plt.show()