"""
CSCI-603 PreTee Lab
Author: Sean Strout @ RIT CS
Author: Rohit Ravishankar (rr9105@rit.edu)
Author: Parinitha Nagaraja (pn4972@rit.edu)

The main program and class for a prefix expression interpreter of the
PreTee language.  See prog1.pre for a full example.

Usage: python3 pretee.py source-file.pre
"""

import sys              # argv
from _csv import field_size_limit

import literal_node     # literal_node.LiteralNode
import variable_node    # variable_node.VariableNode
import assignment_node  # assignment_node.AssignmentNode
import print_node       # print_node.PrintNode
import math_node        # math_node.MathNode
import syntax_error     # syntax_error.SyntaxError
import runtime_error    # runtime_error.RuntimeError

class PreTee:
    """
    The PreTee class consists of:
    :slot srcFile: the name of the source file (string)
    :slot symTbl: the symbol table (dictionary: key=string, value=int)
    :slot parseTrees: a list of the root nodes for valid, non-commented
        line of code
    :slot lineNum:  when parsing, the current line number in the source
        file (int)
    :slot syntaxError: indicates whether a syntax error occurred during
        parsing (bool).  If there is a syntax error, the parse trees will
        not be evaluated
    """
    __slots__ = 'srcFile', 'symTbl', 'parseTrees', 'lineNum', 'syntaxError'

    # the tokens in the language
    COMMENT_TOKEN = '#'
    ASSIGNMENT_TOKEN = '='
    PRINT_TOKEN = '@'
    ADD_TOKEN = '+'
    SUBTRACT_TOKEN = '-'
    MULTIPLY_TOKEN = '*'
    DIVIDE_TOKEN = '//'
    MATH_TOKENS = ADD_TOKEN, SUBTRACT_TOKEN, MULTIPLY_TOKEN, DIVIDE_TOKEN

    def __init__(self, srcFile ):
        """
        Initialize the parser.
        :param srcFile: the source file (string)
        """
        self.srcFile = srcFile
        self.symTbl = {}
        self.parseTrees = []
        self.lineNum = 0
        self.syntaxError = False

    def __parse(self, tokens):
        """
        The recursive parser that builds the parse tree from one line of
        source code.
        :param tokens: The tokens from the source line separated by whitespace
            in a list of strings.
        :exception: raises a syntax_error.SyntaxError with the message
            'Incomplete statement' if the statement is incomplete (e.g.
            there are no tokens left and this method was called).
        :exception: raises a syntax_error.SyntaxError with the message
            'Invalid token {token}' if an unrecognized token is
            encountered (e.g. not one of the tokens listed above).
        :return:
        """
        if len(tokens) < 1:
            return
        firstToken = tokens[0]

        if firstToken is self.COMMENT_TOKEN:
            return

        if firstToken.isdigit():
            node = literal_node.LiteralNode(firstToken)
            self.parseTrees.append(node)

        elif firstToken.isidentifier():
            self.symTbl[firstToken] = ''
            node = variable_node.VariableNode(firstToken,self.symTbl)
            self.parseTrees.append(node)

        elif firstToken == self.ASSIGNMENT_TOKEN:
            first = self.parseTrees.pop()
            second = self.parseTrees.pop()
            valid = self.checkIfPoppedNodesAreValidForAssignmentNode(first,second)
            if valid==True:
                node = assignment_node.AssignmentNode(first,second,self.symTbl,firstToken)
                self.parseTrees.append(node)
                node.evaluate()
            else:
                self.syntaxError = True
                raise syntax_error.SyntaxError('Incomplete Statement' + ' line Number ' + str(self.lineNum))


        elif firstToken in self.MATH_TOKENS:
            first = self.parseTrees.pop()
            second = self.parseTrees.pop()
            valid = self.checkIfPoppedNodesAreValidForMathNode(first,second)
            if valid==True:
                node = math_node.MathNode(first,second,firstToken)
                self.parseTrees.append(node)
            else:
                self.syntaxError = True
                raise syntax_error.SyntaxError('Incomplete Statement' + ' line Number ' + str(self.lineNum))

        self.__parse(tokens[1:])


    def checkIfPoppedNodesAreValidForAssignmentNode(self, first, second):
        valid = True
        if not isinstance(first,(variable_node.VariableNode,math_node.MathNode)):
            valid = False
        if not isinstance(second,(variable_node.VariableNode,math_node.MathNode,literal_node.LiteralNode)):
            valid = False
        return valid

    def checkIfPoppedNodesAreValidForMathNode(self, first, second):
        valid = True
        if not isinstance(first,(math_node.MathNode,literal_node.LiteralNode,variable_node.VariableNode)):
            valid = False
        if not isinstance(second,(math_node.MathNode,literal_node.LiteralNode ,variable_node.VariableNode)):
            valid = False
        return valid



    def parse(self):
        """
        The public parse is responsible for looping over the lines of
        source code and constructing the parseTree, as a series of
        calls to the helper function that are appended to this list.
        It needs to handle and display any syntax_error.SyntaxError
        exceptions that get raised.
        : return None
        """
        with open(self.srcFile) as file:
            for line in file:
                self.lineNum += 1
                try:
                    line = line.strip()
                    if '#' in line or line == '':
                        continue
                    myList = line.split()
                    invalidToken = self.validate(myList)

                    s1 = set(self.MATH_TOKENS)
                    s2 = set(myList)

                    if s1.intersection(s2):
                        if self.ASSIGNMENT_TOKEN in myList:
                          if (len(myList)-1) < 3 :
                            self.syntaxError = True
                            raise syntax_error.SyntaxError('Incomplete Statement' + ' line Number ' + str(self.lineNum))

                    if not self.isIncompleteExpression(myList) and invalidToken == "":
                        myList = myList[::-1]
                        self.__parse(myList)
                    else:
                        pass
                        # self.syntaxError = True
                        # raise syntax_error.SyntaxError('Invalid token ' + str(invalidToken) + ' line Number ' + str(self.lineNum))
                except syntax_error.SyntaxError as e:
                    print('***Syntax Error:', e)

    def validate(self, mylist):
        count = 0
        length = len(mylist)
        for i in mylist:
            count += 1
            if i != self.ASSIGNMENT_TOKEN and i not in self.MATH_TOKENS and i != self.PRINT_TOKEN and not i.isidentifier() and not i.isdigit():
                self.syntaxError = True
                raise syntax_error.SyntaxError(
                    'Invalid token ' + str(i) + ' line Number ' + str(self.lineNum))
                return i
            if i == self.PRINT_TOKEN and count <= length and count != 1:
                self.syntaxError = True
                raise syntax_error.SyntaxError('Bad assignment expression' + ' line Number ' + str(self.lineNum))
                return i
        return ""

    def isIncompleteExpression(self,mylist):
        length = len(mylist)
        if length < 3 and mylist[0] in self.MATH_TOKENS:
            self.syntaxError = True
            raise syntax_error.SyntaxError('Incomplete Statement' + ' line Number ' + str(self.lineNum))
            return True

        if length < 3 and mylist[0] == self.ASSIGNMENT_TOKEN:
            self.syntaxError = True
            raise syntax_error.SyntaxError('Incomplete Statement' + ' line Number ' + str(self.lineNum))
            return True
        return False






    def emit(self):
        """
        Prints an infiex string representation of the source code that
        is contained as root nodes in parseTree.
        :return None
        """
        for node in self.parseTrees:
            str = print_node.PrintNode(node).emit()
            print(str)

    def evaluate(self):
        """
        Prints the results of evaluating the root notes in parseTree.
        This can be viewed as executing the compiled code.  If a
        runtime error happens, execution halts.
        :exception: runtime_error.RunTimeError may be raised if a
            parse tree encounters a runtime error
        :return None
        """
        if not self.syntaxError == True:
            for node in self.parseTrees:
                if not isinstance(node, assignment_node.AssignmentNode):
                    print(node.evaluate())
                else:
                    # pass
                    node.evaluate()
                    # print(self.symTbl[node.variable.id])
        else:
            pass
def main():
    """
    The main function prompts for the source file, and then does:
        1. Compiles the prefix source code into parse trees
        2. Prints the source code as infix
        3. Executes the compiled code
    :return: None
    """
    if len(sys.argv) != 2:
        print('Usage: python3 pretee.py source-file.pre')
        return

    pretee = PreTee(sys.argv[1])
    print('PRETEE: Compiling', sys.argv[1] + '...')
    pretee.parse()
    print('\nPRETEE: Infix source...')
    pretee.emit()
    print('\nPRETEE: Executing...')
    try:
        pretee.evaluate()
    except runtime_error.RuntimeError as e:
        # on first runtime error, the supplied program will halt execution
        print('*** Runtime error:', e)

if __name__ == '__main__':
    main()