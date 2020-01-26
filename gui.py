from tkinter import *
from tkinter.ttk import Combobox,  Checkbutton
from tkinter import filedialog
from PIL import ImageTk, Image

#from tkinter import Menu

window = Tk()
window.title('welcome to the best program in the world')

# define size of window
window.geometry('1000x800')

# create text label
lbl = Label(window , text='hello', font=('Arial Bold', 50))
lbl.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=1, row=0)
txt.focus() # set focus to entry widget such that you can write right away

def clicked():
    string = 'You did it !! You typed: "{}" !'.format(txt.get())
    lbl.configure(text=string)

# adding a button widget
btn = Button(window, text ='click me if you can', bg='orange', fg='green',
    command = clicked)
btn.grid(column=2, row=0)

# combo widget
combo = Combobox(window)
combo['values'] = (1,2,3,4,5, 'Text')
combo.current(1) # set the selected item
combo.grid(column=0, row=1)

combo_string = combo.get()

# heckbutto widget
chk_state = BooleanVar() # also IntVar available

chk_state.set(True) #set check state,

chk = Checkbutton(window, text='Choose', var=chk_state)

chk.grid(column=0, row=2)


# add radio buttons
selected = IntVar()
rad1 = Radiobutton(window,text='First', value=1, variable=selected)
rad2 = Radiobutton(window,text='Second', value=2, variable=selected)
rad3 = Radiobutton(window,text='Third', value=3, variable=selected)

rad1.grid(column=0, row=3)
rad2.grid(column=1, row=3)
rad3.grid(column=2, row=3)

# create button for filedialog
def clicked_2():
    # filedialog
    global image_file
    image_file = filedialog.askopenfilename(filetypes = (("Image files","*.jpg"),("all files","*.*")))

btn_2 = Button(window, text ='Choose file for processing', bg='purple', fg='green',
    command = clicked_2)
btn_2.grid(column=0, row=4)


# add menü bar
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='Reset')
new_item.add_separator()
new_item.add_command(label='Exit')
menu.add_cascade(label='Options', menu=new_item)
window.config(menu=menu)


window.mainloop()
