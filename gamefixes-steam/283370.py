""" Marine Sharpshooter II: Jungle Warfare
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    util.winedll_override('d3d8', 'n,b') # dgVoodoo2 component
    util.protontricks('mfc42')