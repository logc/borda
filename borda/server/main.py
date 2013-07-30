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


def main():
    run(host='localhost', port=DEFAULT_PORT, debug=True)
