import cv2
import numpy as np
def get_center_of_bbox(bbox):
    center_x=(bbox[0]+bbox[2])/2
    center_y=(bbox[1]+bbox[3])/2
    return center_x,center_y
def get_width_of_bbox(bbox):
    return bbox[2]-bbox[0]
def get_height_of_bbox(bbox):
    return bbox[3]-bbox[1]
def get_area_off_bbox(bbox):
    return get_width_of_bbox(bbox)*get_height_of_bbox(bbox)
def calculate_iou(bbox1,bbox2):
    x_left = max(bbox1[0], bbox2[0])
    y_top = max(bbox1[1], bbox2[1])
    x_right = min(bbox1[2], bbox2[2])
    y_bottom = min(bbox1[3], bbox2[3])
    if x_right <= x_left or y_bottom<=y_top:
        return 0.0
    intersection_area = (x_right - x_left) * (y_bottom - y_top)
    bbox1_area = (bbox1[2] - bbox1[0]) * (bbox1[3] - bbox1[1])
    bbox2_area = (bbox2[2] - bbox2[0]) * (bbox2[3] - bbox2[1])
    union_area = bbox1_area + bbox2_area - intersection_area
    if union_area == 0:
        return 0.0
    return intersection_area / union_area
def draw_bbox_on_frame(frame,bbox,color=(0,255,0),thickness=2):
    x1,y1,x2,y2=bbox
    cv2.rectangle(frame,(x1,y1),(x2,y2),color,thickness)
    return frame

