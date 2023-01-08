<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">

    <xsl:template match="w:p">
        <xsl:element name="w:p">
            <xsl:copy-of select="./*[local-name()='pPr']" copy-namespaces="yes"/>
            <xsl:apply-templates select="node()[not(self::w:pPr)]|@*"/>
        </xsl:element>
    </xsl:template>

    <xsl:template match="w:drawing">
        <xsl:variable name="rId" select="@r:id"/>
        <xsl:variable name="imagePath" select="//*[@r:id=$rId]/@Target"/>
        <img src="{$imagePath}"/>
    </xsl:template>

    <xsl:template match="w:r">
        <xsl:copy>
            <xsl:apply-templates select="node()|@*"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="w:b">
        <xsl:element name="w:b">
            <xsl:apply-templates select="node()|@*"/>
        </xsl:element>
    </xsl:template>

    <xsl:template match="w:i">
        <xsl:element name="w:i">
            <xsl:apply-templates select="node()|@*"/>
        </xsl:element>
    </xsl:template>

    <xsl:template match="w:u">
        <xsl:element name="w:u">
            <xsl:apply-templates select="node()|@*"/>
        </xsl:element>
    </xsl:template>

    <xsl:template match="w:p[not(node())]">
        <!-- Do nothing -->
    </xsl:template>

    <xsl:template match="w:tbl">
        <w:tbl>
            <w:tblPr>
                <w:tblBorders>
                    <w:top w:val="single" w:sz="4" w:space="0" w:color="000000"/>
                    <w:left w:val="single" w:sz="4" w:space="0" w:color="000000"/>
                    <w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000"/>
                    <w:right w:val="single" w:sz="4" w:space="0" w:color="000000"/>
                    <w:insideH w:val="single" w:sz="4" w:space="0" w:color="000000"/>
                    <w:insideV w:val="single" w:sz="4" w:space="0" w:color="000000"/>
                </w:tblBorders>
            </w:tblPr>
            <xsl:apply-templates select="node()|@*"/>
        </w:tbl>
    </xsl:template>

    <xsl:template match="node()">
        <xsl:copy>
            <xsl:apply-templates select="@*"/>
            <xsl:apply-templates select="node()[not(self::w:pPr)]"/>
        </xsl:copy>
    </xsl:template>

</xsl:stylesheet>