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

        cnf = to_cnf(belief)
        assert cnf == And(And(Or(Not(r), Or(p, q)), Or(Not(p), r)), Or(Not(q), r))

    def test_cnf_2(self):
        p = self.p
        q = self.q
        r = self.r

        belief = Implication(And(p, q), Not(r))
        cnf = to_cnf(belief)
        assert cnf == And(And(Or(Or(Not(p), Not(q)))), Not(r))

    def test_cnf_3(self):
        p = self.p
        q = self.q
        r = self.r
        belief = Biconditional(p, Implication(q, r))
        cnf = to_cnf(belief)
        assert cnf == And(Or(Or(Not(p), Not(q)), r), And(Or(q, p), Or(Not(r), p)))
