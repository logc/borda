===================
borda voting system
===================

The Borda count is a single-winner election method in which voters rank
candidates in order of preference. The Borda count determines the winner of an
election by giving each candidate a certain number of points corresponding to
the position in which he or she is ranked by each voter. Once all votes have
been counted the candidate with the most points is the winner. Because it
sometimes elects broadly acceptable candidates, rather than those preferred by
the majority, the Borda count is often described as a consensus-based electoral
system, rather than a majoritarian one.

    >>> import borda.count
    >>> single_winner = borda.count.Election()

    >>> calisto = borda.count.Candidate()
    >>> calvin = borda.count.Candidate()
    >>> clark = borda.count.Candidate()
    >>> single_winner.set_candidates([calisto, calvin, clark])

    >>> valentine = borda.count.Voter(single_winner)
    >>> veronica = borda.count.Voter(single_winner)

    >>> valentine.votes([clark, calisto, calvin])
    >>> veronica.votes([clark, calvin, calisto])

    >>> single_winner.get_winner() is clark
    True
