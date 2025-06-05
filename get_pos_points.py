import cv2
import numpy as np
import sys

# img = cv2.imread('cap.jpg')
cap = cv2.VideoCapture("video/my.mp4")

# Lấy frame tại giây thứ t.
t = 5  # Giây thứ t để lấy frame
fps = cap.get(cv2.CAP_PROP_FPS)  # Lấy số frame trên giây
cap.set(cv2.CAP_PROP_POS_FRAMES, int(fps * t))  # Đặt vị trí frame tại giây thứ t.
ret, img = cap.read()  # Đọc frame
if not ret:
    print("Không thể lấy frame từ video.")
    sys.exit(0)

points = []

def handle_left_click(event, x, y, flags, points):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])

def draw_polygon(frame, points):
    for point in points:
        frame = cv2.circle(frame, (point[0], point[1]), 5, (0,0,255), -1)

    frame = cv2.polylines(frame, [np.int32(points)], False, (255,0, 0), thickness=2)
    return frame
    

while True:

    # Ve ploygon
    img = draw_polygon(img, points)
    key = cv2.waitKey(1)
    if key == ord('q'): # thoát chương trình.
        break
    elif key == ord('c'): # hoàn thành việc chọn điểm.
        points.append(points[0])

    # Hien anh ra man hinh
    cv2.imshow("get_pos_points", img)

    cv2.setMouseCallback('get_pos_points', handle_left_click, points)
cv2.destroyAllWindows()
print("Points selected:", points)