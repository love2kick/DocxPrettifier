import zipfile
import os


def unzip(filepath):
    if os.path.exists('Sample') == False or os.path.exists('Sample/temp') == False:
        os.mkdir('Sample')
        os.mkdir('Sample/temp')
    with zipfile.ZipFile(filepath, 'r') as target:
        target.extractall('Sample/temp')

def rezip():
    for root, dirs, files in os.walk('Sample/temp'):

unzip('Sample/sample1.docx')
