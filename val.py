import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('runs/train/YOLOV8(URPC)/weights/best.pt')
    model.val(data='URPCdata.yaml',
              split='test',
              imgsz=640,
              batch=1,
              # rect=False,
              # save_json=True, # if you need to cal coco metrice
              project='runs/val',
              name='FEB2',
              )