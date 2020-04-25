# coding=UTF-8

from setuptools import setup

setup(
    name='autotasks',
    version='1.0.3',
    author='Marcelo Horita',
    author_email='datazeus.tecnologia@gmail.com.br',
    packages=['autotasks'],
    description='Pacote de automação de processos',
    long_description='Pacote que ajuda automatizar processos web, sys, rpa, vba, msg e pdf',
    url='https://github.com/mfhorita',
    license='GNU',
    keywords='autotasks vba rpa msg pdf web scrapy sys',
    classifiers=[
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Scientific/Engineering :: Physics'
    ],
    install_requires=[
        'PyAutoGUI==0.9.48',
        'beautifulsoup4==4.8.1',
        'selenium==3.7.0',
        'pytesseract==0.3.0',
        'psutil==5.7.0',
        'pywin32>=223',
        'PyPDF2==1.26.0'
    ]
)
