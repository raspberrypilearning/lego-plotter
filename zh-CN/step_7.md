## 添加实时数据源

您可以将多种传感器添加到您的 Raspberry Pi 中，为您的绘图仪提供数据。

让我们从一个内置数据源开始：Raspberry Pi 的 CPU 的温度。 如果您还没有安装 `vcgencmd` 库，请现在安装。

--- collapse ---
---
title：安装 Vcgencmd Python 库
---

确保您已连接到互联网。

按下<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>，在 Raspberry Pi 上打开一个终端窗口。

在提示符后键入： `sudo pip3 install vcgencmd` 并按 <kbd>回车</kbd>。

等收到确认消息（不会花费很长时间）后，关闭终端窗口。

--- /collapse --- 

--- task ---

在 Thonny 中使用 **Shell/REPL** ，输入以下 Python 行来测试和读取 CPU 温度。

```python
>>> from vcgencmd import Vcgencmd
```
按 <kbd>回车</kbd>。

输入：
```python
>>> vcgm = Vcgencmd()
```
按 <kbd>回车</kbd>。

输入：
```python
vcgm.measure_temp()
```
按 <kbd>回车</kbd>。

你应该看到 **Shell窗口** 返回了一个数值（应该在 50 左右）——这就是你的 CPU 运行的温度。

--- /task ---

现在我们通过让 CPU 做一些工作来提高温度！

--- task ---

打开网络浏览器并观看 YouTube 视频。 几秒钟后，回到 Thonny 并重新运行最后一行的Python命令，您应该会看到温度升高了。

--- /task ---

现在您知道如何使用 Python 读取 CPU 的温度，您可以修改您的 `plotter.py` 程序，让它用CPU温度作为数据源。

--- task ---

首先，在文件顶部的现有导入行下方，添加用于导入 Vcgencmd 库的行：

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
创建一个vcgencmd对象

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

更改程序，改为使用CPU实时温度而不是随机生成的数字。 为此，您需要将 `randint(-180, 180)` 替换为 `vcgm.measure_temp()`。

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

在将 Raspberry Pi CPU 的温度用作绘图仪的数据源之前，您需要确保数据源产生的最大可能范围在经过数学转换后，匹配到 -180 到 180 之间的范围.

`vcgencmd` 产生的温度值范围应该是从 50°C 左右（当Raspberry Pi启动，但运行程序不多）到低于 90°C 时（在 85°C时，Raspberry Pi会限制其性能以保持温度低于此值）。 假设您要绘制从 40°C 到 90°C 的范围——您需要将其映射到您的可用值：-180 到 180之间。

您可以创建一个函数来将一个范围的值重新映射到另一个范围。

--- task ---

将此函数添加到`while` 循环前。 它需要知道一个温度范围和一个角度范围，就可以将一个温度映射到一个角度。

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

现在，在 `while` 循环中，您可以使用此函数计算马达需要转向的新角度。

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

现在可以运行您的程序了。 像上次一样让 Raspberry Pi 的CPU 变热，您就会看到画笔逐渐滴向上移动。 如果您的画笔移动量不大，请尝试更改 `min_temp` 和 `max_temp`参数

![上下移动的画笔在绘图仪送出的纸张上绘制出一条波动的线的动图。](images/plotter_demo_2.gif)


--- save ---
