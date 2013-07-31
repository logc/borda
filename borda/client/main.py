import requests


def resource(path):
    base_url = 'http://localhost:1031/'
    return base_url + path


def create_new_election():
    election = requests.post(resource('election'))
    return election.status_code == requests.codes.ok


def add_candidate(name):
    candidate = {'name': name}
    candidate_request = requests.put(
        resource('election'), data=candidate)
    return candidate_request.status_code == requests.codes.ok


def add_voter(name):
    voter = {'name': name}
    voter_request = requests.post(
        resource('vote'), data=voter)
    return voter_request.status_code == requests.codes.ok


def voter_votes(name, votes):
    voter_votes = {
        'name': name,
        'votes': votes}
    voter_votes_request = requests.put(
        resource('vote'), data=voter_votes)
    return voter_votes_request.status_code == requests.codes.ok


def get_election_winner():
    winner = requests.get(resource('election'))
    print winner.text
    return winner.status_code == requests.codes.ok


def run():
    print "Borda client"
