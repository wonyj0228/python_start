from tkinter import *  #tkinter 에서 가져온다.
# import tkinter 라고치면, 모든 입력값 앞에 tkinter.~~~ 라고 주소값을 쳐줘야함.
from tkinter import messagebox   #메세지박스 가져옴


#버튼을 눌렀을 때 로그인 기능을 처리해야함.
#특정한 기능은 하나의 함수로 만들어 주면 됨.
#버튼 눌렀을 때 처리하고자 하는 기능하나는 함수하나가 됨.
#함수를 만드는 것을 함수를 정의한다라고 함.
#기능을 프로그래머가 정의하기 때문에 함수를 정의한다고 표현함.
# def = definition

def login():
    #id 입력한 값, pw 입력한 값 가지고 와야함.
    #원래 회원가입할 때의 id/pw와 입력한 값을 비교해야 함.
    id2 = id_entry.get() #.get 은 입력한 값을 가져와라
    print('입력한 id는 ', id2)
    pw2 = pw_entry.get()
    print('입력한 pw는 ', pw2)

    if id2 == 'root' and pw2 == '1234':
        print('로그인에 성공하였습니다.')
        messagebox.showinfo('로그인 성공','축하합니다.')

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

        number = Label(w2, text='번호', font=('돋움', 40))  # 번호 항목
        number.pack()

        number_entry = Entry(w2, font=('돋움', 40), bg='black', fg='white')  # 번호 입력창
        number_entry.pack()

        title = Label(w2, text='제목', font=('돋움', 40))  # 제목 항목
        title.pack()

        title_entry = Entry(w2, font=('돋움', 40), bg='black', fg='white')  # 제목 입력창
        title_entry.pack()

        contents = Label(w2, text='내용', font=('돋움', 40))  # 내용 항목
        contents.pack()

        contents_entry = Entry(w2, font=('돋움', 40), bg='black', fg='white')  # 내용 입력창
        contents_entry.pack()

        writer = Label(w2, text='작성자', font=('돋움', 40))  # 작성자 항목
        writer.pack()

        writer_entry = Entry(w2, font=('돋움', 40), bg='black', fg='white')  # 작성자 입력창
        writer_entry.pack()

        b = Button(w2, text='글쓰기 완료.', font=('돋움', 40), bg='yellow', fg='black',
                   command=check)  # 버튼창
        b.pack()

        w.mainloop()

    else:
        print('로그인에 실패하였습니다.')


    #root/1234

w = Tk()
w.geometry("500x250")  #크기설정

#pack 으로 올린 순서대로 웹에 올라감

#User Interface(UI)
#2가지 방식으로 만들 수 있음 => 1.명령어 치는 방법 2. 그래픽으로 실행하는 방법
#command line interface(CLI) : 사용자가 명령어를 쳐서 프로그램을 실행/사용 (리눅스)
#GUI = 그래픽 유저 인터페이스 Graphic UI(윈도우 아이콘, 파이썬 tkinter)을 사용/실행

#label = 글자를 올리는 것. label(올릴 위치, 텍스트 = )
id = Label(w, text = 'ID입력', font = ('궁서',30)) #id라는 글자가 올라감
id.pack()

id_entry = Entry(w, font = ('궁서',30),bg='blue',fg='white')   #w 화면에 띄울것이라는 뜻 / id를 입력할 것
id_entry.pack()

pw = Label(w, text = 'PW입력',font = ('궁서',30))
pw.pack()

pw_entry = Entry(w, font = ('궁서',30),bg='blue',fg='white')  #pw를 입력
pw_entry.pack()


b = Button(w, text = '로그인 처리', font = ('궁서',30), bg='yellow',
           command=login)  #클릭버튼, command 할때 괄호 안씀

b.pack()

w.mainloop()