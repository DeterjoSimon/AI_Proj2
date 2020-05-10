


class Base:
    # Belief base class #
    def __init__(self):
        self.beliefs = set([])

    # Printing function #
    # Subset = True, used for printing after a contraction (as multiple subsets exist) #
    # Subset = False, used before contraction #
    def print(self, subset):
        print("{", end = "")
        if subset:
            for subsets in self.beliefs:
                print("{", end = "")
                for belief in subsets:
                    print(belief.to_str(), end = "")
                    print(", ", end = "")
                print("},", end = "")

        else:
            for belief in self.beliefs:
                print(belief.to_str() + ", ", end = "")
        print("}")

    # Belief base expansion #
    # Does not have to be consistent #
    def expansion(self,new_belief):
        if new_belief not in self.beliefs:
            self.beliefs.add(new_belief)

    # Method for contraction of belief #
    # Updates the belief base #
    # Can create multiple subsets which are contained in the new belief base #
    def contraction(self, removed_belief):
        new_belief_base = set([])

        for belief in self.beliefs:
            foo = belief.contraction(removed_belief)
            if foo is not None:
                new_belief_base.add(tuple([foo]))

        self.beliefs = new_belief_base

    # Finds the belief set from belief base #
    # PART 2 #
    # TODO: From our belief base, which new sentences can we entail?
    def entailment(self):
        pass



