
from tkinter import *

root = Tk()
root.title('Simple Calculator')

e = Entry(root, width = 35, borderwidth = 5) #entry widget
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady=10) #this extry fill will span for 3 buttons


# e.insert(0, 'Enter your name:

def button_click(number):
    # e.delete(0, END)
    current = e.get()#current number
    e.delete(0, END)
    e.insert(0, str(current) + str(number))#current number add new number

#define clear button
def button_clear():
    e.delete(0, END)

#Define add button function
def button_add():
    first_num = e.get() #first number user enter will be save here
    global f_num  #first number
    global math
    math = 'addition'
    f_num = int(first_num) #make sure f_num is a integer
    e.delete(0, END)


#define equal button function
def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == 'addition':
        e.insert(0, f_num + int(second_number)) #add the first num to second num
    elif math == 'subtraction':
        e.insert(0, f_num - int(second_number))

    elif math =='multiplication':
        e.insert(0, f_num * int(second_number))

    elif math =='division':
        e.insert(0, f_num / int(second_number))


#define subtract, multiply and divide functions
def button_subtract():
    first_num = e.get()  # first number user enter will be save here
    global f_num  # first number
    global math
    math = 'subtraction'
    f_num = int(first_num)  # make sure f_num is a integer
    e.delete(0, END)

def button_multiply():
    first_num = e.get()  # first number user enter will be save here
    global f_num  # first number
    global math
    math = 'multiplication'
    f_num = int(first_num)  # make sure f_num is a integer
    e.delete(0, END)

def button_divide():
    first_num = e.get()  # first number user enter will be save here
    global f_num  # first number
    global math
    math = 'division'
    f_num = int(first_num)  # make sure f_num is a integer
    e.delete(0, END)

#define buttons 0-9
button_1 = Button(root, text = '1', padx = 40, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = '2', padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = '3', padx = 40, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text = '4', padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = '5', padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = '6', padx = 40, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text = '7', padx = 40, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = '8', padx = 40, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = '9', padx = 40, pady = 20, command = lambda: button_click(9))
button_0 = Button(root, text = '0', padx = 40, pady = 20, command = lambda: button_click(0))

#put the buttons on the screen
button_1.grid(row =3 , column = 0 )
button_2.grid(row = 3, column =  1)
button_3.grid(row = 3, column =  2)

button_4.grid(row = 2, column = 0 )
button_5.grid(row = 2, column =  1)
button_6.grid(row = 2, column =  2)

button_7.grid(row =1 , column =0  )
button_8.grid(row =1 , column =1 )
button_9.grid(row =1 , column = 2)

button_0.grid(row =4 , column =0  )

#add, clear and equal buttons define
button_add = Button(root, text = '+', padx = 39, pady = 20, command = button_add)
button_equal = Button(root, text = '=', padx = 89, pady = 20, command = button_equal)
button_clear = Button(root, text = 'Clear', padx = 80, pady = 20, command = button_clear)

#position of the three buttons
button_clear.grid(row =4 , column =1, columnspan = 2 )
button_add.grid(row =5 , column =0 )
button_equal.grid(row =5 , column =1, columnspan = 2 )

#Subtract, multiply, divide buttons define
button_subtract = Button(root, text = '-', padx = 41, pady = 20, command = button_subtract)
button_multiply = Button(root, text = 'X', padx = 42, pady = 20, command = button_multiply)
button_divide = Button(root, text = '/', padx = 41, pady = 20, command = button_divide)

#position of the above buttons
button_subtract.grid(row = 6, column = 0)
button_multiply.grid(row = 6, column = 1)
button_divide.grid(row = 6, column = 2)

root.mainloop()