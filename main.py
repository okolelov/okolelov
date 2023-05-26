from ttkbootstrap import *
from ttkbootstrap.constants import *
import customtkinter
from threading import Thread
import os

def run_text():
	os.system("python3 office_apps/text_docx.py")

def run_db():
	os.system("python3 office_apps/datbase_docx.py")

def run_table():
	os.system("python3 office_apps/table_docx.py")

def run_press():
	os.system("python3 office_apps/press_docx.py")


class App(Window):

	def __init__(self):
		super().__init__(title="Ruffice hub", themename="darkly")
		Thread(target=self.user_interface).start()
		self.themename="darkly" 
		self.title="Ruffice hub"

	def user_interface(self):
		self.w, self.h = self.winfo_screenwidth(), self.winfo_screenheight()
		self.geometry("%dx%d" % (self.w, self.h)) 

		self.docx = ttk.Button(master=self, text="Текстовый редактор", command=lambda : self.app_run("text_docx"))
		self.docx.place(x=10, y=20)

		self.tables = ttk.Button(master=self, text="Таблицы", command=lambda : self.app_run("table_docx"))
		self.tables.place(x=10, y=60)

		self.press = ttk.Button(master=self, text="Презентации", command=lambda : self.app_run("press_docx"))
		self.press.place(x=10, y=100)

		self.database = ttk.Button(master=self, text="Базы данных", command=lambda : self.app_run("db_docx"))
		self.database.place(x=10, y=140)

		self.exit_app = ttk.Button(master=self, text="Выход из офиса", command=self.destroy)
		self.exit_app.place(x=10, y=180)

	def app_run(self, docs_type):
		from functions import sub_title
		
		if docs_type == "table_docx":
			sub_title("Таблицы")
			Thread(target=run_table).start()

		elif docs_type == "text_docx":
			sub_title("Текстовый редактор")
			Thread(target=run_text).start()

		elif docs_type == "press_docx":
			sub_title("Презентации")
		
		elif docs_type == "db_docx":
			sub_title("Базы данных")

if __name__=="__main__":
	app = App()
	app.mainloop()