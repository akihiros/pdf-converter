from pathlib import Path
import PyPDF2

# フォルダ内のPDFファイル一覧
pdf_dir = Path("D:\eBook")
pdf_files = sorted(pdf_dir.glob("*.pdf"))

print('以下の全てのpdfが結合されます。')
[print(i) for i in pdf_files]

val = input('ok? y or n: ')
if val != 'y':
    print('プログラムを終了します。')
    exit()

# １つのPDFファイルにまとめる
pdf_writer = PyPDF2.PdfFileWriter()
for pdf_file in pdf_files:
    pdf_reader = PyPDF2.PdfFileReader(str(pdf_file))
    if not pdf_reader.isEncrypted:
        for i in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(i))
    else:
        print('pdfが暗号化されています。')
        exit()

# 保存ファイル名
merged_file = pdf_files[0].stem + "-" + pdf_files[-1].stem + ".pdf"

# 保存
with open(merged_file, "wb") as f:
    pdf_writer.write(f)

print('正常に保存されました：', merged_file)