Sign Language Detection using YOLOv5
This project is designed to detect hand gestures for sign language using the YOLOv5 object detection model. The model recognizes five sign language gestures: "Hello", "Love You", "No", "Thank You", and "Yes."

Project Structure
dataset/: Contains images and annotations for training and testing.

train/: Training images and labels.
valid/: Validation images and labels.
test/: Test images for detection.
runs/: Stores the training and detection results.

train/: Logs and model weights from training.
detect/: Images with detections.
src/: Scripts for training and detection.

train.py: Script to train the model.
detect.py: Script to run the model on new images.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/sign-language-detection-yolov5.git
cd sign-language-detection-yolov5
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Dataset
The dataset includes labeled images of hand gestures in YOLO format. You can upload your own images and annotations or use the provided dataset.

Training
To train the model, use the following command:

bash
Copy code
python train.py --data dataset/data.yaml --weights yolov5s.pt --epochs 50 --batch-size 16 --img-size 640
Detecting Hand Gestures
Once the model is trained, you can use it to detect hand gestures from images:

bash
Copy code
python detect.py --weights runs/train/exp/weights/best.pt --source path/to/image.jpg --img 640 --conf-thres 0.25 --iou-thres 0.45
For real-time webcam detection:

bash
Copy code
python detect.py --weights runs/train/exp/weights/best.pt --source 0 --img 640 --conf-thres 0.25 --iou-thres 0.45
Results
Detection results will be saved in runs/detect/. The images will be annotated with bounding boxes around detected gestures
