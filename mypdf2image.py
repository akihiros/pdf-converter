from pdf2image import convert_from_path
import glob
import os
import sys


help = ''' ----------------------------------------
How to use

python mypdf2image.py input_path output_path
 ... ex: python mypdf2image.py pdf\test.pdf jpg\test

default
 ... input_path: pdf/*.pdf
 ... output_path: jpg
--------------------------------------------
'''

print(help)

# if no jpg and pdf folders, create them
os.makedirs('jpg', exist_ok=True)
os.makedirs('pdf', exist_ok=True)

files = glob.glob('pdf/*.pdf')

args = sys.argv
if len(args) >= 2: # input指定
    if len(args) >= 3: # output指定
        output = args[2]
        args.pop(-1)
    args.pop(0)
    files = args

print('デフォルトではpdfフォルダにある全てのpdfファイルをjpegに変換します。\n変換するファイル一覧：{}'.format(files))

# pdf to image
for path in files:
    images = convert_from_path(path)

    for i, image in enumerate(images, 1):
        # ファイルが1つ（指定）の場合、指定されたoutput path_連番.jpgで保存
        # ファイルが複数（デフォルト）の場合、pdf/元のファイル名_連番.jpgを保存
        if 'output' in locals():
            image.save(output + '_{}.jpg'.format(i), 'jpeg')
        else:
            image.save('jpg/{}_{}.jpg'.format(path.replace('pdf/', '').replace('.pdf', ''), i).replace('pdf\\', ''), 'jpeg')

    print('{} complete!'.format(path))