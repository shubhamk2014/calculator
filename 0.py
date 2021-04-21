from tkinter import *


def click_button(event):
    inp = event.widget.cget("text")
    if inp == "AC":
        text.set("")
    elif inp == "C":
        text.set(text.get()[:-1])
    elif inp == "=":
        try:
            if text.get().isdigit():
                val = int(text.get())
            else:
                val = eval(text.get())
            text.set(val)
        except SyntaxError:
            pass
    elif inp == "1/x":
        try:
            text.set(1/float(text.get()))
        except SyntaxError:
            pass
        except ValueError:
            pass
    elif inp == "x^2":
        try:
            if text.get().isdigit():
                val = int(text.get())
            else:
                val = eval(text.get())
            text.set(val*val)
        except SyntaxError:
            pass
        except ValueError:
            pass

    else:
        text.set(text.get()+inp)


root = Tk()
root.title("Calculator")
text = StringVar()
text.set("")

e = Entry(root,width = 15, textvariable = text, font ="Times 25").pack(pady = 2, padx= 2)
values = [['AC', '1/x', 'x^2', 'C'],['9','8','7','/'],['6','5','4','*'],['3','2','1','-'],['0','=','.','+']]

for value in values:
    frame = Frame(root, width=56, height=50, bg= "#888")
    for i in range(0,4):
        btn = Button(frame,text=value[i], width=3, height = 1, font = "Times 25", bg = "sky blue")
        btn.pack(side= LEFT, padx= 3, pady = 3)
        btn.bind("<Button-1>",click_button)
    frame.pack()
root.mainloop()
