# read the idx file and extract all the words,then write into a txt file
import sys

import message
import search_engine 

# reload(sys) 
# sys.setdefaultencoding('utf8')

def show(info, line_break=False):
	if isinstance(info, bytes):
		sys.stdout.buffer.write(info.decode('utf-8').encode('gb18030'))
	else:
		print(info)
	if line_break:
		print('\n')

def quit():
	print(message.wrap('bye'))

def dict_info():
	return message.head("haithink's Dict", contant='Contact 330240295@qq.com')

def queryModel():
	search_engine.load_idx()
	while True:
		try:
			word = input(message.wrap("Please enter the word('ctrl+c' to quit):"))
		except KeyboardInterrupt:
			quit()
			break
		show(search_engine.get_desc(word), line_break = True)

# Main Function!
if __name__ == '__main__':
	message.clear_screen('cls')
	show(dict_info())
	queryModel()
