from re import search as re_search      # Regex


def getSoupHtmlParser(url):
    # Retorna o Soup html parser do BeautifulSoup atraves do request de um site
    import requests
    from bs4 import BeautifulSoup
    r = requests.get(url)
    return BeautifulSoup(r.content, "html.parser")


def getChromeBrowser(url=False, ignore_images=False):  # , headless=False):
    # ---------------------------------------------------------------
    #     Abre o browser Chrome em um instancia Selenium.
    # ---------------------------------------------------------------
    #     Argumentos:
    #         ignore_images (bool): nao abre imagens
    #         headless (bool): executa sem janela
    #     Retorno:
    #         webdriver: Selenium Webdriver
    #     Exemplo:
    #         browser = ChromeBrowser(ignore_images=True)
    #         browser.get('https://github.com')
    # ---------------------------------------------------------------

    import os
    import platform

    if platform.system() == 'Linux':
        chromedriver_path = '\\bin\\webdriver\\linux64\\chromedriver'
    elif platform.system() == 'Windows':
        chromedriver_path = '\\bin\\win32\\chromedriver.exe'
    else:
        chromedriver_path = '\\bin\\mac64\\chromedriver.exe'

    from selenium.webdriver import Chrome, ChromeOptions

    chrome_options = ChromeOptions()

    # if headless:
    #    chrome_options.add_argument("--headless")

    if ignore_images:
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)

    s_path = os.path.abspath(__file__)
    s_file = s_path[:s_path.rfind("\\") + 1]
    browser = Chrome(s_file + chromedriver_path, chrome_options=chrome_options)

    if url:
        browser.get(url)

    return browser


def chromeRunning():
    # Retorna True quando o Chrome esta executanto.
    import psutil
    for p in psutil.process_iter():
        if "chrome.exe" in p.name():
            return True
    return False
