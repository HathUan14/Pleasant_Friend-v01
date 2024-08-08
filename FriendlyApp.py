from tkinter import *
from algorithm import Backpack1, DivideIntoTwoMostBalance

root = Tk()
root.title('Pleasant Friend')
root.geometry('400x790')
root.resizable(False, False)

def updateDescriptioin():
    updateListBox()
    if option.get() == 1:
        description_label.config(text='Making decisions for your trip, by deciding on the time and value for each activity')
    elif option.get() == 2:
        description_label.config(text='Make your purchasing decision, based on price and your need')
    elif option.get() == 3:
        description_label.config(text='Divide the shares into 2 equal part among a diverse group of values')

task_list_1 = []
val_list_1 = []
wei_list_1 = []
task_list_2 = []
val_list_2= []
wei_list_2 = []
task_list_3 = []
val_list_3 = []

def updateListBox():
    listbox.delete(0, END)
    if option.get() == 1:
        right_spacer.pack_forget()
        left_spacer.pack_forget()
        header1.config(width=22, text='Action')
        button_add.pack_forget()
        header3.pack(side=LEFT, expand=True, fill=X)
        header3.config(text='Weight')
        task_entry3.pack(side=LEFT)
        button_add.pack(side=LEFT, padx=5, pady=10)
        task_entry1.config(width=24)

        button_cal.pack_forget()
        header4.pack(side=LEFT, expand=True, fill=X)
        task_entry4.pack(side=LEFT, expand=True, fill=X)
        button_cal.pack(side=LEFT, padx=15, pady=10)
        for i in range(len(task_list_1)):
            listbox.insert(END, f'{i+1}. {task_list_1[i].ljust(18, '_')}_{val_list_1[i].ljust(7,'_')}_{wei_list_1[i]}')
    elif option.get() == 2:
        right_spacer.pack_forget()
        left_spacer.pack_forget()
        header1.config(width=22, text='Item')
        button_add.pack_forget()
        header3.pack(side=LEFT, expand=True, fill=X)
        header3.config(text='Price')
        task_entry3.pack(side=LEFT)
        button_add.pack(side=LEFT, padx=5, pady=10)
        task_entry1.config(width=24)

        button_cal.pack_forget()
        header4.pack(side=LEFT, expand=True, fill=X)
        task_entry4.pack(side=LEFT, expand=True, fill=X)
        button_cal.pack(side=LEFT, padx=15, pady=10)
        for i in range(len(task_list_2)):
            listbox.insert(END, f'{i+1}. {task_list_2[i].ljust(18, '_')}_{val_list_2[i].ljust(7,'_')}_{wei_list_2[i]}')
    elif option.get() == 3:
        header3.pack_forget()
        header1.config(width=30, text='Item')
        task_entry3.pack_forget()
        task_entry1.config(width=32)

        header4.pack_forget()
        task_entry4.pack_forget()
        button_cal.pack_forget()
        right_spacer.pack_forget()
        left_spacer.pack_forget()
        right_spacer.pack(side=LEFT)
        button_cal.pack(side=LEFT, padx=15, pady=10)
        left_spacer.pack(side=LEFT)
        for i in range(len(task_list_3)):
            listbox.insert(END, f'{i+1}. {task_list_3[i].ljust(22, '_')}_{val_list_3[i]}')

