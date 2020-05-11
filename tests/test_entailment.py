from unittest import TestCase

from logic_operators import *
from entailment import res_entailment


class TestEntailment(TestCase):
    s = Proposition("s")
    p = Proposition("p")
    r = Proposition("r")



    def test_entailment(self):
        """
        Test entailment on KB:
            Robert does well in the exam if and only if he is prepared or lucky.
            Robert does not do well in the exam

        Formula for entailment:
            Robert is not prepared

        :return:
        """
        r = self.r
        p = self.p
        s = self.s

        # KB in CNF and split into clauses
        clauses = {Or(Or(Not(r), p), s), Or(Not(p), r), Or(Not(s), r), Not(r)}

        # Test if the formula: Not(p) is entailed from the KB
        assert res_entailment(clauses, Not(p))
