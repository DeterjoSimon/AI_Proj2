from unittest import TestCase

from engine.language.grammar import parser
from engine.logic_operators import *


class Test_grammar(TestCase):
    def test_ast_words(self):
        """
        Test abstract syntax tree for words
        """

        result = parser.parse("not a and b or c")
        assert (isinstance(result, And)
                and isinstance(result.formulas[0], Not)
                and isinstance(result.formulas[1], Or)
                and isinstance(result.formulas[0].formulas[0], Proposition)
                and isinstance(result.formulas[1].formulas[0], Proposition)
                and isinstance(result.formulas[1].formulas[1], Proposition)
                )

    def test_ast_symbols(self):
        """
        Test abstract syntax tree for symbols
        """

        result = parser.parse("-a & ~b | c")
        assert (isinstance(result, And)
                and isinstance(result.formulas[0], Not)
                and isinstance(result.formulas[1], Or)
                and isinstance(result.formulas[0].formulas[0], Proposition)
                and isinstance(result.formulas[1].formulas[0], Not)
                and isinstance(result.formulas[1].formulas[0].formulas[0], Proposition)
                and isinstance(result.formulas[1].formulas[1], Proposition)
                )

    def test_presedence_implication_biconditional(self):
        """
        Test implication and biconditional presedence
        """

        result = parser.parse("a -> b <=> a")
        assert (isinstance(result, Biconditional)
                and isinstance(result.formulas[0], Implication)
                and isinstance(result.formulas[1], Proposition))

    def test_grouping(self):
        """
        Test grouping with parentheses
        """

        result = parser.parse("not(a and c -> a)")
        assert (isinstance(result, Not)
                and isinstance(result.formulas[0], And)
                and isinstance(result.formulas[0].formulas[0], Proposition)
                and isinstance(result.formulas[0].formulas[1], Implication)
                and isinstance(result.formulas[0].formulas[1].formulas[0], Proposition)
                and isinstance(result.formulas[0].formulas[1].formulas[1], Proposition))
