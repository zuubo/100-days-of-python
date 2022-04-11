import tkinter as tk
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
checks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps, checks
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="0:00")
    reps = 0
    checks = ""
    checkmarks.config(text=checks)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if reps % 2 != 0 and reps < 7:
        reps += 1
        print(reps, "short break")
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_secs)
    elif reps == 7:
        count_down(long_break_secs)
        reps = 0
        title_label.config(text="Break", fg=RED)
        print(reps, "long break")
    else:
        reps += 1
        count_down(work_secs)
        title_label.config(text="Work", fg=GREEN)
        print(reps, "work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    global checks
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checks += "✔"
            checkmarks.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Tomate")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=2, row=1)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="0:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

checkmarks = tk.Label(fg=GREEN, bg=YELLOW, font=('arial', 18, 'normal'))
checkmarks.grid(column=2, row=4)

window.mainloop()
