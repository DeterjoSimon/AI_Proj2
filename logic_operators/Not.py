from logic_operators.Formula import Formula


class Not(Formula):
    # A class, that when applied to a variable changes the boolean value.
    def __init__(self, *formula):
        if not len(formula) == 1:
            raise ValueError("A negation can only have 1 element")

        super().__init__(*formula)

    def to_str(self):
        return "¬" + self.formulas[0].to_str()



