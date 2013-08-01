===================
Borda voting client
===================

This package holds a client for the Borda voting server.

    >>> import borda.client

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

    >>> args = Mock('argparse.Namespace')
    >>> borda.client.create_new_election(args)
    Called requests.post('http://localhost:1031/election')
    True

Add a candidate for the election

    >>> args.name = 'calisto'
    >>> borda.client.add_candidate(args)
    Called requests.put('http://localhost:1031/election',
        data={'name': 'calisto'})
    True

Add a voter to the election

    >>> args.name = 'veronica'
    >>> borda.client.add_voter(args)
    Called requests.post('http://localhost:1031/vote',
        data={'name': 'veronica'})
    True

A voter votes

    >>> args.name = 'veronica'
    >>> args.votes = ['clark', 'calisto', 'calvin']
    >>> borda.client.voter_votes(args)
    Called requests.put(
        'http://localhost:1031/vote',
        data={'votes': ['clark', 'calisto', 'calvin'], 'name': 'veronica'})
    True

Get who is the winner of the election

    >>> borda.client.get_election_winner(args)
    Called requests.get('http://localhost:1031/election')
    clark
    True
