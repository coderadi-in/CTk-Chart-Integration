'''coderadi'''

# ? Importing Libraries
import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# ! The root window
root = ctk.CTk(fg_color="#1A1A1D")
root.title("Chart integration")
root.geometry("600x400")

# * Dummy Dataset
set1 = [random.randint(1, 10) for _ in range(10)]
set2 = list(range(1, 11))
set3 = [
    'Python', 'JavaScript', 'C/C++', 'Java', 'Swift',
    'C#', 'Go', 'Ruby', 'Dart', 'Kotlin'
]
set4 = []
for _ in range(10):
    hex = '#'
    for _ in range(6):
        hex += random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F'])
    set4.append(hex)

# * Create a Figure object
fig = Figure(figsize=(5, 4), dpi=100, facecolor="#1A1A1D")
plot = fig.add_subplot(1, 1, 1)

plot.plot(set2, [
    random.randint(1, 10) for _ in range(10)
], color="#4C8EFF", label="Sales of X")

plot.plot(set2, [
    random.randint(1, 10) for _ in range(10)
], color="#77DD77", label="Sales of X")
plot.legend()
plot.set_facecolor("#1A1A1D")
plot.grid(True)

# * Chart integratio
chart = FigureCanvasTkAgg(fig, root)
chart.get_tk_widget().pack()
chart.draw()

# ! Run the UI
root.mainloop()