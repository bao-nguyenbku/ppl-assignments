"""
 * @author nhphung
"""
from statistics import variance
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

import json

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
# (Optional) function to print checking param as json
def toJSON(data):
    f = open('./main/d96/checker/param.json', 'w', encoding='utf-8')
    try:
        f.write(json.dumps(data, sort_keys=False, indent=4))
    except Exception as e:
        f.write(e)
    finally:
        f.close()
def toJSONTerminal(data):
    try:
        print(json.dumps(data, sort_keys=False, indent=4))
    except Exception as e:
        print(e)
class Data:
    def ID(): return '<ID>'
    def INT(): return '<INT>'
    def FLOAT(): return '<FLOAT>'
    def BOOL(): return '<BOOL>'
    def STRING(): return '<STRING>'
    def NULL(): return '<NULL>'
    def ARRAY(): return '<ARRAY>'
    def SELF(): return '<SELF>'
    def CLASS(): return '<CLASS>'
    def VOID(): return '<VOID>'
    def METHOD(): return '<METHOD>'
    def STATIC(): return '<STATIC>'
    def INSTANCE(): return '<INSTANCE>'
    def UNDEFINED(): return None
  

class GlobalChecker(BaseVisitor, Utils):
    # infer(self, name, typ, param):

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
        return param

    # classname: Id,  memlist: List[MemDecl],  parentname: Id = None
    # MemDecl include MethodDecl and AttributeDecl
    def visitClassDecl(self, ast, param):
        if ast.classname.name in param:
            raise Redeclared(Class(), ast.classname.name)
        param[ast.classname.name] = {
            'type': Data.CLASS(),
            'parent': ast.parentname.name if ast.parentname else None,
            'attribute': {},
            'method': {}
        }
        for mem in ast.memlist:
            self.visit(mem, [param, ast.classname.name, 'MemDecl'])
    # kind: SIKind, name: Id, param: List[VarDecl], body: Block
    def visitMethodDecl(self, ast, param):
        className = param[1]
        if ast.name.name in param[0][className]['method']:
            raise Redeclared(Method(), ast.name.name)
        '''
        ** example structure **
        'method': {
            '$get': {
                'kind': 'static',
                'type': '<METHOD>',
                'param': [], // list of parameter
                'body': [] // list dict of var declare inside method (use for method and block scope)
            }
        }
        '''
        
        paramList = [self.visit(eachParam, [param[0], param[1], 'ParamDecl']) for eachParam in ast.param]

        param[0][className]['method'][ast.name.name] = {
            'kind': Data.STATIC() if isinstance(ast.kind, Static) else Data.INSTANCE(),
            'type': Data.METHOD(),
            'param': paramList,
            'body': []
        }

    # kind: SIKind, decl: StoreDecl (VarDecl or ConstDecl)
    def visitAttributeDecl(self, ast, param):
        '''
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
        '''
        self.visit(ast.decl, param)

    # variable: Id, varType: Type, varInit: Expr = None
    def visitVarDecl(self, ast:VarDecl, param):
        className = param[1]
        if param[2] == 'MemDecl':
            if ast.variable.name in param[0][className]['attribute']:
                raise Redeclared(Attribute(), ast.variable.name)
            if ast.variable.name.startswith('$'):
                param[0][className]['attribute'][ast.variable.name] = {
                    'kind': Data.STATIC(),
                    'type': self.visit(ast.varType, param[0]),
                    'const': False,
                    'init': self.visit(ast.varInit, param[0]) if ast.varInit else Data.UNDEFINED()
                }
        elif param[2] == 'ParamDecl':
            parameter = {
                'name': ast.variable.name,
                'kind': Data.INSTANCE(),
                'type': self.visit(ast.varType, param[0]),
                'const': False,
                'init': Data.UNDEFINED()
            }
            return parameter

    # constant: ID,  constType: Type,   value: Expr = None
    def visitConstDecl(self, ast:ConstDecl, param):
        className = param[1]
        if ast.constant.name in param[0][className]['attribute']:
            raise Redeclared(Attribute(), ast.constant.name)
        constType = self.visit(ast.constType, param[0])
        initialType = self.visit(ast.value, param[0]) if ast.value else None

        if isinstance(constType, dict):
            constType = constType['type']

        if initialType is None:
            raise IllegalConstantExpression(None)
        
        
        if constType != initialType:
            raise IllegalConstantExpression(ast.value)

        if ast.constant.name.startswith('$'):
            param[0][className]['attribute'][ast.constant.name] = {
                'kind': Data.STATIC(),
                'type': constType,
                'const': True,
                'init': initialType if initialType else Data.UNDEFINED()
            }
        


    def visitId(self, ast, param):
        # This is name of class
        if ast.name in param:
            return param[ast.name]
        # This is name of attribute in class
        for key in param:
            if ast.name in param[key]['attribute']:
                return param[key]['attribute'][ast.name]

            if ast.name in param[key]['method']:
                return param[key]['method'][ast.name]        
        return None
        
    def visitBinaryOp(self, ast, param):
        return None
    
    # op: str,  body: Expr
    def visitUnaryOp(self, ast, param):
        operandType = self.visit(ast.body, param)
        if ast.op == '!':
            if operandType == Data.UNDEFINED(): pass
                # self.infer(ast.body.name, Data.BOOL(), param)
        
            if operandType != Data.BOOL():
                TypeMismatchInExpression(ast)
            return Data.BOOL()
                
    # obj: Expr,    method: Id, param: List[Expr]
    def visitCallExpr(self, ast, param):

        return None
    def visitNewExpr(self, ast, param):
        return None
    def visitArrayCell(self, ast, param):
        return None
    
    # obj: Expr,    fieldname: Id
    def visitFieldAccess(self, ast, param):
        objType = self.visit(ast.obj, param)
        fieldName = self.visit(ast.fieldname, param)
        if fieldName is None:
            raise Undeclared(Attribute(), ast.fieldname.name)
        
        if fieldName['kind'] == Data.STATIC():
            if objType['type'] != Data.CLASS():
                raise IllegalMemberAccess(ast)
            elif objType['type'] == Data.CLASS():
                return fieldName['type']

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
        return Data.INSTANCE()
    def visitStatic(self, ast, param):
        return Data.STATIC()
    def visitIntLiteral(self, ast, param):
        return Data.INT()
    def visitFloatLiteral(self, ast, param):
        return Data.FLOAT()
    def visitStringLiteral(self, ast, param):
        return Data.STRING()
    def visitBooleanLiteral(self, ast, param):
        return Data.BOOL()
    def visitNullLiteral(self, ast, param):
        return Data.NULL()
    def visitSelfLiteral(self, ast, param):
        return Data.SELF()
    def visitArrayLiteral(self, ast, param):
        return Data.ARRAY()

    ''' DATA TYPE'''
    def visitIntType(self, ast, param):
        return Data.INT()
    def visitFloatType(self, ast, param):
        return Data.FLOAT()
    def visitBoolType(self, ast, param):
        return Data.BOOL()
    def visitStringType(self, ast, param):
        return Data.STRING()
    def visitArrayType(self, ast, param):
        return Data.ARRAY()
    def visitClassType(self, ast, param):
        return Data.CLASS()
    def visitVoidType(self, ast, param):
        return Data.VOID()


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
        toJSON(param)
        return []

    def visitClassDecl(self, ast, c):
        return None

