import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage.morphology import binary_dilation, binary_erosion

def filling_factor(region):
    return region.image.mean()

def change_symbol(tmp):
    tm_labeled = label(tmp)
    return regionprops(tm_labeled)

def recognize(region):
    if filling_factor(region) == 1:
        return "-"
    else:
        euler = region.euler_number
        tmp = region.image.copy()
        tmp_regions = change_symbol(binary_erosion(tmp))
        flag = True
        if 1 in tmp_regions[0].image.mean(0):
            flag = False
        if euler == -1: #B or 8
            tmp = region.image.copy()
            tmp_regions = change_symbol(binary_erosion(tmp))
            if 1 in tmp_regions[0].image.mean(0):
                return "B"
            else:
                return "8"
        elif euler == 0 and flag: #A or 0  and 1 not in region.image.mean(0)
            tmp = region.image.copy()
            tmp[-1, :] = 1
            tmp_regions = change_symbol(binary_dilation(tmp))
            euler1 = tmp_regions[0].euler_number
            if euler1 == -1:
                return "A"
            elif euler1 == 1:
                return "*"      
            else:
                return "0"
        elif euler == 0 and not(flag): #D P
            coords = region.bbox
            middle = int((coords[3] - coords[1])/2) + int((coords[3] - coords[1])/3)
            tmp = region.image.copy()
            tmp[middle, :] = 1
            tmp_regions = change_symbol(tmp)
            euler1 = tmp_regions[0].euler_number
            if euler1 == -1:
                
                return "D"
            else: 
                return "P"
        else: #1 W X * /
            if 1 in region.image.mean(0):
                if region.eccentricity < 0.5:
                    return "*"
                else:
                    return "1"
            tmp = region.image.copy()
            tmp[[0, -1], :] = 1
            tm_labeled = label(tmp)
            tmp_regions = regionprops(tm_labeled)
            euler = tmp_regions[0].euler_number
            if euler == -1:
                return "X"
            elif euler == -2:
                return "W"
            if region.eccentricity > 0.5:
                return "/"
            else:
                return "*"
            
    return "?"

img = plt.imread('symbols.png')
binary = img.mean(2)
binary[binary!=0] = 1

labeled = label(binary)

regions = regionprops(labeled)

counts = {}
for region in regions:
    symbol = recognize(region)
    if symbol not in counts:
        counts[symbol] = 0
    counts[symbol] += 1

print(counts)
print(1 - counts.get("?", 0)/labeled.max()) #сколько символов распознали
