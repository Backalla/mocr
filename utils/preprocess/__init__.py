import cv2
import numpy as np
import os

def image_show(image_object,image_name="Image"):
    cv2.imshow(image_name, image_object)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def binarize(image_path):
    image_object = cv2.imread(image_path,0)
    # print image_object.shape
    # image_show(image_object)

    image_gaussian = cv2.GaussianBlur(image_object,(5,5),0)
    # image_show(image_gaussian,"Gaussian blurred")
    (thresh,im_bw_gaussian) = cv2.threshold(image_gaussian, 128, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    (thresh, im_bw) = cv2.threshold(image_object, 128, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    # print thresh
    # image_show(im_bw,"Binary")
    # image_show(im_bw_gaussian,"Binary Gaussian")
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    im_sharp = cv2.filter2D(im_bw, -1, kernel)
    # image_show(im_sharp,"Sharpened")
    return im_bw_gaussian

def save_image(image_path,image_obj):
    image_dirname = os.path.dirname(image_path)
    if not os.path.exists(image_dirname):
        os.makedirs(image_dirname)
    cv2.imwrite(image_path, image_obj)


if __name__ == '__main__':
    binarize("../../data/words/words/a01/a01-000u/a01-000u-00-03.png")