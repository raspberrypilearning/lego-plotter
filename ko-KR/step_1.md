## 소개

LEGO®와 Raspberry Pi Build HAT를 사용하여 데이터 플로터를 만들어 보세요.

### 만들 작품

--- no-print ---

![LEGO® 플로터가 작동하는 모습을 보여주는 동영상 펜으로 추적하는 녹색 신호와 함께 종이 한 장이 기계에서 급지되고 있는 모습](images/plotter_demo.gif)

--- /no-print ---

--- print-only --- ![A photo of the completed plotter project.](images/completed.jpg) --- /print-only ---

### 배울 지식

+ 회전 각도를 계산하는 방법
+ 시각화를 위해 데이터 범위를 적절한 스케일에 매핑하는 방법
+ 조건문 사용 방법(if문/else문)

### 하드웨어

+ Raspberry Pi
+ A Raspberry Pi Build HAT
+ LEGO® Technic™ 모터 2개
+ A LEGO® SPIKE™ Force Sensor OR a push button, breadboard, and jumper wires
+ 바퀴 2개를 포함한 다양한 LEGO®([LEGO® Education SPIKE™ Prime 키트](https://education.lego.com/en-gb/product/spike-prime)에서 선택 사용)
+ 배럴 잭이 있는 7.5V 전원 공급 장치 (대신 보조배터리를 사용할 수 있지만 모든 셀이 완전히 충전되었는지 확인)

### 소프트웨어

+ Python 3
+ Vcgencmd Python3 라이브러리

### 다운로드

+ [LEGO® SPIKE™ Prime 조립 설명서: *소포 추적* (1/2)](https://le-www-live-s.legocdn.com/sc/media/lessons/prime/pdf/building-instructions/track-your-packages-bi-pdf-book1of2-05883f81fed73ac3738781d084e0d4e2.pdf){:target="_blank"}
+ [LEGO® SPIKE™ Prime 조립 설명서: *소포 추적* (2/2)](https://le-www-live-s.legocdn.com/sc/media/lessons/prime/pdf/building-instructions/track-your-packages-bi-pdf-book2of2-80dc3c8c61ec2d2ffa785b688326ef74.pdf){:target="_blank"}
+ [Lego Plotter 완성된 스크립트](http://rpf.io/p/en/lego-plotter-go){:target="_blank"}

--- collapse ---
---
title: Vcgencmd Python 라이브러리 설치
---

인터넷에 연결되어 있는지 확인하세요.

Open the terminal on your Raspberry Pi by pressing <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd> on your keyboard.

프롬프트에서 `pip3 install vcgencmd` 을 입력 하고 <kbd>Enter</kbd> 를 입력합니다.

확인 메시지를 기다린 다음(오래 걸리지 않음) 터미널 창을 닫습니다.

--- /collapse ---

--- collapse ---
---
title: 교육자를 위한 추가 정보
---

완성 된 프로젝트는 [여기](http://rpf.io/p/en/projectName-get){:target="_blank"} 에서 다운로드 할 수 있습니다.

이 프로젝트를 인쇄한다면 [프린트용 버전](https://projects.raspberrypi.org/en/projects/projectName/print){:target="_blank"}을 사용해 주십시오.

--- /collapse ---

시작하기 전에 Raspberry Pi 컴퓨터를 설정하고 Build HAT를 연결해야 합니다.

--- task ---

M2 볼트와 너트를 사용하여 LEGO Build Plate에 Raspberry Pi를 장착하고 Raspberry Pi가 '가장자리' 쪽에 없는지 꼭 확인합니다.

 ![마젠타색 LEGO 빌드 플레이트에 볼트로 고정된 Raspberry Pi](images/build_11.jpg)

--- /task ---

Mounting the Raspberry Pi this way round enables easy access to the ports as well as the SD card slot. Build Plate를 사용하면 Raspberry Pi를 대시보드에 더 쉽게 연결할 수 있습니다.

--- task ---

Build HAT를 Raspberry Pi와 정렬하여 `This way up` 레이블이 보이도록 합니다. 모든 GPIO 핀이 HAT로 덮여 있는지 확인하고 단단히 눌러주세요. (이 예시에서는 [스택 헤더](https://www.adafruit.com/product/2223){:target="_blank"}을 사용하므로 핀이 더 길어집니다.)

![Build HAT 상단을 관통하는 GPIO 핀의 이미지](images/build_15.jpg) ![Raspberry Pi에 적합한 Build HAT을 보여주는 애니메이션](images/haton.gif)

--- /task ---

이제 Build HAT의 7.5V 배럴 잭을 사용하여 Raspberry Pi에 전원을 공급해야 합니다. 그러면 이제부터 모터를 사용할 수 있습니다.

--- task ---

아직 설정하지 않았다면 다음 지침에 따라 Raspberry Pi를 설정하세요.

[Setting up your Raspberry Pi](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up){:target="_blank"}

--- /task ---

--- task ---

Raspberry Pi가 부팅되면 Raspberry 메뉴 버튼을 클릭하고 "기본 설정(Preferences)"를 선택한 다음 "Raspberry Pi Configuration"을 선택하여 Raspberry Pi Configuration 도구를 엽니다.

Click on the “interfaces” tab and adjust the Serial settings as shown below:

![직렬 포트가 활성화되고 직렬 콘솔이 비활성화된 Raspberry Pi 구성 화면을 보여주는 이미지](images/configshot.jpg)

--- /task ---

--- task ---

또한 다음 지침에 따라 buildhat python 라이브러리를 설치해야 합니다:

--- collapse ---
---
title: buildhat Python 라이브러리 설치
---

<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>를 눌러 Raspberry Pi에서 터미널 창을 엽니다.

커맨드 창에서 다음을 입력합니다: `sudo pip3 install buildhat`

<kbd>Enter</kbd> 를 누르고 "설치 완료" 메시지를 확인합니다.

--- /collapse ---

--- /task ---