def addTask():
    result_listbox.delete(0,END)
    if option.get() == 1:
        try:
            if task_entry1.get() and int(task_entry2.get()) > 0 and int(task_entry3.get()) > 0:
                task = task_entry1.get() + '\n' + task_entry2.get() + '\n' + task_entry3.get() + '\n'
                with open('data_1.txt', 'a') as file:
                    file.write(f'{task}')
                task_list_1.append(task_entry1.get())
                val_list_1.append(task_entry2.get())
                wei_list_1.append(task_entry3.get())
                task_entry1.delete(0, END)
                task_entry2.delete(0, END)
                task_entry3.delete(0, END)
            else:
                result_listbox.insert(END, '-->The task must have a name, value ')
                result_listbox.insert(END, 'and weight must be an interger > 0')
        except ValueError:
            result_listbox.insert(END, '-->The task must have a name, value ')
            result_listbox.insert(END, 'and weight must be an interger > 0')
    if option.get() == 2:
        try:
            if task_entry1.get() and int(task_entry2.get()) > 0 and int(task_entry3.get()) > 0:
                task = task_entry1.get() + '\n' + task_entry2.get() + '\n' + task_entry3.get() + '\n'
                with open('data_2.txt', 'a') as file:
                    file.write(f'{task}')
                task_list_2.append(task_entry1.get())
                val_list_2.append(task_entry2.get())
                wei_list_2.append(task_entry3.get())
                task_entry1.delete(0, END)
                task_entry2.delete(0, END)
                task_entry3.delete(0, END)
            else:
                result_listbox.insert(END, '-->The item must have a name, value ')
                result_listbox.insert(END, 'and price must be an interger > 0')
        except ValueError:
            result_listbox.insert(END, '-->The item must have a name, value ')
            result_listbox.insert(END, 'and price must be an interger > 0')
    if option.get() == 3:
        try:
            if task_entry1.get() and int(task_entry2.get()) > 0:
                task = task_entry1.get() + '\n' + task_entry2.get() + '\n'
                with open('data_3.txt', 'a') as file:
                    file.write(f'{task}')
                task_list_3.append(task_entry1.get())
                val_list_3.append(task_entry2.get())
                task_entry1.delete(0, END)
                task_entry2.delete(0, END)
            else:
                result_listbox.insert(END, '-->The item must have a name, value ')
        except ValueError:
            result_listbox.insert(END, '-->The item must have a name, value ')
    updateListBox()

def deleteTask():
    if option.get() == 1:
        for index in reversed(listbox.curselection()): #reversed is for the changed order of the list
            del(task_list_1[index])
            del(val_list_1[index])
            del(wei_list_1[index])
        l = len(task_list_1)
        with open('data_1.txt', 'w') as file:
            for i in range(l):
                file.write(f'{task_list_1[i]}\n{val_list_1[i]}\n{wei_list_1[i]}\n')
    elif option.get() == 2:
        for index in reversed(listbox.curselection()): #reversed is for the changed order of the list
            del(task_list_2[index])
            del(val_list_2[index])
            del(wei_list_2[index])
        l = len(task_list_2)
        with open('data_2.txt', 'w') as file:
            for i in range(l):
                file.write(f'{task_list_2[i]}\n{val_list_2[i]}\n{wei_list_2[i]}\n')
    elif option.get() == 3:
        for index in reversed(listbox.curselection()): #reversed is for the changed order of the list
            del(task_list_3[index])
            del(val_list_3[index])
        l = len(task_list_3)
        with open('data_3.txt', 'w') as file:
            for i in range(l):
                file.write(f'{task_list_3[i]}\n{val_list_3[i]}\n')
    updateListBox()

def openDataFile():
    # option.get() == 1:
    try:
        with open('data_1.txt', 'r') as file:
            data = file.readlines()
            l = len(data)
            for i in range(0, l, 3):
                task_list_1.append(data[i][:-1]) # Not pick the leter '\n'
                val_list_1.append(data[i+1][:-1])
                wei_list_1.append(data[i+2][:-1])
            updateListBox()
    except:
        print('Nos')
        file=open('data_1.txt', 'w')
        file.close()
    # option.get() == 2:
    try:
        with open('data_2.txt', 'r') as file:
            data = file.readlines()
            l = len(data)
            for i in range(0, l, 3):
                task_list_2.append(data[i][:-1])
                val_list_2.append(data[i+1][:-1])
                wei_list_2.append(data[i+2][:-1])
            updateListBox()
    except:
        print('Nos')
        file=open('data_2.txt', 'w')
        file.close()
    # option.get() == 3:
    try:
        with open('data_3.txt', 'r') as file:
            data = file.readlines()
            l = len(data)
            for i in range(0, l, 2):
                task_list_3.append(data[i][:-1])
                val_list_3.append(data[i+1][:-1])
            updateListBox()
    except:
        print('Nos')
        file=open('data_3.txt', 'w')
        file.close()

