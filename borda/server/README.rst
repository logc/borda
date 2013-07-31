===================
Borda voting server
===================

This package holds a REST interface to the Borda voting system.

    >>> import borda.server.main

Start a server

    >>> import threading, time
    >>> thread = threading.Thread(target=borda.server.main.main)
    >>> thread.daemon = True
    >>> thread.start()

    >>> def resource(path):
    ...     base_url = 'http://localhost:1031/'
    ...     return base_url + path

Create a new election

    >>> import requests
    >>> election = requests.get(resource('new_election'))
    >>> election.status_code
    200

Add a candidate for the election

    >>> first_candidate = {'name': 'calisto'}
    >>> first_candidate_request = requests.post(
    ...     resource('add_candidate'), data=first_candidate)
    >>> first_candidate_request.status_code
    200

Add further candidates

    >>> further_candidate1 = {'name': 'calvin'}
    >>> candidate_request1 = requests.post(
    ...     resource('add_candidate'), data=further_candidate1)
    >>> candidate_request1.status_code
    200

    >>> further_candidate2 = {'name': 'clark'}
    >>> candidate_request2 = requests.post(
    ...     resource('add_candidate'), data=further_candidate2)
    >>> candidate_request2.status_code
    200

Add a voter to the election

    >>> first_voter = {'name': 'valentine'}
    >>> first_voter_request = requests.post(
    ...     resource('add_voter'), data=first_voter)
    >>> first_voter_request.status_code
    200

Add further voters

    >>> further_voter = {'name': 'veronica'}
    >>> further_voter_request = requests.post(
    ...     resource('add_voter'), data=further_voter)
    >>> further_voter_request.status_code
    200

A voter votes

    >>> voter_votes = {
    ...     'name': 'valentine',
    ...     'votes': ['clark', 'calisto', 'calvin']}
    >>> voter_votes_request = requests.post(
    ...     resource('vote'), data=voter_votes)
    >>> voter_votes_request.status_code
    200

Further votes

    >>> further_votes = {
    ...     'name': 'veronica',
    ...     'votes': ['clark', 'calvin', 'calisto']}
    >>> further_votes_request = requests.post(
    ...     resource('vote'), data=further_votes)

Get who is the winner of the election

    >>> winner = requests.get(resource('election'))
    >>> print winner.text
    clark

Clean up after the tests

    >>> time.sleep(0.1) # might need adjusting
    >>> thread.join(0.1) # might need adjusting
    >>> thread._Thread__stop()