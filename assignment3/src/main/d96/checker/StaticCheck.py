"""
 * @author nhphung
"""
#*********************************
from AST import *
from Visitor import *
# from Utils import Utils
from StaticError import *
import json
#*********************************
class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value
# (Optional) function to print checking param as json
def toJSON(data, typ=None):
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
    def ARRAY(size, eleType): return '[' + str(size) + ']' + eleType
    def SELF(): return '<SELF>'
    def CLASS(name): return '<CLASS>(' + name + ')'
    def VOID(): return '<VOID>'
    def METHOD(): return '<METHOD>'
    def STATIC(): return '<STATIC>'
    def INSTANCE(): return '<INSTANCE>'
    def UNDEFINED(): return None

class ForLoopChecker(BaseVisitor):
    def visitAssign(self, ast, o): pass

    def visitIf(self, ast, o):
        self.visit(ast.thenStmt, o)
        if ast.elseStmt is None:
            return
        self.visit(ast.elseStmt, o)

    def visitFor(self, ast, o):
        self.visit(ast.loop, ['For'] + o)

    def visitBreak(self, ast, o):
        if not 'For' in o:
            raise MustInLoop(ast)

    def visitContinue(self, ast, o):
        if not 'For' in o:
            raise MustInLoop(ast)

    def visitReturn(self, ast, o): pass
    def visitCallStmt(self, ast, o): pass
    def visitVarDecl(self, ast, o): pass
    def visitConstDecl(self, ast, o): pass

    def visitBlock(self, ast, o):
        for inst in ast.inst:
            self.visit(inst, o)
# * Visit all initial expression of Attribute Declare * #
# **************************************
#                                      *
# *             GET LHS                *
#                                      *
# **************************************
class GetLHS(BaseVisitor):
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
            if left['const'] == True:
                left = left['type']
            else: raise IllegalConstantExpression(ast)
        if isinstance(right, dict):
            if right['const'] == True:
                right = right['type']
            else: raise IllegalConstantExpression(ast)
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
            if body['const'] == True:
                body = body['type']
            else: raise IllegalConstantExpression(ast)
        op = ast.op
        if op == '!' and body == Data.BOOL():
            return Data.BOOL()

        if op == '-' and body in [Data.INT(), Data.FLOAT()]:
            return body
        raise TypeMismatchInExpression(ast)

    # obj: Expr,    method: Id, param: List[Expr]
    def visitCallExpr(self, ast, o):
        obj = ''
        kind = Data.INSTANCE()
        # ast.obj now is a Identifier
        if hasattr(ast.obj, 'name'):
            name = ast.obj.name
            # * If obj was declared in block scope
            if 'block' in o:
                for block in o['block']:
                    if name in block:
                        obj = block[name]['type']
            # * obj empty and the name is a class name
            if obj == '' and name in o['global']:
                obj = Data.CLASS(name)
                # * Mean that, if obj is a class name but its method invocation in 'instance' kind
                if ast.method.name[0] != '$':
                    raise IllegalMemberAccess(ast)
                kind = Data.STATIC()
            if obj != '' and kind == Data.INSTANCE() and ast.method.name[0] == '$': raise Undeclared(Class(), name)
            if obj == '': raise Undeclared(Identifier(), name)

        else: obj = self.visit(ast.obj, o)
        if not obj.startswith('<CLASS>') or obj[0] == '[':
            raise TypeMismatchInExpression(ast)
        if obj.startswith('<CLASS>') and not obj[8:-1] in o['global']:
            raise Undeclared(Class(), obj[8:-1])
        
        method_name = ast.method.name
#       * If kind is 'instance', that mean, 'obj' is a object of class, not a class name
#       * If kind is 'Static', 'obj' is now class name
#       * A subclass is able to access attribute of superclass
        parent = obj[8:-1]
        while True:
            if method_name in o['global'][parent]['method']:
                param_env = o['global'][parent]['method'][method_name]['param']
                arg_env = [self.visit(arg, o) for arg in ast.param]
                # * Check type matching of parameter and argument
                StaticChecker.matchArgumentType(ast, param_env, arg_env)
                if o['global'][parent]['method'][method_name]['type'] != Data.VOID():
                    return o['global'][parent]['method'][method_name]['type']  
                else: raise TypeMismatchInExpression(ast)
            parent = o['global'][parent]['parent']
            if parent == '': 
                raise Undeclared(Attribute(), method_name)

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
            raise Undeclared(SpecialMethod(), 'Constructor')

        # Check for argument and parameter matching
        # paramEnv is list of dict param declare
        param_env = o['global'][class_name]['method']['Constructor']['param']
        argument_type = [self.visit(arg, o) for arg in ast.param]

        StaticChecker.matchArgumentType(ast, param_env, argument_type)
        # [<INT>, <FLOAT>,...] for example
        return Data.CLASS(class_name)

    # arr: Expr,    idx: List[Expr]
    def visitArrayCell(self, ast, o):
        arr = self.visit(ast.arr, o)
        if isinstance(arr, dict):
            arr = arr['type']
        list_idx = list(
            map(lambda ele: ele['type'] if isinstance(ele, dict) else ele, [self.visit(idx, o) for idx in ast.idx]))

        if arr[0] != '[':
            raise TypeMismatchInExpression(ast)
        for idx in list_idx:
            if idx != Data.INT():
                raise TypeMismatchInExpression(ast)

        '''Get type of element in array base on list of index access'''
        for _ in list_idx:
            if arr[0] != '[':
                raise TypeMismatchInExpression(ast)
            while arr[0] != ']':
                arr = arr[1:]
            arr = arr[1:]
        return arr

    # obj: Expr,    fieldname: Id
    def visitFieldAccess(self, ast, o):
        # ast.obj now is a Identifier
        obj = ''
        kind = Data.INSTANCE()
        # FieldAccess(A, s)
        if hasattr(ast.obj, 'name'):
            name = ast.obj.name
            # * If obj is a variable
            # * which is declared in block scope
            if 'block' in o:
                for block in o['block']:
                    if name in block:
                        obj = block[name]['type']
            # * Undeclaration of obj but
            # * 'name' is a class name
            if obj == '' and name in o['global']:
                obj = Data.CLASS(name)
                # * When obj is a class name, that mean,
                # * this is a static access attribute
                if ast.fieldname.name[0] != '$':
                    raise IllegalMemberAccess(ast)
                kind = Data.STATIC()
            if obj != '' and kind == Data.INSTANCE() and ast.fieldname.name[0] == '$': raise Undeclared(Class(), name)
            if obj == '' and ast.fieldname.name[0] == '$': raise Undeclared(Class(), name)
            if obj == '' and ast.fieldname.name[0] != '$':
                raise Undeclared(Identifier(), name)

        else: obj = self.visit(ast.obj, o)
        if isinstance(obj, dict):
            obj = obj['type']
        if not obj.startswith('<CLASS>') or obj[0] == '[':
            raise TypeMismatchInExpression(ast)
        if obj.startswith('<CLASS>') and not obj[8:-1] in o['global']:
            raise Undeclared(Class(), obj[8:-1])

        field_name = ast.fieldname.name
