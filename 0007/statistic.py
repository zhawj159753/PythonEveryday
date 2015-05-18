# coding = utf-8

def read_file(path):
	txt = open(path)
	lines = txt.readlines()
	return lines

def classify(lines):
	comment_num = 0
	code_num = 0
	space_num = 0
	multi_num = 0

	for line in lines:
		line = line.strip()
		if line == '':
			space_num += 1
		elif line.startswith('#'):
			comment_num += 1
		else:
			code_num += 1
	return comment_num, code_num, space_num


if __name__ == '__main__':
	txt = read_file(raw_input('input the file: '))
	comment, code, space = classify(txt)
	print 'comment:', comment
	print 'code:', code
	print 'space:', space



