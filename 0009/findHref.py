# coding = utf-8

import urllib2
from lxml import etree

def get_web_page(url):
	page = urllib2.urlopen(url)
	content = page.read().decode('utf-8')
	return content

def get_hyperlink(content, rule):
	tree = etree.HTML(content)
	return tree.xpath(rule)

if __name__ == '__main__':
	url = 'http://www.baidu.com'
	rule = '//@src'
	content = get_web_page(url)
	hyperlink_list = get_hyperlink(content, rule)
	for link in hyperlink_list:
		print link
