# !/usr/bin/python
import os


def to_printer(file):
    base = 'lpr -P HP_Officejet_Pro_8610 '
    os.system(base + file)

to_printer("geckodriver.log")