## 실시간 데이터 소스 추가하기

플로터에 데이터 피드를 제공하기 위해 Raspberry Pi에 추가할 수 있는 많은 센서가 있습니다.

내장 데이터 소스부터 시작해 보겠습니다. Raspberry Pi 자체의 CPU 온도를 구할 수 있습니다. `vcgencmd` 라이브러리를 설치하지 않았다면 지금 설치하시면 됩니다.

--- collapse ---
---
title: Vcgencmd Python 라이브러리 설치
---

인터넷에 연결되어 있는지 확인하세요.

키보드에서 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd> 를 눌러 Raspberry Pi에서 터미널을 엽니다.

프롬프트에서 `pip3 install vcgencmd` 을 입력 하고 <kbd>Enter</kbd> 를 입력합니다.

확인 메시지를 기다린 다음(오래 걸리지 않음) 터미널 창을 닫습니다.

--- /collapse --- 

--- task ---

Thonny의 **Shell/REPL** 을 사용하여 다음 Python 줄을 입력하여 CPU 온도를 테스트하고 읽어 보세요.

```python
>>> from vcgencmd import Vcgencmd
```
<kbd>Enter</kbd> 를 누릅니다.

유형:
```python
>>> vcgm = Vcgencmd()
```
<kbd>Enter</kbd> 를 누릅니다.

유형:
```python
>>> vcgm.measure_temp()
```
<kbd>Enter</kbd> 를 누릅니다.

**Shell** 이 숫자 값을 반환하는 것을 볼 수 있어야 합니다(약 50이어야 합니다). 이것이 CPU가 실행되는 온도입니다.

--- /task ---

이제 CPU가 일부 작업을 수행하도록 하여 작업을 돌려 보겠습니다.

--- task ---

웹 브라우저를 열고 YouTube 동영상을 보세요. 몇 초 후에 Thonny로 돌아가서 Python의 마지막 줄을 다시 실행하면, 온도가 상승한 것을 볼 수 있습니다.

--- /task ---

이제 Python으로 CPU 온도를 읽는 방법을 보았으므로 이를 데이터 소스로 사용하도록 `plotter.py`를 수정하세요.

--- task ---

먼저 파일 상단의 기존 불러오기 행 아래에, Vcgencmd 라이브러리를 불러오는 행을 추가합니다.

--- code ---
---
language: python 
filename: plotter.py 
line_numbers: true 
line_number_start: 1
line_highlights: 4
---

from random import randint 
from time import sleep 
from buildhat import Motor, ForceSensor 
from vcgencmd import Vcgencmd

--- /code ---

--- /task ---

--- task ---
vcgencmd 객체를 만드세요:

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 1
line_highlights: 9
---

from random import randint
from time import sleep
from buildhat import Motor, ForceSensor
from vcgencmd import Vcgencmd

motor_y = Motor('A')
motor_x = Motor('B')
button = ForceSensor('C')
vcgm = Vcgencmd()

motor_y.run_to_position(0, 100)
motor_x.start(-25)

--- /code ---

--- /task ---

--- task ---

랜덤하게 생성된 숫자가 아닌 실시간 온도 값을 사용하도록 프로그램을 변경합니다. 이렇게 하려면 `randint(-180, 180)` 을 `vcgm.measure_temp()` 로 바꿔야 합니다.

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 15
line_highlights: 16
---

while not button.is_pressed():
    temp = vcgm.measure_temp()
    current_angle = motor_y.get_aposition()

--- /code ---

--- /task ---

Raspberry Pi의 CPU 온도를 플로터의 데이터 소스로 사용하기 전에 데이터 소스에서 생성된 가능한 최대 값이 수학적으로 변환되어 -180에서 180 사이의 눈금에 맞도록 하여야 합니다.

`vcgencmd` 의해 생성된 온도 값의 범위는 약 50°C(Raspberry Pi가 켜져 있지만 그다지 많이 작동하지 않을 때)에서 열심히 일할 때(85°C에서 Raspberry Pi가 작동할 때) 90°C 미만이어야 합니다. 온도를 이 값 아래로 유지하기 위해 성능을 잘 조절하십시오. 40°C ~ 90°C 범위를 표시하고 싶다고 가정해 보겠습니다. 우리는 이를 사용 가능한 값(-180 ~ 180)에 매핑해야 합니다.

하나의 값 범위를 다른 값 범위에 다시 매핑하는 함수를 만들 수 있습니다.

--- task ---

`while` 루프 위에 이 함수를 추가하십시오. 온도 범위와 각도 범위를 취한 다음 특정 각도로 온도를 할당합니다.

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 12
line_highlights: 13
---

def remap(min_temp, max_temp, min_angle, max_angle, temp):
    temp_range = (max_temp - min_temp)
    motor_range = (max_angle - min_angle)
    mapped = (((temp - min_temp) * motor_range) / temp_range) + min_angle
    return int(mapped)

--- /code ---

이제 `while` 루프에서 이 함수를 사용하여 모터가 회전할 새로운 각도를 계산할 수 있습니다.

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 21
line_highlights: 24
---

while not button.is_pressed():
    temp = vcgm.measure_temp()
    current_angle = motor_y.get_aposition()
    new_angle = remap(50, 90, -170, 170, temp)
--- /code ---

--- /task ---

이제 프로그램을 실행해 보세요. 이전처럼 Raspberry Pi CPU를 따뜻하게 하면 펜이 점점 위로 움직이는 것을 볼 수 있습니다. 펜이 잘 움직이지 않는다면 `min_temp` 및 `max_temp` 매개변수를 자유롭게 수정해 보세요.

![펜이 움직이고 변동하는 선을 그리는 동안 플로터를 통해 움직이는 종이를 보여주는 애니메이션](images/plotter_demo_2.gif)


--- save ---
