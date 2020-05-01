## Autotasks - Automatizador de tarefas:

### from autotasks import msg       # MsgBox tasks

	from autotasks.msg import alert

	from autotasks.msg import prompt

	from autotasks.msg import confirm

	from autotasks.msg import password

	def credencial(mask='*', timeout=None):
	    ''' Os dois primeiros argumentos são os PDFs que precisam ser mesclados, inseridos como um caminho. As páginas do pdf2 serão adicionadas ao pdf2. O PDF mesclado recebe um novo caminho especificado pelo terceiro argumento. '''

	def input(text='', title='', default='', root=None, timeout=None):
	    ''' Essa função extrai todo o texto de uma determinada página e o retorna como uma string. O pdf precisa ser inserido como um caminho. Preste atenção que a página inserida precisa ser maior que 0. '''

### from autotasks import pdf       # PDF tasks
	
	def mergePDF(pdf1, pdf2, merged_path):
	
	def extractTextFromPDFPage(pdf_file, txt_file=None, bgn_page=1, end_page=1):

### from autotasks import rpa       # Robotics tasks
	
	from autotasks.rpa import sleep

	from autotasks.rpa import press
	from autotasks.rpa import hotkey
	from autotasks.rpa import typewrite

	from autotasks.rpa import position
	from autotasks.rpa import mouseUp
	from autotasks.rpa import mouseDown
	from autotasks.rpa import moveTo
	from autotasks.rpa import moveRel
	from autotasks.rpa import vscroll
	from autotasks.rpa import hscroll
	from autotasks.rpa import dragTo
	from autotasks.rpa import dragRel

	def click(x=None, y=None, clicks=1, interval=0.0, button=['left', 'right', 'double'][0],
          duration=0.0, pause=0.0, logScreenshot=None):
    
    def clickOnImage(filename=None, button=['left', 'right', 'double'][0]):
	    ''' Clica com o botao esquerdo, direito ou duplo click sobre uma imagem... '''

	def waitOnImage(filename=None, timeout=30, button=['left', 'right', 'double'][0]):
    	''' Aguarda ate que uma determinada imagem apareca na tela... '''	
	def carregaImage(img_file):

	def extractTextFromImage(img_file):

	def typeInRunWindow(text=None):
	    ''' Abre o "Run" do windows e escreve algo. '''


### from autotasks import web       # Web tasks

	from autotasks.web import re_search

	def getSoupHtmlParser(url):
	    ''' Retorna o Soup html parser do BeautifulSoup atraves do request de um site '''

	def getChromeBrowser(url=False, ignore_images=False):  # , headless=False):
	    '''
		-----------
	        Abre o browser Chrome em um instancia Selenium.
		-----------
	        Argumentos:
	            ignore_images (bool): nao abre imagens
	            headless (bool): executa sem janela
	        Retorno:
	            webdriver: Selenium Webdriver
	        Exemplo:
	            browser = ChromeBrowser(ignore_images=True)
	            browser.get('https://github.com')
		-----------
	    '''

	def chromeRunning():
    	''' Retorna True quando o Chrome esta executanto. '''


### from autotasks import sys       # System tasks

	from autotasks.sys import sleep

	from autotasks.sys import ip_externo
	from autotasks.sys import username
	from autotasks.sys import architecture
	from autotasks.sys import hostname
	from autotasks.sys import system

	from autotasks.sys import getcwd
	from autotasks.sys import startfile
	from autotasks.sys import folderSelect
	from autotasks.sys import folderCreate
	from autotasks.sys import folderRemove
	from autotasks.sys import folderRename
	from autotasks.sys import fileExist
	from autotasks.sys import folderExist
	from autotasks.sys import folderZip
	from autotasks.sys import folderUnzip

	def processRunning(name):
	    ''' Checks if given process name (name) is currently running on the system. Returns True or False. '''

	def listRunningProcesses():
	    ''' Returns a list with all names of unique processes currently running on the system. '''

	def waitForFile(path):
    	''' Wait until a file with the entered path exists. '''

### from autotasks import vba       # Excel e Word tasks
	
	''' Constantes e funções do Word -'''

	wdNewBlankDocument = 0
	wdExtend = 1
	wdCharacter = 1
	wdWord = 2
	wdLine = 5
	wdStory = 6

	def getNewWordApplication(visible=False):

	def openWordDocument(word_filename=None, visible=False):

	def convertWordToPDF(word_filename=None, pdf_filename=None):

	''' Constantes e funções do Excel -'''

	xlExcel12 = 50
	xlOpenXMLWorkbook = 51
	xlOpenXMLWorkbookMacroEnabled = 52
	xlExcel8 = 56
	xlCSVUTF8 = 62

	def getNewExcelApplication(visible=False):

	def openExcelWorkbook(excel_filename=None, visible=False):
