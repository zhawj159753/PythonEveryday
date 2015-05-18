# coding = utf-8

import Image

def resize(path, x, y):
	im = Image.open(path)
	width, height = im.size
	if width/x > height/y:
		new_im = im.resize((x, y * x / width), Image.ANTIALIAS)
	else:
		new_im = im.resize((x * y / height, y), Image.ANTIALIAS)
	new_im.save('output.jpg', 'JPEG')

if __name__ == '__main__':
	path = 'input.jpg'
	resize(path, 100, 200)

