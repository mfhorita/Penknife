from time import sleep
from getpass import getuser as username

from platform import machine as architecture
from platform import node as hostname
from platform import system

from os import getcwd
from os import startfile
from os import chdir as folderSelect
from os import mkdir as folderCreate
from os import rmdir as folderRemove
from os import rename as folderRename
from os.path import isfile as fileExist
from os.path import isdir as folderExist
from shutil import make_archive as folderZip


def ip_externo(url=''):
    from autotasks import web
    soup = web.getSoupHtmlParser(url)
    rst_soup = soup.findAll('h3', {'class', 'm-0 font-weight-bold'})
    return web.re_search(r'[0-9]+.[0-9]+.[0-9]+.[0-9]+', rst_soup.__str__())[0]


def processRunning(name):
    # Checks if given process name (name) is currently running on the system. Returns True or False.
    if name:
        import psutil
        for p in psutil.process_iter():
            if name in p.name():
                return True
    return False


def listRunningProcesses():
    # Returns a list with all names of unique processes currently running on the system.
    process_list = []
    import psutil
    for p in psutil.process_iter():
        process_list.append(p.name())
    return set(process_list)


def folderUnzip(path, new_path=False):
    import os
    import zipfile
    if os.path.exists(path):
        zipp = zipfile.ZipFile(path)
        if not new_path:
            base_path = "\\".join(path.split("\\")[:-1])
            zipp.extractall(base_path)
        elif os.path.isdir(path):
            zipp.extractall(path)
        zipp.close()
    return


def waitForFile(path):
    # Wait until a file with the entered path exists.
    import os
    from time import sleep
    while not os.path.exists(path):
        sleep(1)
    return


def getUniqueKey128bits(length=36):
    # Universally unique identifier (UUID) is a 128-bit number used to identify information in computer systems.
    # This key can be considered as unique for there to be a one in a billion chance of duplication, 103 trillion
    # version 4 UUIDs must be generated. The general form is e.g. "123e4567-e89b-12d3-a456-4266554". The argument
    # specifies the length of the returned string. If it is omitted, the entire 128-bit UUID is returned.
    import uuid
    return str(uuid.uuid4())[:length]
