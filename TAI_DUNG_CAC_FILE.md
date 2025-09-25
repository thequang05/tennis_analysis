# 📁 TÁC DỤNG CÁC FILE TRONG PROJECT TENNIS ANALYSIS

## 📋 PHASE 1: SETUP CƠ BẢN

### **1. `requirements.txt`**
**Tác dụng**: Liệt kê tất cả thư viện Python cần thiết
- **ultralytics**: Để sử dụng YOLO models
- **torch**: Deep learning framework
- **opencv-python**: Xử lý video và hình ảnh
- **pandas**: Xử lý dữ liệu dạng bảng
- **numpy**: Tính toán số học
- **gdown**: Tải models từ Google Drive

---

## 🛠️ UTILITIES - CÁC FILE TIỆN ÍCH

### **2. `utils/video_utils.py`**
**Tác dụng**: Xử lý video cơ bản
- **`read_video()`**: Đọc file video thành danh sách các frame (ảnh)
- **`save_video()`**: Lưu danh sách frames thành file video
- **`resize_video()`**: Thay đổi kích thước video (giảm tải máy)
- **`get_video_info()`**: Lấy thông tin video (fps, kích thước, số frame)
- **`extract_frames_at_timestamps()`**: Lấy frame tại thời điểm cụ thể

### **3. `utils/bbox_utils.py`**
**Tác dụng**: Xử lý bounding box (hộp bao quanh object)
- **`get_center_of_bbox()`**: Lấy tâm của hộp bao
- **`get_width_of_bbox()`**: Lấy chiều rộng hộp
- **`get_height_of_bbox()`**: Lấy chiều cao hộp
- **`get_area_of_bbox()`**: Tính diện tích hộp
- **`calculate_iou()`**: Tính độ trùng lặp giữa 2 hộp
- **`draw_bbox_on_frame()`**: Vẽ hộp lên ảnh

### **4. `utils/conversions.py`**
**Tác dụng**: Chuyển đổi đơn vị và tính toán
- **`measure_distance()`**: Tính khoảng cách giữa 2 điểm
- **`convert_pixel_distance_to_meters()`**: Chuyển pixel sang mét thật
- **`convert_meters_to_pixel_distance()`**: Chuyển mét sang pixel
- **`calculate_speed_mps()`**: Tính tốc độ (m/s)
- **`convert_mps_to_kmh()`**: Chuyển m/s sang km/h
- **`calculate_angle_between_points()`**: Tính góc giữa 2 điểm

### **5. `constants/__init__.py`**
**Tác dụng**: Lưu các hằng số cố định
- **Kích thước sân tennis thật**: SINGLE_LINE_WIDTH, DOUBLE_LINE_WIDTH...
- **Chiều cao người chơi**: PLAYER_1_HEIGHT_METERS...
- **Cài đặt video**: DEFAULT_FPS, DEFAULT_VIDEO_CODEC
- **Ngưỡng phát hiện**: DEFAULT_CONFIDENCE_THRESHOLD...

---

## 🎯 PHASE 2: OBJECT DETECTION

### **6. `trackers/player_tracker.py`**
**Tác dụng**: Phát hiện và theo dõi người chơi
- **`__init__()`**: Khởi tạo YOLO model để phát hiện người
- **`detect_frame()`**: Phát hiện người trong 1 frame
- **`detect_frames()`**: Phát hiện người trong nhiều frames
- **`choose_players()`**: Chọn 2 người gần sân tennis nhất
- **`choose_and_filter_players()`**: Lọc chỉ giữ lại 2 người chơi
- **`draw_bboxes()`**: Vẽ hộp bao quanh người chơi
- **`calculate_player_speed()`**: Tính tốc độ di chuyển

### **7. `trackers/ball_tracker.py`**
**Tác dụng**: Phát hiện và theo dõi bóng tennis
- **`__init__()`**: Khởi tạo fine-tuned YOLO model
- **`detect_frame()`**: Phát hiện bóng tennis trong 1 frame
- **`detect_frames()`**: Phát hiện bóng trong nhiều frames
- **`interpolate_ball_positions()`**: Điền vị trí bóng bị mất
- **`get_ball_shot_frames()`**: Phát hiện thời điểm đánh bóng
- **`calculate_ball_speed()`**: Tính tốc độ bóng
- **`draw_bboxes()`**: Vẽ hộp bao quanh bóng
- **`track_ball_trajectory()`**: Theo dõi quỹ đạo bóng

---

## 🧪 TESTING

### **8. `test_phase_1_2.py`**
**Tác dụng**: Test tất cả functions đã viết
- **`test_video_utils()`**: Test các function xử lý video
- **`test_bbox_utils()`**: Test các function xử lý bounding box
- **`test_conversions()`**: Test các function chuyển đổi
- **`test_player_tracker()`**: Test phát hiện người chơi
- **`test_ball_tracker()`**: Test phát hiện bóng tennis

---

## 🎯 TẠI SAO CẦN CÁC FILE NÀY?

