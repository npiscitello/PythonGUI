import Tkinter

window = Tkinter.Tk()

focus = False



def button(string):
	buttonstatus.config(text = 'Button %s was pressed!' % string)

def enter():
	if len(e.get()) > 0:
		sized = e.get()
		if len(sized) > 30:
			sized = sized[:27] + '...'
		textstatus.config(text = sized)

def entertemplate():
	if templates.curselection() != ():
		e.delete(0, 'end')
		e.insert(0, templates.get(templates.curselection()))
		enter()

def infocus(event):
	global focus
	focus = True

def outfocus(event):
        global focus
	focus = False

def enterkey(event):
	global focus
	if focus:
		entertemplate()
	else:
		enter()



text = Tkinter.StringVar()
buttonframe = Tkinter.Frame(window)
textframe = Tkinter.Frame(window)
labelframe = Tkinter.Frame(window)

b1 = Tkinter.Button(buttonframe, text='one', command=lambda: button('one'))
b2 = Tkinter.Button(buttonframe, text='two', command=lambda: button('two'))
b3 = Tkinter.Button(buttonframe, text='three', command=lambda: button('three'))

lbl = Tkinter.Label(labelframe, text='GUI Development', font=('Helvetica', '30', 'bold'))
buttonstatus = Tkinter.Label(labelframe, text='button status', font=('Helvetica', '16', 'italic'))
textstatus = Tkinter.Label(labelframe, text='text box status', font=('Helvetica', '16', 'italic'))

e = Tkinter.Entry(textframe, textvariable=text, width=30)
textenter = Tkinter.Button(textframe, text='enter', command = enter)
templatelabel = Tkinter.Label(textframe, text='Sample Text:', font=('Helvetica', '16', 'bold'))
templates = Tkinter.Listbox(textframe, height = 5)
for i in range(1,11):
	templates.insert('end', "Template %d" % i)
templateenter = Tkinter.Button(textframe, text='enter', command = entertemplate)
window.bind('<Return>', enterkey)
templates.bind('<FocusIn>', infocus)
templates.bind('<FocusOut>', outfocus)


lbl.pack(side = 'top', padx = 15)
buttonstatus.pack(padx = 5, pady = 2)
textstatus.pack(padx = 5, pady = 2)
#buttonstatus.grid(row = 0, column = 0, padx = 10)
#textstatus.grid(row = 0, column = 1, padx = 10)

b1.pack(side='left', padx=10)
b2.pack(side='left', padx=10)
b3.pack(side='left', padx=10)

e.grid(row = 0, column = 0, padx = 5, pady = 10)
textenter.grid(row = 0, column = 1, padx = 5, pady = 10)
templatelabel.grid(row=1, column = 0, padx = 5)
templates.grid(row = 2, column = 0, padx = 5)
templateenter.grid(row = 2, column = 1, padx = 5)

labelframe.pack(pady = 10)
buttonframe.pack(pady = 10)
textframe.pack(pady = 10)



window.mainloop()
