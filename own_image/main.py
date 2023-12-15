import cv2

image = cv2.imread('image.png')  
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

video = 'output.avi'
video = cv2.VideoCapture(video)

count = 0
ret, frame = video.read()

while ret:
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(frame_gray, gray, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9

    if result > threshold:
        count += 1
    ret, frame = video.read()

video.release()

print(f"Количество моего изобраения(подарка) в видео: {count}")