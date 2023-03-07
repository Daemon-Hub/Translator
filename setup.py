from cx_Freeze import setup, Executable;

setup(
	name="Translator",
	options = {
		"build_exe":{
			"packages":[
					"tkinter","googletrans",
					"gtts","playsound",
					"speech_recognition","pyperclip",
					"os","tkinter.messagebox"
					],
			"include_files":[
				r"D:\Python\Translator\arrow.png",
				r"D:\Python\Translator\dinamic.png",
				r"D:\Python\Translator\\copy.png",
				r"D:\Python\Translator\microphone.png",
				r"D:\Python\Translator\paste.png",
				r"D:\Python\Translator\icon.ico"
			]
		}
	},
	version="2.0",
	description="My cool translator!",
	executables=[
		Executable(
			r"D:\Python\Translator\main.py",
			icon=r"D:\Python\Translator\icon.ico",
			shortcut_name="Translator",
			shortcut_dir="DesktopFolder",
			base="Win32GUI"
	)]
)