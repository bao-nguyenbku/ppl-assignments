
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
    CLASS = ID
    VOID = 0

class GlobalChecker(BaseVisitor, Utils):
    def visitProgram(self, ast, param):
        '''
        //** Param structure for global scope **//
            param = {
                'Dog': {
                    'type': CLASS,
                    'parent': 'Animal',
                    'attribute': {
                        '$a': {
                            'kind': 'static',
                            'type': 'int',
                            'const': false // if this attribute is a constant, flag will be true
                        }
                    },
                    'method': {
                        '$get': {
                            'kind': 'static',
                            'type': 'method',
                            'param': [], // list of parameter
                            'field': [] // list dict of var declare inside method (use for method and block scope)
                        }
                    }
                }
                ...
            }
        '''
        for element in ast.decl:
            self.visit(element, param)
        return list(param.items())
    # classname: Id,  memlist: List[MemDecl],  parentname: Id = None
    # MemDecl include MethodDecl and AttributeDecl
    def visitClassDecl(self, ast, param):
        if ast.classname.name in param:
            raise Redeclared(Class(), ast.classname)
        param[ast.classname.name] = {
            'type': Data.CLASS,
            'parent': ast.parentname.name if ast.parentname else None,
            'attribute': {},
            'method': {}
        }

        for mem in ast.memlist:
            self.visit(mem, param[ast.classname.name])

    def visitMethodDecl(self, ast, param):
        return None

    # kind: SIKind, decl: StoreDecl (VarDecl or ConstDecl)
    def visitAttributeDecl(self, ast, param):
        '''
        param = {
            'type':, 
            'parent':, 
            'attribute': {},
            'method': {}
        }
        '''
        self.visit(ast.decl, param['attribute'])

    # variable: Id, varType: Type, varInit: Expr = None
    def visitVarDecl(self, ast, param):
        '''
        {
            '$a': {
                'kind': 'static',
                'type': 'int',
                'const': False
                'init':
            }
        }
        '''
        if ast.variable.name in param:
            raise Redeclared(Attribute(), ast.variable.name)
        
        param[ast.variable.name] = {
            'kind': 'static' if ast.variable.name.startswith('$') else 'instance',
            'type': self.visit(ast.varType, param),
            'const': False,
            'init': None
        }

    def visitConstDecl(self, ast, param):
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

    ''' DATA TYPE'''
    def visitIntType(self, ast, param):
        return Data.INT
    def visitFloatType(self, ast, param):
        return Data.FLOAT
    def visitBoolType(self, ast, param):
        return Data.BOOL
    def visitStringType(self, ast, param):
        return Data.STRING
    def visitArrayType(self, ast, param):
        return Data.ARRAY
    def visitClassType(self, ast, param):
        return Data.CLASS
    def visitVoidType(self, ast, param):
        return Data.VOID


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
        c = {}
        param = GlobalChecker().visit(ast, c)
        return param

    def visitClassDecl(self, ast, c):
        return None

