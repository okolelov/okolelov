import os

def sub_title(mess):
	title = "Ruffice     " 
	command=f'''notify-send "{title}" "{mess}"
	'''

	os.system(command)