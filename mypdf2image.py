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

# コマンドライン引数からパスを指定
# なければデフォルトの値を使用
args = sys.argv
if len(args) > 1:
    files = args
    if len(args) > 2:
        output = args[2]
        args.pop(-1)
    args.pop(0)
else:
    os.makedirs('jpg', exist_ok=True)  # jpgフォルダを作成
    os.makedirs('pdf', exist_ok=True)  # pdfフォルダを作成
    args = glob.glob('pdf/*.pdf')  # デフォルトのinput

# pdfを画像に変換
# 引数指定がなければデフォルトのoutputを使用
# 画像名は1から順に番号を振る形式
for path in args:
    images = convert_from_path(path)

    for i, image in enumerate(images, 1):
        if 'output' in locals():
            image.save(output + '_{}.jpg'.format(i), 'jpeg')
        else:
            image.save('jpg/sample_{}.jpg'.format(i), 'jpeg')

    print('{} complete!'.format(path))
