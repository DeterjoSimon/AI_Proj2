from logic_operators.Formula import Formula


class Implication(Formula):
    def __init__(self, *formula):
        super().__init__(*formula)
        if not len(formula) == 2:
            raise ValueError("An implication can only have 2 elements")

    def to_str(self):
        return self.formulas[0].to_str() + " → " + self.formulas[1].to_str()
