import sys
from antlr4 import *
from D96Lexer import D96Lexer
from D96Parser import D96Parser
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.tree.Trees import Trees

def main(argv):
    input = FileStream('code.txt')
    lexer = D96Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = D96Parser(stream)
    tree = parser.program()
    print(Trees.toStringTree(tree, None, parser))  
    traverse(tree, parser.ruleNames, parser.symbolicNames)

def traverse(tree, rule_names, symbolic_names, indent = 0):
    if tree.getText() == "<EOF>":
        return

    elif isinstance(tree, TerminalNodeImpl):
        print("{0}TOKEN->'{1}'".format("|  " * indent, tree.getText()))
    else:
        print("{0}{1}".format("|  " * indent, rule_names[tree.getRuleIndex()]))
        for child in tree.children:
            traverse(child, rule_names, symbolic_names, indent + 1) 
if __name__ == '__main__':
    main(sys.argv)