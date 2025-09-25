import cv2
import os
def read_video(video_path):
    vid=cv2.VideoCapture("tennis_analysis_project/input_videos/input_video.mp4")
    frames=[]
    success = True
    while(success):
        success,image=vid.read()
        if(not success):
            break
        frames.append(image)
    return frames
def save_video(frames,output_path,fps=24):
    fourcc=cv2.VideoWriter_fourcc(*'MJPG')
    height,width,channels=frames[0].shape
    out=cv2.VideoWriter(output_path,fourcc,fps,(width,height))
    for frame in frames:
        out.write(frame)
    out.release()
def resize_video(frames,target_width=None,target_height=None):
    new_frames = []
    for frame in frames:
        h, w = frame.shape[:2]

        # Nếu không có target thì giữ nguyên
        if target_width is None and target_height is None:
            new_frames.append(frame)
            continue

        # Nếu chỉ có width
        if target_height is None:
            aspect_ratio = target_width / w
            target_height = int(h * aspect_ratio)

        # Nếu chỉ có height
        if target_width is None:
            aspect_ratio = target_height / h
            target_width = int(w * aspect_ratio)

        resized = cv2.resize(frame, (target_width, target_height))
        new_frames.append(resized)
    return new_frames
def get_video_info(video_path):
    vid=cv2.VideoCapture(video_path)
    fps=vid.get(cv2.CAP_PROP_FPS)
    frame_count = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    vid.release()
    return {
        "fps": fps,
        "frame_count": frame_count,
        "width": width,
        "height": height
    }
def extract_frames_at_timestamps(video_path,timestamps):
    vid=cv2.VideoCapture(video_path)

    fps = vid.get(cv2.CAP_PROP_FPS)
    frames = []

    for t in timestamps:
        # Tính frame index tương ứng
        frame_number = int(t * fps)
        # Set vị trí frame
        vid.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = vid.read()
        if not ret:
            print(f"⚠️ Không thể đọc frame tại {t} giây (frame {frame_number})")
            frames.append(None)
        else:
            frames.append(frame)

    vid.release()
    return frames