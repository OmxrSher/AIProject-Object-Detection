from ultralytics import YOLO

model = YOLO("yolov8s.pt")

model.train(
    data="/content/custom_dataset/data.yaml",
    epochs=60,
    imgsz=640,
    batch=8,
    project="/content/drive/MyDrive/yolo_runs",
    name="final_model_saved",
    patience=15,
    save=True,
    plots=True,
    cache=False,
    workers=2,
    dropout=0.1,
    mosaic=0.3,
    close_mosaic=15,
    scale=0.1,
    translate=0.05,
    fliplr=0.5,
    hsv_h=0.015,
    hsv_s=0.5,
    hsv_v=0.3
)