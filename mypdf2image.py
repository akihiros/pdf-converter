from pdf2image import convert_from_path
import glob
import os
import sys


help = ''' ----------------------------------------
How to use

python mypdf2image.py input_path output_path
 ... ex: python mypdf2image.py pdf/test.pdf jpg/test
--------------------------------------------
'''

print(help)

# if no jpg and pdf folders, create them
os.makedirs('jpg', exist_ok=True)
os.makedirs('pdf', exist_ok=True)

# Specify the path
args = sys.argv
if len(args) > 1:
    if len(args) > 2:
        output = args[2]
        args.pop(-1)
    args.pop(0)

# If no path is specified, use the default path
files = args if os.path.exists(args[0]) else glob.glob('pdf/*.pdf')

# pdf to image
for path in files:
    images = convert_from_path(path)

    for i, image in enumerate(images, 1):
        if 'output' in locals():
            image.save(output + '_{}.jpg'.format(i), 'jpeg')
        else:
            image.save('jpg/{}_{}.jpg'.format(path.replace('pdf/', '').replace('.pdf', ''), i).replace('pdf\\', ''), 'jpeg')

    print('{} complete!'.format(path))
