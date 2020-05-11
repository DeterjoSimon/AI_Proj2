from unittest import TestCase

from cnf import cnf
from logic_operators import *


class TestCnf(TestCase):
    s = Proposition("s")
    p = Proposition("p")
    r = Proposition("r")

    def test_cnf(self):
        """
        Convert belief: Robert will pass the exam if and only if he will be prepared or lucky
        to CNF.
        """
        r = self.r
        p = self.p
        s = self.s

        belief = Biconditional(r, Or(p, s))

        assert cnf(belief) == {Or(Or(Not(r), p), s), Or(Not(p), r), Or(Not(s), r)}