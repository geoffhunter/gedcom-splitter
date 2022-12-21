from tkinter import *
import ged_lib as gl
import tag_records as tag
import write_ged_file as wgf

want_ui = True

def clicked1():
    gl.process_ged_file()

def clicked2():
    tag.tag_ancestors_families()

def clicked3():
    wgf.write_ged_file()
    
def exit():
    root.destroy()

if want_ui:
    font = "Tahoma"
    font_size = 10
    root = Tk()
    root.title("")
    root.geometry('340x520') #width, height
    f00 = Label(root, text=" V1.00",font=(font, font_size))
    f00.grid(row=0, column=0)
    f11 = Label(root, text="  ",font=(font, 10))
    f11.grid(row=1, column=1)
    f31 = Label(root, text="Family Tree Splitter",font=(font, font_size))
    f31.grid(row=3, column=1)
    f41 = Label(root, text=" ",font=(font, font_size))
    f41.grid(row=4, column=1)
    f51 = Button(root, text="   Process GED file   ", font=(font, font_size), command=clicked1)
    f51.grid(row=5, column=1)
    f61 = Label(root, text=" ",font=(font, font_size))
    f61.grid(row=6, column=1)
    f71 = Button(root, text="      Tag Records      ", font=(font, font_size), command=clicked2)
    f71.grid(row=7, column=1)
    f81 = Label(root, text=" ",font=(font, font_size))
    f81.grid(row=8, column=1)
    f91 = Button(root, text=" Write New GED File ", font=(font, font_size), command=clicked3)
    f91.grid(row=9, column=1)
    f101 = Label(root, text=" ",font=(font, font_size))
    f101.grid(row=10, column=1)
    f111 = Button(root, text="              Exit            ", font=(font, font_size), command=exit)
    f111.grid(row=11, column=1)
    f121 = Label(root, text=" ",font=(font, font_size))
    f121.grid(row=12, column=1)
    f131 = Button(root, text="     Edit Parameters    ", font=(font, font_size), command=gl.edit_params)
    f131.grid(row=13, column=1)
    root.mainloop()
else:
    gl.process_ged_file()
    tag.tag_ancestors_families()
    wgf.write_ged_file()
