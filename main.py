import zipfile
import os


def unzip(filepath):
    if os.path.exists('Sample') is False or os.path.exists('Sample/temp') is False:
        os.mkdir('Sample')
        os.mkdir('Sample/temp')
    with zipfile.ZipFile(filepath, 'r') as target:
        target.extractall('Sample/temp')


def rezip(path, target):
    rootdir = os.path.basename(path)

    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            parentpath = os.path.relpath(filepath, path)
            arcname = os.path.join(rootdir, parentpath)
            target.write(filepath, arcname)


with zipfile.ZipFile('Target.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    rezip('Sample/temp', zipf)
