## Utils
This directory contains utility functions

### preprocess
This module takes in the path of an image and applies 5x5 Gaussian filter to smoothen it an binarizes it.
Returns the inverted binarized and smoothened image.

### loadData
This module take xml file paths that contain labels and returns data dictionary({image_path:label}),vocab,image_paths_list to be used by model.  
This module has 2 functions. `loadData_word` to use words dataset and `load` to use lines dataset.