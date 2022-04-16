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
    def ARRAY(size, eleType): return '['+ str(size) + ']' + eleType
    def SELF(): return '<SELF>'
    def CLASS(name): return '<CLASS>(' + name + ')'
    def VOID(): return '<VOID>'
    def METHOD(): return '<METHOD>'
    def STATIC(): return '<STATIC>'
    def INSTANCE(): return '<INSTANCE>'
    def UNDEFINED(): return None
class GetReturnType(BaseVisitor):
    def visitAssign(self, ast, o): pass
    def visitIf(self, ast, o):
        self.visit(ast.thenStmt, o)
        if ast.elseStmt is None: return
        self.visit(ast.elseStmt, o)
    def visitFor(self, ast, o):
        self.visit(ast.loop, o)
    def visitBreak(self, ast, o): pass
    def visitContinue(self, ast, o): pass
    def visitReturn(self, ast, o): pass
    def visitCallStmt(self, ast, o): pass
    def visitVarDecl(self, ast, o): pass
    def visitBlock(self, ast, o):
        for inst in ast.inst: 
            self.visit(inst, o)

class ForLoopChecker(BaseVisitor, Utils):
    def visitAssign(self, ast, o): pass
    def visitIf(self, ast, o):
        self.visit(ast.thenStmt, o)
        if ast.elseStmt is None: return
        self.visit(ast.elseStmt, o)
    def visitFor(self, ast, o):
        self.visit(ast.loop, ['For'], o)
    def visitBreak(self, ast, o):
        if not 'For' in o: raise MustInLoop(ast)
    def visitContinue(self, ast, o):
        if not 'For' in o: raise MustInLoop(ast)
    def visitReturn(self, ast, o): pass
    def visitCallStmt(self, ast, o): pass
    def visitVarDecl(self, ast, o): pass
    def visitBlock(self, ast, o):
        for inst in ast.inst: 
            self.visit(inst, o)
