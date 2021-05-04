from win32com import client as vba

# Constantes do Word

wdNewBlankDocument = 0
wdExtend = 1
wdCharacter = 1
wdWord = 2
wdLine = 5
wdStory = 6

# Constantes do Excel

xlExcel12 = 50
xlOpenXMLWorkbook = 51
xlOpenXMLWorkbookMacroEnabled = 52
xlExcel8 = 56
xlCSVUTF8 = 62

# Funções do Word


def getNewWordApplication(visible=False):
    import platform
    if platform.system() == 'Windows':
        word = vba.DispatchEx('Word.Application')
        word.Visible = visible
        return word
    else:
        print(ValueError('Not implemented for other platforms than Windows.'))


def openWordDocument(word_filename=None, visible=False):
    import platform
    if platform.system() == 'Windows':
        word = vba.DispatchEx('Word.Application')
        word.Visible = visible
        word_document = word.Documents.Open(word_filename)
        return word, word_document
    else:
        print(ValueError('Not implemented for other platforms than Windows.'))


def convertWordToPDF(word_filename=None, pdf_filename=None):
    import platform
    if platform.system() == 'Windows':
        word = vba.DispatchEx('Word.Application')
        word_document = word.Documents.Open(word_filename)
        word_document.SaveAs(pdf_filename, FileFormat=17)
        word_document.Close()
    else:
        print(ValueError('Not implemented for other platforms than Windows.'))


# Funções do Excel


def getNewExcelApplication(visible=False):
    import platform
    if platform.system() == 'Windows':
        xl = vba.DispatchEx('Excel.Application')
        xl.Visible = visible
        return xl
    else:
        print(ValueError('Not implemented for other platforms than Windows.'))


def openExcelWorkbook(excel_filename=None, visible=False):
    import platform
    if platform.system() == 'Windows':
        xl = vba.DispatchEx('Excel.Application')
        xl.Visible = visible
        xl_plan = xl.Workbooks.Open(excel_filename)
        return xl, xl_plan
    else:
        print(ValueError('Not implemented for other platforms than Windows.'))