#    * Instance access, obj is an object of class, not a class name
#    * A subclass is able to access attribute of superclass
        parent = obj[8:-1]
        while True:
            if field_name in o['global'][parent]['attribute']:
                return o['global'][parent]['attribute'][field_name]
               
            parent = o['global'][parent]['parent']
            if parent == '':
                raise Undeclared(Attribute(), field_name)

    '''LITERALS'''
    def visitInstance(self, ast, o): return Data.INSTANCE()
    def visitStatic(self, ast, o): return Data.STATIC()
    def visitIntLiteral(self, ast, o): return Data.INT()
    def visitFloatLiteral(self, ast, o): return Data.FLOAT()
    def visitStringLiteral(self, ast, o): return Data.STRING()
    def visitBooleanLiteral(self, ast, o): return Data.BOOL()
    def visitNullLiteral(self, ast, o): return Data.NULL()

    def visitSelfLiteral(self, ast, o):
        for class_name in o['global'].keys():
            if o['global'][class_name] == o['class']:
                return Data.CLASS(class_name)
    # value: List[Expr]

    def visitArrayLiteral(self, ast, o):
        list_type = list(
            map(lambda ele: ele['type'] if isinstance(ele, dict) else ele, [self.visit(ele, o) for ele in ast.value]))
        example_type = ''
        if len(list_type) != 0:
            example_type = list_type[0]
            for each_type in list_type[1:]:
                if each_type != example_type:
                    raise IllegalArrayLiteral(ast)
        return Data.ARRAY(len(list_type), example_type)
    
    '''DATA TYPE'''
    def visitIntType(self, ast, o): return Data.INT()
    def visitFloatType(self, ast, o): return Data.FLOAT()
    def visitBoolType(self, ast, o): return Data.BOOL()
    def visitStringType(self, ast, o): return Data.STRING()
    def visitArrayType(self, ast, o):
        return Data.ARRAY(ast.size, self.visit(ast.eleType, o))
    def visitClassType(self, ast, o):
        return Data.CLASS(ast.classname.name)
    def visitVoidType(self, ast, o): return Data.VOID()

# **************************************
#                                      *
# *         GET TYPE OF CONSTANT       *
#                                      *
# **************************************
class GetTypeConstant(BaseVisitor):
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
            if left['const'] == True:
                left = left['type']
            else: raise IllegalConstantExpression(ast)
        if isinstance(right, dict):
            if right['const'] == True:
                right = right['type']
            else: raise IllegalConstantExpression(ast)
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
            if body['const'] == True:
                body = body['type']
            else: raise IllegalConstantExpression(ast)
        op = ast.op
        if op == '!' and body == Data.BOOL():
            return Data.BOOL()

        if op == '-' and body in [Data.INT(), Data.FLOAT()]:
            return body
        raise TypeMismatchInExpression(ast)

    # obj: Expr,    method: Id, param: List[Expr]
    def visitCallExpr(self, ast, o):
        obj = ''
        kind = Data.INSTANCE()
        # ast.obj now is a Identifier
        if hasattr(ast.obj, 'name'):
            name = ast.obj.name
            # * If obj was declared in block scope
            if 'block' in o:
                for block in o['block']:
                    if name in block:
                        obj = block[name]['type']
            # * obj empty and the name is a class name
            if obj == '' and name in o['global']:
                obj = Data.CLASS(name)
                # * Mean that, if obj is a class name but its method invocation in 'instance' kind
                if ast.method.name[0] != '$':
                    raise IllegalMemberAccess(ast)
                kind = Data.STATIC()
            if obj != '' and kind == Data.INSTANCE() and ast.method.name[0] == '$': raise Undeclared(Class(), name)
            if obj == '': raise Undeclared(Identifier(), name)

        else: obj = self.visit(ast.obj, o)
        if not obj.startswith('<CLASS>') or obj[0] == '[':
            raise TypeMismatchInExpression(ast)
        if obj.startswith('<CLASS>') and not obj[8:-1] in o['global']:
            raise Undeclared(Class(), obj[8:-1])
        
        method_name = ast.method.name
