import cv2
from ultralytics import solutions
import os

cap = cv2.VideoCapture("video/my.mp4")
assert cap.isOpened(), "Error reading video file"

# region_points = [(219, 585), (508, 586)]                                    # line counting (use by thuong)
# region_points = [(20, 400), (1080, 400), (1080, 360), (20, 360)]  # rectangle region
region_points = [(92, 401), (341, 406), (343, 991), (54, 986), (92, 401)]   # polygon region (use by thuong)

# Remove existing output file if it exists
output_path = "video/object_counting_output.avi"
if os.path.exists(output_path):
    os.remove(output_path)

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("video/object_counting_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Initialize object counter object
counter = solutions.ObjectCounter(
    show=True,  # display the output
    region=region_points,  # pass region points
    model="model/yolo11n.pt",  # model="yolo11n-obb.pt" for object counting with OBB model.
    classes=[3],  # count specific classes i.e. person and car with COCO pretrained model.
    tracker="botsort.yaml",  # choose trackers i.e "bytetrack.yaml"
    conf=0.60
)

# Process video
while cap.isOpened():

    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or processing is complete.")
        break

    results = counter(im0)

    # print(results)  # access the output

    video_writer.write(results.plot_im)  # write the processed frame.

cap.release()
video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows


# # CLI
# # Run a counting example
# yolo solutions count show=True

# # Pass a source video
# yolo solutions count source="car_0_6.mp4"

# # Pass region coordinates
# yolo solutions count region="[(222, 588), (497, 588), (521, 783), (198, 759)]"
# yolo solutions count source="car_0_6.mp4" show=True region="[(219, 585), (508, 586)]"
# yolo task=detect mode=predict model=yolov8n.pt source="https://nld.mediacdn.vn/291774122806476800/2025/2/3/img17385495066481738549519497-1738549566769692420503.jpg" show=True
# Train với CLI.
# !yolo task=detect mode=train model=yolov8n.pt data=data_train/mydataset.yaml epochs=50 imgsz=640

# Train with python script.
# results = model.train(data="D:/Duan/19object-counting/data_train/mydataset.yaml", epochs=5, imgsz=640)