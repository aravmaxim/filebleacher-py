import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '../src'))

import bmp

def test_bmp_simple():
  with open('tests/bmp_files/simple_bmp.bmp', mode='rb') as file:
    fileContent = file.read()
    assert bmp.check_bmp(fileContent, {}) == True