#       * If kind is 'instance', that mean, 'obj' is a object of class, not a class name
#       * If kind is 'Static', 'obj' is now class name
#       * A subclass is able to access attribute of superclass
        parent = obj[8:-1]
        while True:
            if method_name in o['global'][parent]['method']:
                param_env = o['global'][parent]['method'][method_name]['param']
                arg_env = [self.visit(arg, o) for arg in ast.param]
                # * Check type matching of parameter and argument
                StaticChecker.matchArgumentType(ast, param_env, arg_env)
                if o['global'][parent]['method'][method_name]['type'] != Data.VOID():
                    return o['global'][parent]['method'][method_name]['type']  
                else: raise TypeMismatchInExpression(ast)
            parent = o['global'][parent]['parent']
            if parent == '': 
                raise Undeclared(Attribute(), method_name)

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
            raise Undeclared(SpecialMethod(), 'Constructor')

        # Check for argument and parameter matching
        # paramEnv is list of dict param declare
        param_env = o['global'][class_name]['method']['Constructor']['param']
        argument_type = [self.visit(arg, o) for arg in ast.param]

        StaticChecker.matchArgumentType(ast, param_env, argument_type)
        # [<INT>, <FLOAT>,...] for example
        return Data.CLASS(class_name)

    # arr: Expr,    idx: List[Expr]
    def visitArrayCell(self, ast, o):
        arr = self.visit(ast.arr, o)
        if isinstance(arr, dict):
            if arr['const'] == True:
                arr = arr['type']
            else: raise IllegalConstantExpression(ast)
        list_idx = [self.visit(idx, o) for idx in ast.idx]
        list_idx = list(
            map(lambda ele: ele['type'] if isinstance(ele, dict) else ele, list_idx))
        #  array type example: [1][2]<INT>
        if arr[0] != '[':
            raise TypeMismatchInExpression(ast)
        for idx in list_idx:
            if idx != Data.INT():
                raise TypeMismatchInExpression(ast)
        for _ in list_idx:
            if arr[0] != '[':
                raise TypeMismatchInExpression(ast)
            while arr[0] != ']':
                arr = arr[1:]
            arr = arr[1:]
        return arr

    # obj: Expr,    fieldname: Id
    def visitFieldAccess(self, ast, o):
        # ast.obj now is a Identifier
        obj = ''
        kind = Data.INSTANCE()
        # FieldAccess(A, s)
        if hasattr(ast.obj, 'name'):
            name = ast.obj.name
            # * If obj is a variable
            # * which is declared in block scope
            if 'block' in o:
                for block in o['block']:
                    if name in block:
                        if block[name]['const'] == True:
                            obj = block[name]['type']
                        else:
                            raise IllegalConstantExpression(ast)

            # * Undeclaration of obj but
            # * 'name' is a class name
            if obj == '' and name in o['global']:
                obj = Data.CLASS(name)
                # * When obj is a class name, that mean,
                # * this is a static access attribute
                if ast.fieldname.name[0] != '$':
                    raise IllegalMemberAccess(ast)
                kind = Data.STATIC()
            if obj != '' and kind == Data.INSTANCE() and ast.fieldname.name[0] == '$': raise Undeclared(Class(), name)
            if obj == '' and ast.fieldname.name[0] == '$': raise Undeclared(Class(), name)
            if obj == '' and ast.fieldname.name[0] != '$':
                raise Undeclared(Identifier(), name)

        else: obj = self.visit(ast.obj, o)
        if not obj.startswith('<CLASS>') or obj[0] == '[':
            raise TypeMismatchInExpression(ast)
        if obj.startswith('<CLASS>') and not obj[8:-1] in o['global']:
            raise Undeclared(Class(), obj[8:-1])

        field_name = ast.fieldname.name
#    * Instance access, obj is an object of class, not a class name
#    * A subclass is able to access attribute of superclass
        parent = obj[8:-1]
        while True:
            if field_name in o['global'][parent]['attribute']:
                if o['global'][parent]['attribute'][field_name]['const'] == True:
                    return o['global'][parent]['attribute'][field_name]['type']
                else:
                    raise IllegalConstantExpression(ast)
            parent = o['global'][parent]['parent']
            if parent == '':
                raise Undeclared(Attribute(), field_name)

    '''LITERALS'''
    def visitInstance(self, ast, o): return Data.INSTANCE()
    def visitStatic(self, ast, o): return Data.STATIC()
    def visitIntLiteral(self, ast, o): return Data.INT()
    def visitFloatLiteral(self, ast, o): return Data.FLOAT()
    def visitStringLiteral(self, ast, o): return Data.STRING()
    def visitBooleanLiteral(self, ast, o): return Data.BOOL()
    def visitNullLiteral(self, ast, o): return Data.NULL()

    def visitSelfLiteral(self, ast, o):
        for class_name in o['global'].keys():
            if o['global'][class_name] == o['class']:
                return Data.CLASS(class_name)
    # value: List[Expr]

    def visitArrayLiteral(self, ast, o):
        list_type = [self.visit(ele, o) for ele in ast.value]
        list_type = list(
            map(lambda ele: ele['type'] if isinstance(ele, dict) else ele, list_type))
        example_type = ''
        if len(list_type) != 0:
            example_type = list_type[0]
            for each_type in list_type[1:]:
                if each_type != example_type:
                    raise IllegalArrayLiteral(ast)
        return Data.ARRAY(len(list_type), example_type)
    
    '''DATA TYPE'''
    def visitIntType(self, ast, o): return Data.INT()
    def visitFloatType(self, ast, o): return Data.FLOAT()
    def visitBoolType(self, ast, o): return Data.BOOL()
    def visitStringType(self, ast, o): return Data.STRING()
    def visitArrayType(self, ast, o):
        return Data.ARRAY(ast.size, self.visit(ast.eleType, o))
    def visitClassType(self, ast, o):
        return Data.CLASS(ast.classname.name)
    def visitVoidType(self, ast, o): return Data.VOID()

