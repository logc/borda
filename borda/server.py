"""This module serves responses to requests on the Borda voting system. The
requests typically create a new election, register new candidates and voters,
issue votes for the election, and also retrieve the resulting winner."""
import json
import os.path
import shelve
from contextlib import closing

import bottle

import borda.count

DEFAULT_PORT = 1031

ELECTION = None
VOTERS = []

app = bottle.Bottle()
db = shelve.open(
    os.path.join(app.resources.base, 'shelve.db'), writeback=True)


@app.route('/election', method='GET')
def get_election_result():
    """Get election result"""
    if db['election'] is None:
        return "Sorry, no election defined"
    return db['election'].get_winner().name


@app.route('/election', method='POST')
def create_election():
    """Create a new election"""
    election = borda.count.Election()
    election.set_candidates([])
    db['election'] = election


@app.route('/election', method='PUT')
def add_candidate():
    """Add a candidate to the open election"""
    name = bottle.request.POST.get('name')
    candidate = borda.count.Candidate(name)
    db['election'].add_candidate(candidate)


@app.route('/vote', method='GET')
def list_candidates():
    """List all candidates"""
    return json.dumps([c.name for c in db['election'].candidates])


@app.route('/vote', method='POST')
def add_voter():
    """Add a voter to the open election"""
    name = bottle.request.POST.get('name')
    voter = borda.count.Voter(db['election'], name)
    db['voters'].append(voter)


@app.route('/vote', method='PUT')
def vote():
    """Issue votes from a voter in the election"""
    name = bottle.request.POST.get('name')
    for voter in db['voters']:
        if voter.name == name:
            posted_votes = bottle.request.POST.getlist('votes')
            votes = []
            for posted_vote in posted_votes:
                votes.append(borda.count.Candidate(posted_vote))
            voter.votes(votes)


def main_debug():
    """Test entry point"""
    run_app(True)


def main():
    """Main entry point"""
    run_app(False)


def run_app(do_debug=False):
    """Run the web app, wheter with or without debugging"""
    db.setdefault('election', None)
    db.setdefault('voters', [])
    with closing(db):
        app.run(host='localhost', port=DEFAULT_PORT, debug=do_debug)
