from tkinter import *

def check():
    number2 = number_entry.get()
    print('입력한 번호는', number2)
    title2 = title_entry.get()
    print('입력한 제목은', title2)
    contents2 = contents_entry.get()
    print('입력한 내용은', contents2)
    writer2 = writer_entry.get()
    print('입력한 작성자는', writer2)

w2 = Tk()
w2.geometry("700x700")

number = Label(w2, text = '번호',font = ('돋움',40))  #번호 항목
number.pack()

number_entry = Entry(w2, font = ('돋움',40), bg = 'black', fg = 'white')   #번호 입력창
number_entry.pack()

title = Label(w2, text = '제목',font = ('돋움',40))   #제목 항목
title.pack()

title_entry = Entry(w2, font = ('돋움',40), bg = 'black', fg = 'white')   #제목 입력창
title_entry.pack()

contents = Label(w2, text = '내용',font = ('돋움',40))   #내용 항목
contents.pack()

contents_entry = Entry(w2, font = ('돋움',40), bg = 'black', fg = 'white')   #내용 입력창
contents_entry.pack()

writer = Label(w2, text = '작성자',font = ('돋움',40))   #작성자 항목
writer.pack()

writer_entry = Entry(w2, font = ('돋움',40), bg = 'black', fg = 'white')   #작성자 입력창
writer_entry.pack()

b = Button(w2, text = '글쓰기 완료.', font = ('돋움',40), bg = 'yellow', fg = 'black',
           command = check)  #버튼창
b.pack()

w. mainloop()