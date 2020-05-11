from unittest import TestCase

from cnf import to_cnf, cnf_to_clauses
from logic_operators import *


class TestCnf(TestCase):
    p = Proposition("p")
    q = Proposition("q")
    r = Proposition("r")

    def test_cnf_1(self):
        """
        Convert belief: Robert will pass the exam if and only if he will be prepared or lucky
        to CNF.
        """
        p = self.p
        q = self.q
        r = self.r

        belief = Biconditional(r, Or(p, q))

        clauses = to_cnf(belief)
        assert clauses == {Or(Or(Not(r), p), q), Or(Not(p), r), Or(Not(q), r)}

    def test_cnf_2(self):
        p = self.p
        q = self.q
        r = self.r

        belief = Implication(And(p, q), Not(r))
        clauses = to_cnf(belief)
        assert clauses == {Or(Or(Not(p), Not(q)), Not(r))}

    def test_cnf_3(self):
        p = self.p
        q = self.q
        r = self.r
        belief = Biconditional(And(p, q), Implication(Or(r, q), And(p, r)))
        clauses = to_cnf(belief)
        assert clauses == {Or(r, q), Or(Or(Not(p), Not(r)), q), Or(Or(r, Not(q)), Not(p))}
