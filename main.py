from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1 #25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_mark_number = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    canvas.itemconfig(timer_text, text="00:00")  # canvas iç
    check_label.config(text="")
    window.after_cancel(timer) #zamanlayıcıyı durdurmak için yazdık!
    timer_label.config(text="Timer")
    global reps
    reps = 0




# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, check_mark_number
    reps += 1
    # print(reps)
    work_secs = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_secs)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_secs)
        timer_label.config(text="Work", fg=GREEN)









# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count=12):
    global reps, check_mark_number
    count_min = math.floor(count / 60)
    count_sec = int(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}" # dynamic typing yapmış olduk. değişkene atanan değer ile değişkenin tipi int to string oldu.
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") # canvas için
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1) #count-1, count_down fonksyionunun bir sonraki girdisini/input ifade ediyor.
    # window.after ile ilgili fonksyion belirlenen sürede bir defa çağırılır. Fonsiyonu kendi içinde çağırarark döngü oluşturduk!
    else:
        start_timer()
        if reps % 2 == 0:
            check_mark_number += 1
            check_label.config(text="✔" * check_mark_number)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.minsize(height=400, width=400)
window.config(padx=100,pady=60, bg=YELLOW) # bg=backcolor

# def say_something(thing):
#     print(thing)
# # window.after: Call function once after given time.
# window.after(1000, say_something, "hello") # after içindeki *args ifadesi ilgili fonksyiona gönderilecek olan pararmetreleri temsil ediyor!



## Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bg_image = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=bg_image) # 100 ve 112 çoklu pozsiyonal argümanlar oluğ x ve y değerlerini temsil ediyor.
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white") # 100 ve 130 x ve y koordinatları. *args olarak sonsuz miktarda sayı girilebilir!
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = Label(fg=GREEN, bg=YELLOW)  # fg stands for foreground color
check_label.grid(row=3, column=1)







window.mainloop()










