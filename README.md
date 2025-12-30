# Traffic Sign Detector

## Overview
This project is a real-time traffic sign detection system built using YOLOv8 and OpenCV. It can identify and classify various traffic signs including speed limits, stop signs, and directional indicators.

## Features
- Real-time traffic sign detection using webcam
- Detection of 14 different traffic sign classes
- Pre-trained YOLOv8 model for accurate detection
- Simple and easy-to-use interface

## Requirements
- Python 3.8+
- OpenCV
- Ultralytics YOLOv8

## Installation
```bash
pip install ultralytics opencv-python
```

## Usage
Run the main detection script:
```bash
python adas.py
```

## Dataset
The model was trained on a custom dataset containing various traffic signs with the following classes:
- adas_dur (Stop)
- adas_durak (Bus Stop)
- adas_girilmez (No Entry)
- adas_hiz20 (Speed Limit 20)
- adas_hiz30 (Speed Limit 30)
- adas_hiz40 (Speed Limit 40)
- adas_hiz50 (Speed Limit 50)
- adas_hiz60 (Speed Limit 60)
- adas_sag (Turn Right)
- adas_sagadonulmez (No Right Turn)
- adas_sol (Turn Left)
- adas_soladonulmez (No Left Turn)
- adas_yayagecidi (Pedestrian Crossing)
- adas_yolcalismasi (Road Work)

## Example Detections
The system can detect various traffic signs in real-time, as shown in the example images:

1. Speed Limit 30 Detection
   ![Speed Limit 30](images/IMG_6440.png)
2. Stop Sign (DUR) Detection
   ![Stop Sign](images/IMG_6442.png)
3. No Entry Sign Detection
   ![No Entry](images/IMG_6443.png)

## Model
The project uses a YOLOv8 model trained on a custom dataset of traffic signs. The model file `bestv8.pt` contains the weights for the trained model.

## License
This dataset is licensed under CC BY 4.0 as specified in the Roboflow project.

## Credits
Dataset created using Roboflow: https://universe.roboflow.com/adastrafficsign-g8dj1/adas_traffic_sign-rmmc1/dataset/2
