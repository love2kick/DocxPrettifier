<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">

    <xsl:template match="node()|@*">
        <xsl:copy>
            <xsl:apply-templates select="node()|@*"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="*[local-name()='p']">
        <xsl:element name="w:p">
            <xsl:element name="w:pPr">
                <w:spacing w:line="285" w:before="100" w:after="100"/>
                <w:b/>
            </xsl:element>
            <xsl:apply-templates select="*[local-name()!='pPr']"/>
        </xsl:element>
    </xsl:template>

    <xsl:template match="text()">
        <xsl:value-of select="."/>
    </xsl:template>

    <xsl:template name="insert_attr">
        <xsl:attribute name="test">
            <xsl:text>something</xsl:text>
        </xsl:attribute>
    </xsl:template>

</xsl:stylesheet>