#**** Visit all statics and method declares ****#
# * NO initial value check * #
class GetGlobalEnv(BaseVisitor, Utils):
    def visitProgram(self, ast, o):
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
            self.visit(element, o)
        return o

    # classname: Id,  memlist: List[MemDecl],  parentname: Id = None
    # MemDecl include MethodDecl and AttributeDecl
    def visitClassDecl(self, ast, o):
        '''
        dict class form:
        o[class_name] = {
            'type': <CLASS>
            'parent': parent_name,
            'attribute': {dict of attribute}
            'method': {dict of method}
        }
        '''
        class_name = ast.classname.name
        if class_name in o:
            raise Redeclared(Class(), class_name)
        parent_name = ''
        if not ast.parentname is None:
            parent_name = ast.parentname.name
            if parent_name == class_name:
                raise Undeclared(Class(), parent_name)
        
        o[class_name] = {
            'parent': parent_name,
            'attribute': {},
            'method': {}
        }
        for mem in ast.memlist:
            self.visit(mem, o[class_name])
    # kind: SIKind, name: Id, param: List[VarDecl], body: Block
    def visitMethodDecl(self, ast, o):
        '''
            o['method'][method_name] = {
                'type'  : return type of method,
                'kind'  : "instance" or "static"
                'body' : [{}, {}] list dictionary {var decl}, use for method scope and block scope
                'param' : {list parameter}
            }
        '''
        name = ast.name.name
        if name in o['method']:
            raise Redeclared(Method(),name)
        
        o['method'][name] = {
            'type': Data.VOID(),
            'kind': self.visit(ast.kind, o),
            'body': [{}],
            'param': {}
        }

        for eachPar in ast.param:
            o['method'][name]['param'] = GetGlobalEnv().visitParam(eachPar, o['method'][name]['param'])
    
    # variable: Id, varType: Type, varInit: Expr = None
    def visitParam(self, ast:VarDecl, o):
        '''
        o[var_name] = {
            'kind': <INSTANCE> or <STATIC> // With global attribute, kind is <STATIC>
            'type': type of this attribute (INT, FLOAT,...)
            'init': UNDEFINED
            'const': False
        }
        '''
        name = ast.variable.name

        if name in o:
            raise Redeclared(Parameter(), name)
        typ = self.visit(ast.varType, o)
        o[name] = {
            'type': typ,
            'kind': Data.INSTANCE(),
            'init': Data.UNDEFINED(),
            'const': False
        }
        return o

    # kind: SIKind, decl: StoreDecl (VarDecl or ConstDecl)
    def visitAttributeDecl(self, ast, o):
        name = self.visit(ast.decl, o)
        if not name is None:
            o['attribute'][name]['kind'] = Data.STATIC()
            
    # variable: Id, varType: Type, varInit: Expr = None
    def visitVarDecl(self, ast:VarDecl, o):
        '''
        o['attribute'][var_name] = {
            'kind': <INSTANCE> or <STATIC> // With global attribute, kind is <STATIC>
            'type': type of this attribute (INT, FLOAT,...)
            'init': initial type of this attribute, update later
            'const': boolean flag to know this attribte is constant or variable
        }
        '''
        name = ast.variable.name
        if name.startswith('$'):
            if name in o['attribute']:
                raise Redeclared(Attribute(), name)

            typ = self.visit(ast.varType, o)
            o['attribute'][name] = {
                'type': typ,
                'init': Data.UNDEFINED(),
                'const': False
            }
            return name

    # constant: ID,  constType: Type,   value: Expr = None
    def visitConstDecl(self, ast:ConstDecl, o):
        '''
        o['attribute'][const_name] = {
            'kind': <INSTANCE> or <STATIC> // With global attribute, kind is <STATIC>
            'type': type of this attribute (INT, FLOAT,...)
            'init': initial type of this attribute, update later
            'const': boolean flag to know this attribte is constant or variable
        }
        '''
        name = ast.constant.name
        if name.startswith('$'):
            if name in o['attribute']:
                raise Redeclared(Attribute(), name)
            if ast.value is None:
                raise IllegalConstantExpression(None)
            typ = self.visit(ast.constType, o)
            o['attribute'][name] = {
                'type': typ,
                'init': Data.UNDEFINED(),
                'const': True
            }
            return name
        
    def visitId(self, ast, param):
        return ast.name
    
    def visitInstance(self, ast, param):
        return Data.INSTANCE()
    def visitStatic(self, ast, param):
        return Data.STATIC()

    ''' DATA TYPE'''
    def visitIntType(self, ast, o):
        return Data.INT()
    def visitFloatType(self, ast, o):
        return Data.FLOAT()
    def visitBoolType(self, ast, o):
        return Data.BOOL()
    def visitStringType(self, ast, o):
        return Data.STRING()
    def visitArrayType(self, ast, o):
        return Data.ARRAY(ast.size, self.visit(ast.eleType, o))
    def visitClassType(self, ast, o):
        return Data.CLASS(self.visit(ast.classname, o))
    def visitVoidType(self, ast, o):
        return Data.VOID()

