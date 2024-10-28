import cv2
import os
import pytesseract
from PIL import Image
def cv2_show(img,name = 'test'):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('python\\opencv\\test.png')#路径自己修改
if img.shape[0]>2048 or img.shape[1]>2048:
    x = int(img.shape[0])
    y  =int(img.shape[1])
    img  =cv2.resize(img,(x,y))
#预处理
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#灰度
gray_img = cv2.GaussianBlur(gray_img,(3,3),0)#高斯滤波
edge = cv2.Canny(img,75,200)#边缘计算
#cv2_show(edge)

cnts= cv2.findContours(edge.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[0]
cnts = sorted(cnts,key = cv2.contourArea,reverse=True)

for contour in cnts:
    length = cv2.arcLength(contour,True)
    approx = cv2.approxPolyDP(contour,0.02*length,True)
    if len(approx) == 4:
        scr = approx
        break

if scr is not None and len(scr) == 4:  # 确保 scr 不为空且只有 4 个点  
    miny = min(scr[0][0][1], scr[1][0][1], scr[2][0][1], scr[3][0][1])  
    maxy = max(scr[0][0][1], scr[1][0][1], scr[2][0][1], scr[3][0][1])  
    minx = min(scr[0][0][0], scr[1][0][0], scr[2][0][0], scr[3][0][0])  
    maxx = max(scr[0][0][0], scr[1][0][0], scr[2][0][0], scr[3][0][0])  
    img =img[miny:maxy,minx:maxx]
else:  
    print("未找到有效的四边形轮廓")

cv2.imwrite('python\\opencv\\out.jpg',img)


 
