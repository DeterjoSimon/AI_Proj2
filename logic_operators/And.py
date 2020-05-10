from logic_operators.Formula import Formula


class And(Formula):
    def __init__(self, *formula):
        if not len(formula) == 2:
            raise ValueError("A logical AND can only have 2 elements")

        super().__init__(*formula)

    def to_str(self):
        return self.formulas[0].to_str() + " ∧ " + self.formulas[1].to_str()










