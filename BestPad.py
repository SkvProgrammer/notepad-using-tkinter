from tkinter import Toplevel,Label,Menu,Tk,Text,BOTH,Scrollbar,RIGHT,Y,END
import tkinter.messagebox  as mb
import sys
import os
from tkinter.filedialog import asksaveasfilename,askopenfilename
def helpme():
	mb.showinfo("Tip","Please Visit our official website")
def openfile():
	global file
	file  = askopenfilename(
		defaultextension = ".txt",filetype = [("All Files","*.*"),("Text Documents","*.txt")]
		)
	if file ==  " ":
		file = None
	else:
		root.title(os.path.basename(file) + " -Notepad")
		TextArea.delete(1.0,END)
		f  = open(file,"r")
		TextArea.insert(1.0,f.read())
		f.close()
def newfile():
	global file
	root.title("Untitled -Notepad")
	file = None
	TextArea.delete(1.0,END)

def savefile():
	global file 

	if file == None:
		file = asksaveasfilename(
			initialfile = "Untitled.txt",
			defaultextension = "*.txt",
			filetypes = [("All Files","*.*"),("Text Documents","*.txt")]
			)
		if file == " ":
			file = None
		else:
			f = open(file,"w")
			f.write(TextArea.get(1.0,END))
			f.close()


			root.title(os.path.basename(file) + "- Notepad")
			mb.showinfo("File Saved","Click ok to back")
	else:
		f = open(file,"w")
		f.write(TextArea.get(1.0,END))
		f.close()
def quitApp():
	quit()
def aboutus():
	mb.showinfo("Developer","Satyam Kumar Verman")
def cut():
	TextArea.event_generate(("<<Cut>>"))	
def copy():
	TextArea.event_generate(("<<Copy>>"))
def paste():
	TextArea.event_generate(("<<Paste>>"))
if __name__ == '__main__':

	#Basic Set Set
	root = Tk()
	root.title("Untitled - Notepad")
	root.geometry("644x788")
	TextArea = Text(root,font="lucida 13")
	TextArea.pack(expand = True,fill = BOTH)
	file = None
	menubar = Menu(root)
	file = Menu(menubar,tearoff = 0)

	file.add_command(label = "New",command = newfile)
	file.add_command(label = "Open",command = openfile)
	file.add_command(label = "Save",command = savefile)
	#file.add_command(label = "Save As",command = savefile)
	#file.add_seperator()
	file.add_command(label = "Exit",command = quitApp)

	menubar.add_cascade(label = "File",menu = file)


	edit = Menu(menubar,tearoff = 0)

	edit.add_command(label = "Cut",command = cut)
	edit.add_command(label = "Copy",command = copy)
	edit.add_command(label = "Paste",command = paste)
	menubar.add_cascade(label = "Edit",menu = edit)
	about  = Menu(menubar,tearoff = 0)
	about.add_command(label = "About BestPad",command = aboutus)
	menubar.add_cascade(label = "About" ,menu = about)
	helpx = Menu(menubar,tearoff = 0)
	helpx.add_command(label = "Help",command = helpme)
	menubar.add_cascade(label = "Help" , menu = helpx)
	scroll =Scrollbar(TextArea)
	scroll.pack(side  = RIGHT,fill = Y)
	scroll.config(command = TextArea.yview)
	TextArea.config(yscrollcommand  = scroll.set)
	root.config(menu = menubar)
	root.mainloop()