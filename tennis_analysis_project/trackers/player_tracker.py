from ultralytics import YOLO
import cv2
import pickle
import sys, os
sys.path.append('../')
from ..utils.bbox_utils import get_center_of_bbox, draw_bbox_on_frame
from ..utils.conversions import measure_distance

class PlayerTracker:
    def __init__(self,model_path):
        self.model=YOLO(model_path)
    def detect_frame(self,frame):
        results=self.model.track(frame,show=True,persist=True)[0]
        player_dict={}
        id_name_dict=results.names
        for box in results.boxes:
            track_id = int(box.id.tolist()[0])
            result = box.xyxy.tolist()[0]
            object_cls_id = box.cls.tolist()[0]
            object_cls_name = id_name_dict[object_cls_id]
            if object_cls_name == "person":
                player_dict[track_id] = result
        return player_dict
    def detect_frames(self,frames,read_from_stub=False,stub_path=None):
        player_dict={}
        if(read_from_stub and stub_path is not None):
            with open(stub_path, "rb") as f:
                results = pickle.load(f)
            return results
        for frame in frames:
            player = self.detect_frame(frame)
            player_dict.append(player)
        if stub_path is not None:
            with open(stub_path, 'wb') as f:
                pickle.dump(player_dict, f)
        return player_dict
    def choose_players(selfs,court_keypoints,player_dict):
        distance={}

        for key,value in player_dict.items():
            distance.append((key,measure_distance(get_center_of_bbox(value),court_keypoints)))
        distance=sorted(distance,key=lambda item: item[1])
        





