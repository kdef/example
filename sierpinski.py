import math
import Tkinter as tk

def drawTriangle(canvas, x, y, width, height):
    # draw a triangle within a bounding rectangle

    coords = [x + width / 2, y,       # top
              x + width, y + height,  # bottom right
              x, y + height]          # bottom left
    canvas.create_polygon(coords, outline='green', width=1)

def drawFractal(canvas, x, y, width, height):
    # draw a triangle fractal within a bounding rectangle

    drawTriangle(canvas, x, y, width, height)
    
    # base case
    if width < 8 or height < 8:
        return

    w = width / 2
    h = height / 2
    drawFractal(canvas, x + w / 2, y, w, h)
    drawFractal(canvas, x, y + h, w, h)
    drawFractal(canvas, x + w, y + h, w, h)

window = tk.Tk()
window.title('Sierpinski Triangle')
win_h = math.sqrt(3) / 2 * 600
win_w = 600

can = tk.Canvas(window, width=win_w, height=win_h, bg='black')
drawFractal(can, 10, 10, win_w, win_h)
can.pack(ipadx=10, ipady=10, expand=1)

tk.Button(window, text="Close", command=window.quit).pack()

window.mainloop()
