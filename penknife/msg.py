from pyautogui import password, confirm, alert, prompt


def credencial(mask='*', timeout=None):
    import getpass
    username = getpass.getuser()
    return password(text=username, title="Informe sua senha:", mask=mask, timeout=timeout)


def input(text='', title='', default='', root=None, timeout=None):
    result = prompt(text=text, title=title, default=default, root=root, timeout=timeout)
    return result
