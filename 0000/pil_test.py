# coding=utf-8


import ImageFont, Image, ImageDraw

import sys
import os
import time


def getImage():
	return raw_input('input the path of the image: ')

def getNumber():
	return (raw_input('input the content you want to display: '))

def union():
	path = getImage()
	number = getNumber()

	im = Image.open(path)
	width, tmp = im.size

	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype('msyh.tty', 12)
	#font_w, font_
	draw.text((width, 0), number, font = font, fill = '#ff0000')
	del draw

	#filename = time.strftime('%Y-%m-%d %X', time.localtime(time.time())) + '.jpg'
	filename = str(time.time()) + '.jpg'

	im.save(os.path.dirname(path) + os.sep + filename)
 
if __name__ == '__main__':
	union()