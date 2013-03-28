import unittest
import message

class test_message(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass
	
	def test_wrap(self):
		message.line_length=5  # easy to construct expt result

		# functional check
		self.assertEquals(message.wrap('ab'), '-ab--\n')
		self.assertEquals(message.wrap('abc'), '-abc-\n')
		self.assertEquals(message.wrap(3), '--3--\n')
		self.assertEquals(message.wrap(34), '-34--\n')
		self.assertEquals(message.wrap(None),None)

		# bound check
		self.assertEquals(message.wrap('123456'),'123456\n')
		self.assertEquals(message.wrap('12345'),'12345\n')
		self.assertEquals(message.wrap('1234'),'1234-\n')
		self.assertEquals(message.wrap(123456),'123456\n')
		self.assertEquals(message.wrap(''),'-----\n')

	def test_stars(self):
		message.line_length=5  # easy to construct expt result

		self.assertEquals(message.stars_line(),'*****\n')

	def test_head(self):
		# functional check
		message.line_length=5  # easy to construct expt result

		self.assertEquals(message.head('a', 3, a='bc', b=5),
			'*****\n--a--\n--3--\n-bc--\n--5--\n*****\n')


if __name__=='__main__':
	suite=unittest.TestSuite()

	suite.addTest(test_message('test_wrap'))
	suite.addTest(test_message('test_stars'))
	suite.addTest(test_message('test_head'))

	runner=unittest.TextTestRunner()
	runner.run(suite)
