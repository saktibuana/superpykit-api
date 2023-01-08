# Importing Library
from PIL import Image, ImageEnhance
from sys import argv
import numpy as np
import re #regex

# List of colors
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
purple = (142, 68, 173)

# this module should only be receiving inline string not a paragraph. try to return the string first.
def mengubahsebaristulisan(tulisan=None):
    print(tulisan)