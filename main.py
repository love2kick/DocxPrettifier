import zipfile
import os
import shutil


class DocxContentSwapper(object):
    def __init__(self, target):
        if not target.endswith('.docx'):
            self.target = target + '.docx'
        else:
            self.target = target
        self.unzip(self.target)
        self.doc_swap()
        with zipfile.ZipFile(f'NEW{self.target}', 'w', zipfile.ZIP_DEFLATED) as zipf:
            self.rezip('Template/', zipf)
        self.cleanup()

    @staticmethod
    def unzip(filepath):
        if os.path.exists('temp') is False:
            os.mkdir('temp')
        with zipfile.ZipFile(filepath, 'r') as target:
            target.extractall('temp')

    @staticmethod
    def doc_swap():
        tempdocpath = os.path.join(os.path.dirname(__file__), 'temp/word/document.xml')
        prettydocpath = os.path.join(os.path.dirname(__file__), 'Template/word/document.xml')
        shutil.copyfile(tempdocpath, prettydocpath)

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
        prettydocpath = os.path.join(os.path.dirname(__file__), 'Template/word/document.xml')
        temppath = os.path.join(os.path.dirname(__file__), 'temp')
        try:
            os.remove(prettydocpath)
            shutil.rmtree(temppath)
        except OSError as e:
            print("Error: %s" % e.strerror)


if __name__ == '__main__':
    DocxContentSwapper(input('Enter file name:'))
