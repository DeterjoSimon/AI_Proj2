from typing import Set

from cnf import to_cnf
from logic_operators import *
from resolution import resolve


def entailment(kb, phi):
    """
    Figure 7.12 in the book
    """
    # Negate phi
    if isinstance(phi, Not):
        phi = phi.formulas[0]
    else:
        phi = Not(phi)

    clauses: Set = kb.union({to_cnf(phi)})

    new = set()

    while True:
        # Pair all clauses and apply resolution
        for cl_i in clauses:
            for cl_j in clauses:
                res_clause = resolve(cl_i, cl_j)

                # If empty set is found (unsatisfiable) then entailment is true
                if False in res_clause:
                    return True

                # Add clause to resolution clauses
                for clause in res_clause:
                    new.add(clause)

        # No new clauses have been added
        if new.issubset(clauses):
            return False

        clauses = clauses.union(new)

