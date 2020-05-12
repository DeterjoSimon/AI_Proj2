from unittest import TestCase

from belief_base import BeliefBase, Belief
from logic_operators import *


def select_largest_set(remainders):
    return [max(remainders, key=lambda x: len(x))]


class TestBeliefBaseAGMPostulates(TestCase):
    belief_base = BeliefBase(selection_function=select_largest_set)
    p = Proposition("p")
    q = Proposition("q")

    def setUp(self) -> None:
        self.belief_base.clear()
        bb = self.belief_base
        p = self.p
        q = self.q

        bb.expand(Belief(p))
        bb.expand(Belief(q))
        bb.expand(Belief(And(p, q)))
        bb.expand(Belief(Or(p, q)))
        bb.expand(Belief(Implication(p, q)))


