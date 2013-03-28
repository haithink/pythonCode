""" run as main module to show demo
format to show"""

line_length = 60

def wrap(info):
	start_length = int((line_length - len(info)) / 2)
	return "{}{}{}\n".format('-' * start_length, info,
		'-' * (line_length - start_length - len(info)))

def stars_line():
	return '*' * line_length + '\n'
def clear_screen(cmd):
	import os
	os.system(cmd)

def head(*args, **kwargs):
	head_info = stars_line()
	for info in args:
		head_info += wrap(info)
	for info in kwargs.values():
		head_info += wrap(info)
	head_info += stars_line()
	return head_info

if __name__ == "__main__":
	#print(tt.wrap('dict'))
	#print(tt.stars())
	print(head("haithink's Dict", contant='Contact 330240295@qq.com'))
