Drone_Detection_RFDETRBase

Since have been noticed that Roboflow's RFDETRBase incorporates the drone class as an additional class, this drone detection program is presented.

Installation:

Download the files to a directory on disk. Unzip the file with the test images (Test1).

Since these are Roboflow utilities updated on August 16, 2025, which may cause incompatibilities with previous versions, it is recommended to create a new environment and install in  it.

pip install torchvision

pip install supervision

pip install rfdetr

Run the test

python TEST_Drone_Detection_RFDETRBase.py

You can change the folder with the test images by modifying line 7 of the program.

Notes:

Despite lowering the THRESHOLD parameter to 0.3 (line 11 of the program), some drones are not detected.

The program used in this project is based on the program found at https://blog.roboflow.com/train-rf-detr-on-a-custom-dataset/, with some modifications.

Although as of 09/10/2025 in the list of classes of the COCO dataset, with which most of the models are pre-trained, class 5 appears as "airplane", by running this simple program it can be verified that drones are detected that do not have any appearance of airplanes.

You can make comparisons with other projects; the ones I've found to be the most accurate are:

https://universe.roboflow.com/drone-detection-pexej/drone-detection-data-set-yolov7/dataset/1 (you may need a Roboflow API key, which is free and easily obtained).

https://github.com/ablanco1950/Drone-Detection_Yolov10

https://app.roboflow.com/a-stx8a/drone_detection_rf_detr-9ghzn/models/drone_detection_rf_detr-9ghzn/1

https://github.com/ablanco1950/Drone-Detection-fasterrcnn_resnet50_fpn

On the other hand, RFDETRBase, besides of a very good precission, allows for the simultaneous detection of not only drones but also multiple objects.

It is observed that these projects are complementary, some objects are detected by some, but not by others, so a solution could be a project that uses several modules in cascade as occurs in the project https://github.com/ablanco1950/Drone-Detection_Yolov10

Cite:

James Gallagher, Piotr Skalski. (Mar 20, 2025). How to Train RF-DETR on a Custom Dataset. Roboflow Blog: https://blog.roboflow.com/train-rf-detr-on-a-custom-dataset/
