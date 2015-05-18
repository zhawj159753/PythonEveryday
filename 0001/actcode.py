# coding = utf-8

import random

def generate_one_code(number):
	s = ''
	for i in range(number):
		s = s + str(random.randint(0, 9))
	return s

def store_code(path, codes):
	fname = open(path, 'w')
	fname.writelines(codes)
	fname.close()

if __name__ == '__main__':
	number = input("How many numbers for one code: ")
	path = raw_input("To store the code at: ")

	codes = []
	for i in range(200):
		codes.append(generate_one_code(number)+'\n')

	store_code(path, codes)

