import pytest
import unittest
d = {}
class s(unittest.TestCase):
	def check(self):
		d.clear()
		counter('aab')
		self.assertTrue(d == {'a':2, 'b': 1})
def counter(g):
	'''
	>>> counter('a')
	{'a': 1}
	'''
	for i in g:
		if i in d:
			d[i] = d[i]+1
		else:
			d[i]=1
	print(d)
def pyTest():
	d.clear()
	counter("aba")
	assert d == {'a': 2, 'b': 1}
if __name__ == "__main__":
	import doctest
	doctest.testmod()
	pyTest()
	unittest.main()
	#with open("1.txt") as a:
	#	for i in a:
	#		counter(i)
	print(d)