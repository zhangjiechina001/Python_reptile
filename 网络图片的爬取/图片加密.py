import cv2
import numpy as np
def img_screct(input_img,screct_img):
    mask1=0b11110000#宿主图像掩码
    mask2=0b11110000#加密图像掩码
    host=input_img#宿主数据
    screct=screct_img#加密数据
    host=np.bitwise_and(mask1,input_img)
    screct=np.bitwise_and(mask2,screct_img)
    screct=screct>>4
    res=host+screct
    return res

#解密图片
def img_decrypt(screct_img):
    mask=0b00001111
    res=np.bitwise_and(mask,screct_img)
    return res<<4


#宿主图片,小点的图片
input_img=cv2.imread('pics\\18681759_143805185000_2.jpg',cv2.IMREAD_ANYCOLOR)
w,h,c=input_img.shape
#加密图片,大点的图片
screct_img=cv2.imread('pics\\19570481.jpg',cv2.IMREAD_ANYCOLOR)
screct_img=screct_img[0:w,0:h,:]
w,h,channels=input_img.shape

res=img_screct(input_img,screct_img)
decrypt_img=img_decrypt(res)
cv2.imshow('img',res)
cv2.imshow('descrypt_img',decrypt_img)
# cv2.imshow('host_img',input_img)
# cv2.imshow('screct_img',screct_img)
cv2.waitKey()
