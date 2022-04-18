"""
 * @author nhphung
"""
from dataclasses import field
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
def toJSON(data, typ = None):
    if typ == 't':
        try:
            print(json.dumps(data, sort_keys=False, indent=4))
        except Exception as e:
            print(e)
    else:
        f = open('./main/d96/checker/param.json', 'w', encoding='utf-8')
        try:
            f.write(json.dumps(data, sort_keys=False, indent=4))
        except Exception as e:
            f.write(e)
        finally:
            f.close()
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

class ForLoopChecker(BaseVisitor, Utils):
    def visitAssign(self, ast, o): pass
    def visitIf(self, ast, o):
        self.visit(ast.thenStmt, o)
        if ast.elseStmt is None: return
        self.visit(ast.elseStmt, o)
    def visitFor(self, ast, o):
        self.visit(ast.loop, ['For'] + o)
    def visitBreak(self, ast, o):
        if not 'For' in o: raise MustInLoop(ast)
    def visitContinue(self, ast, o):
        if not 'For' in o: raise MustInLoop(ast)
    def visitReturn(self, ast, o): pass
    def visitCallStmt(self, ast, o): pass
    def visitVarDecl(self, ast, o): pass
    def visitConstDecl(self, ast, o): pass
    def visitBlock(self, ast, o):
        for inst in ast.inst: 
            self.visit(inst, o)
        
