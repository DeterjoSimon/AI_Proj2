from unittest import TestCase

from logic_operators import *
from resolution import get_literals, resolve


class TestResolution(TestCase):
    p = Proposition("p")
    q = Proposition("q")
    r = Proposition("r")
    
    def test_get_literals(self):
        q = self.q
        p = self.p

        clause = Or(Not(q), Or(p, q))
        assert get_literals(clause) == [Not(q), p, q]

    def test_resolve_unit(self):
        """
        Resolve in unit resolution
        """
        q = self.q
        p = self.p

        clause1 = Or(Not(p), q)
        clause2 = Not(q)

        assert resolve(clause1, clause2)[0] == Not(p)

    def test_resolve_full(self):
        """
        Resolve in full resolution
        """
        p = self.p
        q = self.q
        r = self.r

        clause1 = Or(Or(Not(p), Not(q)), r)
        clause2 = Or(p, q)

        resolvents = resolve(clause1, clause2)
        assert resolvents[0] == Or(Or(q, r), Not(q)) and resolvents[1] == Or(Or(p, r), Not(p))

    def test_resolve_factor(self):
        """
        Resolve for two simple clauses
        """
        p = self.p
        q = self.q

        clause1 = Or(q, p)
        clause2 = Or(q, Not(p))

        assert resolve(clause1, clause2)[0] == q

    def test_resolve_no_resolvents(self):
        """
        Resolve on clauses which results in no resolvents
        """
        p = self.p
        q = self.q
        r = self.r
        t = Proposition("t")

        clause1 = Or(q, p)
        clause2 = Or(r, Not(t))

        assert not resolve(clause1, clause2)