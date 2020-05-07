import cv2 

''' Read image to applly changes '''
img = cv2.imread("RRR.png")

''' Convert image to black and white '''
def blackNwhite(img):
	return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	
''' Convert image to black and white Dots'''
def blackNwhitedots(img,blockSize,constant):
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	gray = cv2.medianBlur(gray,1)
	return cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,blockSize,constant)
	
''' Convert image to Cartoon Effect '''
def cartoon(img,blockSize,constant):
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	gray = cv2.medianBlur(gray,1)

	edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,blockSize,constant)

	color = cv2.bilateralFilter(img,9,250,250)
	return cv2.bitwise_and(color,color,mask=edges)	

''' Display Image '''
cv2.imshow("Black & White",blackNwhite(img))
cv2.imshow("Black & White Dots",blackNwhitedots(img,141,7))
cv2.imshow("Cartoon",cartoon(img,141,7))

cv2.waitKey(0)
cv2.destroyAllWindows()
