# https://blog.roboflow.com/train-rf-detr-on-a-custom-dataset/
# modified by ablanco50, Alfonso Blanco

# directory of test images
#dirname ="Drone_detection\\train"

dirname ="Test1"

classes=['drone']

THRESHOLD=0.3

import supervision as sv

from rfdetr import RFDETRBase

import supervision as sv
import numpy as np
from PIL import Image

model = RFDETRBase()
model.optimize_for_inference()

Cont_drones_Detected=0
Cont_drones_No_Detected=0

import os
import re
def loadimages(dirname):
 
     imgpath = dirname + "\\"      
     
     images = []
     TabFileName=[]   
    
     print("Reading images from ",imgpath)
     NumImage=-2
     
     Cont=0
     for root, dirnames, filenames in os.walk(imgpath):
        
         NumImage=NumImage+1
         
         for filename in filenames:
             
             if re.search("\.(jpg|jpeg|png|bmp|tiff|JPEG)$", filename):
                 
                 
                 filepath = os.path.join(root, filename)
                 image = Image.open(filepath)                
                 
                                         
                 images.append(image)
                 TabFileName.append(filename)
                 
                 Cont+=1
                 
     print("Readed " + str(len(images)))
     
     return images, TabFileName

#
# MAIN
#


images, TabFileName=loadimages(dirname)

for i in range(len(images)):

    image=images[i]

    detections = model.predict(image, threshold=THRESHOLD)

    text_scale = sv.calculate_optimal_text_scale(resolution_wh=image.size)
    thickness = sv.calculate_optimal_line_thickness(resolution_wh=image.size)

    bbox_annotator = sv.BoxAnnotator(thickness=thickness)
    label_annotator = sv.LabelAnnotator(
            text_color=sv.Color.BLACK,
            text_scale=text_scale,
            text_thickness=thickness,
            smart_position=True)



    #print(detections.confidence)

    detections_labels = [
            
            f"drone  {str(confidence)[12:16]}"
            
            for confidence
            
            in zip( detections.confidence)
    ]

    #print(detections_labels)

    detections_image = image.copy()
    #print(detections)

    detections_image = bbox_annotator.annotate(detections_image, detections)

    #print(detections_labels)
    #print(detections.class_id)

    Cont_drones=0

    detections_image_drone=[]
    for i in range(len(detections.class_id)):
      if  detections.class_id[i] == 5:   # class 5 in  RFDETRBase is drone        
         
          detections_image_drone=label_annotator.annotate(detections_image, detections[i], [detections_labels[i]])
          sv.plot_images_grid(images=[detections_image_drone], grid_size=(1, 2), titles=["Detection"])
          Cont_drones=Cont_drones+1

    if Cont_drones==0:
         Cont_drones_No_Detected= Cont_drones_No_Detected +1
    else:
         Cont_drones_Detected= Cont_drones_Detected + Cont_drones

    print("Detected drones = " + str(Cont_drones))

print("Drones no detected = " + str(Cont_drones_No_Detected))
print("Drones detected = " + str(Cont_drones_Detected))

    
