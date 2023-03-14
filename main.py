from tkinter import Tk, Canvas, Frame, PhotoImage, Scrollbar, Label, Text, StringVar, Button, TOP, END
from tkinter.ttk import Combobox
from gtts import gTTS
from playsound import playsound
from speech_recognition import Recognizer, Microphone
from googletrans import LANGUAGES, Translator
from pyperclip import copy, paste
from tkinter.messagebox import showinfo

import os

WIDTH=600
HEIGHT=300
BG = "gray20"

EN_WORDS = list(map(chr, range(97, 123)))

pashalca = "Меня создал Кертов Ислам! Ой, я хотела сказать:,"

#==========================><Скрипты><==========================#

#==========><Запись текста><==========#

def Record():

	lan = "en_US" if lng_Cbx1['text'] == "english" else "ru_RU"

	recognizer = Recognizer()

	with Microphone(device_index=1) as source:
		audio = recognizer.listen(source)
		speech = recognizer.recognize_google(audio, language=lan).lower()
		txt.delete('1.0', END)
		txt.insert('1.0', speech)

#==========><Воспроизведение текста><==========#

def Reproduce():

	if os.path.exists('sound.mp3'): os.remove("sound.mp3")

	if "тебя создал" in txt.get('1.0', 'end') or "создал тебя" in txt.get('1.0', 'end'):
		text = pashalca + txt.get('1.0', 'end')
	else:
		text = txt.get('1.0', 'end')

	for i in text:
		if i in EN_WORDS: 
			lan = "en"
			break
		else: 
			lan = "ru"

	tts = gTTS(text=text, lang=lan)

	mp3 = "sound.mp3"

	tts.save(mp3)

	playsound(mp3)

#==========><Коппирование текста><==========#

def Copy():

	text = txt.get('1.0', 'end')

	coped = copy(text)

	return coped

#==========><Вставка текста><==========#

def Paste():
	
	past = paste()

	# txt.delete('1.0', END)
	txt.insert('1.0', past)

#==========><Форматирование полученных языков><==========#

def get_key(k, d, value):

    for i in k:

        if d[i] == value:

            return str(i)

#==========><Перевод><==========#

def Translation():

	text = txt.get('1.0', 'end')

	lng_Cbx1_txt = get_key(LANGUAGES.keys(), LANGUAGES, str(lng_Cbx1.get()))

	lng_Cbx2_txt = get_key(LANGUAGES.keys(), LANGUAGES, str(lng_Cbx2.get()))

	translator = Translator()

	result = translator.translate(text, src=lng_Cbx1_txt, dest=lng_Cbx2_txt)

	txt.delete('1.0', END)
	txt.insert('1.0', result.text)

#==========><Удалить текст><==========#

def delete_text():

    txt.delete(1.0, END)

#==========><Инвертировать языки><==========#

def Invert():

	lng_Cbx1['text'], lng_Cbx2['text'] = lng_Cbx2['text'], lng_Cbx1['text']

#==========================><Интерфейс(GUI)><==========================#

#==========><Пораметры окна><==========#

window = Tk()
window.geometry('{}x{}+440+270'.format(WIDTH, HEIGHT))
window.resizable(width=False, height=False)
window.config(bg=BG)
window.title('Translator')
window.wm_iconbitmap("icon.ico")

#==========><Встречающий текст><==========#

label = Label(text='Крутой переводчик!!!', font=('Comic', 16), fg='blue4', bg=BG)
label.pack()

#==========><Текстовое поле><==========#

txt = Text(width=65, height=10)
txt.place(x=37, y=75)

#==========><Ползунок><==========#

scroll = Scrollbar(command=txt.yview)
scroll.place(x=563,y=75,height=164)

txt.config(yscrollcommand=scroll.set)

#==========><Другое><==========#

frame = Frame(bg="gray").pack(side=TOP)

#==========><Выбор первого языка><==========#

lng1 = StringVar()
lng_Cbx1 = Combobox(width = 24, textvariable = lng1)
lng_Cbx1['values']=("\n".join(LANGUAGES.values()).replace("(","").replace(")",""))
lng_Cbx1.place(x=40, y=40)
lng_Cbx1.current()

lng_Cbx1.set("russian")

#==========><Выбор второго языка><==========#

lng2 = StringVar()
lng_Cbx2 = Combobox(window, width = 24, textvariable = lng2)
lng_Cbx2['values']="\n".join(LANGUAGES.values())
lng_Cbx2.place(x=255, y=40)
lng_Cbx2.current()

lng_Cbx2.set("english")

#==========><Кнопка очистки поля><==========#

delBt = Button(

		frame, text='Очистить', bg="gray51",
		activebackground="gray51", command=delete_text

);	delBt.place(x=46, y=250, width=250, height=25)

#==========><Кнопка перевода><==========#

button = Button(

		frame, text='Перевести', bg="gray51",
		activebackground="gray51", command=Translation

);	button.place(x=305, y=250, width=250, height=25)

#==========><Кнопка инвертирования языков><==========#

img = PhotoImage(file='arrow.png')

all_lng_Bt = Button(

		frame, image=img, bg="gray51",
		activebackground="gray51", command=Invert,
		width=30 ,height=21

);	all_lng_Bt.place(x=214, y=38)

#==========><Кнопка начала записи><==========#

rec_img = PhotoImage(file='microphone.png')

recordBt = Button(

		frame, image=rec_img, bg="gray51",
		activebackground="gray51", command=Record,
		width=25, height=23

);  recordBt.place(x=435, y=38)

#==========><Кнопка воспроизведения записи><==========#

sound_img = PhotoImage(file='dinamic.png')

soundBt = Button(

		frame, image=sound_img, bg="gray51",
		activebackground="gray51", command=Reproduce,
		width=25, height=23

);  soundBt.place(x=470, y=38)
#==========><Кнопка копирования><==========#

copy_img = PhotoImage(file='copy.png')

copyBt = Button(

		frame, image=copy_img, bg="gray51", 
		activebackground="gray51", command=Copy,
		width=20, height=24

);	copyBt.place(x=505, y=38)

#==========><Кнопка вставки><==========#

paste_img = PhotoImage(file='paste.png')

pasteBt = Button(

		frame, image=paste_img, bg="gray51",
		activebackground="gray51", command=Paste,
		width=20, height=24

);	pasteBt.place(x=535, y=38)

#==========><Конец><==========#

showinfo("Важно!", "Сейчас переводчик поддерживает запись только русской и английской речи!\
				Поэтому не пытайтесь говорить на других языках.")

window.mainloop()
