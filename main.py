
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1

# ---------------------------- TIMER RESET ----- -------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(zero_timer, text="00:00")
    header.config(text="TIMER")
    tik_mark.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def go():
    return count_down(25 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        header.config(text="Break Time", font=(FONT_NAME, 35, "bold"), fg=PINK, bg=GREEN)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        header.config(text="Break Time", font=(FONT_NAME, 35, "bold"), fg=YELLOW, bg=GREEN)

    else:
        count_down(work_sec)
        header.config(text="Break Time", font=(FONT_NAME, 35, "bold"), fg=RED, bg=GREEN)


def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(zero_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        for _ in range(math.floor(reps / 2)):
            tik_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomato Timer")
window.config(padx=90, pady=100, bg="#9bdeac")

mark = "✓"
fg = RED
canvas = Canvas(width=220, height=220, bg="#9bdeac", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
img = canvas.create_image(115, 100, image=tomato_img)
zero_timer = canvas.create_text(115, 120, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=3, row=2)


header = Label(text="TIMER", font=(FONT_NAME, 35, "bold"), fg=RED, bg=GREEN)

header.grid(column=3, row=1)

start_button = Button(text="Start", highlightthickness=0, command=go)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=4, row=3)

tik_mark = Label(bg="#9bdeac", fg=RED)
tik_mark.grid(column=3, row=3)

window.mainloop()