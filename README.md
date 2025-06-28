##### PyCODE &bull; @_py.code

# Chart integration in CTk

This documentation will give a deep understanding in how to integrate charts in CustomTkinter app using `matplotlib`, python's one of the most capable library to build charts.

- [Installation](#installation)
- [UI Setup](#setup-the-ui)
- [Creating charts](#create-charts)
    - [Importing libraries](#1-import-matplotlib)
    - [Creating figure](#2-create-matplotlib-figure)
    - [Creating plots](#3-create-plots)
    - [Drawing charts](#4-draw-charts)
    - [Integration](#5-integrate-chart-in-the-app)
- [Final code](#whole-code)

## Installation
```bash
pip install customtkinter
pip install matplotlib
```

## Setup the UI

First create a black window using CTk boilerplate.

```python
# Importing Libraries
from customtkinter import *

# The root window
root = CTk()
root.title("Chart Integration")
root.geometry("600x400")

# Run the UI
root.mainloop()
```

## Create Charts
### 1. Import Matplotlib

```python
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
```

- The `Figure` will work like a paper on which we'll draw charts.

- The `FigureCanvasTkAgg` will allow us to integration the chart drawn in `Figure` in our app.

### 2. Create matplotlib figure

```python
fig = Figure(figsize=(5, 4), dpi=100)
```

- We've passed (5, 4) in the figsize attribute, this makes our chart 5 inches in width and 4 inches in height

- The dpi attribute gives the given amount of pixels per inch. Here we've given 100, that means every inch has 100 pixels.

Our chart is 5 inches in width * 100 dpi = 500 px wide, and it is 4 inches in height * 100 dpi = 400 px high.

### 3. Create plots

```python
plot = fig.add_subplot(1, 1, 1)
```

Here ;
 - The first attribute is the number of rows, means how many charts can be drawn vertically.
 - The second attribute is the number of columns, menas how many charts can be drawn horizontally.
 - The third attribute is the index of chart, means which cell will be assigned to the chart.

For example ;

- If we've to add 4 charts in our app, we'll give two rows and two columns, right? So in rows we'll pass 2 and in columns we'll pass 2 here also.

- And we'll have four chart drawers ;

```python
plot1 = fig.add_subplot(2, 2, 1)
plot2 = fig.add_subplot(2, 2, 2)
plot3 = fig.add_subplot(2, 2, 3)
plot4 = fig.add_subplot(2, 2, 4)
```

- Each chart drawer has a specific cell to be place in, `plot1` has 1st cell, `plot2` has 2nd, `plot3` has 3rd, and `plot4` has 4th, you can see the code.

### 4. Draw charts

Now you can simple draw charts using matplotib's structure, like this ;

```python
plot.bar(
    [1, 2, 3, 4],
    [20, 30, 45, 45],
    color=['#a1e5ff', '#77dd77', '#FFFEE0', '#ff8680'],
    label=['Java', 'C/C++', 'JavaScript', 'Python']
)
plot.set_xticks(list(range(1, 5)))
plot.set_xticklabels(['Java', 'C/C++', 'JavaScript', 'Python'])
# plot.grid(True)
plot.set_xlabel("Languages")
plot.set_ylabel("Rating/50")
plot.set_title("Languages and their ratings")
plot.set_facecolor("#d9f5ff")
plot.legend()
```

```python
plot2.plot([1, 2, 3, 4], [4, 3, 6, 5])
```

### 5. Integrate chart in the app

Now you're at the final level, you've to integrate the charts in the CTk app. Here's how ;

```python
# * Adding the chart in the window
chart = FigureCanvasTkAgg(fig, root)
chart.get_tk_widget().pack(fill='both', expand=True)
chart.draw()
```

Here ;
- `FigureCanvasTkAgg` creates the chart in the root window.
    - The first attribute is the `Figure` object where we've created our charts.
    - The second attribute is the `root` window where our chart as a widget will be placed.

- The `get_tk_widget()` methods returns a Tkinter widget that we'll pack using the `pack()` method.

- The `draw` method draws all the charts on the Tk chart widget. You've to call it after packing/griding the chart widget.


## Whole code

```python
# Importing Libraries
import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# The root window
root = ctk.CTk()
root.title("Chart integration")
root.geometry("600x400")

# Creating matplotlib figure
fig = Figure(figsize=(5, 4), dpi=100)
plot = fig.add_subplot(2, 1, 1)
plot2 = fig.add_subplot(2, 1, 2)

# Adding some data to chart
plot.bar(
    [1, 2, 3, 4],
    [20, 30, 45, 45],
    color=['#a1e5ff', '#77dd77', '#FFFEE0', '#ff8680'],
    label=['Java', 'C/C++', 'JavaScript', 'Python']
)
plot.set_xticks(list(range(1, 5)))
plot.set_xticklabels(['Java', 'C/C++', 'JavaScript', 'Python'])
# plot.grid(True)
plot.set_xlabel("Languages")
plot.set_ylabel("Rating/50")
plot.set_title("Languages and their ratings")
plot.set_facecolor("#d9f5ff")
plot.legend()

plot2.plot([1, 2, 3, 4], [4, 3, 6, 5])

# Adding the chart in the window
chart = FigureCanvasTkAgg(fig, root)
chart.get_tk_widget().pack(fill='both', expand=True)
chart.draw()

# Run the UI
root.mainloop()
```

---

#### PyCODE &bull; 2025 &bull; PyCTK