from difflib import SequenceMatcher
with open('file 1.txt') as f1, open('file 2.txt') as f2:
	file_1 = f1.read()
	file_2 = f2.read()
	c = SequenceMatcher(None, file_1, file_2).ratio()
	print(c)