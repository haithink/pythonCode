# core dictionary functions.
# query, add/modify/remove word descriptions

import pickle
import sys

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

