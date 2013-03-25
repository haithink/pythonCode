# read the idx file and extract all the words,then write into a txt file
import sys
import os
import struct
import cPickle

reload(sys) 
sys.setdefaultencoding('utf8')

#convert the coded format!
#don't konw why do this temporarily
def ConvertCN(s):
    return s.encode('gb18030')

#get the sense of word from dictFile
dictObject = file('oxford-gb.dict', 'rb')	
def getSense(start):
	senStart, = struct.unpack('>i', chunk[start:start+4])
	senSize, = struct.unpack('>i', chunk[start+4:start+8])

	return senStart, senSize
	
def printSense(offset, size):
	dictObject.seek(offset)
	senceChunk2 = dictObject.read(size)
	print ConvertCN(senceChunk2)


haiDict = {};
dictData = 'wordInfo.data'
# Read back from the storage
f = file(dictData)
haiDict = cPickle.load(f)
f.close();


bQuery = True	
while(bQuery):
	try:
		query = raw_input('Please enter the word:\n')
		#print query
		#print haiDict
		try:
			[QsenStart, QsenSize] = haiDict[query.lower()]
			print QsenStart, QsenSize
			printSense(QsenStart, QsenSize)
		except KeyError:
			print 'cannot find this world!'
	except EOFError:
		print 'Quit the programe'
		dictObject.close()
		bQuery = False	