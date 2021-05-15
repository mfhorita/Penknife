# coding=UTF-8

from setuptools import setup

setup(
    name='penknife',
    version='2021.05.09',
    author='Marcelo Horita',
    author_email='datazeus.tecnologia@gmail.com.br',
    packages=['penknife'],
    description='Pacote de automação de processos',
    long_description='Pacote que ajuda automatizar processos web, sys, rpa, vba, msg e pdf',
    url='https://github.com/mfhorita',
    license='GNU',
    keywords='penknife autotasks vba rpa msg pdf web scrapy sys',
    classifiers=[
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Scientific/Engineering :: Physics'
    ],
    install_requires=[
        'PyAutoGUI>=0.9.47',
        'beautifulsoup4>=4.8.0',
        'selenium>=3.7.0',
        'pytesseract>=0.3.0',
        'psutil>=5.7.0',
        'pywin32>=223',
        'PyPDF2>=1.26.0'
    ]
)