# * Visit all instance attribute * #
class GetClassEnv(BaseVisitor, Utils):
    def visitProgram(self, ast, o):
        for element in ast.decl:
            self.visit(element, o)
        return o

    # classname: Id,  memlist: List[MemDecl],  parentname: Id = None
    # MemDecl include MethodDecl and AttributeDecl
    def visitClassDecl(self, ast, o):
        '''
        o = {
            'class_name': {
                'attribute': {},
                'method': {}
            }
        }
        '''
    
        for mem in ast.memlist:
            self.visit(mem, o[ast.classname.name])
    # kind: SIKind, name: Id, param: List[VarDecl], body: Block
    def visitMethodDecl(self, ast, o): pass
    
    # kind: SIKind, decl: StoreDecl (VarDecl or ConstDecl)
    def visitAttributeDecl(self, ast, o):
        '''
            { <- o here
                'attribute': {}
            }
        '''
        name = self.visit(ast.decl, o)
        if not name is None:
            o['attribute'][name]['kind'] = Data.INSTANCE()
        
    # variable: Id, varType: Type, varInit: Expr = None
    def visitVarDecl(self, ast:VarDecl, o):
        '''
        o['attribute'][var_name] = {
            'kind': <INSTANCE> or <STATIC> // With global attribute, kind is <STATIC>
            'type': type of this attribute (INT, FLOAT,...)
            'init': initial type of this attribute, update later
            'const': boolean flag to know this attribte is constant or variable
        }
        '''
        name = ast.variable.name
        typ = self.visit(ast.varType, o)
        if not name.startswith('$'):
            if name in o['attribute']:
                raise Redeclared(Attribute(), name)
            
            o['attribute'][name] = {
                'type': typ,
                'init': Data.UNDEFINED(),
                'const': False
            }
            return name

    # constant: ID,  constType: Type,   value: Expr = None
    def visitConstDecl(self, ast:ConstDecl, o):
        '''
        o['attribute'][const_name] = {
            'kind': <INSTANCE> or <STATIC> // With global attribute, kind is <STATIC>
            'type': type of this attribute (INT, FLOAT,...)
            'init': initial type of this attribute, update later
            'const': boolean flag to know this attribte is constant or variable
        }
        '''
       
        name = ast.constant.name
        if ast.value is None:
            raise IllegalConstantExpression(None)
    
        typ = self.visit(ast.constType, o)
        if not name.startswith('$'):
            if name in o['attribute']:
                raise Redeclared(Attribute(), name)
            
            o['attribute'][name] = {
                'type': typ,
                'init': Data.UNDEFINED(),
                'const': True
            }
            return name
    
    #name: str
    def visitId(self, ast, o):
        return ast.name
        
    # op: str,  left: Expr,     right: Expr
    def visitBinaryOp(self, ast, o): pass
        # left = self.visit(ast.left, o)
        # right = self.visit(ast.right, o)
        # op = ast.op
        # if op in ['%']:
        #     if left == Data.INT() and right == Data.INT():
        #         return Data.INT()
        # if op in ['+', '-', '*', '/']:
        #     if left == Data.INT() and right == Data.INT():
        #         return Data.INT()
        #     if left in [Data.INT(), Data.FLOAT()] and right in [Data.INT(), Data.FLOAT()]:       
        #         return Data.FLOAT()
        # if op in ['&&', '||']:
        #     if left == Data.BOOL() and right == Data.BOOL():
        #         return Data.BOOL()
        # if op in ['==', '!=']:
        #     if left == right and left in [Data.INT(), Data.BOOL()]:
        #         return Data.BOOL()
        # if op in ['>', '<', '>=', '<=']:
        #     if left in [Data.INT(), Data.FLOAT()] and right in [Data.INT(), Data.FLOAT()]:
        #         return Data.BOOL()

        # if op == '==.':
        #     if left == right and left == Data.STRING():
        #         return Data.BOOL()
        # if op == '+.':
        #     if left == right and left == Data.STRING():
        #         return Data.STRING()
        # raise TypeMismatchInExpression(ast)
    
    # # op: str,  body: Expr
    def visitUnaryOp(self, ast, o): pass
        # body = self.visit(ast.body, o)
        # op = ast.op
        # if op == '!' and body == Data.BOOL():
        #     return Data.BOOL()
        
        # if op == '-' and body in [Data.INT(), Data.FLOAT()]:
        #     return body
        # raise TypeMismatchInExpression(ast)
                     
    # # obj: Expr,    method: Id, param: List[Expr]
    def visitCallExpr(self, ast, param): pass
    
    # classname: Id,    param: List[Expr]
    def visitNewExpr(self, ast, o): pass
        # class_name = ast.classname.name
        # if not class_name in o:
        #     raise Undeclared(Class(), class_name)
        
        # # Check if don't have Constructor in class declare
        # if not 'Constructor' in o[class_name]['method']:
        #     raise Undeclared(Method(), 'Constructor')
        
        # # Check for argument and parameter matching
        # # paramEnv is list of dict param declare
        # param_env = o[class_name]['method']['Constructor']['param']
        
        # # [<INT>, <FLOAT>,...] for example
        # list_param_type = [param_env[par_name]['type'] for par_name in param_env]
        
        # argument_type = [self.visit(arg, o) for arg in ast.param]
        # if len(argument_type) != len(param_env):
        #     raise TypeMismatchInExpression(ast)
        
        # for i in range(len(list_param_type)):
        #     if list_param_type[i] != argument_type[i]:
        #         raise TypeMismatchInExpression(ast)
        # return Data.CLASS(class_name)
    
    # arr: Expr,    idx: List[Expr]
    def visitArrayCell(self, ast, o): pass
        # arr = self.visit(ast.arr, o)
        # list_idx = [self.visit(idx, o) for idx in ast.idx]
        # #  array type example: [1][2]<INT>
        # if arr[0] != '[':
        #     raise TypeMismatchInExpression(ast)
        # for idx in list_idx:
        #     if idx != Data.INT():
        #         raise TypeMismatchInExpression(ast)
        
        # while arr[0] != ']':
        #     arr = arr[1:]
        # return arr[1:]

        # return None
    
    # obj: Expr,    fieldname: Id
    def visitFieldAccess(self, ast, o): pass
        # obj_type = self.visit(ast.obj, o)
        # field_name_type = self.visit(ast.fieldname, o)
        # # Check static attribute access
        # return field_name_type
    
    def visitAssign(self, ast, o): pass
    
    def visitIf(self, ast, o): pass
    def visitFor(self, ast, o): pass
    def visitBreak(self, ast, o): pass
    def visitContinue(self, ast, o): pass
    def visitReturn(self, ast, o): pass
    def visitCallStmt(self, ast, o): pass
    def visitBlock(self, ast, o): pass
    
    def visitInstance(self, ast, o):
        return Data.INSTANCE()
    def visitStatic(self, ast, o):
        return Data.STATIC()
    def visitIntLiteral(self, ast, o):
        return Data.INT()
    def visitFloatLiteral(self, ast, o):
        return Data.FLOAT()
    def visitStringLiteral(self, ast, o):
        return Data.STRING()
    def visitBooleanLiteral(self, ast, o):
        return Data.BOOL()
    def visitNullLiteral(self, ast, o):
        return Data.NULL()
    def visitSelfLiteral(self, ast, o):
        return Data.SELF()

    # value: List[Expr]
    def visitArrayLiteral(self, ast, o): pass
        # list_type = [self.visit(ele, o) for ele in ast.value]
        # example_type = ''
        # if len(list_type) != 0:
        #     example_type = list_type[0]
        #     for each_type in list_type[1:]:
        #         if each_type != example_type:
        #             raise IllegalArrayLiteral(ast)
        
        # return Data.ARRAY(len(list_type), example_type)

    ''' DATA TYPE'''
    def visitIntType(self, ast, o):
        return Data.INT()
    def visitFloatType(self, ast, o):
        return Data.FLOAT()
    def visitBoolType(self, ast, o):
        return Data.BOOL()
    def visitStringType(self, ast, o):
        return Data.STRING()
    def visitArrayType(self, ast, o):
        return Data.ARRAY(ast.size, self.visit(ast.eleType, o))
    def visitClassType(self, ast, o):
        return Data.CLASS(self.visit(ast.classname, o))
    def visitVoidType(self, ast, o):
        return Data.VOID()

