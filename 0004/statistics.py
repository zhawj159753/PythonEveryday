# coding = utf-8

import re

def sta(path):
	fname = open(path)
	count = 0
	for line in fname:
		l = re.findall(r'[a-zA-Z]+(\'[a-zA-Z]+|\b)', line)
		print l
		count += len(l)
	return count

if __name__ == '__main__':
	path = raw_input("Input the txt: ")
	print sta(path)