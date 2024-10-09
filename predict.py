from ultralytics import YOLO

model = YOLO('./runs/detect/train2/weights/best.pt')

model.predict('./test/images/23_jpg.rf.abb6cb90fd681a0617caa682b113b1f1.jpg', save=True, show=True, conf=0.7)