class Formula:
    def __init__(self, *formula):
        if len(formula) > 2:
            raise ValueError("A formula can only have 1 or 2 elements")

        self.formulas = list(formula)

    def to_str(self):
        """
        Traverse the formula (tree) in-order.

        :return: str
        """
        for f in self.formulas:
            return f.to_str()
