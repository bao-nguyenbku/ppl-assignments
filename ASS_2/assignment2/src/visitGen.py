import re
with open('./main/d96/parser/D96.g4', 'r', encoding='utf-8') as file:
    for header in file:
        if header.startswith('program'):
            break
    rule = header[:header.find(':')].title()
    # Write header and program rule to output file
    ASTFile = open('visitAST.py', 'w', encoding='utf-8')
    ASTFile.write("""from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
""")
    ASTFile.write("""class ASTGeneration(D96Visitor):""")
    ASTFile.write("""
    def visit{0}(self, ctx: D96Parser.{0}Context):
        return None\n
    """.format(rule))
    

    for line in file:
        if line.startswith('//') or line == '\n':
            continue
        
        m = re.search('^[a-z]', line)
        if (m is not None) and (line.startswith('fragment') == False):
            tmp = line[:line.find(':')].strip() 
            commonRule = tmp[0].upper() + tmp[1:]
            commonVisit = """def visit{0}(self, ctx: D96Parser.{0}Context):
        return None\n
    """.format(commonRule)
            ASTFile.write(commonVisit)
    
    ASTFile.close()

file.close()

