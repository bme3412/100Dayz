from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Money Never Sleeps')
window.config(padx=100, pady=50)

# use canvas and add image
canvas = Canvas(width=526, height=316)
file_path = "stocks.png"
image = PhotoImage(file=file_path)


canvas.create_image(258, 158, image=image)
canvas.pack()


window.mainloop()
