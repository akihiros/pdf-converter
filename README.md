# PDF to Text / PDF to Image / Image to Text

PDFからtxtファイルを生成する簡易サンプルコード。

- pdfminer：pdf→text
- pdf2image：pdf→image
- OCR：image→text

## How to use

Python 3.6.9 :: Anaconda, Inc.

### pdfminer

[pdfminer/pdfminer.six: Python PDF Parser -- fork with Python 2+3 support using six](https://github.com/pdfminer/pdfminer.six)

- Request 
    - `pip install pdfminer.six`
    - `pip install chardet`

- Run test code
  - `python pdf2txt.py simple1.pdf`

pdf2txt.pyのpathは環境によって異なるので注意。Anacondaであれば`C:\Users\ユーザー名\Anaconda3\envs\環境名\Scripts/pdf2txt.py`等。

used [this](https://github.com/pdfminer/pdfminer.six/blob/master/samples/simple1.pdf) in the sample.

- Run
  - `python mypdf2txt.py test.pdf test.txt`
  - 第一引数に変換したいpdfのパス、第二引数に変換後のテキストのパスを指定してください。

### pdf2image

[Belval/pdf2image: A python module that wraps the pdftoppm utility to convert PDF to PIL Image object](https://github.com/Belval/pdf2image)

- Request
  - conda install pillow / pip install pillow
  - conda install -c conda-forge poppler / [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/)
  - pip install pdf2image

- Run
  - `python mypdf2image.py`
  - デフォルトの入力パスと出力パスが使用されます。
  
- Option
  - `python mypdf2image.py pdf/test.pdf jpg/test`
  - 第1引数に変換したいpdfのパス、第二引数に変換後のパスを指定してください。変換後の画像は、指定した名前の後に1から順に番号が振られます（拡張子を付けないように注意）。
    - jpg/test_1.jpg, jpg/test_2.jpg, jpg/test_3.jpg ...

### OCR

そのうち