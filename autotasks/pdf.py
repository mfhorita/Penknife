import PyPDF2


def mergePDF(pdf1, pdf2, merged_path):

    # Os dois primeiros argumentos sao os PDFs que precisam ser mesclados, inseridos como um caminho. As paginas do
    # pdf2 serao adicionadas ao pdf2. O PDF mesclado recebe um novo caminho especificado pelo terceiro argumento.

    from PyPDF2 import PdfFileMerger

    pdfs = [str(pdf1), str(pdf2)]
    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write(merged_path)
    return


def extractTextFromPDFPage(pdf_file, txt_file=None, bgn_page=1, end_page=1):

    # Extrai todo o texto de uma determinada pagina e o retorna como uma string. O pdf precisa ser inserido
    # como um caminho. Preste atencao que a pagina inserida precisa ser maior que 0.

    import os
    if os.path.isfile(pdf_file):

        pdf_reader = PyPDF2.PdfFileReader(open(pdf_file, "rb"))

        bgn_page = max(bgn_page, 1)
        end_page = max(end_page, 1)

        if end_page > pdf_reader.numPages:
            end_page = pdf_reader.numPages

        if bgn_page > pdf_reader.numPages:
            bgn_page = pdf_reader.numPages
        elif bgn_page > end_page:
            bgn_page = end_page

        page_content = ''
        for i_page in range(bgn_page - 1, end_page):
            page = pdf_reader.getPage(i_page)
            page_content += page.extractText()

        with open(txt_file, 'w') as f:
            f.write(page_content.__str__())
        f.close()

        return page_content
