import cv2
import numpy as np

img = cv2.imread(r"E:\Download\GMw5Rz7XwAA34KI.jpg")
cv2.imshow('kucing',img)
cv2.waitKey(0)

print('ukurang citra warna : ',img.shape)
print('matriks dari citra warna pada baris 0 dan kolom 0 : ',img[0,0])

(blue,green,red) = cv2.split(img)
cv2.imshow('komponen biru',blue)

zeroMatrix = np.zeros(img.shape[:2],img.dtype)
m = zeroMatrix
blue = cv2.merge([blue,m,m])
