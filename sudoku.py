from tkinter import *

# constants
ENTRY_WIDTH = 5

root = Tk()

box = []

scolumn = 0
for x in range(81):
    if(x%9 == 0 and x != 0):
        scolumn+=1
    box.append(Entry(root,
                    justify=CENTER,
                    width=ENTRY_WIDTH)
                    .grid(row = x%9, column = scolumn))

#e1 = Entry(root, justify=CENTER, )
#e1.pack()



# the loop that keeps the program running
root.mainloop()