def calculate():
    result_listbox.delete(0, END)
    if option.get() == 1:
        try:
            W = int(task_entry4.get())
            total, res = Backpack1(list(map(int,val_list_1)), list(map(int, wei_list_1)), W) #convert into int
            total_weight = 0
            for i in res:
                total_weight += int(wei_list_1[i])
            result_listbox.insert(END, '-->Tasks highlighted')
            result_listbox.insert(END, '-->Total weight: '+ str(total_weight))
            result_listbox.insert(END, '-->Best total value: '+ str(total))
            listbox.selection_clear(0, END)
            for index in res:
                listbox.select_set(index)
        except ValueError:
            result_listbox.insert(END, 'The total weight must be an interger > 0')
    elif option.get() == 2:
        try:
            W = int(task_entry4.get())
            total, res = Backpack1(list(map(int,val_list_2)), list(map(int, wei_list_2)), W)
            total_weight = 0
            for i in res:
                total_weight += int(wei_list_2[i])
            result_listbox.insert(END, '-->Items highlighted')
            result_listbox.insert(END, '-->Total weight: '+ str(total_weight))
            result_listbox.insert(END, '-->Best total value: '+ str(total))
            listbox.selection_clear(0, END)
            for index in res:
                listbox.select_set(index)
        except ValueError:
            result_listbox.insert(END, 'The total weight must be an interger > 0')
    elif option.get() == 3:
        try:
            indexList1, indexList2 = DivideIntoTwoMostBalance(list(map(int, val_list_3)))
            sum1, sum2 = 0, 0
            for index in indexList1:
                sum1 += int(val_list_3[index])
            for index in indexList2:
                sum2 += int(val_list_3[index])
            result_listbox.insert(END, '-->A part of two part highlighted, total: ' + str(sum1+sum2))
            result_listbox.insert(END, '-->Highlighted part: '+ str(sum1))
            result_listbox.insert(END, '-->The other part: '+ str(sum2))
            for index in indexList1:
                listbox.select_set(index)
        except ValueError:
            result_listbox.insert(END, 'Please check the input')

icon = PhotoImage(file='task.png')
root.iconphoto(False, icon)
topbar_img=PhotoImage(file='topbar.png')
Label(root, image=topbar_img).pack()
friend_img = PhotoImage(file='friend.png')
Label(root, image=friend_img, bg='#32405b').place(x=15, y=10)
note_img = PhotoImage(file='task.png')
Label(root, image=note_img, bg='#32405b').place(x=340, y=25)
heading = Label(root, text='Pleasant Friend', font=('arial',20,'bold')
              , fg='white', bg='#32405b')
heading.place(x=95, y=20)

#__radio_options__

frame0 = Frame(root, width=400, height=100)
frame0.place(x=20, y=100)
option = IntVar()
option.set(1)
radio1 = Radiobutton(frame0, text='option 1', variable=option, value=1,
                     command=updateDescriptioin, indicatoron=0,
                     width=10, relief=RAISED, bg='#34a8eb')
radio2 = Radiobutton(frame0, text='option 2', variable=option, value=2,
                      command=updateDescriptioin, indicatoron=0, 
                      width=10, relief=RAISED, bg='#34a8eb')
radio3 = Radiobutton(frame0, text='option 3', variable=option, value=3,
                      command=updateDescriptioin, indicatoron=0, 
                      width=10, relief=RAISED, bg='#34a8eb')
radio1.pack(side=LEFT, padx=20, expand= True, fill=X)
radio2.pack(side=LEFT, padx=20, expand= True, fill=X)
radio3.pack(side=LEFT, padx=20, expand= True, fill=X)

frame01 = Frame(root, width=400, height=100)
frame01.place(x=50, y=140)
description_label = Label(frame01, text="Making decisions for your trip, by deciding on the time and value for each activity",
                           borderwidth=2, relief="solid", padx=10, pady=10, wraplength=250)