#**** Visit all statics and method declares ****#
# * NO initial value check * #
class GetGlobalEnv(BaseVisitor, Utils):
    def visitProgram(self, ast, o):
        '''
        //** Param structure for global scope **//
            o = {
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
            'type': Data.VOID(), # will update return type later
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
        o['attribute'][name]['kind'] = self.visit(ast.kind, o)
     
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

# * Visit all initial expression of Attribute Declare * #
class GetClassExprType(BaseVisitor, Utils):
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
                'class_name_1': {
                    'attribute': {},
                    'method': {}
                },
                'class_name 2': {}
            }
        }
        '''
        class_env = {
            'global': o,
            'class': o[ast.classname.name]# <- current class visit
        }
        for mem in ast.memlist:
            self.visit(mem, class_env)
    # kind: SIKind, name: Id, param: List[VarDecl], body: Block
    def visitMethodDecl(self, ast, o):
        '''
        o = {
            'global': {},
            'class': {} <- current scope
        }
        '''
        method_name = ast.name.name
        # Make new environment traverse
        env = {
            'global': o['global'],
            'class': o['class'],
            'method': o['class']['method'][method_name],
            # block: [{}]
            'block': o['class']['method'][method_name]['body']
        }

        # Copy param declaration to body scope
        for key in env['method']['param'].keys():
            env['block'][0][key] = {
                'type': env['method']['param'][key]['type'],
                'kind': Data.INSTANCE(),
                'init': Data.UNDEFINED(),
                'const': False
            }
        ForLoopChecker().visitBlock(ast.body, [])
        GetMethodBlockEnv().visitBlock(ast.body, env)
    # kind: SIKind, decl: StoreDecl (VarDecl or ConstDecl)
    def visitAttributeDecl(self, ast, o):
        '''
        o = {
            'global': {
                'class_name': {
                    'attribute': {},
                    'method': {}
                }
            },
            'class': {}
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
            },
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
        typ = o['class']['attribute'][name]['type']
        init = self.visit(ast.varInit, o) if ast.varInit else Data.UNDEFINED()
        
        if typ.startswith('<CLASS>'):
            o['class']['attribute'][name].update({'init': init})

        elif init != Data.UNDEFINED():
            if typ != init:
                raise TypeMismatchInStatement(ast)
            o['class']['attribute'][name].update({'init': init})

    # constant: ID,  constType: Type,   value: Expr = None
    def visitConstDecl(self, ast:ConstDecl, o):
        '''
        o = {
            'global': {
                'class_name': {
                    'attribute': {},
                    'method': {}
                }
            },
            'class': {}
        }
        ['attribute'][const_name] = {
            'kind': <INSTANCE> or <STATIC> // With global attribute, kind is <STATIC>
            'type': type of this attribute (INT, FLOAT,...)
            'init': initial type of this attribute, update later
            'const': boolean flag to know this attribte is constant or variable
        }
        '''
       
        name = ast.constant.name
        typ = o['class']['attribute'][name]['type']
        init = self.visit(ast.value, o)
        if typ != init:
            raise TypeMismatchInStatement(ast)
        o['class']['attribute'][name].update({'init': init})
    
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
            'class': {}
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
    def visitFieldAccess(self, ast, o):
        obj_type = self.visit(ast.obj, o)
        # Check if obj is class name for static access
        obj_name = obj_type
        if obj_type.startswith('<CLASS>'):
            obj_name = obj_type[-2:-1]
        if (obj_name[0] == '<' and obj_name[-1] == '>') or obj_name[0] == '[':
            raise IllegalMemberAccess(ast)
        
        if not obj_name in o['global']:
            raise Undeclared(Class(), obj_name)
        
        attr = ast.fieldname.name
        if not attr in o['global'][obj_name]['attribute']:
            raise Undeclared(Attribute(), attr)
        
        # If attr is instance member, check this attr is in curent class or its superclass
        if attr in o['global'][obj_name]['attribute'] and o['global'][obj_name]['attribute'][attr]['kind'] == Data.INSTANCE():
            # Check inside class first
            if not attr in o['class']['attribute']:
                parent = o['global'][obj_name]['parent']
                if parent in o['global']:
                    if not attr in o['global'][parent]['attribute']:
                        raise Undeclared(Attribute(), attr)
                    return o['global'][parent]['attribute']
            else:
                return o['class']['attribute'][attr]['type']  

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

    '''DATA TYPE'''
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

class GetMethodBlockEnv(BaseVisitor, Utils):
    # variable: Id, varType: Type, varInit: Expr = None
    def visitVarDecl(self, ast:VarDecl, o):
        '''
        o = {
            'global': {
                'class_name': {
                    'attribute': {},
                    'method': {}
                }
            },
            'class': {
                'attribute': {},
                'method': {}
            },
            'method': {} <- current scope
            'block': [{}] <- current scope
        }
        '''
        name = ast.variable.name
        typ = self.visit(ast.varType, o)
        init = self.visit(ast.varInit, o) if ast.varInit else Data.UNDEFINED()
        

        if init != Data.UNDEFINED() and not typ.startswith('<CLASS>'):
            if typ != init:
                raise TypeMismatchInStatement(ast)
        
        o['block'][0][name] = {
            'type': typ,
            'kind': Data.INSTANCE(),
            'const': False,
            'init': init
        }
    # constant: ID,  constType: Type,   value: Expr = None
    def visitConstDecl(self, ast:ConstDecl, o):
        '''
        o = {
            'global': {
                'class_name': {
                    'attribute': {},
                    'method': {}
                }
            },
            'class': {},
            'method': {},
            'block': {}
        }
        '''
       
        name = ast.constant.name
        if ast.value is None:
            raise IllegalConstantExpression(None)
        typ = self.visit(ast.constType, o)
        init = self.visit(ast.value, o)
        if typ != init:
            raise TypeMismatchInStatement(ast)
        
        o['block'][0][name] = {
            'type': typ,
            'kind': Data.INSTANCE(),
            'init': init,
            'const': False
        }
    
    # * STATEMENTS * #

    # lhs: Expr, exp: Expr
    def visitAssign(self, ast, o):
        lhs = self.visit(ast.lhs, o)
        rhs = self.visit(ast.exp, o)
        lhs_type = ''
        rhs_type = ''
        if isinstance(lhs, dict):
            lhs_type = lhs['type']
        if isinstance(rhs, dict):
            rhs_type = rhs['type']
        
        
        
    # expr: Expr,   thenStmt: Stmt, elseStmt: Stmt = None
    def visitIf(self, ast, o):
        expr = self.visit(ast.expr, o)
        if expr != Data.BOOL():
            raise TypeMismatchInStatement(ast)
        
        env = {
            'global': o['global'],
            'class': o['class'],
            'method': o['method'],
            'block': o['block']
        }
        env['block'] = [{}] + env['block']
        self.visit(ast.thenStmt, env)

        if not ast.elseStmt is None:
            env = {
                'global': o['global'],
                'class': o['class'],
                'method': o['method'],
                'block': o['block']
            }
            env['block'] = [{}] + env['block']
            self.visit(ast.elseStmt, env)
    # id: Id, expr1: Expr, expr2: Expr, loop: Stmt, exp3: Expr = None
    def visitFor(self, ast, o):
        id_name = ast.id.name
        id_dict = {}
        for block in o['block']:
            if id_name in block:
                id_dict = block[id_name]
        if id_dict == {}:
            raise Undeclared(Variable(), id_name)
        if id_dict['const'] == True:
            raise CannotAssignToConstant(Assign(ast.id, ast.expr1))
        
        exp1 = self.visit(ast.expr1, o)
        exp2 = self.visit(ast.expr2, o)
        if id_dict['type'] != Data.INT() or exp1 != Data.INT() or exp2 != Data.INT():
            raise TypeMismatchInStatement(ast)
        
        env = {
            'global': o['global'],
            'class': o['class'],
            'method': o['method'],
            'block': o['block']
        }

        env['block'] = [{ id_name: id_dict }] + env['block']
        self.visit(ast.loop, env)

    def visitBreak(self, ast, o): pass
    def visitContinue(self, ast, o): pass
    # expr: Expr = None
    def visitReturn(self, ast, o):
        return_type = self.visit(ast.expr, o) if ast.expr else Data.VOID()
        o['method']['type'] = return_type
    
    # obj: Expr, method: Id, param: List[Expr]
    def visitCallStmt(self, ast, o):
        obj = self.visit(ast.obj, o)
        if isinstance(obj, dict):
            if not obj['type'].startswith('<CLASS>'):
                raise TypeMismatchInStatement(ast)
            
    def visitBlock(self, ast, o):
        for inst in ast.inst:
            self.visit(inst, o)

    # * EXPRESSION * #
    #name: str
    def visitId(self, ast, o):
        name = ast.name
        if 'block' in o:
            for block in o['block']:
                if name in block:
                    return block[name]
                    # 'name': {
                    #   'type', 'kind', 'init', 'const'
                    # }
        
        raise Undeclared(Identifier(), name)
    # op: str,  left: Expr,     right: Expr
    def visitBinaryOp(self, ast, o):
        left = self.visit(ast.left, o)
        right = self.visit(ast.right, o)
        if isinstance(left, dict):
            left = left['type']
        if isinstance(right, dict):
            right = right['type']
        
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
        if isinstance(body, dict):
            body = body['type']
        op = ast.op
        if op == '!' and body == Data.BOOL():
            return Data.BOOL()
        
        if op == '-' and body in [Data.INT(), Data.FLOAT()]:
            return body
        raise TypeMismatchInExpression(ast)
                     
    # # obj: Expr,    method: Id, param: List[Expr]
    def visitCallExpr(self, ast, o):
        # ast.obj now is a Identifier
        obj = ''
        if hasattr(ast.obj, 'name'):
            name = ast.obj.name
            if 'block' in o:
                for block in o['block']:
                    if name in block:
                        obj = block[name]['type']
            
            if obj == '' and name in o['global']:
                obj = Data.CLASS(name)
            if obj == '':
                raise Undeclared(Identifier(), name)

        else: obj = self.visit(ast.obj, o)

        if not obj.startswith('<CLASS>') or obj[0] == '[':
            raise TypeMismatchInExpression(ast)
        
        if obj.startswith('<CLASS>'):
            if not obj[8:-1] in o['global']:
                raise Undeclared(Class(), obj[8:-1])
        
        field_name = ast.fieldname.name
        env = o['global'][obj[8:-1]]

        # Instance access, that mean, obj is a object of class, not a class name
        current_class = o['class']
        # A subclass is able to access attribute of superclass
        while current_class != env:
            parent = current_class['parent']
            if parent == '': 
                Undeclared(Attribute(), field_name)
            current_class = o['global'][parent]

        # If kind is 'Static', that mean field_name may be a static attribute, so I must check all static attribute in global scope
        if field_name.startswith('$'):
            for global_class_name in o['global']:
                if field_name in o['global'][global_class_name]['attribute']:
                    if o['global'][global_class_name]['attribute'][field_name]['kind'] == Data.STATIC():
                        return o['global'][global_class_name]['attribute'][field_name]['type']
            raise Undeclared(Attribute(), field_name)
        
        parent = obj[8:-1]
        while True:
            #field: s
            if field_name in env['attribute']:
                return env['attribute'][field_name]['type']
            
            parent = o['global'][parent]['parent']
            if parent == '': raise Undeclared(Attribute(), field_name)
            env = o['global'][parent]

    
    # classname: Id,    param: List[Expr]
    def visitNewExpr(self, ast, o):
        '''
        o = {
            'global': {}
            'class': {}
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

        argument_type = list(map(lambda ele: ele['type'] if isinstance(ele, dict) else ele, argument_type))

        if len(argument_type) != len(param_env):
            raise TypeMismatchInExpression(ast)
        
        for i in range(len(list_param_type)):
            if list_param_type[i] != argument_type[i]:
                raise TypeMismatchInExpression(ast)
        return Data.CLASS(class_name)
    
    # arr: Expr,    idx: List[Expr]
    def visitArrayCell(self, ast, o):
        arr = self.visit(ast.arr, o)
        if isinstance(arr, dict):
            arr = arr['type']
        list_idx = [self.visit(idx, o) for idx in ast.idx]
        list_idx = list(map(lambda ele: ele['type'] if isinstance(ele, dict) else ele, list_idx))
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
    def visitFieldAccess(self, ast, o):
        # ast.obj now is a Identifier
        obj = ''
        # FieldAccess(A, s)
        if hasattr(ast.obj, 'name'):
            name = ast.obj.name
            if 'block' in o:
                for block in o['block']:
                    if name in block:
                        obj = block[name]['type']
            if obj == '' and name in o['global']:
                obj = Data.CLASS(name)
            if obj == '':
                raise Undeclared(Identifier(), name)

        else: obj = self.visit(ast.obj, o)

        if not obj.startswith('<CLASS>') or obj[0] == '[':
            raise TypeMismatchInExpression(ast)
        
        if obj.startswith('<CLASS>'):
            if not obj[8:-1] in o['global']:
                raise Undeclared(Class(), obj[8:-1])
        
        field_name = ast.fieldname.name
        
        # If kind is 'Static', that mean field_name may be a static attribute, so I must check all static attribute in global scope
        if field_name.startswith('$'):
            for global_class_name in o['global']:
                if field_name in o['global'][global_class_name]['attribute']:
                    if o['global'][global_class_name]['attribute'][field_name]['kind'] == Data.STATIC():
                        return o['global'][global_class_name]['attribute'][field_name]['type']
            raise Undeclared(Attribute(), field_name)

        # Instance access, that mean, obj is a object of class, not a class name
        env = o['global'][obj[8:-1]]
        current_class = o['class']
        # A subclass is able to access attribute of superclass
        while current_class != env:
            parent = current_class['parent']
            if parent == '': 
                Undeclared(Attribute(), field_name)
            current_class = o['global'][parent]

        
        
        parent = obj[8:-1]
        while True:
            #field: s
            if field_name in env['attribute']:
                return env['attribute'][field_name]['type']
            
            parent = o['global'][parent]['parent']
            if parent == '': raise Undeclared(Attribute(), field_name)
            env = o['global'][parent]
 
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
        list_type = list(map(lambda ele: ele['type'] if isinstance(ele, dict) else ele, list_type))
        example_type = ''
        if len(list_type) != 0:
            example_type = list_type[0]
            for each_type in list_type[1:]:
                if each_type != example_type:
                    raise IllegalArrayLiteral(ast)
        return Data.ARRAY(len(list_type), example_type)

    '''DATA TYPE'''
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
        return Data.CLASS(ast.classname.name)
    def visitVoidType(self, ast, o):
        return Data.VOID()

# ********* MAIN CLASS STATIC CHECKER ********* #
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
        env = GetClassExprType().visitProgram(ast, o)
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

