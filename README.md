## Penknife

### Pacote que ajuda automatizar processos web, sys, rpa, vba, msg e pdf

#### Baixar webdriver chrome em https://chromedriver.chromium.org/downloads e salvar em ..\Lib\site-packages\penknife\bin\win32

## Automatizador de tarefas:

### from penknife import msg       # MsgBox tasks

	from penknife.msg import alert

	from penknife.msg import prompt

	from penknife.msg import confirm

	from penknife.msg import password

	def credencial(mask='*', timeout=None):
	    ''' Os dois primeiros argumentos são os PDFs que precisam ser mesclados, inseridos como um caminho. As páginas do pdf2 serão adicionadas ao pdf2. O PDF mesclado recebe um novo caminho especificado pelo terceiro argumento. '''

	def input(text='', title='', default='', root=None, timeout=None):
	    ''' Essa função extrai todo o texto de uma determinada página e o retorna como uma string. O pdf precisa ser inserido como um caminho. Preste atenção que a página inserida precisa ser maior que 0. '''

### from penknife import pdf       # PDF tasks
	
	def mergePDF(pdf1, pdf2, merged_path):
	
	def extractTextFromPDFPage(pdf_file, txt_file=None, bgn_page=1, end_page=1):

### from penknife import rpa       # Robotics tasks
	
	from penknife.rpa import sleep

	from penknife.rpa import press
	from penknife.rpa import hotkey
	from penknife.rpa import typewrite

	from penknife.rpa import position
	from penknife.rpa import mouseUp
	from penknife.rpa import mouseDown
	from penknife.rpa import moveTo
	from penknife.rpa import moveRel
	from penknife.rpa import vscroll
	from penknife.rpa import hscroll
	from penknife.rpa import dragTo
	from penknife.rpa import dragRel

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


### from penknife import web       # Web tasks

	from penknife.web import re_search

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


### from penknife import sys       # System tasks

	from penknife.sys import sleep

	from penknife.sys import ip_externo
	from penknife.sys import username
	from penknife.sys import architecture
	from penknife.sys import hostname
	from penknife.sys import system

	from penknife.sys import getcwd
	from penknife.sys import startfile
	from penknife.sys import folderSelect
	from penknife.sys import folderCreate
	from penknife.sys import folderRemove
	from penknife.sys import folderRename
	from penknife.sys import fileExist
	from penknife.sys import folderExist
	from penknife.sys import folderZip
	from penknife.sys import folderUnzip

	def processRunning(name):
	    ''' Checks if given process name (name) is currently running on the system. Returns True or False. '''

	def listRunningProcesses():
	    ''' Returns a list with all names of unique processes currently running on the system. '''

	def waitForFile(path):
    	''' Wait until a file with the entered path exists. '''

### from penknife import vba       # Excel e Word tasks
	
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
