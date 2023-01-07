from tkinter import *


calc_open_window = Tk()
calc_open_window.title('Калькулятор')
calc_open_window.resizable(0,0)
calc_open_window.geometry('240x270+100+200')
calc_open_window['bg'] = '#282828'

calc_variable = Entry(calc_open_window)
calc_variable.grid(row=0, column=0, columnspan=3, stick='we', padx=5)

def add_operation_to_string(operation):
    new_calc_value = calc_variable.get()
    if new_calc_value[-1] in '-+/*':
        new_calc_value = new_calc_value[:-1]
    
    calc_variable.delete(0, END)
    calc_variable.insert(0, new_calc_value + operation)


def add_number_to_string(digit):
    new_calc_value = calc_variable.get() + str(digit)
    calc_variable.delete(0, END)
    calc_variable.insert(0, new_calc_value)

def equality():
    value = calc_variable.get()
    calc_variable.delete(0, END)
    calc_variable.insert(0, eval(value))



calc_variable = Entry(calc_open_window, justify=RIGHT, font=('Arial 15'), width=15)
calc_variable.grid(row=0, column=0, columnspan=3, stick='we')

number_1 = Button(text='1', bd=3, font=('Arial 13 bold'), command=lambda : add_number_to_string(1), bg='Chocolate', fg='white')
number_1.grid(row=3, column=0, stick='wens', padx=1, pady=1)

number_2 = Button(text='2', bd=3, font=('Arial 13 bold'), command=lambda : add_number_to_string(2), bg = 'Chocolate', fg='white')
number_2.grid(row=3, column=1, stick='wens', padx=1, pady=1)

number_3 = Button(text='3', bd=3, font=('Arial 13 bold'), command=lambda : add_number_to_string(3), bg = 'Chocolate', fg='white')
number_3.grid(row=3, column=2, stick='wens', padx=1, pady=1)

number_4 = Button(text='4', bd=3, font=('Arial 13 bold'), command=lambda : add_number_to_string(4), bg = 'Chocolate', fg='white')
number_4.grid(row=2, column=0, stick='wens', padx=1, pady=1)

number_5 = Button(text='5', bd=3, font=('Arial 13 bold'), command=lambda : add_number_to_string(5), bg = 'Chocolate', fg='white')
number_5.grid(row=2, column=1, stick='wens', padx=1, pady=1)

number_6 = Button(text='6', bd=3, font=('Arial 13 bold'), command=lambda : add_number_to_string(6), bg = 'Chocolate', fg='white')
number_6.grid(row=2, column=2, stick='wens', padx=1, pady=1)

number_7 = Button(text='7', bd=3, font=('Arial 13 bold'), command=lambda : add_number_to_string(7), bg = 'Chocolate', fg='white')
number_7.grid(row=1, column=0, stick='wens', padx=1, pady=1)

number_8 = Button(text='8', bd=3, font=('Arial 13 bold'), command=lambda : add_number_to_string(8), bg = 'Chocolate', fg='white')
number_8.grid(row=1, column=1, stick='wens', padx=1, pady=1)

number_9 = Button(text='9', bd=3, font=('Arial 13 bold'), command=lambda : add_number_to_string(9), bg = 'Chocolate', fg='white')
number_9.grid(row=1, column=2, stick='wens', padx=1, pady=1)

number_0 = Button(text='0', bd=3, font=('Arial 13 bold'), command=lambda : add_number_to_string(0), bg = 'Chocolate', fg='white')
number_0.grid(row=4, column=0, stick='wens', padx=1, pady=1)



operation_addition = Button(text='+', bd=3, font=('Arial 13 bold'), fg = 'white', bg='Chocolate', command=lambda : add_operation_to_string('+'))
operation_addition.grid(row=1, column=3, stick='wens', padx=1, pady=1)
operation_subtraction =  Button(text='-', bd=3,  font=('Arial 13 bold'), fg = 'white', bg='Chocolate', command=lambda : add_operation_to_string('-'))
operation_subtraction.grid(row=2, column=3, stick='wens', padx=1, pady=1)
operation_multiplication =  Button(text='*', bd=3,  font=('Arial 13 bold'), fg = 'white', bg='Chocolate', command=lambda : add_operation_to_string('*'))
operation_multiplication.grid(row=3, column=3, stick='wens', padx=1, pady=1)
operation_division  =  Button(text='/', bd=3,  font=('Arial 13 bold'), fg = 'white', bg='Chocolate', command=lambda : add_operation_to_string('/'))
operation_division.grid(row=4, column=3, stick='wens', padx=1, pady=1)

button_equality = Button(text='=', bd=3, font=('Arial 13 bold'), bg= 'Tomato', fg='White', command=lambda : equality())
button_equality.grid(row=4, column=1, columnspan=2, stick='wens', padx=1, pady=1)



calc_open_window.grid_columnconfigure(0, minsize=60)
calc_open_window.grid_columnconfigure(1, minsize=60)
calc_open_window.grid_columnconfigure(2, minsize=60)
calc_open_window.grid_columnconfigure(3, minsize=60)

calc_open_window.grid_rowconfigure(1, minsize=60)
calc_open_window.grid_rowconfigure(2, minsize=60)
calc_open_window.grid_rowconfigure(3, minsize=60)
calc_open_window.grid_rowconfigure(4, minsize=60)




calc_open_window.mainloop()
