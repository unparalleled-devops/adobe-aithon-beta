from PIL import Image
from ultralytics import YOLO
import cv2

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

img = cv2.imread("img1.jpg")

objects = []

# question 1: predict on image and find entities

results = model.predict(img, stream=True)                 # run prediction on img
for result in results:                                         # iterate results
    boxes = result.boxes.cpu().numpy()                         # get boxes on cpu in numpy
    for box in boxes:                                          # iterate boxes
        r = box.xyxy[0].astype(int)                            # get corner points as int
        print(r)                                               # print boxes
        cv2.rectangle(img, r[:2], r[2:], (255, 255, 255))       # draw boxes on img
        name = result.names[int(box.cls[0])]
        print(name)

        obj = {"name": name, "box": r}
        objects.append(obj)

#cv2.imshow("lalala", img)
#k = cv2.waitKey(0)


# question 2: count entities, group like entities and give counts for each
entities_by_name = []
for obj in objects:
    name = obj["name"]
    flag = 0
    for t in entities_by_name:
        if name in t:
            t.append(name)
            flag = 1

    if flag == 0:
        entities_by_name.append([name])

print(entities_by_name)
for e in entities_by_name:
    c = len(e)
    if c > 1:
        print(f"there are {c} {e[0]}s in the image")
    else: 
        print(f"there is 1 {e[0]} in the image")
