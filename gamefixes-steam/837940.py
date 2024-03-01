""" Mobile Forces
"""
#pylint: disable=C0103

import os

from protonfixes import util

def main():
    util.winedll_override('d3d8', 'n,b') # Use packaged D3D8 for frame limiting/game fixes
