## 添加一个控制按钮

您可以在构建中添加一个按钮，来停止和启动绘图仪的运行。

--- task ---

乐高（LEGO®）SPIKE™ Prime 的压力传感器可以作为一个简单的按钮。 在 Build HAT 上的端口 C上连接一个（压力传感器）。

![安装了压力传感器的乐高（LEGO®)绘图仪的特写照片。](images/force.jpg)

--- /task ---

--- task ---

编辑您的 `plotter.py` 程序，增加一个按钮控件。 在`from buildhat import Motor`行的末尾添加一个逗号，然后加上 `ForceSensor`（确保包含 **两个** 大写字母！）：

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 1
line_highlights: 3
---

from random import randint from time import sleep from buildhat import Motor, ForceSensor

--- /code ---

--- /task ---

--- task ---

和添加马达对象一样，用下面语句添加一个按钮的对象

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 5
line_highlights: 7
---

motor_y = Motor('A') motor_x = Motor('B') button = ForceSensor('C') motor_y.run_to_position(0, 100) motor_x.start(-25)

--- /code ---

--- /task ---

--- task ---

将主循环从 `while True` 更改为：

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 13
line_highlights:
---

while not button.is_pressed(): current_angle = motor_y.get_aposition() new_angle = randint(-180, 180)

--- /code ---

--- /task ---

--- task ---

现在您可以通过按下按钮来停止绘图仪的运作。 为了整洁以及能同时停止两个马达，请在程序末尾添加以下行。

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 19
line_highlights: 24-26
---

    elif new_angle < current_angle:
        motor_y.run_to_position(new_angle, 100, direction="anticlockwise")
        print('Turning ACW')
    sleep(0.1)

motor_x.stop() motor_y.run_to_position(0, 100)

--- /code ---

--- /task ---

现在您已可以测试您的绘图仪了。 您的最终代码应该像这样：

--- code ---
---
language: python filename: plotter.py line_numbers: true
line_number_start: 1
---

# !/usr/bin/python3
from random import randint from time import sleep from buildhat import Motor, ForceSensor

button = ForceSensor('C') motor_y = Motor('A') motor_x = Motor('B')

motor_y.run_to_position(0, 100) motor_x.start(speed=-25)

while not button.is_pressed(): current_angle = motor_y.get_aposition() new_angle = randint(-180, 180) if new_angle > current_angle: motor_y.run_to_position(new_angle, 100, direction="clockwise") print('Turning CW') elif new_angle < current_angle: motor_y.run_to_position(new_angle, 100, direction="anticlockwise") print('Turning ACW') sleep(0.1)

motor_x.stop() motor_y.run_to_position(0, 100)

--- /code ---

--- task ---

从绘图仪的后方送入一张纸，使得纸张的短边正好超过画笔。

--- /task ---

--- task ---

在 Thonny 中启动程序，然后观察画笔在纸上绘制着随机数据！

--- /task ---

--- task ---

在纸张用完后，按下压力传感器按钮来停止一切。

--- /task ---

![一张已经被绘图仪绘制了绿色轨迹的纸片的图片](images/paper.JPG)

下一步，您将使用实时数据源做为输入数据！

--- save ---
