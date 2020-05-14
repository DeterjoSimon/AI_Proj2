from unittest import TestCase

from belief_base import BeliefBase, Belief
from entailment import entails
from logic_operators import *


def select_largest_set(remainders):
    return [max(remainders, key=lambda x: len(x))]


class TestAGMPostulates(TestCase):
    belief_base = BeliefBase(selection_function=select_largest_set)
    p = Proposition("p")
    q = Proposition("q")

    def setUp(self) -> None:
        print("Setting up belief base")
        self.belief_base.clear()
        bb: BeliefBase = self.belief_base
        p = self.p
        q = self.q

        bb.expand(Belief(p))
        bb.expand(Belief(q))
        bb.expand(Belief(And(p, q)))
        bb.expand(Belief(Or(p, q)))
        bb.expand(Belief(Implication(p, q)))
        self.belief_base = bb

    def test_closure_revision(self):
        """
        The outcome of revision is logically closed
        """
        bb = self.belief_base
        bb.revise(Belief(self.p))

        clauses = bb.get_clauses()

        cn_bb = BeliefBase(selection_function=select_largest_set)

        # Check that all formulas in the belief base is a logical consequence of the belief base
        for belief in bb.beliefs:
            if entails(clauses, belief.formula):
                cn_bb.expand(belief)

        print(f"Logical Consequence of Belief base: {cn_bb}")
        print(f"Belief base: {bb}")
        assert cn_bb == bb

    def test_closure_contraction(self):
        """
        The outcome of contraction is logically closed
        """
        bb = self.belief_base
        bb.contract(Belief(self.p))

        clauses = bb.get_clauses()

        cn_bb = BeliefBase(selection_function=select_largest_set)

        # Check that all formulas in the belief base is a logical consequence of the belief base
        for belief in bb.beliefs:
            if entails(clauses, belief.formula):
                cn_bb.expand(belief)

        print(f"Logical Consequence of Belief base: {cn_bb}")
        print(f"Belief base: {bb}")
        assert cn_bb == bb

    def test_success_contraction(self):
        bb = self.belief_base
        phi = self.p

        # Phi is not a tautology
        if entails({}, phi):
            assert False

        bb.contract(Belief(phi))

        assert not entails(bb.get_clauses(), phi)

    def test_success_revision(self):
        bb = self.belief_base
        phi = self.p

        bb.revise(Belief(phi))

        assert entails(bb.get_clauses(), phi)

    def test_inclusion_contraction(self):
        bb = self.belief_base
        phi = self.p

        # Phi is not a tautology
        if entails({}, phi):
            assert False

        bb.revise(Belief(phi))

        assert entails(bb.get_clauses(), phi)

    def test_inclusion_revision(self):
        bb = self.belief_base
        bb2 = BeliefBase(self.belief_base.beliefs, selection_function=select_largest_set)

        phi = self.p
        bb.revise(Belief(phi))
        bb2.expand(Belief(phi))

        assert bb.beliefs.issubset(bb2.beliefs)

    def test_vacuity_contraction(self):
        bb = self.belief_base
        phi = Proposition("r")

        # Phi is not a member of Belief Base
        if entails(bb.get_clauses(), phi):
            assert False

        bb.contract(Belief(phi))

        assert bb == bb

    def test_vacuity_revision(self):
        bb = self.belief_base
        phi = self.p
        bb2 = BeliefBase(self.belief_base.beliefs, selection_function=select_largest_set)

        # Phi is not a member of Belief Base
        if entails(bb.get_clauses(), Not(phi)):
            assert False

        bb.revise(Belief(phi))
        bb2.expand(Belief(phi))

        assert bb == bb2

    def test_extensionality_contraction(self):
        bb = self.belief_base
        bb2 = BeliefBase(self.belief_base.beliefs, selection_function=select_largest_set)
        phi = Implication(self.p, self.q)
        xi = Or(Not(self.p), self.q)

        # Phi is not a member of Belief Base
        if entails({}, Biconditional(phi, xi)):
            assert False

        bb.contract(Belief(phi))
        bb2.contract(Belief(xi))

        assert bb == bb2

    def test_extensionality_revision(self):
        bb = self.belief_base
        bb2 = BeliefBase(self.belief_base.beliefs, selection_function=select_largest_set)
        phi = Or(self.p, self.q)
        xi = Or(self.p, self.q)

        # Phi is not a member of Belief Base
        if not entails({}, Biconditional(phi, xi)):
            assert False

        bb.revise(Belief(phi))
        bb2.revise(Belief(xi))

        assert bb == bb2


