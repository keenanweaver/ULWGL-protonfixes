""" Monster Hunter World
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Requires media foundation dlls
    """
    util.set_environment('WINEDLLOVERRIDES','nvapi,nvapi64=')
    util.protontricks('mf_install')
 
