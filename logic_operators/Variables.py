
class Variables:
    def __init__(self, name, Bool):
        self.Bool = Bool
        self.name = name

    def change_boolean(self):
        self.Bool = 1 if self.Bool == 0 else 0

    def contraction(self, removed_belief):
        # Remove if same boolean value #
        if type(removed_belief) is Variables:

            if removed_belief.Bool == self.Bool and removed_belief.name == self.name:
                return None
            else:
                return self
        return self

    def to_str(self):
        return self.name if self.Bool else "not " + self.name





