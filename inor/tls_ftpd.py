"""
...
"""

import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import TLS_FTPHandler
from pyftpdlib.servers import FTPServer


CERTFILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "keycert.pem"))


def main():
    authorizer = DummyAuthorizer()

    authorizer.add_user(
        "user",
        "aghast-unhealthy-sloppy-elastic-referable",
        "/root/inor",
        perm="elradfmwMT",
    )
    authorizer.add_user(
        "basic",
        "aghast-unhealthy-sloppy-elastic-referable",
        "/root/inor/basic",
        perm="elr",
    )
    authorizer.add_user(
        "advanced",
        "aghast-unhealthy-sloppy-elastic-referable",
        "/root/inor/advanced",
        perm="elr",
    )
    authorizer.add_user(
        "premium",
        "aghast-unhealthy-sloppy-elastic-referable",
        "/root/inor/premium",
        perm="elr",
    )

    authorizer.add_anonymous("/root/inor")
    handler = TLS_FTPHandler
    handler.certfile = CERTFILE
    handler.authorizer = authorizer
    # requires SSL for both control and data channel
    # handler.tls_control_required = True
    # handler.tls_data_required = True
    server = FTPServer(("", 2121), handler)
    server.serve_forever()


if __name__ == "__main__":
    main()
