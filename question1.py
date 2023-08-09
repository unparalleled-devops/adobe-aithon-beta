from ultralytics import YOLO
import cv2
from predict import predict

# Load a pretrained YOLOv8n model
# model = YOLO('yolov8n.pt')

# img = cv2.imread("img1.jpg")

# objects = []

# results = model.predict(img, stream=True)                 # run prediction on img
# for result in results:                                         # iterate results
#     boxes = result.boxes.cpu().numpy()                         # get boxes on cpu in numpy
#     for box in boxes:                                          # iterate boxes
#         r = box.xyxy[0].astype(int)                            # get corner points as int
#         print(r)                                               # print boxes
#         cv2.rectangle(img, r[:2], r[2:], (255, 255, 255))       # draw boxes on img
#         name = result.names[int(box.cls[0])]
#         print(name)

#         obj = {"name": name, "box": r}
#         objects.append(obj)

# #cv2.imshow("lalala", img)
# #k = cv2.waitKey(0)

# question 1: predict on image and find entities
objects = predict("images/img2.png", show=True)
for obj in objects:
    name = obj["name"]
    box = obj["box"]
    print(f"entity : location --> {name} : {box}")