# **************************************
#                                      *
# *          METHOD VISITOR            *
#                                      *
# **************************************
class GetMethodBlockEnv(BaseVisitor):
    # variable: Id, varType: Type, varInit: Expr = None
    def visitVarDecl(self, ast: VarDecl, o):
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
        if name in o['block'][0]:
            raise Redeclared(Variable(), name)
        typ = self.visit(ast.varType, o)
        init = self.visit(ast.varInit, o) if ast.varInit else Data.UNDEFINED()

        if isinstance(init, dict):
            init = init['type']
        if init != Data.UNDEFINED() and not typ.startswith('<CLASS>'):
            if typ == Data.FLOAT() and init in [Data.FLOAT(), Data.INT()]:
                init = typ
            if typ != init:
                raise TypeMismatchInStatement(ast)
        o['block'][0][name] = {
            'type': typ,
            'kind': Data.INSTANCE(),
            'const': False,
            'init': init
        }
    # constant: ID,  constType: Type,   value: Expr = None

    def visitConstDecl(self, ast: ConstDecl, o):
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
        if name in o['block'][0]:
            raise Redeclared(Constant(), name)
        if ast.value is None:
            raise IllegalConstantExpression(None)
        typ = self.visit(ast.constType, o)
        if ast.value is None:
            raise IllegalConstantExpression(None)
        init = ast.value.accept(GetTypeConstant(), o)
        if typ == Data.FLOAT() and init in [Data.FLOAT(), Data.INT()]:
            init = typ
        if typ != init:
            raise TypeMismatchInStatement(ast)

        o['block'][0][name] = {
            'type': typ,
            'kind': Data.INSTANCE(),
            'init': init,
            'const': True
        }

    # * STATEMENTS * #
    # lhs: Expr, exp: Expr
    # !TODO: when lhs is attribute access, its return type is a type of that attribute, check it again
    def visitAssign(self, ast, o):
        rhs = self.visit(ast.exp, o)
        lhs = ast.lhs.accept(GetLHS(), o)
        lhs_type = lhs
        rhs_type = rhs
        if isinstance(lhs, dict):
            lhs_type = lhs['type']
            if lhs['const'] == True:
                raise CannotAssignToConstant(ast)
        if isinstance(rhs, dict):
            rhs_type = rhs['type']

        
        # If lhs_type is Float, rhs_type can either Float or Int type
        if lhs_type == Data.FLOAT() and rhs_type in [Data.FLOAT(), Data.INT()]:
            lhs['init'] = rhs_type
            lhs['type'] = rhs_type
            lhs_type = rhs_type

        if lhs_type != rhs_type:
            raise TypeMismatchInStatement(ast)

        if isinstance(lhs, dict):
            lhs['init'] = rhs_type
            lhs['type'] = rhs_type
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

    def visitBreak(self, ast, o):
        if not '<FOR>' in o:
            raise MustInLoop(ast)

    def visitContinue(self, ast, o):
        if not '<FOR>' in o:
            raise MustInLoop(ast)
    # id: Id, expr1: Expr, expr2: Expr, loop: Stmt, exp3: Expr = None
    def visitFor(self, ast, o):
        id_name = ast.id.name
        id_dict = {}
        for block in o['block']:
            if id_name in block:
                id_dict = block[id_name]
                break
        if id_dict == {}:
            raise Undeclared(Variable(), id_name)
        if id_dict['const'] == True:
            raise CannotAssignToConstant(Assign(ast.id, ast.expr1))

        exp1 = self.visit(ast.expr1, o)
        exp2 = self.visit(ast.expr2, o)
        exp3 = self.visit(ast.expr3, o) if not ast.expr3 is None else Data.UNDEFINED()
        if id_dict['type'] != Data.INT() or exp1 != Data.INT() or exp2 != Data.INT() or (exp3 != Data.INT() and exp3 != Data.UNDEFINED()):
            raise TypeMismatchInStatement(ast)

        env = {
            'global': o['global'],
            'class': o['class'],
            'method': o['method'],
            'block': o['block'],
            '<FOR>': 1
        }

        env['block'] = [{id_name: id_dict}] + env['block']
        self.visit(ast.loop, env)

    # expr: Expr = None
    def visitReturn(self, ast, o):
        return_type = self.visit(ast.expr, o) if ast.expr else Data.VOID()
        if isinstance(return_type, dict):
            return_type = return_type['type']

        for key in o['class']['method']:
            if o['class']['method'][key] == o['method']:
                if key != 'Destructor':
                    o['method']['type'] = return_type

    def visitBlock(self, ast, o):
        for inst in ast.inst:
            self.visit(inst, o)

    # obj: Expr, method: Id, param: List[Expr]
    def visitCallStmt(self, ast, o):
        obj = ''
        kind = Data.INSTANCE()
        # ast.obj now is a Identifier
        if hasattr(ast.obj, 'name'):
            name = ast.obj.name
            # * If obj was declared in block scope
            if 'block' in o:
                for block in o['block']:
                    if name in block:
                        obj = block[name]['type']
            # * obj empty and the name is a class name
            if obj == '' and name in o['global']:
                obj = Data.CLASS(name)
                # * Mean that, if obj is a class name but its method invocation in 'instance' kind
                if ast.method.name[0] != '$':
                    raise IllegalMemberAccess(ast)
                kind = Data.STATIC()
            if obj != '' and kind == Data.INSTANCE() and ast.method.name[0] == '$': raise Undeclared(Class(), name)
            if obj == '': raise Undeclared(Identifier(), name)

        else: obj = self.visit(ast.obj, o)
        if not obj.startswith('<CLASS>') or obj[0] == '[':
            raise TypeMismatchInExpression(ast)
        if obj.startswith('<CLASS>') and not obj[8:-1] in o['global']:
            raise Undeclared(Class(), obj[8:-1])
        
        method_name = ast.method.name
