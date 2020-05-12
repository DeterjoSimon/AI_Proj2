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
        clean_str_self = self.__str__().replace("(", "").replace(")", "")
        clean_str_other = other.__str__().replace("(", "").replace(")", "")
        return clean_str_self == clean_str_other

    def __lt__(self, other):
        return self.__str__() < other.__str__()

    def __hash__(self):
        return hash(self.__str__())
