from tkinter import *

#-----------------window
window = Tk()
window.geometry("420x420")
window.title("My first GUI Python")

icon = PhotoImage(file='buttonToRight.png')
window.iconphoto(True, icon)
window.config(background='#d0eb06')

#-----------------labels
photo1 = PhotoImage(file='friend.png')
label = Label(window, text='Pleasant Friend',
              font=('Arial',30,'bold'),
              fg='#34a8eb',bg='#d0eb06',
              #relief=RAISED,bd=10,padx=20,pady=10,
              image=photo1,compound='bottom')
label.pack()
#label.place(x=0, y=0)

#-----------------buttons
count = 0
def click():
    global count
    count = count + 1
    print(f'quit {count}')
button1_photo = PhotoImage(file='upsideArrow.png')
button1 = Button(window, text='Quit!', command=click,
                font=('Comic Sans',10),
                fg='#0e29b0',bg='white',
                activeforeground='white',activebackground='black',
                state=ACTIVE, image=button1_photo,
                compound='left')
button1.pack()

#-----------------checkbox
x1 = IntVar()
def display():
    if x1.get() == 1:
        window.config(background='white')
    else:
        window.config(background='#d0eb06')
check_button1 = Checkbutton(window, text='light',
                            variable=x1, onvalue=1, offvalue=0,
                            command=display, padx=10, pady=10)
check_button1.pack()

#-----------------radiobutton
foods = ['pizza', 'hamberger', 'hotdog']
x2 = IntVar()
def order():
    print('You ordered', foods[x2.get()])
for i in range(len(foods)):
    rbutton = Radiobutton(window, text=foods[i], variable=x2, value=i,
                          padx=10, pady=10, font=('impact', 10),
                          #indicatoron=0,
                          command=order)
    rbutton.pack(anchor=W) 

#-----------------entry
def submit():
    name = entry.get()
    print('Hello '+ name)
def backspace():
    entry.delete(len(entry.get()) - 1,END)
#entry.insert(0,'Press here') #entry.config(state=DISABLED) #entry.config(show='*')
entry = Entry(window, font = ('Arial', 10),
              bg='#34a8eb',fg='#0e29b0',
              width=40)

entry.pack(side=LEFT)
submit_button = Button(window, text='submit', command=submit,
                       font=('Comic Sans',10),
                       fg='#0e29b0',bg='white',
                       activeforeground='white',activebackground='black',
                       state=ACTIVE)
backspace_button = Button(window, text='backspace', command=backspace,
                       font=('Comic Sans',10),
                       fg='#0e29b0',bg='white',
                       activeforeground='white',activebackground='black',
                       state=ACTIVE)
submit_button.pack(side=RIGHT)
backspace_button.pack(side=RIGHT)

#-----------------
#-----------------
#-----------------
#-----------------
#-----------------
#-----------------
#-----------------
#-----------------


window.mainloop() 