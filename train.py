import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/mymodels/yolov8-C2f-Faster-EMA-bifpn.yaml')
    #model.load('yolov8n.pt') # loading pretrain weights  yolov8-C2f-Faster-EMA-bifpn
    model.train(data='data.yaml',
                cache=False,
                imgsz=640,
                epochs=300,
                batch=16,
                close_mosaic=10,
                workers=8,
                device='0',
                optimizer='SGD', # using SGD
                #resume='runs/train/yolov8-bifpn-EMA(no.8)/weights/last.pt', # last.pt path
                # amp=False # close amp
                # fraction=0.2,
                project='runs/train',
                name='YOLOV8',
                seed=0,
                #cos_lr=True,
                #lr0=0.02   #初始学习率
                #dropout=1.0  # (float) use dropout regularization (classify train only)
                )