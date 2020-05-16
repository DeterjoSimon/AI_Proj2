from engine.logic_operators.Formula import Formula


class Proposition(Formula):
    def __init__(self, *formula):
        if not len(formula) == 1:
            raise ValueError("A proposition can only have 1 element")

        if not isinstance(*formula, str):
            raise ValueError("Propositions can only be letters")

        super().__init__(*formula)

    def __str__(self):
        return self.formulas[0]
