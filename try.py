from utils import preprocess
import pickle
import os

data_dict = pickle.load(open("pickles/data_dict",'r'))
images = [(key,data_dict[key]) for key in data_dict.keys()]
new_data_dict = {}
for image_path,label in images:
    # preprocess.binarize(image_path)
    old_path = image_path.split('/')
    new_path = old_path
    new_path[2] = "processed_lines"
    new_path = '/'.join(new_path)
    print new_path
    try:
        preprocess.save_image(new_path,preprocess.binarize(image_path))
        new_data_dict[new_path] = label
    except:
        print new_path, "not found"
pickle.dump(new_data_dict,open('data_dict','wb'))