# * Visit all initial expression of Attribute Declare * #
class GetTypeExpr(BaseVisitor, Utils):
    def visitProgram(self, ast, o):
        for element in ast.decl:
            self.visit(element, o)
        return o

    # classname: Id,  memlist: List[MemDecl],  parentname: Id = None
    # MemDecl include MethodDecl and AttributeDecl
    def visitClassDecl(self, ast, o):
        '''
        o = {
            'global': {
                'class_name': {
                    'attribute': {},
                    'method': {}
                }
            }
        }
        '''
        for mem in ast.memlist:
            self.visit(mem, [o, ast.classname.name])
    # kind: SIKind, name: Id, param: List[VarDecl], body: Block
    def visitMethodDecl(self, ast, o): pass
    
    # kind: SIKind, decl: StoreDecl (VarDecl or ConstDecl)
    def visitAttributeDecl(self, ast, o):
        '''
        o = {
            'global': {
                'class_name': {
                    'attribute': {},
                    'method': {}
                }
            }
        }
        '''
        self.visit(ast.decl, o)
        
    # variable: Id, varType: Type, varInit: Expr = None
    def visitVarDecl(self, ast:VarDecl, o):
        '''
        o = {
            'global': {
                'class_name': {
                    'attribute': {},
                    'method': {}
                }
            }
        }
        o['attribute'][var_name] = {
            'kind': <INSTANCE> or <STATIC> // With global attribute, kind is <STATIC>
            'type': type of this attribute (INT, FLOAT,...)
            'init': initial type of this attribute, update later
            'const': boolean flag to know this attribte is constant or variable
        }
        '''
        name = ast.variable.name
        
        typ = o[0]['global'][o[1]]['attribute'][name]['type']
        init = self.visit(ast.varInit, o[0]) if ast.varInit else Data.UNDEFINED()

        if init != Data.UNDEFINED():
            if typ != init:
                raise TypeMismatchInStatement(ast)
        o[0]['global'][o[1]]['attribute'][name].update({'init': init})

    # constant: ID,  constType: Type,   value: Expr = None
    def visitConstDecl(self, ast:ConstDecl, o):
        '''
        o = {
            'global': {
                'class_name': {
                    'attribute': {},
                    'method': {}
                }
            }
        }
        ['attribute'][const_name] = {
            'kind': <INSTANCE> or <STATIC> // With global attribute, kind is <STATIC>
            'type': type of this attribute (INT, FLOAT,...)
            'init': initial type of this attribute, update later
            'const': boolean flag to know this attribte is constant or variable
        }
        '''
       
        name = ast.constant.name
        typ = o[0]['global'][o[1]]['attribute'][name]['type']
        init = self.visit(ast.value, o[0])

        if typ != init:
            raise TypeMismatchInStatement(ast)
            
        o[0]['global'][o[1]]['attribute'][name].update({'init': init})
    
    #name: str
    def visitId(self, ast, o):
        return ast.name
        
    # op: str,  left: Expr,     right: Expr
    def visitBinaryOp(self, ast, o):
        left = self.visit(ast.left, o)
        right = self.visit(ast.right, o)
        op = ast.op
        if op in ['%']:
            if left == Data.INT() and right == Data.INT():
                return Data.INT()
        if op in ['+', '-', '*', '/']:
            if left == Data.INT() and right == Data.INT():
                return Data.INT()
            if left in [Data.INT(), Data.FLOAT()] and right in [Data.INT(), Data.FLOAT()]:       
                return Data.FLOAT()
        if op in ['&&', '||']:
            if left == Data.BOOL() and right == Data.BOOL():
                return Data.BOOL()
        if op in ['==', '!=']:
            if left == right and left in [Data.INT(), Data.BOOL()]:
                return Data.BOOL()
        if op in ['>', '<', '>=', '<=']:
            if left in [Data.INT(), Data.FLOAT()] and right in [Data.INT(), Data.FLOAT()]:
                return Data.BOOL()

        if op == '==.':
            if left == right and left == Data.STRING():
                return Data.BOOL()
        if op == '+.':
            if left == right and left == Data.STRING():
                return Data.STRING()
        raise TypeMismatchInExpression(ast)
    
    # # op: str,  body: Expr
    def visitUnaryOp(self, ast, o):
        body = self.visit(ast.body, o)
        op = ast.op
        if op == '!' and body == Data.BOOL():
            return Data.BOOL()
        
        if op == '-' and body in [Data.INT(), Data.FLOAT()]:
            return body
        raise TypeMismatchInExpression(ast)
                     
    # # obj: Expr,    method: Id, param: List[Expr]
    def visitCallExpr(self, ast, param): pass
    
    # classname: Id,    param: List[Expr]
    def visitNewExpr(self, ast, o):
        '''
        o = {
            'global': {}
        }
        '''
        class_name = ast.classname.name
        if not class_name in o['global']:
            raise Undeclared(Class(), class_name)
        
        # Check if don't have Constructor in class declare
        if not 'Constructor' in o['global'][class_name]['method']:
            raise Undeclared(Method(), 'Constructor')
        
        # Check for argument and parameter matching
        # paramEnv is list of dict param declare
        param_env = o['global'][class_name]['method']['Constructor']['param']
        
        # [<INT>, <FLOAT>,...] for example
        list_param_type = [param_env[par_name]['type'] for par_name in param_env]
        
        argument_type = [self.visit(arg, o) for arg in ast.param]
        if len(argument_type) != len(param_env):
            raise TypeMismatchInExpression(ast)
        
        for i in range(len(list_param_type)):
            if list_param_type[i] != argument_type[i]:
                raise TypeMismatchInExpression(ast)
        return Data.CLASS(class_name)
    
    # arr: Expr,    idx: List[Expr]
    def visitArrayCell(self, ast, o):
        arr = self.visit(ast.arr, o)
        list_idx = [self.visit(idx, o) for idx in ast.idx]
        #  array type example: [1][2]<INT>
        if arr[0] != '[':
            raise TypeMismatchInExpression(ast)
        for idx in list_idx:
            if idx != Data.INT():
                raise TypeMismatchInExpression(ast)
        
        while arr[0] != ']':
            arr = arr[1:]
        return arr[1:]
    
    # obj: Expr,    fieldname: Id
    # TODO: WRITE FIELDACCESS VISIT
    def visitFieldAccess(self, ast, o):
        # Check if obj is class name for static access
        if isinstance(ast.obj, Id): 
            name = ast.obj.name
            # name must be class name in global env
            if not name in o['global']:
                raise Undeclared(Identifier(), name)

            if not ast.fieldname.name in o['global'][name]['attribute']:
                raise IllegalMemberAccess(ast)
            for attr_name in o['global'][name]['attribute'].keys():
                if o['global'][name]['attribute'][attr_name]['type'].startswith('<CLASS>') == False:
                    raise IllegalMemberAccess(ast)

                if attr_name == ast.fieldname.name:
                    return o['global'][name]['attribute'][attr_name]['type']
            
        else: 
            self.visit(ast.obj, o)
    
    def visitAssign(self, ast, o): pass
    
    def visitIf(self, ast, o): pass
    def visitFor(self, ast, o): pass
    def visitBreak(self, ast, o): pass
    def visitContinue(self, ast, o): pass
    def visitReturn(self, ast, o): pass
    def visitCallStmt(self, ast, o): pass
    def visitBlock(self, ast, o): pass
    
    def visitInstance(self, ast, o):
        return Data.INSTANCE()
    def visitStatic(self, ast, o):
        return Data.STATIC()
    def visitIntLiteral(self, ast, o):
        return Data.INT()
    def visitFloatLiteral(self, ast, o):
        return Data.FLOAT()
    def visitStringLiteral(self, ast, o):
        return Data.STRING()
    def visitBooleanLiteral(self, ast, o):
        return Data.BOOL()
    def visitNullLiteral(self, ast, o):
        return Data.NULL()
    def visitSelfLiteral(self, ast, o):
        # for key in o['global'].keys():
        #     if o['global'][key]
        return Data.SELF()

    # value: List[Expr]
    def visitArrayLiteral(self, ast, o):
        list_type = [self.visit(ele, o) for ele in ast.value]
        example_type = ''
        if len(list_type) != 0:
            example_type = list_type[0]
            for each_type in list_type[1:]:
                if each_type != example_type:
                    raise IllegalArrayLiteral(ast)
        return Data.ARRAY(len(list_type), example_type)

    ''' DATA TYPE'''
    def visitIntType(self, ast, o):
        return Data.INT()
    def visitFloatType(self, ast, o):
        return Data.FLOAT()
    def visitBoolType(self, ast, o):
        return Data.BOOL()
    def visitStringType(self, ast, o):
        return Data.STRING()
    def visitArrayType(self, ast, o):
        return Data.ARRAY(ast.size, self.visit(ast.eleType, o))
    def visitClassType(self, ast, o):
        return Data.CLASS(self.visit(ast.classname, o))
    def visitVoidType(self, ast, o):
        return Data.VOID()
