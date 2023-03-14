
import sys
from cx_Freeze import setup, Executable

company_name = 'Daemon-Hub'
product_name = 'Translator'

bdist_msi_options = {
	'upgrade_code': '{48B079F4-B598-438D-A62A-8A233A3F8901}',
	'add_to_path': False,
	'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (company_name, product_name),
}

base = None
if sys.platform == 'win32':
	base = 'Win32GUI'

setup(
	name=product_name,
	options = {
		'bdist_msi': bdist_msi_options, 
		"build_exe":{
			"packages":[
					"tkinter","googletrans",
					"gtts","playsound","pyperclip",
					"os","speech_recognition",
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
			base=base
	)]
)
