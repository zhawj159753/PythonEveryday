# coding = utf-8

import re

def read_file(path):
	f = open(path)
	return f.read()

def get_all_words(string):
	words = re.findall(r'[a-zA-Z]+\b', string)
	return words

def get_frequent_word(words):
	word_dic = {}
	for word in words:
		if word in word_dic:
			word_dic[word] += 1
		else:
			word_dic[word] = 1
	reverse = {}
	for key in word_dic:
		reverse[word_dic[key]] = key
	times = max(reverse)
	word = reverse[times]
	return times, word

if __name__ == '__main__':
	txt = read_file(raw_input('input the txt: '))
	times, word = get_frequent_word(get_all_words(txt))
	print word , ':', times
	