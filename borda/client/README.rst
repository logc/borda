===================
Borda voting client
===================

This package holds a client for the Borda voting server.

    >>> import borda.client.main

Create a new election

    >>> from minimock import Mock, mock
    >>> import requests
    >>> requests.post = Mock('requests.post')
    >>> requests.put = Mock('requests.put')
    >>> requests.get = Mock('requests.get')
    >>> response_mock = Mock('requests.Response')
    >>> response_mock.status_code = requests.codes.ok
    >>> response_mock.text = u'clark'
    >>> requests.post.mock_returns = response_mock
    >>> requests.put.mock_returns = response_mock
    >>> requests.get.mock_returns = response_mock

    >>> borda.client.main.create_new_election()
    Called requests.post('http://localhost:1031/election')
    True

Add a candidate for the election

    >>> borda.client.main.add_candidate('calisto')
    Called requests.put('http://localhost:1031/election',
        data={'name': 'calisto'})
    True

Add a voter to the election

    >>> borda.client.main.add_voter('veronica')
    Called requests.post('http://localhost:1031/vote',
        data={'name': 'veronica'})
    True

A voter votes

    >>> borda.client.main.voter_votes(
    ...     'veronica', ['clark', 'calisto', 'calvin'])
    Called requests.put(
        'http://localhost:1031/vote',
        data={'votes': ['clark', 'calisto', 'calvin'], 'name': 'veronica'})
    True

Get who is the winner of the election

    >>> borda.client.main.get_election_winner()
    Called requests.get('http://localhost:1031/election')
    clark
    True
