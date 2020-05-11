from unittest import TestCase

from entailment import entailment
from resolution import get_literals, resolve
from logic_operators import *


class TestEntailment(TestCase):
    s = Proposition("s")
    p = Proposition("p")
    r = Proposition("r")

    def test_entailment(self):
        """
        Test entailment on KB:
            Robert does well in the exam if and only if he is prepared or lucky.
            Robert does not do well in the exam

        Formula for entailment:
            Robert is not prepared
        """
        r = self.r
        p = self.p
        s = self.s

        # KB in CNF and split into clauses
        clauses = {Or(Or(Not(r), p), s), Or(Not(p), r), Or(Not(s), r), Not(r)}

        # Test if the formula: Not(p) is entailed from the KB
        assert entailment(clauses, Not(p))

    def test_entailment_2(self):
        """
        Test entailment on KB:
            {-p -> q, q -> p, p -> r & s}

        Formula for entailment:
            p & r & s
        """
        p = self.p
        q = Proposition('q')
        r = self.r
        s = self.s

        # KB in CNF and split into clauses
        clauses = {Or(p, q), Or(Not(q), p), Or(Not(p), r), Or(Not(p), s)}

        phi = And(And(p, r), s)
        # Test if the formula: Not(p) is entailed from the KB
        assert entailment(clauses, phi)

    def test_entailment_fail(self):
        """
        Test entailment on KB:
            p <-> r

        Formula for entailment:
            -p & r
        """
        r = self.r
        p = self.p

        # KB in CNF and split into clauses
        clauses = {And(Or(Not(p), r), Or(Not(r), p))}

        # Test if the formula: -p & r is entailed from the KB
        assert not entailment(clauses, And(Not(p), r))