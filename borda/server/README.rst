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

    >>> import requests
    >>> election = requests.get('http://localhost:1031/new_election')
    >>> election.status_code
    200

    >>> new_candidate = {'name': 'calisto'}
    >>> candidate = requests.post(
    ...     'http://localhost:1031/add_candidate', data=new_candidate)
    >>> candidate.status_code
    200

    >>> time.sleep(0.3) # might need adjusting
    >>> thread.join(0.1) # might need adjusting
    >>> thread._Thread__stop()