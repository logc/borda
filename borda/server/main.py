from bottle import route, run

import borda.count

DEFAULT_PORT = 1031


@route('/new_election')
def hello():
    election = borda.count.Election()
    del election


@route('/add_candidate', method='POST')
def add_candidate():
    candidate = borda.count.Candidate()
    del candidate


@route('/add_voter', method='POST')
def add_voter():
    election = borda.count.Election()
    voter = borda.count.Voter(election)
    del voter


@route('/vote', method='POST')
def vote():
    pass


@route('/election')
def election():
    return 'clark'


def main():
    run(host='localhost', port=DEFAULT_PORT, debug=True)
