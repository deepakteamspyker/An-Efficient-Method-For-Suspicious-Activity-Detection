
import time

import cv2
import imutils
import numpy as np
from imutils.video import FileVideoStream

theImage = cv2.imread("data/distracted-walking.jpg")
time.sleep(1.0)

openposeProtoFile = "dnn_models/pose/coco/pose_deploy_linevec.prototxt"
openposeWeightsFile = "dnn_models/pose/coco/pose_iter_440000.caffemodel"
nPoints = 18

objectdetectionProtoFile = "dnn_models/object_detection/MobileNetSSD_deploy.prototxt"
objectdetectionWeightsFile = "dnn_models/object_detection/MobileNetSSD_deploy.caffemodel"

# COCO Output Format
keypointsMapping = ['Nose', 'Neck', 'R-Sho', 'R-Elb', 'R-Wr', 'L-Sho', 'L-Elb', 'L-Wr', 'R-Hip', 'R-Knee', 'R-Ank',
                    'L-Hip', 'L-Knee', 'L-Ank', 'R-Eye', 'L-Eye', 'R-Ear', 'L-Ear']

POSE_PAIRS = [[1, 2], [1, 5], [2, 3], [3, 4], [5, 6], [6, 7],
              [1, 8], [8, 9], [9, 10], [1, 11], [11, 12], [12, 13],
              [1, 0], [0, 14], [14, 16], [0, 15], [15, 17],
              [2, 17], [5, 16]]

mapIdx = [[31, 32], [39, 40], [33, 34], [35, 36], [41, 42], [43, 44],
          [19, 20], [21, 22], [23, 24], [25, 26], [27, 28], [29, 30],
          [47, 48], [49, 50], [53, 54], [51, 52], [55, 56],
          [37, 38], [45, 46]]

colors = [[0, 100, 255], [0, 100, 255], [0, 255, 255], [0, 100, 255], [0, 255, 255], [0, 100, 255],
          [0, 255, 0], [255, 200, 100], [255, 0, 255], [0, 255, 0], [255, 200, 100], [255, 0, 255],
          [0, 0, 255], [255, 0, 0], [200, 200, 0], [255, 0, 0], [200, 200, 0], [0, 0, 0]]

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow",
           "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))


def getKeypoints(prob_map, thres=0.1):
    map_smooth = cv2.GaussianBlur(prob_map, (3, 3), 0, 0)

    map_mask = np.uint8(map_smooth > thres)
    keypoints_array = []

    # find the blobs
    _, contours, _ = cv2.findContours(map_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # for each blob find the maxima
    for cnt in contours:
        blob_mask = np.zeros(map_mask.shape)
        blob_mask = cv2.fillConvexPoly(blob_mask, cnt, 1)
        masked_prob_map = map_smooth * blob_mask
        _, max_val, _, max_loc = cv2.minMaxLoc(masked_prob_map)
        keypoints_array.append(max_loc + (prob_map[max_loc[1], max_loc[0]],))

    return keypoints_array




frame = cv2.addWeighted(frameClone, 0.5, theImage, 0.5, 0.0)

cv2.imshow("Detected Pose", frame)
cv2.waitKey(0)
