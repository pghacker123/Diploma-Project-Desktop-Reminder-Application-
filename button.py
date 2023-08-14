# Import Required Module
from tkinter import *
from tkinter.ttk import *

# Create Root Object
root = Tk()

# Set Geometry(widthxheight)
root.geometry('300x100')

# Create style Object
style = Style()


# Will add style to every available button 
# even though we are not passing style
# to every button widget.
style.configure('TButton', font =
			('calibri', 10, 'bold', 'underline'),
				foreground = 'red')
# button 1
btn1 = Button(root, text = 'Quit !', 
				style = 'TButton',
			command = root.destroy)

btn1.grid(row = 0, column = 3, padx = 100)

# button 2
btn2 = Button(root, text = 'Click me !', command = None)
btn2.grid(row = 1, column = 3, pady = 10, padx = 100)

# Execute Tkinter
root.mainloop()
