import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

from ultralytics import YOLO

model = YOLO('yolov8n.yaml')

results = model.train(data='data.yaml', epochs=100, imgsz=640, workers=1, batch=3)