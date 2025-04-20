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


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    if timer is not None:
        window.after_cancel(timer)
    title_lable.config(text= "Timer",fg="RED")
    global reps
    reps = 0
    check_marks.config(text = "")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps%2==0:
        title_lable.config(text= "Break",fg="RED")
        count_down(short_break_sec)
    elif reps%8==0:
        title_lable.config(text="Break", fg="RED")
        count_down(long_break_sec)
    else:
        title_lable.config(text="Work", fg="Green")
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = (count%60)
    if count_sec <10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔️"
        check_marks.config(text= marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100,pady=50,bg= PINK)
window.title("Pomodoro")


title_lable =Label(text="Timer",fg=GREEN,bg=PINK,font=(FONT_NAME,50))
title_lable.grid(column=1,row = 0)


canvas = Canvas(width = 205, height=224,bg= PINK,highlightthickness=0)
photo = PhotoImage(file = "tomato.png")
canvas.create_image(103,112,image =photo,)
timer_text= canvas.create_text(103,130,text=f"00:00",fill= "white",font =(FONT_NAME,35,"bold"))
canvas.grid(column=1,row = 1)

start_button =Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)


reset_button = Button(text= "Reset",highlightthickness=0, command=reset_timer)
reset_button.grid(column=2,row=2)

check_marks = Label(fg=GREEN,bg=PINK)
check_marks.grid(column=1,row =3)

window.mainloop()