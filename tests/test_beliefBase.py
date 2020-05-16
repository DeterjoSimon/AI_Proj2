from unittest import TestCase

from engine.belief_base import BeliefBase, Belief
from engine.logic_operators import *


def select_largest_set(remainders):
    return [max(remainders, key=lambda x: len(x))]


class TestBeliefBase(TestCase):
    belief_base = BeliefBase(selection_function=select_largest_set)
    p = Proposition("p")
    q = Proposition("q")
    r = Proposition("r")

    def setUp(self) -> None:
        self.belief_base.clear()

    def test_remainder(self):
        """
        Test remainders for KB:
            {p, q, p ∧ q, p ∨ q, p → q}

        Contract formula:
            q

        Resulting remainders:
            {{p, p ∨ q}, {p → q}}
        """

        bb = self.belief_base
        p = self.p
        q = self.q

        bb.expand(Belief(p))
        bb.expand(Belief(q))
        bb.expand(Belief(And(p, q)))
        bb.expand(Belief(Or(p, q)))
        bb.expand(Belief(Implication(p, q)))

        remainders = bb._get_remainders(Belief(q))

        assert remainders == [{Belief(p), Belief(Or(p, q))}, {Belief(Implication(p, q))}]

    def test_contraction(self):
        """
        Selection function selects only the largest set

        Test contraction for KB:
            {p, q, p ∧ q, p ∨ q, p → q}

        Contract formula:
            q

        Resulting best set:
            {p, p ∨ q}
        """

        bb = self.belief_base
        p = self.p
        q = self.q

        bb.expand(Belief(p))
        bb.expand(Belief(q))
        bb.expand(Belief(And(p, q)))
        bb.expand(Belief(Or(p, q)))
        bb.expand(Belief(Implication(p, q)))

        bb.contract(Belief(q))

        assert bb.beliefs == {Belief(p), Belief(Or(p, q))}

    def test_revision(self):
        """
        Test revision for KB:
            {p → q}

        Revise formula:
            p

        Resulting best set:
            {p, p -> q}
        """

        bb = self.belief_base
        p = self.p
        q = self.q

        bb.expand(Belief(Implication(p, q)))

        bb.revise(Belief(p))

        assert bb.beliefs == {Belief(p), Belief(Implication(p, q))}

