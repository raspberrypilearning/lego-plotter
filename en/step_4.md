## Adding a data source

There are are a huge variety of sensors you could add to your Raspberry Pi to provide a data feed for your plotter.

Let's start with an inbuilt data source: the temperature of the CPU on the Raspberry Pi itself. If you haven't installed the `vcgencmd` library, you should do that now. 

--- task ---

Using the Shell/REPL in Thonny, enter the following lines of Python to test reading the CPU temperature.

```python
>>> from vcgencmd import Vcgencmd
>>> vcgm = Vcgencmd()
>>> vcgm.measure_temp()
```

54.0

--- /task ---

--- task ---
Now let's warm things up by getting the CPU to do some work.  You could try opening the Chromium web browser and wathcing a YouTube movie. After a few seconds re-run the last line of Python and you should see that the temperature has increased. 

--- /task ---

Before you can use the temperature of the Raspberry Pi's CPU as a data source for you plotter, you need to map the range of possible temperatures onto the range of motion of the plotter. 
--- save ---