# read the idx file and extract all the words,then write into a txt file
import sys
import os
import struct
import pickle
import codecs
# reload(sys) 
# sys.setdefaultencoding('utf8')

#convert the coded format!
#don't konw why do this temporarily
def ConvertCN(s):
    return s.encode('gb18030')

#get the sense of word from dictFile
#dictObject = file('oxford-gb.dict', 'rb')
dictObject = open('oxford-gb.dict','rb')
def getSense(start):
	senStart, = struct.unpack('>i', chunk[start:start+4])
	senSize, = struct.unpack('>i', chunk[start+4:start+8])

	return senStart, senSize
	
def printSense(offset, size):
	dictObject.seek(offset)
	senceChunk2 = dictObject.read(size)
	print(len(senceChunk2))
	#sys.stdout.buffer.write(senceChunk2.encode('gb18030')) #(ConvertCN(senceChunk2))
	sys.stdout.buffer.write(senceChunk2.decode('utf-8').encode('gb18030'))
	print('\n')

os.system('cls')
print('\
**********************************************************\n\
---------------------haithink\'s Dict----------------------\n\
**********************************************************\n\
---------------------Please Contact 330240295@qq.com------\n\
**********************************************************\n')



def remModel():
	print('-----------------------rem model----------------------\n')
	bRem = True
	while(bRem):
		try:
			rem = input('---------------------Please enter the word:---------------\n')
			print(rem)
		except EOFError:
			print('---------------------Quit the rem model---------------------')
			bRem = False


def queryModel():
	print('-----------------------query model----------------------\n')		
	haiDict = {};
	dictData = 'wordInfo.data'
	# Read back from the storage
	f = open(dictData,'rb')
	haiDict = pickle.load(f)
	f.close();


	bQuery = True	
	while(bQuery):
		try:
			query = input('---------------------Please enter the word:---------------\n')
			#print query
			#print haiDict
			try:
				[QsenStart, QsenSize] = haiDict[query.lower()]
				print(QsenStart, QsenSize)
				printSense(QsenStart, QsenSize)
			except KeyError:
				print('------------------cannot find this word!--------------------')
		except EOFError:
			print('---------------------Quit the query model---------------------')
			dictObject.close()
			bQuery = False	


# Main Function!
print('-----------------------command model----------------------\n')			
bRun = True;
while(bRun):
	try:
		cmd = input('--------------------Please enter the command:-------------\n')
		if(cmd == 'q'):
			queryModel()
		elif(cmd == 'r'):
			remModel()
		else:
			print('-----------------------unkonwn command-----------------------\n')
	except EOFError:
		print('---------------------Quit the programe---------------------')
		bRun = False