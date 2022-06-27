import numpy as np
import matplotlib.pyplot as plt
import cv2


def show_img(image):
    plt.imshow(image)
    plt.show()


img = cv2.imread('DATA/00-puppy.jpg')

# print(type(img))
# print(img.shape)

# normal RGB
# open cv BGR
# show_img(img)

# need convert BGR -> RGB
fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# plt.imshow(img_cvt)
# plt.show()

img_gray = cv2.imread('DATA/00-puppy.jpg', cv2.IMREAD_GRAYSCALE)
# print(img_gray.shape)
# plt.imshow(img_gray, cmap='gray')
# plt.show()

new_img = cv2.resize(fix_img, (1000, 400))
# show_img(new_img)

w_ratio = 0.5
h_ratio = 0.5

new_img = cv2.resize(fix_img, (0, 0), fix_img, w_ratio, h_ratio)
# show_img(new_img)

new_img = cv2.flip(fix_img, 0)
# show_img(new_img)

new_img = cv2.flip(fix_img, 1)  # -1
# show_img(new_img)

cv2.imwrite('new_img.jpg', fix_img)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
# ax.imshow(fix_img)

#############################################################################

while True:
    cv2.imshow('puppy', img)
    if cv2.waitKey() & 0xff == ord('q'):
        break


cv2.destroyAllWindows()