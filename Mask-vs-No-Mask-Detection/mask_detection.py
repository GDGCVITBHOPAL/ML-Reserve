import os
import io
import pandas as pd

pd.options.mode.chained_assignment = None
import numpy as np
import cv2


my_dir = os.getcwd()

if not os.path.exists(f"{my_dir}\\Results"):
    os.mkdir(f"{my_dir}\\Results\\")

image_path = f"{my_dir}\\Dataset\\test\\images\\test_img_7.jpg"

os.system(
    f"python Model/detect.py --weights Model/runs/train/exp3/weights/best.pt --img 940 --conf 0.70 --source {image_path}"
)

detect_path = f"{my_dir}\\Model\\runs\\detect\\"
detections = os.listdir(detect_path)
detections.sort()
this_detect = os.path.join(detect_path, detections[-1])
output_image_name = os.listdir(this_detect)[0]
output_image = cv2.imread(os.path.join(this_detect, output_image_name))

results_path = f"{my_dir}\\Results"
i = 1
while os.path.exists(f"{results_path}\\output_{i}"):
    i += 1

os.mkdir(f"{results_path}\\output_{i}\\")
cv2.imwrite(f"{results_path}\\output_{i}\\{output_image_name}", output_image)
