from ultralytics import YOLO
import cv2

import warnings
warnings.filterwarnings("ignore")

# Load a pretrained YOLOv8n model
def predict(img_url, raw_results=False, show=False):
    model = YOLO('yolov8n.pt')

    img = cv2.imread(img_url)

    objects = []

    # question 1: predict on image and find entities
    results = model.predict(img, stream=True)                 # run prediction on img
    for result in results:                                         # iterate results
        boxes = result.boxes.cpu().numpy()                         # get boxes on cpu in numpy
        for box in boxes:                                          # iterate boxes
            r = box.xyxy[0].astype(int)                            # get corner points as int
            cv2.rectangle(img, r[:2], r[2:], (255, 255, 255))       # draw boxes on img
            name = result.names[int(box.cls[0])]

            obj = {"name": name, "box": r}
            objects.append(obj)

    if show:
        cv2.imshow("image", img)
        k = cv2.waitKey(100000)

    if raw_results:
        return results, objects
    else:
        return objects  


if __name__ == "__main__":
    predict("images/img2.png", show=True)    
