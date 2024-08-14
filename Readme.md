# 1. Environment configuration tutorial
    
    Run pip install -r requirements.txt

    My experimental environment:
    torch: 2.0.1
    torchvision: 0.15.1


# 2. Train your own model--train.py
Modify 'yaml' to choose whether to add bifpn, C2f-faster and EMA attention module.
Modify 'data' to select the data set to use.
The following are training parameters that can be modified, with an explanation of each parameter at the end of each line.

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


# 3. Test model performance--val.py
The following validation parameters can be modified, with an explanation of each parameter at the end of each line.

    if __name__ == '__main__':
    model = YOLO('runs/train/YOLOV8(URPC)/weights/best.pt')
    model.val(data='URPCdata.yaml',
              split='test',
              imgsz=640,
              batch=1,
              # rect=False,
              # save_json=True, # if you need to cal coco metrice
              project='runs/val',
              name='FEB',
              )

# 4. Detect picture--detect.py
The following detection parameters can be modified, with an explanation of each parameter at the end of each line.

    if __name__ == '__main__':
    model = YOLO('runs/train/exp/weights/best.pt') # select your model.pt path
    model.predict(source='dataset/images/test',
                  imgsz=640,
                  project='runs/detect',
                  name='exp',
                  save=True,
                # visualize=True # visualize model features maps
                )

# 5. Model configuration file
The model configuration files are in ultralytics/models/v8.
yolov8 comes in five sizes

    YOLOv8n summary: 225 layers,  3011628 parameters,  3011612 gradients,   8.2 GFLOPs
    YOLOv8s summary: 225 layers, 11137148 parameters, 11137132 gradients,  28.7 GFLOPs
    YOLOv8m summary: 295 layers, 25858636 parameters, 25858620 gradients,  79.1 GFLOPs
    YOLOv8l summary: 365 layers, 43632924 parameters, 43632908 gradients, 165.4 GFLOPs
    YOLOv8x summary: 365 layers, 68156460 parameters, 68156444 gradients, 258.1 GFLOPs

How do you specify which size model to use? The default is n. Suppose I want to choose the size of m model, 
the yaml parameters in the train.py should be specified as ultralytics/cfg/models/mymodels/yolov8m.yaml.


