import requests
from bs4 import BeautifulSoup
import os
import time

url = "http://openaccess.thecvf.com/CVPR2018.py"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
path = "./cvpr2018"


def save_pdf(filename, pdf):
    with open(filename, "wb") as f: 
        f.write(pdf)


def create_filepath(url):
    return path + url.split("/")[-1]


def download_pdf(pdf_url):
    res = requests.get(pdf_url)
    return res.content


td = soup.find_all("td", class_="link")

if not os.path.isdir(path):
    os.mkdir(path)

for link in td:
    report_url = link.a.get('href')
    pdf = download_pdf(report_url)
    filename = create_filepath(report_url)
    save_pdf(filename, pdf)
    time.sleep(2)