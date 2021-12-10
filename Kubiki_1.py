#БИБЛИОТЕКИ
from tkinter import *
from tkinter import messagebox
import random


#КОД ПРОГРАММЫ
def brosok():
    output_field.delete(1.0, END)
    itog = ''
    summ = 0
    grani = int(grani_field.get())
    cubes = int(cubes_field.get())
    
    if grani%2 == 0:
        for i in range(1,cubes+1):
            func = random.randint(1,grani)
            itog = itog+str(i)+'-й кубик: '+str(func)+'\n'
            summ = summ+func
        output_field.insert(1.0, itog+'Сумма: '+str(summ))
    else:
        messagebox.showerror('Ошибка', 'Кол-во граней должно быть чётным!')

def helpp(): #СПРАВКА
    messagebox.showinfo('Справка', 'Введите чётное кол-во граней для корректной работы, далее кол-во кубиков. Чётность/нечетность кубиков на работу программы не влияют! ')
    
    
    

#ИНТЕРФЕЙС
win = Tk()
win.title("Кубики")
win.configure(background = '#CACACA')   
win.geometry("385x230")
win.resizable(height = 0, width = 0)

label = Label(win, text = 'Введите кол-во граней (не менее 2х) → ',bg = "#66A3D2")
label.grid(row = 0, column = 0, padx = 5)

grani_field = Entry(win, font = "lucida 10")
grani_field.grid(row = 0, column = 1, pady = 8)

label2 = Label(win, text = 'Введите кол-во кубиков → ',bg = "#66A3D2")
label2.grid(row = 1, column = 0, padx = 5)

cubes_field = Entry(win, font = "lucida 10")
cubes_field.grid(row = 1, column = 1, pady = 8)

label3 = Label(win, text = 'Вывод ↓ ',bg = "#66A3D2")
label3.grid(row = 2, column = 0, padx = 5)

output_field = Text(win, height = 5, width = 25, font = "lucida 10",)
output_field.grid(row = 3, column = 0, padx = 10)

button = Button(win,text = "Ввод",bg = "#66A3D2",command = brosok)
button.grid(row = 2, column = 1, pady = 8)

button_q = Button(win,text = "Справка",bg = "light blue",command = helpp)
button_q.grid(row = 4, column = 1, sticky = E)

win.mainloop()