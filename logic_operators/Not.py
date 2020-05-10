from logic_operators.Variables import Variables
class Not:
    # A class, that when applied to a variable changes the boolean value.
    def __init__(self, A):
        self.elements = [A]
        A.change_boolean()
    # Calls the class it belongs to when asked for string and contraction
    def to_str(self):
        return self.elements[0].to_str()

    def contraction(self, removed_belief):
        return self.elements[0].contraction(removed_belief)



