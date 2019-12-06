import os

path = "../clone-code/pytorch_advanced_origin/2_objectdetection/data/annotation-PascalVOC-export-fig/Annotations"

files = os.listdir(path)
print(len(files))
print(round(len(files)*0.5), round(len(files)*0.5))

path_train = '../clone-code/pytorch_advanced_origin/2_objectdetection/data/annotation-PascalVOC-export-fig/ImageSets/Main/train.txt'
path_val = '../clone-code/pytorch_advanced_origin/2_objectdetection/data/annotation-PascalVOC-export-fig/ImageSets/Main/val.txt'

with open(path_train, mode='w') as f:
    for i in range(round(len(files)*0.5)):
        f.write(files[i].replace('.xml', ''))
        f.write('\n')

with open(path_val, mode='w') as f:
    for i in range(round(len(files)*0.5), len(files)):
        f.write(files[i].replace('.xml', ''))
        f.write('\n')
