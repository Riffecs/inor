#!/usr/bin/env python3
"""
 Start modules for all imports
"""
import sys


def handler() -> None:
    """
    Manages the CL arguments and distributes them to appropriate commands.
    """
    if sys.argv:
        print("Hallo")