# ********* MAIN CLASS STATIC CHECKER ************* #
class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
            
    def __init__(self,ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    # decl: List[ClassDecl]
    def visitProgram(self, ast, o):
        o = {}
        o = GetGlobalEnv().visitProgram(ast, o)
        o = GetClassEnv().visitProgram(ast, o)
        env = {
            'global': o,
        }
        env = GetTypeExpr().visitProgram(ast, env)
        toJSON(env)        
        # for decl in ast.decl:
        #     self.visit(decl, o)
        return []

    # classname: Id,  memlist: List[MemDecl],  parentname: Id = None
    # MemDecl include MethodDecl and AttributeDecl
    def visitClassDecl(self, ast, o):
        '''
        dict class form:
        o[class_name] = {
            'type': <CLASS>
            'parent': parent_name,
            'attribute': {dict of attribute}
            'method': {dict of method}
        }
        '''
        if ast.parentname:
            if not ast.parentname.name in o:
                raise Undeclared(Class(), ast.parentname.name)
        
        env = {
            'global': o,
            'class': o[ast.classname.name]
        }
        for decl in ast.memlist:
            self.visit(decl, env)
    # kind: SIKind, name: Id, param: List[VarDecl], body: Block 
    def visitMethodDecl(self, ast, o):
        '''
        o = {
            'global': {},
            'class': {}
        }
            o['method'][method_name] = {
                'type'  : return type of method,
                'kind'  : "instance" or "static"
                'body' : [{}, {}] list dictionary {var decl}, use for method scope and block scope
                'param' : {list parameter}
            }
        '''
        ForLoopChecker().visitBlock(ast.body, [])

        env = {
            'global': o['global'],
            'class': o['class'],
            'method': o['class']['method'][ast.name.name],
            'block': o['class']['method'][ast.name.name]['body']
        }

        for param in env['method']['param']:
            env['block'][0][param] = {
                'type': env['method']['param'][param]['type'],
                'kind':  Data.INSTANCE(),
                'init': Data.UNDEFINED(),
                'const': False
            }
        self.visit(ast.body, env)
        GetReturnType().visitBlock(ast.body, o)
    # kind: SIKind, decl: StoreDecl (VarDecl or ConstDecl)
    def visitAttributeDecl(self, ast, o): pass
        # name = self.visit(ast.decl, o)
        # if not name is None:
        #     o['class']['attribute'][name]['kind'] = Data.INSTANCE()
            
    # variable: Id, varType: Type, varInit: Expr = None
    # ! This VarDecl visit is use only inside method declaration, not for attribute of class
    def visitVarDecl(self, ast:VarDecl, o):
        '''
        o = {
            'global': {}
            'class': {}
        }
        o['class']['attribute'][var_name] = {
            'kind': <INSTANCE> or <STATIC> // With global attribute, kind is <STATIC>
            'type': type of this attribute (INT, FLOAT,...)
            'init': initial type of this attribute, update later
            'const': boolean flag to know this attribte is constant or variable
        }
        '''
        name = ast.variable.name
        init = self.visit(ast.varInit, o) if ast.varInit else Data.UNDEFINED()
        typ = self.visit(ast.varType, o)
        if typ != init:
           raise TypeMismatchInStatement(ast)
        
        if name.startswith('$'):
            o['class']['attribute'][name]['init'] = init

        if not name.startswith('$'):
            if name in o['class']['attribute']:
                raise Redeclared(Attribute(), name)
            
            o['class']['attribute'][name] = {
                'type': typ,
                'init': init,
                'const': False
            }
            return name

    # constant: ID,  constType: Type,   value: Expr = None
    # ! This ConstDecl visit is use only inside method declaration, not for attribute of class
    def visitConstDecl(self, ast:ConstDecl, o):
        '''
        o['class']['attribute'][var_name] = {
            'kind': <INSTANCE> or <STATIC> // With global attribute, kind is <STATIC>
            'type': type of this attribute (INT, FLOAT,...)
            'init': initial type of this attribute, update later
            'const': boolean flag to know this attribte is constant or variable
        }
        '''
        name = ast.constant.name
        if ast.value is None:
            raise IllegalConstantExpression(None)
        init = self.visit(ast.value, o)
        typ = self.visit(ast.constType, o)
        if typ != init:
           raise TypeMismatchInStatement(ast)
        
        if name.startswith('$'):
            o['class']['attribute'][name]['init'] = init
        if not name.startswith('$'):
            if name in o['class']['attribute']:
                raise Redeclared(Attribute(), name)
            
            o['class']['attribute'][name] = {
                'type': typ,
                'init': init,
                'const': True
            }
            return name
        
    def visitId(self, ast, o):
        return ast.name
        
    # op: str,  left: Expr,     right: Expr
    def visitBinaryOp(self, ast, o):
        left = self.visit(ast.left, o)
        right = self.visit(ast.right, o)
        op = ast.op
        if op in ['%']:
            if left == Data.INT() and right == Data.INT():
                return Data.INT()
        if op in ['+', '-', '*', '/']:
            if left == Data.INT() and right == Data.INT():
                return Data.INT()
            if left in [Data.INT(), Data.FLOAT()] and right in [Data.INT(), Data.FLOAT()]:       
                return Data.FLOAT()
        if op in ['&&', '||']:
            if left == Data.BOOL() and right == Data.BOOL():
                return Data.BOOL()
        if op in ['==', '!=']:
            if left == right and left in [Data.INT(), Data.BOOL()]:
                return Data.BOOL()
        if op in ['>', '<', '>=', '<=']:
            if left in [Data.INT(), Data.FLOAT()] and right in [Data.INT(), Data.FLOAT()]:
                return Data.BOOL()

        if op == '==.':
            if left == right and left == Data.STRING():
                return Data.BOOL()
        if op == '+.':
            if left == right and left == Data.STRING():
                return Data.STRING()
        raise TypeMismatchInExpression(ast)
    
    # # op: str,  body: Expr
    def visitUnaryOp(self, ast, o):
        body = self.visit(ast.body, o)
        op = ast.op
        if op == '!' and body == Data.BOOL():
            return Data.BOOL()
        
        if op == '-' and body in [Data.INT(), Data.FLOAT()]:
            return body
        raise TypeMismatchInExpression(ast)
            
                
    # # obj: Expr,    method: Id, param: List[Expr]
    def visitCallExpr(self, ast, param):

        return None
    # classname: Id,    param: List[Expr]
    def visitNewExpr(self, ast, o):
        class_name = ast.classname.name
        if not class_name in o['global']:
            raise Undeclared(Class(), class_name)
        
        # Check if don't have Constructor in class declare
        if not 'Constructor' in o['global'][class_name]['method']:
            raise Undeclared(Method(), 'Constructor')
        
        # Check for argument and parameter matching
        # paramEnv is list of dict param declare
        param_env = o['global'][class_name]['method']['Constructor']['param']
        
        # [<INT>, <FLOAT>,...] for example
        list_param_type = [param_env[par_name]['type'] for par_name in param_env]
        
        argument_type = [self.visit(arg, o) for arg in ast.param]
        if len(argument_type) != len(param_env):
            raise TypeMismatchInExpression(ast)
        
        for i in range(len(list_param_type)):
            if list_param_type[i] != argument_type[i]:
                raise TypeMismatchInExpression(ast)
        return Data.CLASS(class_name)
    
    # arr: Expr,    idx: List[Expr]
    def visitArrayCell(self, ast, o):
        arr = self.visit(ast.arr, o)
        list_idx = [self.visit(idx, o) for idx in ast.idx]
        #  array type example: [1][2]<INT>
        if arr[0] != '[':
            raise TypeMismatchInExpression(ast)
        for idx in list_idx:
            if idx != Data.INT():
                raise TypeMismatchInExpression(ast)
        
        while arr[0] != ']':
            arr = arr[1:]
        return arr[1:]

        return None
    
    # obj: Expr,    fieldname: Id
    def visitFieldAccess(self, ast, o):
        obj_type = self.visit(ast.obj, o)
        field_name_type = self.visit(ast.fieldname, o)
        # Check static attribute access
        return field_name_type
    
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
    def visitIntType(self, ast, o):
        return Data.INT()
    def visitFloatType(self, ast, o):
        return Data.FLOAT()
    def visitBoolType(self, ast, o):
        return Data.BOOL()
    def visitStringType(self, ast, o):
        return Data.STRING()
    def visitArrayType(self, ast, o):
        return Data.ARRAY(ast.size, self.visit(ast.eleType, o))
    def visitClassType(self, ast, o):
        return Data.CLASS(self.visit(ast.classname, o))
    def visitVoidType(self, ast, o):
        return Data.VOID()

