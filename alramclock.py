



from tkinter import  *
import  datetime
import time
import winsound






# #create a function for alarm
def set_alarm(set_alarm_timer):
    while True: #makes program automatically work
        time.sleep(1) #halts the execution of the further commands given until we get the time value from the user later in the code and returns the background thread of the clock time going on at a regular interval.
        curr_time = datetime.datetime.now() #library.class.m ????
        curr_time_atm = curr_time.strftime("%H:%M:%S")
        curr_date = curr_time.strftime("%d/%m/%y")
        print("Date set to ",curr_date)
        print(curr_time_atm)
        if curr_time == set_alarm_timer:
            print("wakey wakey")
            winsound.PlaySound("sounds.wav",winsound.SND_ASYNC)
            #isse sound wave freeze during time of alaram
            break


# #create a function for actual time
def pc_actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    #call dunction alram
    set_alarm(set_alarm_timer)



dispclock = Tk()
dispclock.title("Python Alarm Clock with Sound")
dispclock.geometry("450x200")
dispclock.config(bg="PeachPuff")
format_sequence_time=Label(dispclock, text= "Time format should be in 24 hours", fg="red", bg= "PeachPuff", font="Arial").place(x=100,y=120)
addTime = Label(dispclock,text = "Hour  Min   Sec",font=1000, bg= "PeachPuff").place(x = 152)
setAlarm = Label(dispclock,text = "When to wake you up",fg="blue",font=("Helevetica",7,"bold"), bg= "PeachPuff").place(x=20, y=29)

#stringvar is used for initializing  the h/m/s
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hour_gui= Entry(dispclock,textvariable = hour,bg = "pink",width = 15).place(x=140,y=30)
min_gui= Entry(dispclock,textvariable = min,bg = "pink",width = 15).place(x=190,y=30)
sec_gui = Entry(dispclock,textvariable = sec,bg = "pink",width = 15).place(x=250,y=30)

#To take the time input by user:
set_alram_gui = Button(dispclock,text = "Set Alarm",fg="red",width = 14,command = pc_actual_time).place(x =140,y=70)

dispclock.mainloop()

