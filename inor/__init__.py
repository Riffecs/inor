"""
 Start modules for all imports
"""
import os
import sys
from datetime import datetime

import numpy as np
from pyftpdlib.authorizers import DummyAuthorizer
from inor import functions
from inor.errors import Errors

CERTFILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "keycert.pem"))

authorizer = DummyAuthorizer()


def handler() -> None:
    """
    Manages the CL arguments and distributes them to appropriate commands.
    """
    # time Handler
    start = datetime.now()

    # Error Object
    error = Errors()

    if len(sys.argv) >= 2:
        # Deletes the path and the basic command from the array
        command_list = np.delete(np.array(sys.argv), [0, 1])

        # Create a variable that stores the main command.
        loader: str = sys.argv[1]

        # Converts the Numpy array back to a normal list
        flags: list[str] = np.ndarray.tolist(command_list)

        # PyLint container
        riox = "riox"
        print(riox, flags, error, loader)

    # End Time Managment
    diff = datetime.now() - start
    print(f"run: {diff.seconds}s")