description_label.pack( pady=0, fill=X, padx=20)

#__entry__

header_frame = Frame(root, width=400, height=20)
header_frame.place(x=8, y=200)
header1 = Label(header_frame, text='Action', width=22,
                font=('arial',10,'bold'))
header2 = Label(header_frame, text='Value', width=8,
                font=('arial',10,'bold'))
header3 = Label(header_frame, text='Weight', width=8,
                font=('arial',10,'bold'))
header1.pack(side=LEFT, expand=True, fill=X)
header2.pack(side=LEFT, expand=True, fill=X)
header3.pack(side=LEFT, expand=True, fill=X)

frame = Frame(root, width=400, height=40, bg='white')
frame.place(x=8, y=220)

task = StringVar()
task_entry1 = Entry(frame, width=24, font='arial 10',
                   bd = 5, highlightbackground='#34a8eb', highlightcolor='#34a8eb',
                   highlightthickness=2, relief='flat')
task_entry2 = Entry(frame, width=8, font='arial 10',
                   bd = 5, highlightbackground='#34a8eb', highlightcolor='#34a8eb',
                   highlightthickness=2, relief='flat')
task_entry3 = Entry(frame, width=8, font='arial 10',
                   bd = 5, highlightbackground='#34a8eb', highlightcolor='#34a8eb',
                   highlightthickness=2, relief='flat')
task_entry1.pack(side=LEFT)
task_entry2.pack(side=LEFT)
task_entry3.pack(side=LEFT)

task_entry1.focus()

button_add = Button(frame, text='ADD', font='arial 10 bold', 
                    width=6, bg='#5a95ff', fg='#fff', bd=0,
                    command=addTask)
button_add.pack(side=LEFT, padx=5, pady=10)

#__listbox__

frame1 = Frame(root, bd=3, width=700, height=200, bg='#32405b')
frame1.place(x=7, y=270)
listbox = Listbox(frame1, font=('Courier New', 12), width=36, height=16,
                  bg='#32405b', fg='white', cursor='hand2', selectmode=MULTIPLE,
                  selectbackground='#ffa500', selectforeground='#32405b')
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scroll1 = Scrollbar(frame1)
scroll1.pack(side=RIGHT, fill = BOTH)
listbox.config(yscrollcommand=scroll1.set)
scroll1.config(command=listbox.yview)

#__action__

delete_icon=PhotoImage(file='delete.png')
Button(root, image=delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

frame2 = Frame(root, bg='white', width=340)
frame2.place(x=30, y=585)
right_spacer = Frame(frame2, width=130) #for center the button_cal
left_spacer = Frame(frame2, width=110)
header4 = Label(frame2, text='Wanted total weight', width=20,
                font=('arial',10,'bold'), bg='white')
header4.pack(side=LEFT, expand=True, fill=X)
task_entry4 = Entry(frame2, width=8, font='arial 10',
                   highlightbackground='#34a8eb', highlightcolor='#34a8eb',
                   highlightthickness=2, relief='flat')
task_entry4.pack(side=LEFT, expand=True, fill=X)
button_cal = Button(frame2, text='CALC', font='arial 10 bold', 
                    width=6, bg='#5a95ff', fg='#fff',
                    command=calculate, relief=FLAT)
button_cal.pack(side=LEFT, padx=15, pady=10)

#__result__

frame02 = Frame(root, bd=3, width=700, height=200, bg='#5a95ff')
frame02.place(x=7, y=625)
result_listbox = Listbox(frame02, font='arial 12', width=40, height=4,
                        bg='#5a95ff', fg='white', cursor='hand2',
                        selectbackground='#32405b')
result_listbox.pack(side=LEFT, fill=BOTH, padx=2)
scroll2 = Scrollbar(frame02)
scroll2.pack(side=RIGHT, fill = BOTH)
result_listbox.config(yscrollcommand=scroll2.set)
scroll2.config(command=result_listbox.yview)


openDataFile()
updateListBox()

root.mainloop()