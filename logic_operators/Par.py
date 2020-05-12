from logic_operators import Formula


class Par(Formula):
    def __init__(self, *formula):
        super().__init__(*formula)

    def __str__(self):
        return "(" + self.formulas[0].__str__() + ")"