#       * If kind is 'instance', that mean, 'obj' is a object of class, not a class name
#       * If kind is 'Static', 'obj' is now class name
#       * A subclass is able to access attribute of superclass
        parent = obj[8:-1]
        while True:
            if method_name in o['global'][parent]['method']:
                param_env = o['global'][parent]['method'][method_name]['param']
                arg_env = [self.visit(arg, o) for arg in ast.param]
                # * Check type matching of parameter and argument
                StaticChecker.matchArgumentType(ast, param_env, arg_env)
                if o['global'][parent]['method'][method_name]['type'] == Data.VOID():
                    return o['global'][parent]['method'][method_name]['type']  
                else: raise TypeMismatchInStatement(ast)
            parent = o['global'][parent]['parent']
            if parent == '': 
                raise Undeclared(Attribute(), method_name)

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

    def matchArgumentType(self, ast, param_env_list, arg_list):
        # Check for argument and parameter matching
        # [<INT>, <FLOAT>,...] for example
        list_param_type = [param_env_list[par_name]['type']
                           for par_name in param_env_list]

        list_argument_type = list(
            map(lambda ele: ele['type'] if isinstance(ele, dict) else ele, arg_list))

        if len(list_argument_type) != len(param_env_list):
            raise TypeMismatchInExpression(ast)
        for i in range(len(list_param_type)):
            if list_param_type[i] == Data.FLOAT() and list_argument_type[i] in [Data.FLOAT(), Data.INT()]:
                list_param_type[i] = list_argument_type[i]
            if list_param_type[i] != list_argument_type[i]:
                raise TypeMismatchInExpression(ast)
    # # obj: Expr,    method: Id, param: List[Expr]

    def visitCallExpr(self, ast, o):
        obj = ''
        kind = Data.INSTANCE()
        # ast.obj now is a Identifier
        if hasattr(ast.obj, 'name'):
            name = ast.obj.name
            # * If obj was declared in block scope
            if 'block' in o:
                for block in o['block']:
                    if name in block:
                        obj = block[name]['type']
            # * obj empty and the name is a class name
            if obj == '' and name in o['global']:
                obj = Data.CLASS(name)
                # * Mean that, if obj is a class name but its method invocation in 'instance' kind
                if ast.method.name[0] != '$':
                    raise IllegalMemberAccess(ast)
                kind = Data.STATIC()
            if obj != '' and kind == Data.INSTANCE() and ast.method.name[0] == '$': raise Undeclared(Class(), name)
            if obj == '': raise Undeclared(Identifier(), name)

        else: obj = self.visit(ast.obj, o)
        if not obj.startswith('<CLASS>') or obj[0] == '[':
            raise TypeMismatchInExpression(ast)
        if obj.startswith('<CLASS>') and not obj[8:-1] in o['global']:
            raise Undeclared(Class(), obj[8:-1])
        
        method_name = ast.method.name
#       * If kind is 'instance', that mean, 'obj' is a object of class, not a class name
#       * If kind is 'Static', 'obj' is now class name
#       * A subclass is able to access attribute of superclass
        parent = obj[8:-1]
        while True:
            if method_name in o['global'][parent]['method']:
                param_env = o['global'][parent]['method'][method_name]['param']
                arg_env = [self.visit(arg, o) for arg in ast.param]
                # * Check type matching of parameter and argument
                StaticChecker.matchArgumentType(ast, param_env, arg_env)
                if o['global'][parent]['method'][method_name]['type'] != Data.VOID():
                    return o['global'][parent]['method'][method_name]['type']  
                else: raise TypeMismatchInExpression(ast)
            parent = o['global'][parent]['parent']
            if parent == '': 
                raise Undeclared(Attribute(), method_name)

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
            raise Undeclared(SpecialMethod(), 'Constructor')

        # Check for argument and parameter matching
        # paramEnv is list of dict param declare
        param_env = o['global'][class_name]['method']['Constructor']['param']
        argument_type = [self.visit(arg, o) for arg in ast.param]

        StaticChecker.matchArgumentType(ast, param_env, argument_type)
        # [<INT>, <FLOAT>,...] for example
        return Data.CLASS(class_name)

    # arr: Expr,    idx: List[Expr]
    def visitArrayCell(self, ast, o):
        arr = self.visit(ast.arr, o)
        if isinstance(arr, dict):
            arr = arr['type']
        list_idx = [self.visit(idx, o) for idx in ast.idx]
        list_idx = list(
            map(lambda ele: ele['type'] if isinstance(ele, dict) else ele, list_idx))
        #  array type example: [1][2]<INT>
        if arr[0] != '[':
            raise TypeMismatchInExpression(ast)
        for idx in list_idx:
            if idx != Data.INT():
                raise TypeMismatchInExpression(ast)
        
        for _ in list_idx:
            if arr[0] != '[':
                raise TypeMismatchInExpression(ast)
            while arr[0] != ']':
                arr = arr[1:]
            arr = arr[1:]
        return arr

    # obj: Expr,    fieldname: Id
    def visitFieldAccess(self, ast, o):
        # ast.obj now is a Identifier
        obj = ''
        kind = Data.INSTANCE()
        # FieldAccess(A, s)
        if hasattr(ast.obj, 'name'):
            name = ast.obj.name
            # * If obj is a variable
            # * which is declared in block scope
            if 'block' in o:
                for block in o['block']:
                    if name in block: obj = block[name]['type']

            # * Undeclaration of obj but
            # * 'name' is a class name
            if obj == '' and name in o['global']:
                obj = Data.CLASS(name)
                # * When obj is a class name, that mean,
                # * this is a static access attribute
                if ast.fieldname.name[0] != '$':
                    raise IllegalMemberAccess(ast)
                kind = Data.STATIC()
            if obj != '' and kind == Data.INSTANCE() and ast.fieldname.name[0] == '$': raise Undeclared(Class(), name)
            if obj == '' and ast.fieldname.name[0] == '$': raise Undeclared(Class(), name)
            if obj == '' and ast.fieldname.name[0] != '$':
                raise Undeclared(Identifier(), name)

        else: obj = self.visit(ast.obj, o)
        if not obj.startswith('<CLASS>') or obj[0] == '[':
            raise TypeMismatchInExpression(ast)
        if obj.startswith('<CLASS>') and not obj[8:-1] in o['global']:
            raise Undeclared(Class(), obj[8:-1])

        field_name = ast.fieldname.name
