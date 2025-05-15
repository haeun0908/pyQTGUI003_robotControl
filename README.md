# pyQTGUI003_robotControl
이 프로그램은 웹캠 영상을 실시간으로 분석해, 사용자 정의 YOLOv5 모델(best.pt)로 객체를 탐지합니다.<br>
탐지된 물체는 화면에 네모 상자와 이름표로 표시되며, 특히 "space-empty"(빈 주차 공간)이 감지되면, 시리얼 포트를 통해 로봇에 제어 명령을 전송합니다.<br>
로봇 동작은 5초 간격으로만 실행되며, 프로그램 종료는 'q' 키로 가능합니다.

## 1. 프로그램 준비
https://github.com/haeun0908/pyQTGUI002_yoloV5<br><br>
지난번에 PyQt6와 OpenCV를 활용해서 만든 웹캠 영상 프로그램을 새 폴더로 옮겼습니다.<br><br>
![1](https://github.com/haeun0908/pyQTGUI003_robotControl/blob/main/images/1.%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8%20%EC%A4%80%EB%B9%84.png)<br>

## 2. 새로운 작업 환경 만들기
```
conda create -n robotControl python=3.9
```
conda create -n [환경 이름] 명령어를 사용해서 다른 프로젝트와 겹치지 않게 새 가상 환경을 만들고 해당 환경을 활성화했습니다.<br>

## 3. motion_controller.py와 serial_port_selector.py 코드 가져오기
https://github.com/Emmett6401/humanoidMotionControl_python<br><br>
PyQt5 기반 GUI를 통해 시리얼 포트를 선택하고, 해당 포트로 로봇 제어 명령을 보내는 기능을 사용하기 위해, 위 링크의 motion_controller.py와 serial_port_selector.py 파일을 작업 폴더에 복제했습니다.<br><br>
![3](https://github.com/haeun0908/pyQTGUI003_robotControl/blob/main/images/3.%20%EC%BD%94%EB%93%9C%20%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0.png)<br>

## 4. 필수 라이브러리 설치
```
pip install torch
pip install opencv-python
pip install pandas
pip install requests
pip install pillow
pip install pyseria
pip install PyQt5
```

## 5. 프로그램 완성 및 기능 구현
AI 결과에 따라서 로봇이 행동을 하도록 프로그램을 완성했습니다.<br><br>
![code](https://github.com/haeun0908/pyQTGUI003_robotControl/blob/main/images/code.png)<br>
