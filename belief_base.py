import itertools
from typing import Set

from entailment import entails
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
    def __init__(self, kb: Set[Belief] = None, selection_function=None):
        self.selection_function = selection_function
        if kb is None:
            kb = set()

        self.beliefs: Set[Belief] = kb

    def _get_remainders(self, phi):
        """
        Find subsets which do not entail phi, disregarding order
        """

        # Local function for finding all subsets
        def find_subsets(s, n):
            return list(set(combination) for combination in itertools.combinations(s, n))

        N = len(self.beliefs) - 1
        remainders = []

        # Start with n - 1 size subsets and iterate to 1
        for n in range(N, 0, -1):
            n_size_subsets = find_subsets(self.beliefs, n)

            for subset in n_size_subsets:
                # Check for a larger subset
                c_prime_exists = sum([subset.issubset(remainder) for remainder in remainders]) > 0

                if c_prime_exists:
                    continue

                # Create clauses of formulas and check that it does not entail phi
                clauses = [belief.formula for belief in subset]
                if not entails(clauses, phi.formula):
                    remainders.append(subset)

        return remainders

    def clear(self):
        self.beliefs = set()

    def expand(self, new_belief):
        # Do not add tautologies or contradictions
        if entails({}, new_belief) or not entails({}, new_belief):
            return

        self.beliefs.add(new_belief)

    def revise(self, new_belief):
        # Do not add tautologies or contradictions
        if entails({}, new_belief) or not entails({}, new_belief):
            return

        not_belief = new_belief
        not_belief.formula = Not(not_belief.formula)

        # Levi identity
        self.contract(not_belief)
        self.expand(new_belief)

    def contract(self, remove_belief):
        """
        Entrenchment based contraction
        """
        if not self.selection_function:
            raise AttributeError("Selection function not specified")

        # Get remainders of contracting with the belief
        remainders = self._get_remainders(remove_belief)

        # If the remainder is empty, return the belief base
        if not len(remainders):
            return self.beliefs

        # Apply selection function
        best_remainders = self.selection_function(remainders)

        # Return intersection of selected elements
        return set.intersection(*best_remainders)

    def __str__(self):
        out = set()
        for belief in self.beliefs:
            out.add(belief.__str__())

        return "Knowledge base: " + out.__str__()
