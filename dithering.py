import cv2

img = cv2.imread('pp.jpg',0)

width, height = img.shape

reducefactor = 3

img = cv2.resize(img,(round(height/reducefactor),round(width/reducefactor)))

width, height = img.shape

nimg = img.astype('float')/255

for y in range(0,height-1):
	for x in range(1,width-1):
		oldpixel = nimg[x,y]
		newpixel = round(oldpixel)
		nimg[x,y] = newpixel
		quant_error = oldpixel - newpixel
		nimg[x + 1,y] = nimg[x + 1,y] + quant_error * 7 / 16
		nimg[x - 1,y + 1] = nimg[x - 1,y + 1] + quant_error * 3 / 16
		nimg[x,y + 1] = nimg[x,y + 1] + quant_error * 5 / 16
		nimg[x + 1,y + 1] = nimg[x + 1,y + 1] + quant_error * 1 / 16

nimg = nimg*255
nimg = cv2.resize(nimg,(round(height*reducefactor),round(width*reducefactor)), interpolation = cv2.INTER_NEAREST)

cv2.imwrite('dithered.png',nimg)
