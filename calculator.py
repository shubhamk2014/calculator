from tkinter import *

def click(event):
    inp= event.widget.cget("text")
    if inp == "AC":
        text.set("")

    elif inp == "C":
        text.set(text.get()[:-1])

    elif inp == "1/x":
        try:
            text.set(1.0/float(text.get()))
        except SyntaxError:
            pass
        except ValueError:
            pass
    elif inp == "=":
        try:
            if text.get().isdigit():
                value = int(text.get())
            else:
                value = eval(text.get())
            text.set(value)
        except SyntaxError:
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
root.geometry("360x450")
root.title("Calculator")

f0 = Frame(root, width = 450, height = 30)
Label(f0, text = "CALCULATOR", font="Times 20 bold").pack()
f0.pack()
text = StringVar()
text.set("")
screen = Entry(root, textvariable = text, font = "Times 19 bold").pack(ipadx= 5,padx = 20,pady = 20)

# f1= Frame(root, width = 450, height = 50)
# for i in range(0,4):
#     num1=['7','8','9','/']
#     Button(f1, text =num1[i],font = "Times 15 bold", width = 5, height = 2).grid(row = 0,column = i)
# f1.pack()
#
# f2= Frame(root, width = 450, height = 50)
# for i in range(0,4):
#     num2 = ['6', '5', '4', '*']
#     Button(f2, text =num2[i],font = "Times 15 bold", width = 5, height =2).grid(row = 0,column = i)
# f2.pack()
#
# f3= Frame(root, width = 450, height = 50)
# for i in range(0,4):
#     num3=['1','2','3','-']
#     Button(f3, text =num3[i],font = "Times 15 bold", width = 5, height = 2).grid(row = 0,column = i)
# f3.pack()
#
# f4= Frame(root, width = 450, height = 50)
# for i in range(0,4):
#     num4=['00','0','.','=']
#     Button(f4, text =num4[i],font = "Times 15 bold", width = 5, height = 2).grid(row = 0,column = i)
# f4.pack()
#

nums=[['AC','1/x','x^2','C'],['7','8','9','/'],['6', '5', '4', '*'],['1','2','3','-'],['0','.','=','+']]
for num in nums:   #for loop for each list in the nums
    f = Frame(root, width=450, height=50)  # frame for eack list in the nums
    for i in range(0, 4):   #for loop for packing four buttons in the row
        b = Button(f, text=num[i], font="Times 15 bold", width=5, height=2)
        b.pack(side = LEFT)
        b.bind("<Button-1>", click)
    f.pack()



root.mainloop()