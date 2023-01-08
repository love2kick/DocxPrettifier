import zipfile
import os
import shutil
from unpack import unload_docxml
from xsltrans import XsltProc as xp


class DocxContentSwapper(object):

    def __init__(self, target):
        if not target.endswith('.docx'):
            self.target = target + '.docx'
        else:
            self.target = target
        self.unzip(self.target)
        self.doc_swap()
        with zipfile.ZipFile(f'NEW_{self.target}', 'w', zipfile.ZIP_DEFLATED) as zipf:
            self.rezip('template/', zipf)
        self.cleanup()
        unload_docxml(f'NEW_{self.target}')

    @staticmethod
    def unzip(filepath):
        if os.path.exists('temp') is False:
            os.mkdir('temp')
        with zipfile.ZipFile(filepath, 'r') as target:
            target.extractall('temp')

    @staticmethod
    def doc_swap():
        tempdocpath = 'temp/word/document.xml'
        prettydocpath = 'template/word/document.xml'
        xp(tempdocpath).transform(prettydocpath)
        shutil.copyfile(prettydocpath, tempdocpath)

    @staticmethod
    def rezip(path, target):
        rootdir = os.path.basename(path)
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                parentpath = os.path.relpath(filepath, path)
                arcname = os.path.join(rootdir, parentpath)
                target.write(filepath, arcname=arcname)

    @staticmethod
    def cleanup():
        prettydocpath = 'template/word/document.xml'
        temppath = 'temp'
        try:
            os.remove(prettydocpath)
            shutil.rmtree(temppath)
        except OSError as e:
            print("Error: %s" % e.strerror)


if __name__ == '__main__':
    DocxContentSwapper("SampleTaxes.docx")
