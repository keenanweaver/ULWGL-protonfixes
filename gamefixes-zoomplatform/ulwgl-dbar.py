""" Dr. Brain: Action Reaction
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    util.winedll_override('ddraw', 'n,b') # DDrawCompat component
