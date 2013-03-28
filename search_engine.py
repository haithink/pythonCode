# core dictionary functions.
# query, add/modify/remove word descriptions
import pickle

dictfile='oxford-gb.dict'

dict_idx = None
def load_idx(dictData = 'wordInfo.data'):
	global dict_idx
	# Read back from the storage
	with open(dictData,'rb') as f:
		dict_idx = pickle.load(f)

def get_desc(word):
	if dict_idx is None:
		return None
	# get idx
	QsenStart, QsenSize = dict_idx[word.lower()]
	# get desc by idx
	desc = None
	with open(dictfile,'rb') as dictObject:
		dictObject.seek(QsenStart)
		desc = dictObject.read(QsenSize)
	return desc
