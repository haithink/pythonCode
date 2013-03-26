# read the idx file and extract all the words,then write into a txt file
import sys
import os
import struct

reload(sys) 
sys.setdefaultencoding('utf8')

#convert the coded format!
#don't konw why do this temporarily
def ConvertCN(s):
    return s.encode('gb18030')

#get the sense of word from dictFile
dictObject = file('oxford-gb.dict', 'rb')	
def getSense(start):
	#print start
	ss = ''
	#print chunk[start:start+4]
	# for i in range(0,4):
		# ss += chunk[start+i]
	senStart, = struct.unpack('>i', chunk[start:start+4])
	senSize, = struct.unpack('>i', chunk[start+4:start+8])
	#print senStart,senSize
	#print dictoffset
	#print int(ss,16)
	# senStart = int(chunk[start:start+4],16)
	# senSize = int(chunk[start+4:start+8],16)
	dictObject.seek(senStart)
	senceChunk = dictObject.read(senSize)
	#print ConvertCN(senceChunk)
	return senStart, senSize
	
def printSense(offset, size):
	dictObject.seek(offset)
	senceChunk2 = dictObject.read(size)
	print ConvertCN(senceChunk2)


def getWord(start):
	index = start
	isChar = True
	while(isChar): 		
		#if(chunk[index].isalpha() or chunk[index].isspace()):
		if(ord(chunk[index]) != 0):
			#print index
			#print chunk[index]
			index = index+1
		else:
			isChar = False
	else:
		return index

offset = 4111 #the offset of 'a' in the idx file
idxFileName = 'oxford-gb.idx'

idxFileSize = os.path.getsize(idxFileName)
#print idxFileSize
idxObject = file(idxFileName, 'rb')
idxObject.seek(offset)

chunk = idxObject.read()
idxObject.close()

chunkSize = len(chunk)
start = 0

wordlistFileName = 'list.txt'
wlObject = file(wordlistFileName, 'w')

#get all words and write into a file
wordlist = []
haiDict = {};
#for i in range(0,3):
while(start < chunkSize):
	# print start
	# print chunk[start]
	end = getWord(start)
	#print chunk[start:end]
	senStart, senSize = getSense(end+1)
	
	wordlist.append(chunk[start:end])
	haiDict[chunk[start:end]] = [senStart, senSize]
	wlObject.write(chunk[start:end])
	wlObject.write('\n')
	print end
	#getSense(end+1)	
	start = end+9
	#print start
print 'over'
wlObject.close()
# print haiDict
# print haiDict['a']

bQuery = True	
while(bQuery):
	try:
		query = raw_input('Please enter the world:\n')
		#print query
		#print haiDict
		try:
			[QsenStart, QsenSize] = haiDict[query]
			print QsenStart, QsenSize
			printSense(QsenStart, QsenSize)
		except KeyError:
			print 'cannot find this world!'
	except EOFError:
		print 'Quit the programe'
		bQuery = False	