from bottle import request, route, run

import borda.count

DEFAULT_PORT = 1031

ELECTION = None
VOTERS = []


@route('/election', method='GET')
def get_election_result():
    return ELECTION.get_winner().name


@route('/election', method='POST')
def create_election():
    election = borda.count.Election()
    election.set_candidates([])
    global ELECTION
    ELECTION = election


@route('/election', method='PUT')
def add_candidate():
    name = request.POST.get('name')
    candidate = borda.count.Candidate(name)
    global ELECTION
    ELECTION.add_candidate(candidate)


@route('/add_voter', method='POST')
def add_voter():
    global ELECTION
    name = request.POST.get('name')
    voter = borda.count.Voter(ELECTION, name)
    VOTERS.append(voter)


@route('/vote', method='POST')
def vote():
    name = request.POST.get('name')
    for voter in VOTERS:
        if voter.name == name:
            posted_votes = request.POST.getlist('votes')
            votes = []
            for posted_vote in posted_votes:
                votes.append(borda.count.Candidate(posted_vote))
            voter.votes(votes)


def main():
    run(host='localhost', port=DEFAULT_PORT, debug=True)
