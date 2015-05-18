# coding = utf-8

import urllib2
import codecs
from lxml import etree

def get_web_page(url):
	page = urllib2.urlopen(url)
	content = page.read()
	return content.decode('utf-8')

def get_text(content, rule):
	tree = etree.HTML(content)
	return tree.xpath(rule)

if __name__ == '__main__':
	url = 'http://www.baidu.com'
	content = get_web_page(url)
	text_list = get_text(content, '//div[@id="wrapper"]//text()')
	for t in text_list:
		print t
	
