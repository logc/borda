# pylint: disable=E1101
"""This module sends requests to a Borda server in order to create an election,
register candidates and voters, and issue votes on behalf of the voters."""
import argparse
import json
import sys
import logging

import requests


def resource(path):
    """Append a path to an entrypoint to form a REST resource"""
    base_url = 'http://localhost:1031/'
    return base_url + path


def create_new_election(args):
    """Create a new election on the server"""
    try:
        election = requests.post(resource('election'))
        return election.status_code == requests.codes.ok
    except requests.exceptions.ConnectionError as ex:
        logging.error(ex.message)
        return False


def add_candidate(args):
    """Add a new candidate to the open election"""
    candidate = {'name': args.name}
    try:
        candidate_request = requests.put(
            resource('election'), data=candidate)
        return candidate_request.status_code == requests.codes.ok
    except requests.exceptions.ConnectionError as ex:
        logging.error(ex.message)
        return False


def list_candidates(args):
    """List all candidates"""
    try:
        candidates_request = requests.get(resource('vote'))
        js = candidates_request.json()
        candidates = json.loads(js)
        for num, candidate in enumerate(candidates):
            print "{0}: {1}".format(num + 1, candidate)
        return candidates_request == requests.codes.ok
    except requests.exceptions.ConnectionError as ex:
        logging.error(ex.message)
        return False


def add_voter(args):
    """Add a voter to the open election"""
    voter = {'name': args.name}
    try:
        voter_request = requests.post(
            resource('vote'), data=voter)
        return voter_request.status_code == requests.codes.ok
    except requests.exceptions.ConnectionError as ex:
        logging.error(ex.message)
        return False


def voter_votes(args):
    """A named voter issues a sorted list of votes"""
    voter = {
        'name': args.name,
        'votes': args.votes}
    try:
        voter_votes_request = requests.put(
            resource('vote'), data=voter)
        return voter_votes_request.status_code == requests.codes.ok
    except requests.exceptions.ConnectionError as ex:
        logging.error(ex.message)
        return False


def get_election_winner(args):
    """Get the winner of the open election"""
    try:
        winner = requests.get(resource('election'))
        print winner.text
        return winner.status_code == requests.codes.ok
    except requests.exceptions.ConnectionError as ex:
        logging.error(ex.message)
        return False


def comma_separated_strings(votes_string):
    """Argparse type check for a comma separated list of strings"""
    try:
        return votes_string.split(',')
    except ValueError:
        msg = "%r is not a comma separated list of strings" % votes_string
        raise argparse.ArgumentTypeError(msg)


def run():
    """Main entry point"""
    parser = argparse.ArgumentParser(prog='borda')
    subparsers = parser.add_subparsers(help='sub-command help')
    parse_create_new_election = subparsers.add_parser('election')
    parse_create_new_election.set_defaults(func=create_new_election)
    parse_add_candidate = subparsers.add_parser('candidate')
    parse_add_candidate.add_argument('-n', '--name', required=True)
    parse_add_candidate.set_defaults(func=add_candidate)
    parse_add_voter = subparsers.add_parser('voter')
    parse_add_voter.add_argument('-n', '--name', required=True)
    parse_add_voter.set_defaults(func=add_voter)
    parse_vote = subparsers.add_parser('vote')
    parse_vote.add_argument('-n', '--name', required=True)
    parse_vote.add_argument('-v', '--votes', required=True,
                            type=comma_separated_strings)
    parse_vote.set_defaults(func=voter_votes)
    parse_winner = subparsers.add_parser('winner')
    parse_winner.set_defaults(func=get_election_winner)
    args = parser.parse_args()
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s')
    success = args.func(args)
    if success:
        sys.exit(0)
    else:
        sys.exit(1)
