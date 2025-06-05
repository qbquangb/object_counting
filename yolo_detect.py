from ultralytics import YOLO
import cv2
from time import sleep

cap = cv2.VideoCapture(0)  # Sử dụng camera mặc định
# img = "picture/test3.jpg"
model = YOLO("model/yolov8n.pt")

while True:

    sleep(1.5)
    ret, frame = cap.read()
    results = model.predict(source = frame, conf = 0.6)

    has_person = False

    for box in results[0].boxes:
        if int(box.cls) == 0:  # Thay đổi giá trị 0 nếu lớp "person" có chỉ số khác
            has_person = True

    # Kiểm tra và in thông báo nếu có người trong ảnh
    if has_person:
        print("Có người trong ảnh.")
    else:
        print("Không có người trong ảnh.")

    result_img = results[0].plot()  # Vẽ kết quả lên ảnh

    cv2.imshow("Kết quả", result_img)  # Hiển thị ảnh kết quả
    key = cv2.waitKey(1)
    if key == ord('q'):  # Nhấn 'q' để thoát
        break
    elif key == ord('s'):  # Nhấn 's' để lưu ảnh kết quả
        result_path = "picture/result.jpg"
        cv2.imwrite(result_path, result_img)
        print(f"Ảnh kết quả đã được lưu tại: {result_path}")

cap.release()
cv2.destroyAllWindows()  # Đóng tất cả cửa sổ hiển thị