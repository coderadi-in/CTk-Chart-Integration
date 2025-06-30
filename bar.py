'''coderadi'''

# ? Importing Libraries
import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# ! The root window
root = ctk.CTk()
root.title("Chart integration")
root.geometry("1000x600")

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
plot1 = fig.add_subplot(1, 1, 1)

plot1.bar(set3, set1, color=set4, label=set3)
plot1.set_facecolor("#1A1A1D")
plot1.set_title("Languages", color="#F3F4F6")
plot1.set_xlabel("X-Axis", color="#F3F4F6")
plot1.set_ylabel("Y-Axis", color="#F3F4F6")
plot1.grid(color='gray')
plot1.set_axisbelow(True)

# * Chart integratio
chart = FigureCanvasTkAgg(fig, root)
chart.get_tk_widget().pack(expand=True, fill='both')
chart.draw()

# ! Run the UI
root.mainloop()