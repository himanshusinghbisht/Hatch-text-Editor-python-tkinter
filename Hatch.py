from tkinter import *
import os
from tkinter import messagebox

from tkinter import filedialog
root = Tk()
root.title('Hatch-Editor v 1.1')
root.call('encoding', 'system', 'utf-8')
root.geometry('400x400')
#######################################
text=Text(root)
text.config(font=("Helvetica", 13 , " italic"),bg="gray19",fg="white")
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)

text.pack(fill=BOTH, expand=True)

def show():
	messagebox.showinfo("About Hatch-Editor v 1.1","Hatch is a Text editor made by   Mr Himanshu singh Bisht  ||   (wick) ||  {Boogeyman}")
def file_open():
	filename =  filedialog.askopenfilename(initialdir = "/home/",title = "Select file",defaultextension=".txt",filetypes = (("txt files","*.txt"),("all files","*.*")))
	if filename == "":
		filename=None
	else:
		root.title(os.path.basename(filename) + " File ")
		text.delete(1.0,END)
		file = open(filename,"r")
		text.insert(END,file.read())
		file.close()
def save_file():
	
	filename = filedialog.asksaveasfilename(initialdir = "/home/",title = "Select file name ",filetypes=(("Txt files","*.txt"),("All files","*.*")))
		
	if filename == "":
		messagebox.showinfo("error","can't save file with no name")
	else:
		file = open(filename,"w")
		file.write(text.get(1.0,END))
		file.close()
def cut():
	text.event_generate("<<Cut>>")

def copy():
	text.event_generate("<<Copy>>")
def paste():
	text.event_generate("<<Paste>>")
def red():
	text.config(bg="red",fg="black")
def green():
	text.config(bg="green",fg="white")
def yellow():
	text.config(bg="yellow",fg="black")
def gray():
	text.config(bg="gray19",fg="white")
def black():
	text.config(bg="black",fg="white")
def mintcream():
	text.config(bg="mint cream",fg="black")
def khaki1():
	text.config(bg="khaki1",fg="black")
def cyan2():
	text.config(bg="cyan2",fg="black")
def burlywood3():
	text.config(bg="burlywood3",fg="black")
def gray43():
	text.config(bg="gray43",fg="white")

##########################################

def PYTHON():
	interpreter = Toplevel(root)
	TextBox = Text(interpreter,bg="gray19",fg="white")
	TextBox.pack(fill=BOTH,expand=True)
	
	file = open("python.py","w")
	file.write(text.get(1.0,END))
	file.close()
	
	os.system("touch output.txt")
	os.system("python python.py > output.txt")
	file = open("output.txt","r")
	
	TextBox.insert(END,"Hatch >> " + file.read())
	file.close()
	os.remove("python.py")
	os.remove("output.txt")
	os.remove("a.out")
	TextBox.config(state=DISABLED)
def Cplus():
	interpreter = Toplevel(root)
	TextBox = Text(interpreter,bg="gray19",fg="white")
	TextBox.pack(fill=BOTH,expand=True)
	
	file = open("C.cpp","w")
	file.write(text.get(1.0,END))
	file.close()
	
	os.system("touch output.txt")
	os.system("g++ C.cpp && ./a.out > output.txt")
	file = open("output.txt","r")
	
	TextBox.insert(END,"wick-interpreter >> " + file.read())
	file.close()
	os.remove("C.cpp")
	os.remove("output.txt")
	TextBox.config(state=DISABLED)
	
###########################################
menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)

about = Menu(menubar,tearoff=0)

edit = Menu(menubar,tearoff=0)
edit.add_command(label='Cut',command=cut)
edit.add_command(label='Copy',command=copy)
edit.add_command(label='Paste',command=paste)

color = Menu(menubar)
PYTHON = menubar.add_command(label="PYTHON",command=PYTHON)
C = menubar.add_command(label="C++",command=Cplus)
color.add_command(label="red",command=red)
color.add_command(label="yellow",command=yellow)
color.add_command(label="green",command=green)
color.add_command(label="black",command=black)
color.add_command(label="gray",command=gray)
color.add_command(label="mint cream",command=mintcream)
color.add_command(label="khaki 1",command=khaki1)
color.add_command(label="cyan 2",command=cyan2)
color.add_command(label="burlywood 3",command=burlywood3)
color.add_command(label="gray 43",command=gray43)
menubar.add_cascade(label="Colors",menu=color)

menubar.add_cascade(label="Edit",menu=edit)
#filemenu.add_command(label="New" )
filemenu.add_command(label="Open",command=file_open )
filemenu.add_command(label="Save",command=save_file )
filemenu.add_separator()
filemenu.add_command(label='Exit',command=root.destroy)
menubar.add_cascade(label="File",menu=filemenu )
########################3
def times():
	text.config(font=("Times",13," bold italic"))
def helvetica():
	text.config(font=("Helvetica",13,"bold italic"))
def symbol():
	text.config(font=("Symbol",13,"bold italic"))
fontstyle = Menu(menubar,tearoff=0)
fontstyle.add_command(label="Times",command=times)
fontstyle.add_command(label="Helvetica",command=helvetica)
fontstyle.add_command(label="Symbol",command=symbol)

menubar.add_cascade(label="Font-Style",menu = fontstyle)
#############
about.add_command(label="About" , command=show)
menubar.add_cascade(label="Help",menu=about )


################################################





root.config(menu=menubar)
root.mainloop()

