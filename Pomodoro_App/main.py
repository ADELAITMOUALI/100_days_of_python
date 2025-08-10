import tkinter as tk 
import math
from tkinter import messagebox


#----------------CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#88C273"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
marks = "🗹"
reps = 0 
Time_in_screen = None
count_min = 0 
count_sec = 0

#----------------TIMER RESET
def Reset_time():
    global reps
    global count_min
    global count_sec
    window.after_cancel(Time_in_screen)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.configure(text="Timer")
    check_mark.configure(text="")
    reps = 0 

#----------------TIMER MECHANISM
def count_down(num):
    global marks
    global Time_in_screen
    count_min = math.floor(num / 60)
    count_sec = num % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if num > 0 :
        Time_in_screen = window.after(1000, count_down, num - 1)
    else:
        timer()
        if reps % 2 == 0 :
            check_mark.config(text = marks)
            marks += "🗹"
  
#----------------COUNTDOWN MECHANISM
def timer():
    global reps
    reps += 1
    WORK_sec = WORK_MIN * 60
    SHORT_BREAK_sec = SHORT_BREAK_MIN *60
    LONG_BREAK_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        timer_label.configure(text="Long Break",font=(FONT_NAME, 50, "bold"),bg=YELLOW ,fg=RED)
        count_down(LONG_BREAK_sec)
        messagebox.showinfo("Break Time!", "Enjoy your long break!")  # Pop-up notification

  
        
    elif reps % 2 == 0 :
        timer_label.configure(text="Short Break",font=(FONT_NAME, 50, "bold"),bg=YELLOW ,fg=PINK)
        count_down(SHORT_BREAK_sec)
        messagebox.showinfo("Break Time!", "Enjoy your long break!")  # Pop-up notification

    
    else:
        timer_label.configure(text="WORK",font=(FONT_NAME, 55, "bold"),bg=YELLOW ,fg=GREEN)
        count_down(WORK_sec)
            
#----------------UI SETUP

window = tk.Tk()
window.config(padx=50, pady=50, bg=YELLOW)
window.title("Pomodoro Timer")
my_image = tk.PhotoImage(file="tomato.png")
canvas = tk.Canvas(width=448,height=462, bg=YELLOW, highlightthickness=0)
canvas.create_image(223,231, image = my_image)
timer_text = canvas.create_text(223,350,text="00:00",fill="white", font=(FONT_NAME, 65))
canvas.grid(column=1,row=1)

#----------------label Timer
timer_label = tk.Label(text="Timer",font=(FONT_NAME, 55, "bold"),bg=YELLOW ,fg=GREEN)
timer_label.grid(column=1,row=0) 

#----------------button start and reset
start_button = tk.Button(text="Start",bg="white", command=timer)
start_button.grid(column=0,row=2)


reset_button = tk.Button(text="Reset",bg="white", command=Reset_time)
reset_button.grid(column=2,row=2)
#----------------check mart
check_mark = tk.Label(font=(FONT_NAME,20,"bold"),fg=GREEN,bg=YELLOW)
check_mark.grid(column=1, row=3)
     


window.mainloop()