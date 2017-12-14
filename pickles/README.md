## Pickle files description

### data_dict
Contains the dictionary with \
keys = relative paths of preprocessed binarized images of lines\
values = Labels of those lines. ie text written in the image

##### Sample
```
('data/lines/processed_lines/a04/a04-099/a04-099-04.png', 'believes : " It is very questionable whether ')
('data/lines/processed_lines/c04/c04-008/c04-008-00.png', 'In his first Hollywood picture , " Let \'s Make Love , " he ')
('data/lines/processed_lines/g06/g06-011e/g06-011e-07.png', 'the soldier - a favourable change in my eye , particularly ')
('data/lines/processed_lines/d01/d01-118/d01-118-03.png', 'a roll or a codex . Rolls were prepared for ')
('data/lines/processed_lines/m06/m06-048/m06-048-02.png', "fleshless jaw said , ' The grub of the tigerfly thinks ")
('data/lines/processed_lines/l01/l01-129/l01-129-03.png', 'ever heard . " I \'m going to get myself ')
('data/lines/processed_lines/a06/a06-025/a06-025-06.png', 'and " unwarranted " interference . " But it ')
('data/lines/processed_lines/h07/h07-084/h07-084-08.png', 'half of whom are known to have been on local ')
('data/lines/processed_lines/a02/a02-090/a02-090-05.png', 'would make the Mau Mau in Kenya " seem like a ')
('data/lines/processed_lines/g06/g06-042o/g06-042o-00.png', 'Nor is this to be wondered at , for even ')

```


### image_files_list
Contains a list of relative paths of preprocessed binarized images of lines

##### Sample
```
data/lines/lines/g03/g03-052/g03-052-00.png
data/lines/lines/g03/g03-052/g03-052-01.png
data/lines/lines/g03/g03-052/g03-052-02.png
data/lines/lines/g03/g03-052/g03-052-03.png
data/lines/lines/g03/g03-052/g03-052-04.png
data/lines/lines/g03/g03-052/g03-052-05.png
data/lines/lines/g03/g03-052/g03-052-06.png
data/lines/lines/g03/g03-052/g03-052-07.png
data/lines/lines/g03/g03-052/g03-052-08.png
data/lines/lines/g03/g03-052/g03-052-09.png
``` 

### vocab
Contains the set of characters encountered in the dataset. ie char vocabulary

#### Sample
```
set(['!', ' ', '#', '"', "'", '&', ')', '(', '+', '*', '-', ',', '/', '.', '1', '0', '3',
'2', '5', '4', '7', '6', '9', '8', ';', ':', '?', 'A', 'C', 'B', 'E', 'D', 'G', 'F', 'I',
'H', 'K', 'J', 'M', 'L', 'O', 'N', 'Q', 'P', 'S', 'R', 'U', 'T', 'W', 'V', 'Y', 'X', 'Z',
'a', 'c', 'b', 'e', 'd', 'g', 'f', 'i', 'h', 'k', 'j', 'm', 'l', 'o', 'n', 'q', 'p', 's',
'r', 'u', 't', 'w', 'v', 'y', 'x', 'z'])
```