### **1. Tách biệt chức năng (Separation of Concerns)**
- Mỗi file có 1 nhiệm vụ cụ thể
- Dễ bảo trì và debug
- Có thể tái sử dụng code

### **2. Modular Design**
- Có thể test từng phần riêng biệt
- Dễ mở rộng thêm tính năng
- Code sạch và có tổ chức

### **3. Reusability**
- Các utility functions có thể dùng nhiều nơi
- Constants được định nghĩa 1 lần, dùng nhiều lần
- Trackers có thể dùng cho video khác

### **4. Testing & Debugging**
- File test riêng để kiểm tra từng function
- Dễ tìm lỗi khi có vấn đề
- Đảm bảo chất lượng code

---

## 📊 LUỒNG SỬ DỤNG CÁC FILE:

```
1. constants/__init__.py → Cung cấp hằng số
2. utils/video_utils.py → Đọc video input
3. trackers/player_tracker.py → Phát hiện người chơi
4. trackers/ball_tracker.py → Phát hiện bóng tennis
5. utils/bbox_utils.py → Xử lý bounding boxes
6. utils/conversions.py → Tính toán tốc độ, khoảng cách
7. utils/video_utils.py → Lưu video output
```

---

## 💡 VÍ DỤ SỬ DỤNG:

### **Kịch bản 1: Đọc và xử lý video**
```python
# 1. Đọc video
frames = read_video("input.mp4")

# 2. Lấy thông tin video
info = get_video_info("input.mp4")

# 3. Resize video để giảm tải
small_frames = resize_video(frames, target_width=640)

# 4. Lưu video đã xử lý
save_video(small_frames, "output.mp4")
```

### **Kịch bản 2: Phát hiện và tracking**
```python
# 1. Khởi tạo trackers
player_tracker = PlayerTracker("yolov8x")
ball_tracker = BallTracker("ball_model.pt")

# 2. Phát hiện objects
player_detections = player_tracker.detect_frames(frames)
ball_detections = ball_tracker.detect_frames(frames)

# 3. Tính toán tốc độ
player_speeds = player_tracker.calculate_player_speed(player_detections)
ball_speeds = ball_tracker.calculate_ball_speed(ball_detections, ball_shot_frames)
```

### **Kịch bản 3: Xử lý bounding box**
```python
# 1. Lấy thông tin bbox
bbox = [100, 200, 300, 400]  # [x1, y1, x2, y2]
center = get_center_of_bbox(bbox)
width = get_width_of_bbox(bbox)
height = get_height_of_bbox(bbox)

# 2. Vẽ bbox lên frame
frame_with_bbox = draw_bbox_on_frame(frame, bbox, color=(0, 255, 0))
```

### **Kịch bản 4: Chuyển đổi đơn vị**
```python
# 1. Tính khoảng cách pixel
pixel_distance = measure_distance((100, 200), (300, 400))

# 2. Chuyển sang mét
meters = convert_pixel_distance_to_meters(
    pixel_distance, 
    DOUBLE_LINE_WIDTH,  # 10.97m
    court_width_pixels  # pixel width của sân
)

# 3. Tính tốc độ
speed_mps = calculate_speed_mps(meters, time_seconds)
speed_kmh = convert_mps_to_kmh(speed_mps)
```

---

## 🔧 MỐI QUAN HỆ GIỮA CÁC FILE:

### **Dependencies (Phụ thuộc):**
```
trackers/player_tracker.py
    ↓ import
utils/bbox_utils.py
utils/conversions.py

trackers/ball_tracker.py
    ↓ import
utils/bbox_utils.py
utils/conversions.py

test_phase_1_2.py
    ↓ import
utils/video_utils.py
utils/bbox_utils.py
utils/conversions.py
trackers/player_tracker.py
trackers/ball_tracker.py
```

### **Data Flow (Luồng dữ liệu):**
```
Video Input → video_utils.py → frames
frames → player_tracker.py → player_detections
frames → ball_tracker.py → ball_detections
detections → bbox_utils.py → bbox_info
bbox_info → conversions.py → metrics
metrics + frames → video_utils.py → Video Output
```

---

## 📈 LỢI ÍCH CỦA CẤU TRÚC NÀY:

### **1. Dễ học và hiểu**
- Mỗi file có mục đích rõ ràng
- Functions được đặt tên dễ hiểu
- Code được tổ chức logic

### **2. Dễ debug**
- Có thể test từng function riêng
- Lỗi dễ tìm và sửa
- Có file test riêng

### **3. Dễ mở rộng**
- Thêm function mới vào file phù hợp
- Không ảnh hưởng code khác
- Modular design

### **4. Dễ tái sử dụng**
- Utility functions dùng được nhiều nơi
- Constants định nghĩa 1 lần
- Trackers có thể dùng cho video khác

**Tóm lại**: Mỗi file có vai trò cụ thể trong việc xây dựng hệ thống phân tích tennis, từ xử lý video cơ bản đến phát hiện objects phức tạp! 🎾
