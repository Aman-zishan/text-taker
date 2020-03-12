import pytesseract
import cv2
img = cv2.imread('test.jpeg')
text = pytesseract.image_to_string(img)
print(text)