#    * Instance access, obj is an object of class, not a class name
#    * A subclass is able to access attribute of superclass
        parent = obj[8:-1]
        while True:
            if field_name in o['global'][parent]['attribute']:
                return o['global'][parent]['attribute'][field_name]['type']
            parent = o['global'][parent]['parent']
            if parent == '':
                raise Undeclared(Attribute(), field_name)

    '''LITERALS'''
    def visitInstance(self, ast, o): return Data.INSTANCE()
    def visitStatic(self, ast, o): return Data.STATIC()
    def visitIntLiteral(self, ast, o): return Data.INT()
    def visitFloatLiteral(self, ast, o): return Data.FLOAT()
    def visitStringLiteral(self, ast, o): return Data.STRING()
    def visitBooleanLiteral(self, ast, o): return Data.BOOL()
    def visitNullLiteral(self, ast, o): return Data.NULL()

    def visitSelfLiteral(self, ast, o):
        for class_name in o['global'].keys():
            if o['global'][class_name] == o['class']:
                return Data.CLASS(class_name)
    # value: List[Expr]

    def visitArrayLiteral(self, ast, o):
        list_type = [self.visit(ele, o) for ele in ast.value]
        list_type = list(
            map(lambda ele: ele['type'] if isinstance(ele, dict) else ele, list_type))
        example_type = ''
        if len(list_type) != 0:
            example_type = list_type[0]
            for each_type in list_type[1:]:
                if each_type != example_type:
                    raise IllegalArrayLiteral(ast)
        return Data.ARRAY(len(list_type), example_type)
    
    '''DATA TYPE'''
    def visitIntType(self, ast, o): return Data.INT()
    def visitFloatType(self, ast, o): return Data.FLOAT()
    def visitBoolType(self, ast, o): return Data.BOOL()
    def visitStringType(self, ast, o): return Data.STRING()
    def visitArrayType(self, ast, o):
        return Data.ARRAY(ast.size, self.visit(ast.eleType, o))
    def visitClassType(self, ast, o):
        name = ast.classname.name
        if name in o['global']:
            return Data.CLASS(ast.classname.name)
        else:
            raise Undeclared(Class(), name)
    def visitVoidType(self, ast, o): return Data.VOID()

