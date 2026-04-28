import tkinter as tk

root = tk.Tk()

root.title("GUI")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#root.attributes('-fullscreen', True)
root.geometry("%dx%d" % (screen_width, screen_height))

label = tk.Label(root, text = "Fullscreen Test")
label.place(x = screen_height / 5, y = 10)

button = tk.Button(root, text = "Start Game", command = lambda: label.config(text="Game started"))
button.place(x = screen_width / 2, y = screen_height / 2)


root.mainloop()