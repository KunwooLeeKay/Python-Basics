from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import pandas as pd

root = Tk()
root.title("Kunwoo's Program1")
root.geometry("500x400")

def add_file():
    files = filedialog.askopenfilenames(title = "파일을 선택하세요",\
         filetypes =(("상관없음", "*.*"), ("엑셀1", "*.xls"), ("엑셀2", "*.xlsx")),\
             initialdir = "C:/")
    for file in files:
        file_name.insert(END, file)

def del_file():
    for index in reversed(file_name.curselection()):
        file_name.delete(index)

def path_sel():
    folder_selected = filedialog.askdirectory()
    if folder_selected == 'None':
        return
    path_name.delete(0, END)
    path_name.insert(0, folder_selected)

def start():
    pass


frame_file = Frame(root)
frame_file. pack(fill = "x", padx = 5, pady = 5)

add_file = Button(frame_file, text = "파일 선택", command = add_file)
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
frame_option. pack(fill = "x", padx = 3, pady = 5)

label_mul = Label(frame_option, text = "가중치", width = 8)
label_mul.pack(side = "left")

opt_mul = ["1.0", "1.2", "1.4", "1.6", "1.8", "2.0"]
cmb_mul = ttk.Combobox(frame_option, state = "readonly", values = opt_mul, width = 14)
cmb_mul.current(0)
cmb_mul.pack(side = "left", padx = 5, pady = 5)

label_type = Label(frame_option, text = "반환 형식", width = 8)
label_type.pack(side = "left")

opt_type = ["excel", "image", "pdf"]
cmb_type = ttk.Combobox(frame_option,state = "readonly", values = opt_type, width = 14)
cmb_type.current(0)
cmb_type.pack(side = "left", padx = 5, pady = 5)

frame_path = LabelFrame(root, text = "경로 선택")
frame_path. pack(fill = "x")

path_name = Entry(frame_path)
path_name. pack(side = "left", fill = "x", expand = True, padx = 5, pady =5)

path_sel = Button(frame_path, text = "저장경로 선택", command = path_sel)
path_sel.pack(side = "right", padx = 5, pady = 5)

frame_action = Frame(root)
frame_action.pack(fill = 'x', ipady = 5, padx = 5, pady = 5)

start = Button(frame_action, text = "시작", padx = 5, pady = 5, command = start)
start. pack(side = "right")

end = Button(frame_action, text = "종료", padx = 5, pady = 5, command = root.quit)
end.pack(side = "right")

root.mainloop()