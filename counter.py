""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
from pickle import dump, load

def update_counter(file_name, reset=False):
	""" Updates a counter stored in the file 'file_name'

		A new counter will be created and initialized to 1 if none exists or if
		the reset flag is True.

		If the counter already exists and reset is False, the counter's value will
		be incremented.

		file_name: the file that stores the counter to be incremented.  If the file
				   doesn't exist, a counter is created and initialized to 1.
		reset: True if the counter in the file should be rest.
		returns: the new counter value

	>>> update_counter('blah.txt',True)
	1
	>>> update_counter('blah.txt')
	2
	>>> update_counter('blah2.txt',True)
	1
	>>> update_counter('blah.txt')
	3
	>>> update_counter('blah2.txt')
	2
	"""

	if (exists(file_name) == False) or (reset == True):
		#What if the file isn't there or the reset is true?
		fin = open(file_name, 'r+') #creates & opens file for writing AND reading
		counter = 1
	elif (exists(file_name) == True) and (reset == False):
		#What if the file is there & the reset is true?
		fin = open(file_name, 'r+')
		counter = load(fin) + 1 #reads a string from the file_name file
								#interprets file_name file as a pickle data stream
								#reconstructs & returns the original object hierarchy
	else:
		return counter


	fin.seek(0, 0)
	dump(counter, fin) #supposed to write a pickled representaiton of an object to the file
	return counter
	fin.close()



#note to self: fin needs to be referenced BEFORE assignment! line 39 can't go before line 38

	


if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest
		doctest.testmod()
	else:
		print "new value is " + str(update_counter(sys.argv[1]))