from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(canvas_timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    # If it's the 1st/3rd/5th/7th rep:
    if reps % 2 == 1:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    # If it's the 8th rep:
    elif reps == 8:
        timer_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    # If it's the 2nd/4th/6th rep:
    else:
        timer_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(canvas_timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_text = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            check_text += "✔"
            check_mark.config(text=check_text)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomadoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_img)
canvas_timer_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Labels
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 11))
check_mark.grid(column=1, row=3)
# Buttons
start_b = Button(text="Start", command=start_timer, highlightthickness=0)
start_b.grid(column=0, row=2)

reset_b = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_b.grid(column=2, row=2)

window.mainloop()
