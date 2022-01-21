## 데이터로 모터 이동하기

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">[지진계](https://ko.wikipedia.org/wiki/%EC%A7%80%EC%A7%84%EA%B3%84) </span> 를 활용하여 진동을 표시하는 장면을 본 적이 있을 것입니다. 

이러한 장치의 디자인은 매우 간단합니다. 하나의 모터는 펜(x축)을 지나 종이를 이동하는 데 사용되는 반면 다른 모터는 첫 번째에 직각으로 변화하는 데이터(y -중심선)에 사용하면 됩니다. </p>

이 프로젝트에서는 LEGO®에서 플로터를 만들고 이를 Raspberry Pi에 연결하여 실시간 데이터를 종이에 그릴 수 있도록 합니다.

--- task ---

모니터, 키보드, 마우스를 Raspberry Pi 장치에 연결합니다. 이전에 Raspberry Pi를 사용한 적이 없다면 [이 프로젝트](https://projects.raspberrypi.org/en/projects/raspberry-pi-getting-started)로 시작하는 것이 좋습니다.

Build HAT를 Raspberry Pi에 연결하고(상단에 Raspberry Pi 로고가 보이는지 확인) Build HAT의 배럴 잭에 7.5V 전원 공급 장치를 연결합니다. 그러면 Raspberry Pi가 부팅될 것입니다.

--- /task ---

--- task ---

프로그래밍 메뉴에서 Thonny를 열고 다음 줄을 추가하여 사용할 라이브러리를 가져와서 프로그램을 시작하세요.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 1
line_highlights: 1,2,3
---

from random import randint from time import sleep from buildhat import Motor

--- /code ---

<kbd>Ctrl</kbd>+<kbd>s</kbd>를 눌러 이 프로그램을 `plotter.py` 로 저장하세요.

--- /task ---

--- task ---

이제 `randint` 함수를 사용하여 범위(이 경우 -180 ~ 180) 사이의 랜덤 값을 만들고 `new_angle`이라는 변수에 저장합니다.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 5
line_highlights: 5,6
---

new_angle = randint(-180,180) print(new_angle)

--- /code ---

--- /task ---

--- task ---

창 상단에 있는 **Run** 버튼을 클릭하여 프로그램을 몇 번 실행하십시오. 매번 코드 아래의 셸에 다른 임의의 값이 표시되어야 합니다.

--- /task ---

이 스크립트를 수동으로 실행하는 대신 **Loop** 를 만들어 스크립트를 반복적으로 실행하십시오. 같은 코드 라인을 계속 실행하려면 `while True:` 루프를 사용할 수 있습니다.

--- task ---

<kbd>Enter</kbd>을 눌러 방금 추가한 코드 위에 빈 줄을 추가합니다.

이 새 줄에 `while True:` 를 추가하세요; 꼭 T가 대문자 'T' 인지 확인하십시오.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 5
line_highlights: 5
---

while True: new_angle = randint(-180,180) print(new_angle)

--- /code ---

--- /task ---

--- task ---

아래의 각 줄 시작 부분에 4개의 공백을 추가하여 **들여쓰기**를 합니다. 이것은 루프에 포함된 라인임을 컴퓨터에 알려줍니다.


--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 5
line_highlights: 6,7
---

while True: new_angle = randint(-180,180) print(new_angle)

--- /code ---

--- /task ---

--- task ---

코드 끝에서 다른 들여쓰기 행을 추가하려면 <kbd>Enter</kbd> 를 누르세요. 여기서는, `sleep(0.1)` 을 사용합니다.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 5
line_highlights: 8
---

while True: new_angle = randint(-180,180) print(new_angle) sleep(0.1)

--- /code ---

--- /task ---

--- task ---

코드를 실행하여 쉘에 인쇄된 값을 확인하십시오. 오류가 발생하면 코드가 다음과 같은지 확인하십시오:

--- code ---
---
language: python filename: plotter.py line_numbers: true
line_number_start: 1
---

from random import randint from time import sleep from buildhat import Motor

while True: new_angle = randint(-180,180) print(new_angle) sleep(0.1)

--- /code ---

--- /task ---

이제 일부 데이터가 있으므로 이 데이터들을 사용하여 모터의 위치를 제어할 수 있습니다.

--- task ---

LEGO® Technic™ 모터를 Build HAT의 포트 A에 연결하세요. 모터 회전을 쉽게 볼 수 있도록 모터 액슬에 LEGO 부품을 추가하세요.

--- /task ---

--- task ---

부품을 모터의 선 표시와 정렬한 다음 모터를 0 위치로 설정합니다.

![인코더를 0도로 설정하는 데 사용되는 막대 사탕과 제로 라벨을 보여주는 LEGO® Technic™ 모터 사진](images/zero.JPG)

--- /task ---

이제 모터가 회전하는 각도가 시뮬레이션된 센서에서 생성된 최신 값과 동일하도록 프로그램의 main 소스코드를 수정하세요.

이렇게 하려면 프로그램에서 액세스할 수 있도록 모터를 설정하여야 합니다.

--- task ---

Build HAT 의 `A` `motor_y` 객체를 `100`의 속도로 `0` 위치로 돌리도록 코드를 제작합니다.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 4
line_highlights: 5, 6
---

motor_y = Motor('A') motor_y.run_to_position(0, 100)

--- /code ---

--- /task ---

--- task ---

다음 라인은 `new_angle`에 저장된 각도로 회전하도록 합니다.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 7
line_highlights: 11
---

while True: new_angle = randint(-180,180) print(new_angle) motor_y.run_to_position(new_angle, 100)

--- /code ---

--- /task ---

--- task ---

**Run** 을 클릭하면 변화하는 데이터에 대한 응답으로 모터가 시계 방향으로 다른 위치로 회전하는 것을 볼 수 있습니다. 프로그램을 다시 실행하면 다시 무작위로 이동하기 전에 `0`으로 포지션이 리셋됩니다.

오류가 발생하면 코드가 다음과 같은지 확인하십시오.

--- code ---
---
language: python filename: plotter.py line_numbers: true
line_number_start: 1
---

from random import randint from time import sleep from buildhat import Motor

motor_y = Motor('A') motor_y.run_to_position(0, 100)

while True: new_angle = randint(-180,180) print(new_angle) motor_y.run_to_position(new_angle, 100) sleep(0.1)

--- /code ---

--- /task ---

![검은색 빔 요소가 부착된 LEGO® Technic™ 모터를 보여주는 동영상 모터는 회전하고 부착된 빔은 데이터에 응답하여 시계 바늘처럼 회전 모터는 0도에서 180도 사이에서만 회전하며 시계 방향과 시계 반대 방향으로 움직임](images/motor_180.gif)

--- save ---
