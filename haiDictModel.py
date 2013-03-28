# read the idx file and extract all the words,then write into a txt file
import sys
import os
import struct
import codecs

import message
import core_dict
# reload(sys) 
# sys.setdefaultencoding('utf8')

#convert the coded format!
#don't konw why do this temporarily
def ConvertCN(s):
    return s.encode('gb18030')

message.clear_screen('cls')
print(message.head("haithink's Dict", contant='Contact 330240295@qq.com'))

# Main Function!
print('-----------------------command model----------------------\n')			
bRun = True;
while(bRun):
	try:
		cmd = input('--------------------Please enter the command:-------------\n')
		if(cmd == 'q'):
			core_dict.queryModel()
		elif(cmd == 'r'):
			print('rem mode to recite a word')
		else:
			print('-----------------------unkonwn command-----------------------\n')
	except EOFError:
		print('---------------------Quit the programe---------------------')
		bRun = False
