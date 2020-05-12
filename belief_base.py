from typing import Set
import itertools

from entailment import entailment
from logic_operators import Not


class Belief:
    def __init__(self, formula, order=0):
        self.formula = formula
        self.order = order

    def __str__(self):
        return self.formula.__str__() + " @ Order: " + self.order.__str__()


class BeliefBase:
    def __init__(self, kb: Set[Belief] = None):
        if kb is None:
            kb = {}

        self.beliefs: Set[Belief] = kb

    def clear(self):
        self.beliefs = set()

    def add(self, belief: Belief):
        self.beliefs.add(belief)

    def revise(self, new_belief):
        pass

    def expansion(self, new_belief):
        if new_belief not in self.beliefs:
            self.beliefs.add(new_belief)

    def _remainder(self, phi):
        """
        Find subsets which do not entail phi, disregarding order
        """

        def findsubsets(s, n):
            return list(itertools.combinations(s, n))

        N = len(self.beliefs) - 1

        remainders = []

        # Start with n - 1 size subsets and iterate to 1
        for n in range(N, 0, -1):
            n_size_subsets = findsubsets(self.beliefs, n)

            for subset in n_size_subsets:
                # Create clauses of formulas
                clauses = set([belief.formula for belief in subset])

                if not entailment(clauses, phi):
                    remainders += [clauses]

        return remainders

    def contraction(self, remove_belief):
        """
        Entrenchment based contraction
        """

        # 1. Find all subsets of B which do not entail the new formula
        # for belief in self.beliefs:

        # 2. Get the inclusion-maximal subsets

        # 3. Partial Meet Contraction

        # 4. Suck a dick
        # dick = Penis("20cm", Color.Black)
        # mouth = Body.Mouth(gag_reflex=False)
        # while not dick.cum():
        #   mouth.insert(dick)
        #   time.sleep(0.5)
        #   mouth.remove(dick)
        #   time.sleep(0.5)

        pass

    def __str__(self):
        out = set()
        for belief in self.beliefs:
            out.add(belief.__str__())

        return out.__str__()
