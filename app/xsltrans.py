import lxml.etree as etree


class XsltProc:
    def __init__(self, xmlpath, xslpath="res/transform.xsl"):
        self.xmlpath = xmlpath
        self.xsltpath = xslpath

    def transform(self, doc_template):
        target = etree.parse(self.xmlpath)
        xsl = etree.parse(self.xsltpath)
        trans = etree.XSLT(xsl)
        newxml = trans(target)
        with open(doc_template, "wb") as nd:
            nd.write(newxml)
