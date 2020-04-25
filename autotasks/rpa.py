from time import sleep                                                                                  # Delay
from pyautogui import press, hotkey, typewrite                                                          # Keyboard

# moveRel: Moves the mouse an x- and y- distance relative to its current pixel position.
# dragTo: Drag the mouse from its current position to a entered x-y position, while holding a specified button.
from pyautogui import position, mouseUp, mouseDown, moveTo, moveRel, vscroll, hscroll, dragTo, dragRel  # Mouse


def click(x=None, y=None, interval=0.0, duration=0.0, pause=0.0,
          button=['left', 'right', 'double'][0], screenshot=None):

    from pyautogui import leftClick, rightClick, doubleClick

    if button == 'right':
        rightClick(x=x, y=y, interval=interval, duration=duration, pause=pause, logScreenshot=screenshot)
    elif button == 'double':
        doubleClick(x=x, y=y, interval=interval, duration=duration, pause=pause, logScreenshot=screenshot)
    else:
        leftClick(x=x, y=y, interval=interval, duration=duration, pause=pause, logScreenshot=screenshot)


def clickOnImage(filename=None, button=['left', 'right', 'double'][0]):
    # Clica com o botao esquerdo, direito ou duplo click sobre uma imagem...
    from pyautogui import locateCenterOnScreen

    try:
        x, y = locateCenterOnScreen(filename)

        if button not in ('right', 'double'):
            click(x=x, y=y, button='left')
        else:
            click(x=x, y=y, button=button)

        return x, y

    except Exception:
        return None


def waitOnImage(filename=None, timeout=30, button=['left', 'right', 'double'][0]):
    # Aguarda ate que uma determinada imagem apareca na tela...
    from pyautogui import locateCenterOnScreen
    for _ in range(timeout):
        try:
            x, y = locateCenterOnScreen(filename)

            if button not in ('right', 'double'):
                click(x=x, y=y, button='left')
            else:
                click(x=x, y=y, button=button)

            return x, y

        except TypeError:
            sleep(1)


def carregaImage(img_file):
    from PIL import Image
    return Image.open(img_file)


def extractTextFromImage(img_file):
    from autotasks import sys
    if sys.system() == 'Windows':
        from pytesseract import pytesseract
        if sys.architecture() == 'x86':
            pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
        else:
            pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

    from PIL import Image
    from pytesseract import image_to_string
    return image_to_string(Image.open(img_file))


def typeInRunWindow(text=None):
    # Abre o "Run" do windows e escreve algo.
    if text:
        hotkey("win", "r")
        typewrite(text, 0.08)
        press("enter")
    return
