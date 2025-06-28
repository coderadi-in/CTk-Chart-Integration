'''coderadi'''

# ? Importing Libraries
import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ! The root window
root = ctk.CTk()
root.title("Chart integration")
root.geometry("600x400")

# * Create a Figure object
fig = Figure(figsize=(5, 4), dpi=100)
plot1 = fig.add_subplot(1, 1, 1)

# * Chart integration
chart = FigureCanvasTkAgg(fig, root)
chart.get_tk_widget().pack()
chart.draw()

# ! Run the UI
root.mainloop()
