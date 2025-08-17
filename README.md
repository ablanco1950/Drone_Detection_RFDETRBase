Drone_Detection_RFDETRBase

Since have been noticed that Roboflow's RFDETRBase incorporates the drone class as an additional class, this drone detection program is presented.

Installation:

Download the files to a directory on disk. Unzip the file with the test images (Test1).

Since these are Roboflow utilities updated on August 16, 2025, which may cause incompatibilities with previous versions, it is recommended to create a new environment and install in  it.

pip install supervision

pip install rfdetr

Run the test

python TEST_Drone_Detection_RFDETRBase.py

You can change the folder with the test images by modifying line 7 of the program.

Notes:

Despite lowering the THRESHOLD parameter to 0.3 (line 11 of the program), some drones are not detected.

It seems that the results are worse than those obtained by testing the models on the Roboflow website at
https://universe.roboflow.com/drone-detection-pexej/drone-detection-data-set-yolov7/dataset/1 (you may need a Roboflow API key, which is free and easily obtained).

Also, considering true positives, looks inferior to those obtained with Yolov10 in the project https://github.com/ablanco1950/Drone-Detection_Yolov10

Even with the project uploaded to the Roboflow website https://app.roboflow.com/a-stx8a/drone_detection_rf_detr-9ghzn/models/drone_detection_rf_detr-9ghzn/1, which was trained with only 342 images.

On the other hand, RFDETRBase, besides of a very good precission, allows for the simultaneous detection of not only drones but also multiple objects.

The program used in this project is based on the program found at https://blog.roboflow.com/train-rf-detr-on-a-custom-dataset/, with some modifications.

Cite:

James Gallagher, Piotr Skalski. (Mar 20, 2025). How to Train RF-DETR on a Custom Dataset. Roboflow Blog: https://blog.roboflow.com/train-rf-detr-on-a-custom-dataset/
