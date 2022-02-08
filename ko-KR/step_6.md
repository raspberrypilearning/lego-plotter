## 버튼 컨트롤 추가하기

플로터 실행을 중지하고 시작하려면 빌드에 버튼을 추가해 주셔야 합니다.

--- task ---

LEGO® SPIKE™ Prime Force Sensor는 단순한 버튼 역할로 사용할 수 있습니다. Build HAT의 포트 C에 모터를 연결하세요.

![힘 센서가 추가된 LEGO® 플로터 부분의 클로즈업 사진](images/force.jpg)

--- /task ---

--- task ---

버튼 컨트롤을 포함하도록 `plotter.py` 프로그램을 편집하세요. 쉼표 뒤에 `ForceSensor`를 추가합니다(대문자 **둘 다** 포함해야 합니다!). `from buildhat import Motor`이라는 줄 아래에 추가해 주세요:

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 1
line_highlights: 3
---

from random import randint
from time import sleep
from buildhat import Motor, ForceSensor

--- /code ---

--- /task ---

--- task ---

스위치에 대한 개체를 만들려면 모터에 대한 유사한 줄 뒤에 다음 줄을 추가합니다.

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 5
line_highlights: 7
---

motor_y = Motor('A')
motor_x = Motor('B')
button = ForceSensor('C')
motor_y.run_to_position(0, 100)
motor_x.start(-25)

--- /code ---

--- /task ---

--- task ---

`while True` main loop를 다음과 같이 변경하세요:

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 13
line_highlights: 
---

while not button.is_pressed():
    current_angle = motor_y.get_aposition()
    new_angle = randint(-180, 180)

--- /code ---

--- /task ---

--- task ---

이제 버튼을 눌러 플로터 작동을 중지하실 수 있습니다. 모든 것을 정리하고 두 모터를 모두 멈추려면 프로그램 끝에 다음 줄을 추가하세요:

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 19
line_highlights: 24-26
---

    elif new_angle < current_angle:
        motor_y.run_to_position(new_angle, 100, direction="anticlockwise")
        print('Turning ACW')
    sleep(0.1)
    
motor_x.stop()
motor_y.run_to_position(0, 100)

--- /code ---

--- /task ---

이제 제작한 플로터를 테스트할 준비가 되었습니다. 다음과 같은 코드가 될 것입니다.:

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 1
---

#!/usr/bin/python3
from random import randint
from time import sleep
from buildhat import Motor, ForceSensor

button = ForceSensor('C')
motor_y = Motor('A')
motor_x = Motor('B')

motor_y.run_to_position(0, 100)
motor_x.start(speed=-25)

while not button.is_pressed():
    current_angle = motor_y.get_aposition()
    new_angle = randint(-180, 180)
    if new_angle > current_angle:
        motor_y.run_to_position(new_angle, 100, direction="clockwise")
        print('Turning CW')
    elif new_angle < current_angle:
        motor_y.run_to_position(new_angle, 100, direction="anticlockwise")
        print('Turning ACW')
    sleep(0.1)
    
motor_x.stop()
motor_y.run_to_position(0, 100)

--- /code ---

--- task ---

앞쪽 짧은 가장자리가 펜 바로 너머에 오도록 플로터 뒤쪽에서 용지 한 장을 공급하세요.

--- /task ---

--- task ---

Thonny에서 프로그램을 시작하고 펜이 종이에 랜덤한 그림을 그리는 것을 지켜보세요!

--- /task ---

--- task ---

용지를 전부 사용한 후에는 힘 센서를 눌러 모든 작업을 중지합니다.

--- /task ---

![플로터가 녹색 흔적을 그린 종이 사진](images/paper.JPG)

다음 단계에서는 입력 데이터에 실시간 데이터 소스를 사용해 볼 것입니다!

--- save ---
