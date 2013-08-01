# pylint: disable=E1101
"""This module sends requests to a Borda server in order to create an election,
register candidates and voters, and issue votes on behalf of the voters."""
import requests


def resource(path):
    """Append a path to an entrypoint to form a REST resource"""
    base_url = 'http://localhost:1031/'
    return base_url + path


def create_new_election():
    """Create a new election on the server"""
    election = requests.post(resource('election'))
    return election.status_code == requests.codes.ok


def add_candidate(name):
    """Add a new candidate to the open election"""
    candidate = {'name': name}
    candidate_request = requests.put(
        resource('election'), data=candidate)
    return candidate_request.status_code == requests.codes.ok


def add_voter(name):
    """Add a voter to the open election"""
    voter = {'name': name}
    voter_request = requests.post(
        resource('vote'), data=voter)
    return voter_request.status_code == requests.codes.ok


def voter_votes(name, votes):
    """A named voter issues a sorted list of votes"""
    voter = {
        'name': name,
        'votes': votes}
    voter_votes_request = requests.put(
        resource('vote'), data=voter)
    return voter_votes_request.status_code == requests.codes.ok


def get_election_winner():
    """Get the winner of the open election"""
    winner = requests.get(resource('election'))
    print winner.text
    return winner.status_code == requests.codes.ok


def run():
    """Main entry point"""
    print "Borda client"