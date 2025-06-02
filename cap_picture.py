import cv2
import os

cap = cv2.VideoCapture(0)
    
while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Lật ảnh theo chiều ngang

    key = cv2.waitKey(1)
    if key == ord('q'): # thoát chương trình.
        break
    elif key == ord('c'):
        
        # Kiểm tra nếu file cap.jpg tồn tại thì xóa
        if os.path.exists("cap.jpg"):
            os.remove("cap.jpg")
        
        # Lưu frame với tên cap.jpg
        cv2.imwrite("cap.jpg", frame)
        height, width, _ = frame.shape
        print(f"Đã lưu file cap.jpg với kích thước {width}x{height}")
    # Hien anh ra man hinh
    cv2.imshow("cap_picture", frame)

cv2.destroyAllWindows()