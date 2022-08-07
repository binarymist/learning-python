# -*- coding: utf-8 -*-

import os
import sys
# Doc: https://stackoverflow.com/questions/39134718/how-to-add-a-package-to-sys-path-for-testing
# The next uncommented line is the same as doing:
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname('.context.py'), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sample

