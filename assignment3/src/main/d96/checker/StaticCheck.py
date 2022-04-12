
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from enum import Enum
class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
class Data(Enum):
    ID = 1
    INT = 2
    FLOAT = 3
    BOOL = 4
    STRING = 5
    NULL = 6
    ARRAY = 7
    SELF = 8

class GlobalChecker(BaseVisitor, Utils):
    def visitProgram(self, ast, param):
        param={}
        return param
    
    def visitClassDecl(self, ast, param):
        return None

    def visitConstDecl(self, ast, param):
        return None
        
    def visitVarDecl(self, ast, param):
        return None
    def visitMethodDecl(self, ast, param):
        return None

    def visitAttributeDecl(self, ast, param):
        return None

    def visitId(self, ast, param):
        return None
    def visitBinaryOp(self, ast, param):
        return None
    def visitUnaryOp(self, ast, param):
        return None
    def visitCallExpr(self, ast, param):
        return None
    def visitNewExpr(self, ast, param):
        return None
    def visitArrayCell(self, ast, param):
        return None
    def visitFieldAccess(self, ast, param):
        return None
    
    def visitAssign(self, ast, param):
        return None
    
    def visitIf(self, ast, param):
        return None
    def visitFor(self, ast, param):
        return None
    def visitBreak(self, ast, param):
        return None
    def visitContinue(self, ast, param):
        return None
    def visitReturn(self, ast, param):
        return None
    def visitCallStmt(self, ast, param):
        return None
    def visitBlock(self, ast, param):
        return None
    
    
    
    def visitInstance(self, ast, param):
        return None
    def visitStatic(self, ast, param):
        return None
    def visitIntLiteral(self, ast, param):
        return None
    def visitFloatLiteral(self, ast, param):
        return None
    def visitStringLiteral(self, ast, param):
        return None
    def visitBooleanLiteral(self, ast, param):
        return None
    def visitNullLiteral(self, ast, param):
        return None
    def visitSelfLiteral(self, ast, param):
        return None
    def visitArrayLiteral(self, ast, param):
        return None
    def visitIntType(self, ast, param):
        return None
    def visitFloatType(self, ast, param):
        return None
    def visitBoolType(self, ast, param):
        return None
    def visitStringType(self, ast, param):
        return None
    def visitArrayType(self, ast, param):
        return None
    def visitClassType(self, ast, param):
        return None
    def visitVoidType(self, ast, param):
        return None


class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
            
    def __init__(self,ast):
        self.ast = ast

 
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c): 
        print(ast, c)
        return None

    def visitClassDecl(self, ast, c):
        return None
    # def visitFuncDecl(self,ast, c): 
    # return list(map(lambda x: self.visit(x,(c,True)),ast.body.stmt)) 

    def visitCallExpr(self, ast, c): 
        at = [self.visit(x,(c[0],False)) for x in ast.param]
        
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(),ast.method.name)
        elif len(res.mtype.partype) != len(at):
            if c[1]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            return res.mtype.rettype

    # def visitIntLiteral(self,ast, c): 
    #     return IntType()
    

