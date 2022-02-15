import sys
from antlr4 import *
from D96Lexer import D96Lexer
from D96Parser import D96Parser
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.tree.Trees import Trees

def main(argv):
    inputFile = '../src/test/testcases/'
    if str(argv[1]).find('.txt') >= 0:
        inputFile += argv[1]
    else:
        inputFile += argv[1] + '.txt'

    input = FileStream(inputFile)
    lexer = D96Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = D96Parser(stream)
    tree = parser.program()
    print('Input test: ' + str(input) + '\n')
    print(Trees.toStringTree(tree, None, parser))  
    print('\n')
    traverse(tree, parser.ruleNames)

def traverse(tree, rule_names, indent = 0):
    if tree.getText() == "<EOF>":
        return
    elif isinstance(tree, TerminalNodeImpl):
        print("{0}TOKEN->'{1}'".format("|  " * indent, tree.getText()))
    else:
        if tree.children is None:
            print("{0}{1}: null".format("|  " * indent, rule_names[tree.getRuleIndex()]))
        if tree.children is not None:
            print("{0}{1}".format("|  " * indent, rule_names[tree.getRuleIndex()]))
            for child in tree.children:
                traverse(child, rule_names, indent + 1) 
if __name__ == '__main__':
    main(sys.argv)