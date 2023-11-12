from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Kunwoo's Program1")
root.geometry("640x480")

def sel_file():
    pass

def del_file():
    pass

frame_file = Frame(root)
frame_file. pack(fill = "x", padx = 5, pady = 5)

add_file = Button(frame_file, text = "파일 선택", command = sel_file)
add_file. pack(side = "right", padx = 5, pady = 5)

del_file = Button(frame_file, text = "파일 제거", command = del_file)
del_file. pack(side = "left")

frame_filename = Frame(root)
frame_filename. pack(fill = "x", padx = 5, pady = 5)

scrollbar = Scrollbar(frame_filename)
scrollbar.pack(side = "right", fill = "y")

file_name = Listbox (frame_filename, selectmode = "extended" ,height = 5, yscrollcommand = scrollbar.set)
file_name. pack(fill = "x", padx = 5, pady = 5)
scrollbar.config(command = file_name.yview)

frame_option = LabelFrame(root, text = "옵션 선택")
frame_option. pack(fill = "x", padx = 5, pady = 5)

opt_mul = ["1.0", "1.2", "1.4", "1.6", "1.8", "2.0"]
cmb_mul = ttk.Combobox(frame_option, state = "readonly", values = opt_mul)
cmb_mul.current(0)
cmb_mul.pack(side = "left", padx = 5, pady = 5)

opt_type = ["excel", "image", "pdf"]
cmb_type = ttk.Combobox(frame_option, state = "readonly", values = opt_type)
cmb_type.current(0)
cmb_type.pack(side = "right", padx = 5, pady = 5)

root.mainloop()