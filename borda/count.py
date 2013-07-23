import operator


class Election(object):
    """Election of Borda votes"""

    def set_candidates(self, candidates):
        self.candidates = candidates
        self.votes = {}

    def get_winner(self):
        sorted_votes = sorted(self.votes.iteritems(),
                              key=operator.itemgetter(1),
                              reverse=True)
        return sorted_votes[0][0]

    def give_points(self, chosen, points):
        for candidate in self.candidates:
            if candidate is chosen:
                self.votes.setdefault(chosen, 0)
                self.votes[chosen] += points


class Voter(object):
    """Voter is a participant in a Borda voting"""

    def __init__(self, election):
        self.election = election

    def votes(self, candidates):
        total = len(candidates)
        for pos, candidate in enumerate(candidates):
            points = total - pos
            self.election.give_points(candidate, points)


class Candidate(object):
    """Candidate is a candidate to be a winner in a Borda voting"""

    pass
