from ttkbootstrap import *
from ttkbootstrap.constants import *
from threading import Thread
  
class App(Window):
	def __init__(self):
		super().__init__(title="Таблицы", themename="darkly")
		Thread(target=self.user_interface).start()

	def user_interface(self):
		self.size()
		self.attributes('-zoomed', True)



app = App()

file = Menu(app)  
new_item = Menu(file, tearoff=False)  
new_item.add_command(label='Сохранить')
new_item.add_command(label='Загрузить')
new_item.add_command(label='Выход')  
file.add_cascade(label='Файл', menu=new_item) 

app.configure(menu=file)
app.mainloop()
		