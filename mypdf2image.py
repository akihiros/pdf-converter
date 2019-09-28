from pdf2image import convert_from_path
import glob

i = 0
files = glob.glob('pdf/*.pdf')
for path in files:
    images = convert_from_path(path)

    for image in images:
        image.save('jpg/sample_{}.jpg'.format(i), 'jpeg')
        i += 1

    print('{}が画像に変換されました。'.format(path))