# **************************************
#                                      *
# *        MAIN CLASS VISITOR          *
#                                      *
# **************************************
class StaticChecker(BaseVisitor):
    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putIntLn", MType([IntType()], VoidType()))
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    # decl: List[ClassDecl]
    def visitProgram(self, ast, o):
        '''
        ** Structure for global scope **
            o = { 'global': {
                'class_name': {
                    'type': CLASS,
                    'parent': 'Animal',
                    'attribute': {
                        'attr_name': {
                            'kind': 'static',
                            'type': 'int',
                            'const': False or True
                            'init': 
                        }
                    },
                    'method': {
                        'method_name': {
                            'kind': STATIC or INSTANCE,
                            'type': RETURN TYPE,
                            'param': {list of param}
                            'body': [{}] // list dict of var declare inside method (use for method and block scope)
                        }
                    }
                }
                ...
            }
            }
        '''
        o = {'global': {}}
        for element in ast.decl:
            self.visit(element, o)
        '''Disable Entry point checker temporarily'''
        # if not 'Program' in o or not 'main' in o['Program']['method']:
        #     raise NoEntryPoint()
        # if o['Program']['method']['main']['param'] or o['Program']['method']['main']['type'] != Data.VOID():
        #     raise NoEntryPoint()
        return []

    # classname: Id,  memlist: List[MemDecl],  parentname: Id = None
    # MemDecl include MethodDecl and AttributeDecl
    def visitClassDecl(self, ast, o):
        '''
        o['class'][class_name] = {
            'parent': parent_name,
            'attribute': {dict of attribute}
            'method': {dict of method}
        }
        '''
        class_name = ast.classname.name
        if class_name in o['global']:
            raise Redeclared(Class(), class_name)
        parent_name = ''
        if not ast.parentname is None:
            parent_name = ast.parentname.name
            if parent_name == class_name:
                raise Undeclared(Class(), parent_name)
            if not parent_name in o['global']:
                raise Undeclared(Class(), parent_name)
        o['global'][class_name] = {
            'parent': parent_name,
            'attribute': {},
            'method': {}
        }
        o['class'] = o['global'][class_name]
        for mem in ast.memlist:
            self.visit(mem, o)

        # if class_name != 'Program':
        #     if not 'Constructor' in o[class_name]['method']:
        #         raise Undeclared(SpecialMethod(), 'Constructor')
        #     if not 'Destructor' in o[class_name]['method']:
        #         raise Undeclared(SpecialMethod(), 'Destructor')

    # kind: SIKind, name: Id, param: List[VarDecl], body: Block
    def visitMethodDecl(self, ast, o):
        '''
            o['method'][method_name] = {
                'type'  : return type of method,
                'kind'  : INSTANCE or STATIC
                'body' : [{}, {}] list dictionary {var decl}, use for method scope and block scope
                'param' : {list parameter}
            }
        '''
        name = ast.name.name
        if name in o['class']['method']:
            raise Redeclared(Method(), name)

        o['class']['method'][name] = {
            'type': Data.VOID(),  # will update return type later
            'kind': self.visit(ast.kind, o),
            'body': [{}],
            'param': {}
        }
        for eachPar in ast.param:
            o['class']['method'][name]['param'] = self.visitParam(eachPar, [o, o['class']['method'][name]['param']])
        env = {
            'global': o['global'],
            'class': o['class'],
            'method': o['class']['method'][name],
            # block: [{}]
            'block': o['class']['method'][name]['body']
        }
        # Copy param declaration to body scope
        for key in env['method']['param'].keys():
            env['block'][0][key] = {
                'type': env['method']['param'][key]['type'],
                'kind': Data.INSTANCE(),
                'init': Data.UNDEFINED(),
                'const': False
            }
        # ForLoopChecker().visitBlock(ast.body, [])
        GetMethodBlockEnv().visitBlock(ast.body, env)
    # variable: Id, varType: Type, varInit: Expr = None
    def visitParam(self, ast: VarDecl, o):
        '''
        o[param_name] = {
            'kind': <INSTANCE> or <STATIC>
            'type': INT, FLOAT,...
            'init': UNDEFINED
            'const': False
        }
        '''
        name = ast.variable.name
        if name in o[1]:
            raise Redeclared(Parameter(), name)
        typ = self.visit(ast.varType, o[0])
        o[1][name] = {
            'type': typ,
            'kind': Data.INSTANCE(),
            'init': Data.UNDEFINED(),
            'const': False
        }
        return o[1]

    # kind: SIKind, decl: StoreDecl (VarDecl or ConstDecl)
    def visitAttributeDecl(self, ast, o):
        self.visit(ast.decl, o)
    # variable: Id, varType: Type, varInit: Expr = None
    def visitVarDecl(self, ast: VarDecl, o):
        '''
        o['class']['attribute'][var_name] = {
            'kind': INSTANCE or STATIC With global attribute, kind is <STATIC>
            'type': type of this attribute (INT, FLOAT,...)
            'init': initial type of this attribute, update later
            'const': boolean flag to know this attribte is constant or variable
        }
        '''
        name = ast.variable.name
        if name in o['class']['attribute']:
            raise Redeclared(Attribute(), name)
        typ = self.visit(ast.varType, o)
        init = self.visit(ast.varInit, o) if ast.varInit else Data.UNDEFINED()
        if typ.startswith('<CLASS>') and init.startswith('<CLASS>'):
            if typ != init:
                parent = o['global'][init[8:-1]]['parent']
                while parent != typ[8:-1]:
                    if parent == '':
                        raise TypeMismatchInStatement(ast)
                    parent = o['global'][parent]['parent']
        elif typ.startswith('<CLASS>') and init == Data.NULL(): pass
        elif init != Data.UNDEFINED():
            if typ == Data.FLOAT() and init in [Data.FLOAT(), Data.INT()]:
                init = typ
            if typ != init:
                raise TypeMismatchInStatement(ast)
        
        o['class']['attribute'][name] = {
            'kind': Data.STATIC() if name.startswith('$') else Data.INSTANCE(),
            'type': typ,
            'init': init,
            'const': False
        }

    # constant: ID,  constType: Type,   value: Expr = None
    def visitConstDecl(self, ast: ConstDecl, o):
        '''
        o['class']['attribute'][const_name] = {
            'kind': INSTANCE or STATIC With global attribute, kind is STATIC
            'type': type of this attribute (INT, FLOAT,...)
            'init': initial type of this attribute, update later
            'const': boolean flag to know this attribte is constant or variable
        }
        '''
        name = ast.constant.name
        if name in o['class']['attribute']:
            raise Redeclared(Attribute(), name)
        typ = self.visit(ast.constType, o)
        if ast.value is None:
            raise IllegalConstantExpression(None)
        init = ast.value.accept(GetTypeConstant(), o)
        # * Check if this is a initial for class type
        if typ.startswith('<CLASS>') and init.startswith('<CLASS>'):
            if typ != init:
                parent = o['global'][init[8:-1]]['parent']
                while parent != typ[8:-1]:
                    if parent == '':
                        raise TypeMismatchInConstant(ast)
                    parent = o['global'][parent]['parent']

        elif typ != init:
            if typ == Data.FLOAT() and init in [Data.FLOAT(), Data.INT()]: init = typ
            raise TypeMismatchInConstant(ast)
        o['class']['attribute'][name] = {
            'kind': Data.STATIC() if name.startswith('$') else Data.INSTANCE(), 
            'type': typ,
            'init': init,
            'const': True
        }

    #name: str
    def visitId(self, ast, o):
        raise Undeclared(Identifier(), ast.name)

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

    def matchArgumentType(ast, param_env_list, arg_list):
        # Check for argument and parameter matching
        # [<INT>, <FLOAT>,...] for example
        list_param_type = [param_env_list[par_name]['type']
                           for par_name in param_env_list]

        list_argument_type = list(
            map(lambda ele: ele['type'] if isinstance(ele, dict) else ele, arg_list))

        if len(list_argument_type) != len(param_env_list):
            raise TypeMismatchInExpression(ast)
        for i in range(len(list_param_type)):
            if list_param_type[i] == Data.FLOAT() and list_argument_type[i] in [Data.FLOAT(), Data.INT()]:
                list_param_type[i] = list_argument_type[i]
            if list_param_type[i] != list_argument_type[i]:
                raise TypeMismatchInExpression(ast)
    # # obj: Expr,    method: Id, param: List[Expr]
    def visitCallExpr(self, ast, o):
        obj = ''
        kind = Data.INSTANCE()
        # ast.obj now is a Identifier
        if hasattr(ast.obj, 'name'):
            name = ast.obj.name
            # * If obj was declared in block scope
            if 'block' in o:
                for block in o['block']:
                    if name in block:
                        obj = block[name]['type']
            # * obj empty and the name is a class name
            if obj == '' and name in o['global']:
                obj = Data.CLASS(name)
                # * Mean that, if obj is a class name but its method invocation in 'instance' kind
                if ast.method.name[0] != '$':
                    raise IllegalMemberAccess(ast)
                kind = Data.STATIC()
            if obj != '' and kind == Data.INSTANCE() and ast.method.name[0] == '$': raise Undeclared(Class(), name)
            if obj == '': raise Undeclared(Identifier(), name)

        else: obj = self.visit(ast.obj, o)
        if not obj.startswith('<CLASS>') or obj[0] == '[':
            raise TypeMismatchInExpression(ast)
        if obj.startswith('<CLASS>') and not obj[8:-1] in o['global']:
            raise Undeclared(Class(), obj[8:-1])
        
        method_name = ast.method.name
