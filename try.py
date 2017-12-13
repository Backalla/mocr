from utils import preprocess
import pickle
import os

data_dict = pickle.load(open("pickles/data_dict",'r'))
images = [(key,data_dict[key]) for key in data_dict.keys()]
for image_path,label in images:
    # preprocess.binarize(image_path)
    old_path = image_path.split('/')
    new_path = old_path
    new_path[2] = "processed_words"
    new_path = '/'.join(new_path)
    print new_path
    try:
        preprocess.save_image(new_path,preprocess.binarize(image_path))
    except:
        print new_path, "not found"