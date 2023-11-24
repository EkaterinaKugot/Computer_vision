import numpy as np
import cv2

def to_binary_image(path):
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        img = cv2.bitwise_not(img)
        return img[:, :img.shape[1]-40]


def find_pencils(path):
        img = to_binary_image(path)
        contours0, hierarchy = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        sides = []

        for cnt in contours0:
                rect = cv2.minAreaRect(cnt) 
                box = cv2.boxPoints(rect) 
                box = np.intp(box) 

                cv2.drawContours(img,[box],0,(255,0,0),2) 

                side1 = cv2.norm(np.intp((box[1][0] - box[0][0],box[1][1] - box[0][1])))
                side2 = cv2.norm(np.intp((box[2][0] - box[1][0], box[2][1] - box[1][1])))

                maxSide = side1
                if side2 > side1:
                        maxSide = side2
                sides.append(maxSide)

        pencils = [i for i in sides if i > 2000 ]
        return len(pencils)

total_pencils = 0
for i in range(1, 13):
        path = f'images/img ({i}).jpg'
        countp = find_pencils(path)
        total_pencils += countp
        print(f"In {i} image: {countp}")

print(f"Total pencils {total_pencils}")
#cv2.destroyAllWindows()