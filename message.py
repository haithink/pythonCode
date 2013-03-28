""" run as main module to show demo
format to show"""

line_length = 60

def __wrap_infomation(info):
	start_length = int((line_length - len(info)) / 2)
	return "{}{}{}\n".format('-' * start_length, info,
		'-' * (line_length - start_length - len(info)))

def __stars_line():
	return '*' * line_length + '\n'
def clear_screen(cmd):
	import os
	os.system(cmd)

def head(*args, **kwargs):
	head_info = __stars_line()
	for info in args:
		head_info += __wrap_infomation(info)
	for info in kwargs.values():
		head_info += __wrap_infomation(info)
	head_info += __stars_line()
	return head_info

if __name__ == "__main__":
	#print(tt.wrap_infomation('dict'))
	#print(tt.stars())
	print(head("haithink's Dict", contant='Contact 330240295@qq.com'))
