def vi():
    view(directory_added_books, list_added_books)
def vi_0():
    view(directory_choice, list_for_analysis)
def t_f_t():
    transfer_file_to_lib(list_for_analysis[number_book() - 1], directory_choice, directory_added_books)

if __name__ == '__main__':
    from tkinter import *

    root = Tk()
    # root.option_add('* tearOff', FALSE)
    root.title("GUI на Python")
    root.geometry("900x250")

    lbl = Label(root, text="Просмотр бибилиотеки", font=("Arial Bold", 30))
    lbl.grid(column=0, row=0)
    lbl = Label(root, text="Файлы на добавление", font=("Arial Bold", 30))
    lbl.grid(column=0, row=1)
    lbl = Label(root, text="Просмотр бибилиотеки", font=("Arial Bold", 30))
    lbl.grid(column=0, row=2)
    lbl = Label(root, text="Просмотр бибилиотеки", font=("Arial Bold", 30))
    lbl.grid(column=0, row=3)


    btn = Button(root, text="Не нажимать!", command=vi, bg="black", fg="red")
    btn.grid(column=1, row=0)
    btn = Button(root, text="Не нажимать!", command=vi_0, bg="black", fg="red")
    btn.grid(column=1, row=1)
    btn = Button(root, text="Не нажимать!", command=t_f_t, bg="black", fg="red")
    btn.grid(column=1, row=2)
    btn = Button(root, text="Не нажимать!", command=vi, bg="black", fg="red")
    btn.grid(column=1, row=3)

    txt = Entry(root, width=10)
    txt.grid(column=2, row=4)

    root.mainloop()