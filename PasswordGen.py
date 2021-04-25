
# Tkinter is a standard GUI library and is one of the easiest ways to build a GUI application.
# pyperclip module allows us to copy and paste text to and from the clipboard to your computer
# The random module can generate random numbers
# string module contains a number of functions to process the standard python string.


from tkinter import *
import  random, string
import pyperclip

#create display

disp = Tk()
disp.geometry('400x400')
disp.resizable(0,0)
disp.config(bg = 'seashell2')
disp.title('Password Generator')

Label(disp, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()
Label(disp, text ='modified by borat', font ='arial 10 bold').pack(side = BOTTOM)


#set password length
pass_label = Label(disp, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(disp, from_ = 8, to_ = 16 , textvariable = pass_len , width = 15).pack()
#pass_len is an integer type variable that stores the length of a password.
# To select the password length we use Spinbox() widget.
# Spinbox() widget is used to select from a fixed number of values. Here the value from 8 to 32


#generate password
pass_str = StringVar()
def Generator():
    password = ''
    for x in range(0,4):
        password= random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)

    #First loop will generate a string of length 4 which is a combination of an uppercase letter, a lowercase letter, digits, and a special symbol and that string will store in password variable.
    #The second loop will generate a random string of length entered by the user – 4 and add to the password variable.Here we minus 4 to the length of the user because we already generate the string of length 4.

    pass_str.set(password)

Button(disp, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)
Entry(disp , textvariable = pass_str).pack()

def Copy_password():
    pyperclip.copy(pass_str.get())
Button(disp, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)
disp.mainloop()
