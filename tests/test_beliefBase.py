from unittest import TestCase

from belief_base import BeliefBase, Belief
from logic_operators import *


class TestBeliefBase(TestCase):
    belief_base = BeliefBase()
    p = Proposition("p")
    q = Proposition("q")
    r = Proposition("r")

    def setUp(self) -> None:
        self.belief_base.clear()

    def test_remainder(self):
        """
        Test contraction for KB:
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
        Test contraction for KB:
            {p, q, p ∧ q, p ∨ q, p → q}

        Contract formula:
            q

        Resulting KBs:
            {q}
        """



        assert False
