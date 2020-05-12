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

    def __eq__(self, other):
        return self.formula == self.formula and self.order == self.order
        pass

    def __hash__(self):
        return hash(self.__str__())


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

    def _get_remainders(self, phi):
        """
        Find subsets which do not entail phi, disregarding order
        """

        # Local function for finding all subsets
        def findsubsets(s, n):
            return list(set(combination) for combination in itertools.combinations(s, n))

        N = len(self.beliefs) - 1
        remainders = []

        # Start with n - 1 size subsets and iterate to 1
        for n in range(N, 0, -1):
            n_size_subsets = findsubsets(self.beliefs, n)

            for subset in n_size_subsets:
                # Check for a larger subset
                c_prime_exists = sum([subset.issubset(remainder) for remainder in remainders]) > 0

                if not c_prime_exists:
                    continue

                # Create clauses of formulas and check that it does not entail phi
                clauses = [belief.formula for belief in subset]
                if not entailment(clauses, phi.formula):
                    remainders.append(subset)

        return remainders

    def contraction(self, remove_belief):
        """
        Entrenchment based contraction
        """
        # Get remainders of contracting with the belief
        remainders = self._get_remainders(remove_belief)

        # 3. Partial Meet Contraction

        return None

    def __str__(self):
        out = set()
        for belief in self.beliefs:
            out.add(belief.__str__())

        return out.__str__()
