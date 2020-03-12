import pytesseract
import cv2
img = cv2.imread('img/YOUR_FILE_NAME.EXTENSION')
text = pytesseract.image_to_string(img)
print(text)
f = open("sample.txt", "a")
f.write(text)
f.close()
