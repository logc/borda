===================
Borda voting server
===================

This package holds a REST interface to the Borda voting system.

    >>> import borda.server.main

You can start a server on your machine like this:

    >>> import threading, time
    >>> thread = threading.Thread(target=borda.server.main.main)
    >>> thread.daemon = True
    >>> thread.start()

    >>> time.sleep(0.3) # might need adjusting
    >>> thread.join(0.1) # might need adjusting
    >>> thread._Thread__stop()