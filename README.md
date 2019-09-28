# PDF to Text

PDFからtxtファイルを生成するサンプルコード。

- pdfminer：pdf→text
- pdf2image：pdf→image
- OCR：image→text

## Tutorial

Python 3.6.9 :: Anaconda, Inc.

### pdfminer

[pdfminer/pdfminer.six: Python PDF Parser -- fork with Python 2+3 support using six](https://github.com/pdfminer/pdfminer.six)

- install 
    - `pip install pdfminer.six`
    - `pip install chardet`

- run test code
  - `python pdf2txt.py simple1.pdf`

pdf2txt.pyのpathは環境によって異なるので注意。Anacondaであれば`C:\Users\ユーザー名\Anaconda3\envs\環境名\Scripts/pdf2txt.py`等。

used [this](https://github.com/pdfminer/pdfminer.six/blob/master/samples/simple1.pdf) in the sample.

If successful, a string is displayed on the terminal.

```
Hello
Hello
Hello
Hello

World

Hello

World

H e l l o

W o r l d

H e l l o

W o r l d
```

- run
  - `python mypdf2txt.py test.pdf test.txt`
  - You need to prepare the pdf file you want to convert.

### pdf2image

[Belval/pdf2image: A python module that wraps the pdftoppm utility to convert PDF to PIL Image object](https://github.com/Belval/pdf2image)

- install
  - conda install pillow / pip install pillow
  - conda install -c conda-forge poppler / [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/)
  - pip install pdf2image

- run
  - `python mypdf2image.py`
  - You need to prepare the pdf/*.pdf you want to convert.

### OCR

not yet.