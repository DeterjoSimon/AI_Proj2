class Formula:
    def __init__(self, *formula):
        if len(formula) > 2:
            raise ValueError("A formula can only have 1 or 2 elements")

        self.formulas = list(formula)

    def __str__(self):
        """
        Traverse the formula (tree) in-order.

        :return: str
        """
        for f in self.formulas:
            return f.__str__()

    def __eq__(self, other):
        """
        Compare string representation of formulas
        """
        return self.__str__() == other.__str__()

    def __hash__(self):
        return hash(self.__str__())