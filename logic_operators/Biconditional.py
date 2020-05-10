from logic_operators.Variables import Variables

class Biconditional:
    def __init__(self, A, B):
        self.elements = [A,B]


    def contraction(self, removed_belief):
        # First two if-statements recursively tries to reach the correct variables
        if type(self.elements[0]) is not Variables:
            self.elements[0] = self.elements[0].contraction(removed_belief)

            if None in self.elements:
                return None
            else:
                return self

        if type(self.elements[1]) is not Variables:
            self.elements[1] = self.elements[1].contraction(removed_belief)
            if None in self.elements:
                return None
            else:
                return self

        # Remove if contracted belief is equal to Biconditional
        if type(removed_belief) is Biconditional:
            if removed_belief.elements[0].name == self.elements[0].name and \
                    removed_belief.elements[1].name == self.elements[1].name:
                return None

        return self

    def to_str(self):
        return self.elements[0].to_str() + " BICOND. " + self.elements[1].to_str()