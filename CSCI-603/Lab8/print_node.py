"""
CSCI-603 Parser Lab
Author: Sean Strout @ RIT CS
Author: Rohit Ravishankar (rr9105@rit.edu)
Author: Parinitha Nagaraja (pn4972@rit.edu)

A print statement is of the prefix form, where {expression} is optional:

    '@ {expression}'

For example:

    '@'
    '@ 10'
    '@ + 10 20'
    '@ x'            # assuming x = 10

When emitted, the string {\tt ``print''} is emitted, followed by a
space, and the emission of the expression that follows.

    'print'
    'print 10'
    'print (10 + 20)'
    'print x'

When evaluated, the expression is evaluated and its result,
if present, is displayed:

                    # just a newline is printed
    10
    30
    10              # the value of x is printed
"""

import literal_node     # literal_node.LiteralNode
import variable_node    # variable_node.VariableNode
import assignment_node  # assignment_node.AssignmentNode
import math_node        # math_node.MathNode
import syntax_error     # syntax_error.SyntaxError
import runtime_error    # runtime_error.RuntimeError


class PrintNode:
    """
    A PrintNode consists of:
    :slot expression: A valid expression node (LiteralNode, VariableNode,
        MathNode)
    """
    __slots__ = 'expression'

    def __init__(self, expression=None):
        """
        Initialize a PrintNode
        :param expression: A valid expression node (LiteralNode, VariableNode,
            MathNode)
        :return: None
        """
        self.expression = expression

    def emit(self):
        """
        Returns a string in infix form, where {expression} is optional:
            print {expression-emit}
        :return: The infix string (str)
        """
        if isinstance(self.expression,math_node.MathNode):
            return 'print ' + self.expression.emit()
        elif isinstance(self.expression,assignment_node.AssignmentNode):
            return  self.expression.emit()
        elif isinstance(self.expression,variable_node.VariableNode):
            return 'print ' + self.expression.emit()
        elif self.expression == '@':
            return 'print'

    def evaluate(self):
        """
        If the expression is not present, just prints a newline, otherwise
        it prints the evaluation of the expression in string form.
        :return: None
        """
        if self.expression is None:
            return '\n'
        else:
            return self.expression.evaluate()
