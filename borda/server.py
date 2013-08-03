"""This module serves responses to requests on the Borda voting system. The
requests typically create a new election, register new candidates and voters,
issue votes for the election, and also retrieve the resulting winner."""
import json

from bottle import request, route, run

import borda.count

DEFAULT_PORT = 1031

ELECTION = None
VOTERS = []


@route('/election', method='GET')
def get_election_result():
    """Get election result"""
    if ELECTION is None:
        return "Sorry, no election defined"
    return ELECTION.get_winner().name


@route('/election', method='POST')
def create_election():
    """Create a new election"""
    election = borda.count.Election()
    election.set_candidates([])
    global ELECTION
    ELECTION = election


@route('/election', method='PUT')
def add_candidate():
    """Add a candidate to the open election"""
    name = request.POST.get('name')
    candidate = borda.count.Candidate(name)
    ELECTION.add_candidate(candidate)


@route('/vote', method='GET')
def list_candidates():
    """List all candidates"""
    return json.dumps([c.name for c in ELECTION.candidates])


@route('/vote', method='POST')
def add_voter():
    """Add a voter to the open election"""
    name = request.POST.get('name')
    voter = borda.count.Voter(ELECTION, name)
    VOTERS.append(voter)


@route('/vote', method='PUT')
def vote():
    """Issue votes from a voter in the election"""
    name = request.POST.get('name')
    for voter in VOTERS:
        if voter.name == name:
            posted_votes = request.POST.getlist('votes')
            votes = []
            for posted_vote in posted_votes:
                votes.append(borda.count.Candidate(posted_vote))
            voter.votes(votes)


def main_debug():
    """Test entry point"""
    run(host='localhost', port=DEFAULT_PORT, debug=True)


def main():
    """Main entry point"""
    run(host='localhost', port=DEFAULT_PORT, debug=False)
