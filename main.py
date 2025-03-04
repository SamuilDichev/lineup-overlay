import tkinter as tk
from screeninfo import get_monitors

def get_dimensions():
	for monitor in get_monitors():
	    if monitor.is_primary:
	        return monitor.width, monitor.height

width, height = get_dimensions()

root = tk.Tk()
root.attributes("-topmost", True, "-transparentcolor", "black")
root.overrideredirect(True)  # Removes window borders

canvas = tk.Canvas(root, width=width, height=height, bg="black", highlightthickness=0)
canvas.pack()
canvas.create_line(width/2, 100, width/2, height-100, fill="green", width=3)

# Fullscreen overlay
root.geometry(f"{width}x{height}+0+0")  
root.bind("<Escape>", lambda e: root.destroy())
root.mainloop()