#       * If kind is 'instance', that mean, 'obj' is a object of class, not a class name
#       * If kind is 'Static', 'obj' is now class name
#       * A subclass is able to access attribute of superclass
        parent = obj[8:-1]
        while True:
            if method_name in o['global'][parent]['method']:
                param_env = o['global'][parent]['method'][method_name]['param']
                arg_env = [self.visit(arg, o) for arg in ast.param]
                # * Check type matching of parameter and argument
                StaticChecker.matchArgumentType(ast, param_env, arg_env)
                if o['global'][parent]['method'][method_name]['type'] != Data.VOID():
                    return o['global'][parent]['method'][method_name]['type']  
                else: raise TypeMismatchInExpression(ast)
            parent = o['global'][parent]['parent']
            if parent == '': 
                raise Undeclared(Attribute(), method_name)

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
            raise Undeclared(SpecialMethod(), 'Constructor')

        # Check for argument and parameter matching
        # paramEnv is list of dict param declare
        param_env = o['global'][class_name]['method']['Constructor']['param']
        argument_type = [self.visit(arg, o) for arg in ast.param]

        StaticChecker.matchArgumentType(ast, param_env, argument_type)
        # [<INT>, <FLOAT>,...] for example
        return Data.CLASS(class_name)

    # arr: Expr,    idx: List[Expr]
    def visitArrayCell(self, ast, o):
        arr = self.visit(ast.arr, o)
        if isinstance(arr, dict):
            arr = arr['type']
        list_idx = [self.visit(idx, o) for idx in ast.idx]
        list_idx = list(
            map(lambda ele: ele['type'] if isinstance(ele, dict) else ele, list_idx))

        if arr[0] != '[':
            raise TypeMismatchInExpression(ast)
        for idx in list_idx:
            if idx != Data.INT():
                raise TypeMismatchInExpression(ast)
                # [2][5]<INT>

        '''Get type of element in array base on list of index access'''
        for _ in list_idx:
            if arr[0] != '[':
                raise TypeMismatchInExpression(ast)
            while arr[0] != ']':
                arr = arr[1:]
            arr = arr[1:]
        return arr

    # obj: Expr,    fieldname: Id
    def visitFieldAccess(self, ast, o):
        # ast.obj now is a Identifier
        obj = ''
        kind = Data.INSTANCE()
        # FieldAccess(A, s)
        if hasattr(ast.obj, 'name'):
            name = ast.obj.name
            # * If obj is a variable
            # * which is declared in block scope
            if 'block' in o:
                for block in o['block']:
                    if name in block: obj = block[name]['type']

            # * Undeclaration of obj but
            # * 'name' is a class name
            if obj == '' and name in o['global']:
                obj = Data.CLASS(name)
                # * When obj is a class name, that mean,
                # * this is a static access attribute
                if ast.fieldname.name[0] != '$':
                    raise IllegalMemberAccess(ast)
                kind = Data.STATIC()
            if obj != '' and kind == Data.INSTANCE() and ast.fieldname.name[0] == '$': raise Undeclared(Class(), name)
            if obj == '' and ast.fieldname.name[0] == '$': raise Undeclared(Class(), name)
            if obj == '' and ast.fieldname.name[0] != '$':
                raise Undeclared(Identifier(), name)
        else: obj = self.visit(ast.obj, o)
        if not obj.startswith('<CLASS>') or obj[0] == '[':
            raise TypeMismatchInExpression(ast)
        if obj.startswith('<CLASS>') and not obj[8:-1] in o['global']:
            raise Undeclared(Class(), obj[8:-1])

        field_name = ast.fieldname.name
#    * Instance access, obj is an object of class, not a class name
#    * A subclass is able to access attribute of superclass
        parent = obj[8:-1]
        while True:
            if field_name in o['global'][parent]['attribute']:
                return o['global'][parent]['attribute'][field_name]['type']
            parent = o['global'][parent]['parent']
            if parent == '':
                raise Undeclared(Attribute(), field_name)

    '''LITERALS'''
    def visitInstance(self, ast, o): return Data.INSTANCE()
    def visitStatic(self, ast, o): return Data.STATIC()
    def visitIntLiteral(self, ast, o): return Data.INT()
    def visitFloatLiteral(self, ast, o): return Data.FLOAT()
    def visitStringLiteral(self, ast, o): return Data.STRING()
    def visitBooleanLiteral(self, ast, o): return Data.BOOL()
    def visitNullLiteral(self, ast, o): return Data.NULL()

    def visitSelfLiteral(self, ast, o):
        for class_name in o['global'].keys():
            if o['global'][class_name] == o['class']:
                return Data.CLASS(class_name)
    
    # value: List[Expr]
    def visitArrayLiteral(self, ast, o):
        list_type = list(
            map(lambda ele: ele['type'] if isinstance(ele, dict) else ele, [self.visit(ele, o) for ele in ast.value]))
        
        example_type = ''
        if len(list_type) != 0:
            example_type = list_type[0]
            for each_type in list_type[1:]:
                if each_type != example_type:
                    raise IllegalArrayLiteral(ast)
        return Data.ARRAY(len(list_type), example_type)
    
    '''DATA TYPE'''
    def visitIntType(self, ast, o): return Data.INT()
    def visitFloatType(self, ast, o): return Data.FLOAT()
    def visitBoolType(self, ast, o): return Data.BOOL()
    def visitStringType(self, ast, o): return Data.STRING()
    def visitArrayType(self, ast, o):
        return Data.ARRAY(ast.size, self.visit(ast.eleType, o))
    def visitClassType(self, ast, o):
        name = ast.classname.name
        if name in o['global']:
            return Data.CLASS(ast.classname.name)
        raise Undeclared(Class(), name)
    def visitVoidType(self, ast, o): return Data.VOID()