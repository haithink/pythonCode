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
	idx = dict_idx.get(word.lower(), None)
	if idx is None:
		return 'word not exist'
	# get desc by idx
	QsenStart, QsenSize = idx
	# set default value, return it if not modified
	desc = 'data file error. filename = {}'.format(dictfile)
	with open(dictfile,'rb') as dictObject:
		dictObject.seek(QsenStart)
		desc = dictObject.read(QsenSize)
	return desc
