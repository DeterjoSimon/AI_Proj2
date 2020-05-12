from typing import Set

from cnf import to_cnf, cnf_to_clauses
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

    # Convert to cnf
    phi_cnf = to_cnf(phi)
    phi_clause = cnf_to_clauses(phi_cnf)

    kb_cnf = set()

    for formula in kb:
        cnf = to_cnf(formula)
        cnf_clause = cnf_to_clauses(cnf)
        kb_cnf = kb_cnf.union(cnf_clause)

    clauses: Set = kb_cnf.union(phi_clause)

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

