import tkinter as tk
"""
Create a canvas with two shapes and bind events to movements
"""


root = tk.Tk()
root.geometry('800x600')
root.title('Canvas Demo - Oval')

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)
canvas.focus_set()


points = (
    (50, 150),
    (200, 300),
)
shape = canvas.create_oval(*points, fill='purple')
def upcircle(event):
    x=0
    y=-1
    canvas.move(shape,x,y)
def downcircle(event):
    x=0
    y=1
    canvas.move(shape,x,y)



canvas.bind("<Up>", upcircle)
canvas.bind("<Down>", downcircle)



root.mainloop()