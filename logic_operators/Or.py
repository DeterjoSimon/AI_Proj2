from logic_operators.Formula import Formula


class Or(Formula):
    def __init__(self, *formula):
        if not len(formula) == 2:
            raise ValueError("A logical OR can only have 2 elements")

        super().__init__(*formula)

    def __str__(self):
        return self.formulas[0].__str__() + " ∨ " + self.formulas[1].__str__()