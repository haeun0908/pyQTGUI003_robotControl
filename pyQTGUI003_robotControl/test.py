import sys
import torch
import cv2
import numpy as np
import time  # ⬅️ 시간 관리를 위해 추가
from PyQt5.QtWidgets import QApplication
from motion_controller import execute_motion
from serial_port_selector import SerialPortSelector

# QApplication을 먼저 생성
app = QApplication(sys.argv)

# YOLOv5 모델 로드
model = torch.hub.load('ultralytics/yolov5',
                       'custom',
                       path='best.pt',
                       force_reload=True)
model.eval()

# 시리얼 포트 선택
selected_port = SerialPortSelector.launch()
if not selected_port:
    print("No serial port selected. Exiting...")
    sys.exit()

# 웹캠 활성화
cap = cv2.VideoCapture(0)

# 마지막 모션 실행 시간을 저장할 변수
last_action_time = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # YOLOv5를 사용한 객체 탐지
    results = model(frame)
    annotated_frame = results.render()[0]

    # 현재 시간 가져오기
    current_time = time.time()

    # 탐지된 객체 확인
    for *box, conf, cls in results.xyxy[0]:
        label = results.names[int(cls)]
        
        if label == "space-empty":
            # 마지막 모션 실행 후 5초가 지났다면 동작 실행
            if current_time - last_action_time >= 5:
                print("Empty parking space detected! Executing robot motion...")
                execute_motion(selected_port, 18)  # 로봇 모션 실행
                last_action_time = current_time  # 마지막 실행 시간 갱신

    # 결과 표시
    cv2.imshow('YOLOv5 Custom', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()

# QApplication 실행
sys.exit(app.exec_())
