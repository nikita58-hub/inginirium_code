import tkinter as tk

def move_by_keys(event):
    info_coords = canvas.coords(lines)
    x = info_coords[0]
    y = info_coords[1]
    label.config(text=str(x) + "                     " + str(y))
    if event.keysym == "w":
        canvas.move(lines, 0, -20)
    elif event.keysym == "s":
        canvas.move(lines, 0, 20)
    elif event.keysym == "a":
        canvas.move(lines, -20, 0)
    elif event.keysym == "d":
        canvas.move(lines, 20, 0)


win = tk.Tk()
label = tk.Label(win, text="Celestial Recode")
label.pack()
canvas = tk.Canvas(win, bg="#fff", width=400, height=400)
canvas.create_line((50,0), (50, 400), fill="black")
canvas.create_line((100,0), (100, 400), fill="black")
canvas.create_line((150,0), (150, 400), fill="black")
canvas.create_line((200,0), (200, 400), fill="black")
canvas.create_line((250,0), (250, 400), fill="black")
canvas.create_line((300,0), (300, 400), fill="black")
canvas.create_line((350,0), (350, 400), fill="black")
canvas.create_line((50,0), (50, 50), fill="black")
canvas.create_line((100,0), (100, 50), fill="black")
canvas.create_line((150,0), (150, 50), fill="black")
canvas.create_line((200,0), (200, 50), fill="black")
canvas.create_line((250,0), (250, 50), fill="black")
canvas.create_line((300,0), (300, 50), fill="black")
canvas.create_line((350,0), (350, 50), fill="black")
canvas.pack()
win.bind("<KeyPress>", move_by_keys)
win.mainloop()