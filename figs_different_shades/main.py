import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage.measure import label, regionprops

def clustering(colors):
    clusters = []
    while colors:
        color1 = colors.pop(0)
        clusters.append([color1])
        for color2 in colors.copy():
            if abs(color1 - color2) < 5:
                clusters[-1].append(color2)
                colors.pop(colors.index(color2))
    return clusters

image = plt.imread("balls_and_rects.png")

hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
binary = image.mean(2) > 0

labeled = label(binary)
print(f"Общее число фигур на изображении: {np.max(labeled)}")

regions = regionprops(labeled)

rect = []
circle = []
h = hsv[:, :, 0]
for region in regions:
    r = h[region.bbox[0]:region.bbox[2], region.bbox[1]:region.bbox[3]]
    if len(np.unique(r)) == 1:
        rect.extend(np.unique(r))
    else:
        circle.extend(np.unique(r)[1:2])


print(f"Количество прямоугольников: {len(rect)}")
print(f"Количество кругов: {len(circle)}")

rect_cluster = clustering(rect)
circle_cluster = clustering(circle)

print(circle_cluster)
print(f"Оттенок\tПрямоуголники\tКруги")
for i in range(len(rect_cluster)):
    idx = [[j for k in circle_cluster[j] if int(k) == int(rect_cluster[i][0])] for j in range(len(circle_cluster))]
    idx = [i[0] for i in idx if i][0]
    #print(idx, rect_cluster[i][0])
    print(f"{int(rect_cluster[i][0])}\t{len(rect_cluster[i])}\t\t{len(circle_cluster[idx])}")
    

print(f"Количество цветов у прямоугольников: {len(rect_cluster)}")
print(f"Количество цветов у кругов: {len(circle_cluster)}")


plt.imshow(labeled)
plt.show()