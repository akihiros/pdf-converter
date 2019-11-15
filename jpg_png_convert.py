from PIL import Image
import os

path = "../clone-code/pytorch_advanced_origin/2_objectdetection/data/original_2/JPEGImages/"
files = os.listdir(path)
print(len(files))

for i in range(len(files)):
    print(files[i])
    img = Image.open(path + files[i])
    name = path + files[i]
    name = name.replace('.jpg', '')
    img.save(name + '.png', 'png')