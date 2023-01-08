import zipfile



def unload_docxml(target):
    docpath = "word/document.xml"
    with zipfile.ZipFile(target, "r") as docx:
        with open("document.xml", "wb") as docfile:
            docfile.write(docx.read(docpath))
