from unittest import TestCase

from entailment import entailment, get_literals, resolve
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

    def test_get_literals(self):
        r = self.r
        p = self.p

        clause = Or(Not(r), Or(p, r))
        assert get_literals(clause) == [Not(r), p, r]

    def test_resolve_unit(self):
        """
        Resolve in unit resolution
        """
        r = self.r
        p = self.p

        clause1 = Or(Not(p), r)
        clause2 = Not(r)

        assert resolve(clause1, clause2)[0] == Not(p)

    def test_resolve_full(self):
        """
        Resolve in full resolution
        """
        r = self.r
        p = self.p
        s = self.s

        clause1 = Or(Or(Not(p), Not(r)), s)
        clause2 = Or(p, r)

        resolvents = resolve(clause1, clause2)
        assert resolvents[0] == Or(Or(r, s), Not(r)) and resolvents[1] == Or(Or(p, s), Not(p))

    def test_resolve_factor(self):
        """
        Resolve for two simple clauses
        """
        r = self.r
        p = self.p

        clause1 = Or(r, p)
        clause2 = Or(r, Not(p))

        assert resolve(clause1, clause2)[0] == r
