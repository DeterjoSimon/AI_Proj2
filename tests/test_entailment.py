from unittest import TestCase

from entailment import entails
from resolution import get_literals, resolve
from logic_operators import *


class TestEntailment(TestCase):
    p = Proposition("p")
    q = Proposition("q")
    r = Proposition("r")
    s = Proposition("s")

    def test_modus_ponens(self):
        """
        KB:
            {p, p -> q}

        Phi:
            q

        """
        r = self.r
        p = self.p

        assert entails({p, Implication(p, r)}, r)

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
        assert entails(clauses, Not(p))

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
        assert entails(clauses, phi)

    def test_and_elimination(self):
        """
        KB: {p & r}

        Phi: p
        """
        p = self.p
        r = self.r

        assert entails({And(p, r)}, p)

    def test_entailment_3(self):
        p = self.p
        q = self.q
        r = self.r

        kb = {And(p, Biconditional(r, Or(p, q)))}

        assert entails(kb, r)

    def test_entailment_tautology(self):
        p = self.p

        assert entails({}, Or(p, Not(p)))

    def test_entailment_contradiction(self):
        p = self.p

        assert not entails({}, Implication(p, Not(p)))

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
        assert not entails(clauses, And(Not(p), r))