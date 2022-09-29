# CIS 521: R2D2 - Homework 0
import math
import os
import sys
import threading
from datetime import datetime
from typing import List, Tuple, Iterator, Dict, Any

import cv2
import numpy
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

# Color Dictionary
color_names_to_rgb = {
    'red': Color(255, 0, 0),
    'orange': Color(255, 165, 0),
    'yellow': Color(255, 255, 0),
    'green': Color(0, 128, 0),
    'blue': Color(0, 0, 255),
    'indigo': Color(75, 0, 130),
    'violet': Color(238, 130, 238),
    'purple': Color(128, 0, 128)
}


# 3. Dictionaries (RGB LED) [5 points]
def set_lights(droid: SpheroEduAPI, color: str, which_light='both'):
    """
    :param color: a string of English name or the hex value of the color
    :param which_light: 'front' - change front only,
                        'back' - change back only,
                        'both' - change front and back
    """
    # Turning on both lights of R2D2, using hex2rgb as helper function
    droid.set_front_led(hex2rgb(color))
    droid.set_back_led(hex2rgb(color))


def hex2rgb(hex_code: str) -> Color:
    """convert HEX to RGB, one line"""
    # If input is HEX, convert to RGB
    if hex_code.startswith('#'):
        h = hex_code.lstrip('#')
        result = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        return Color(result[0],result[1],result[2])
    # If input is the English name of a color, return color from color dictionary
    else:
        return color_names_to_rgb[hex_code]

# Testing hex2rgb outputs
print(hex2rgb('#B4FBB8'))
print(hex2rgb('yellow'))
