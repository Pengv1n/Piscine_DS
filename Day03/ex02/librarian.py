#!/bin/python3

import os
import sys

try:
    if os.environ['VIRTUAL_ENV'][-8:] == 'aregenia':
            os.system('pip3 install bs4 PyTest')
            os.system('pip freeze')
            os.system('pip freeze > requirements.txt')
except KeyError:
    print('Don\'t find environment or env not right')
    sys.exit(1)
