
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
#from Utils import Utils
from StaticError import *
#from main.bkool.codegen.CodeGenerator import ClassType, StringType
#from main.bkool.utils.AST import ArrayCell, ArrayLiteral, ArrayType, Assign, AttributeDecl, BinaryOp, Block, BoolType, BooleanLiteral, Break, CallExpr, CallStmt, ClassDecl, ConstDecl, Continue, Decl, FieldAccess, FloatLiteral, FloatType, For, Id, If, Instance, IntLiteral, IntType, MethodDecl, NewExpr, NullLiteral, Program, Return, SelfLiteral, Static, StoreDecl, StringLiteral, UnaryOp, VarDecl, VoidType, ClassType, StringType

class MakeIO():
    def make(self,o):
        o['io'] = {'parent': '','field' : {}}
        envi = o['io']['field']
        envi['readInt'] = {'field':[{}],'type':'int','kind':'static','param':{}}
        envi['writeInt'] = {'field':[{}],'type':'void','kind':'static','param':{'anArg':'int'}}
        envi['writeIntLn'] = {'field':[{}],'type':'void','kind':'static','param':{'anArg':'int'}}        
        
        envi['readFloat'] = {'field':[{}],'type':'float','kind':'static','param':{}}
        envi['writeFloat'] = {'field':[{}],'type':'void','kind':'static','param':{'anArg':'float'}}
        envi['writeFloatLn'] = {'field':[{}],'type':'void','kind':'static','param':{'anArg':'float'}}
        
        envi['readBool'] = {'field':[{}],'type':'boolean','kind':'static','param':{}}
        envi['writeBool'] = {'field':[{}],'type':'void','kind':'static','param':{'anArg':'boolean'}}
        envi['writeBoolLn'] = {'field':[{}],'type':'void','kind':'static','param':{'anArg':'boolean'}}
        
        envi['readStr'] = {'field':[{}],'type':'string','kind':'static','param':{}}
        envi['writeStr'] = {'field':[{}],'type':'void','kind':'static','param':{'anArg':'string'}}
        envi['writeStrLn'] = {'field':[{}],'type':'void','kind':'static','param':{'anArg':'string'}}
        return o

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class CheckForLoop(BaseVisitor):
    '''
        CLASS TO CHECK IN BREAK OR CONTINUE NOT IN FOR LOOP
    '''
    def visitAssign(self, ast: Assign, o: object): pass
    def visitIf(self, ast: If, o: object):
        ast.thenStmt.accept(self,o)
        if ast.elseStmt is None: return
        ast.elseStmt.accept(self,o)
    def visitFor(self, ast: For, o: object):
        ast.loop.accept(self,[1] + o)
    def visitBreak(self, ast: Break, o: object):
        if not 1 in o: raise MustInLoop(ast)
    def visitContinue(self, ast: Continue, o: object):
        if not 1 in o: raise MustInLoop(ast)
    def visitReturn(self, ast: Return, o: object): pass
    def visitCallStmt(self, ast: CallStmt, o: object): pass
    def visitBlock(self, ast: Block, o: object):
        for stmt in ast.stmt: stmt.accept(self,o)
    def visitParam(self, ast: VarDecl, o: object):
        name = ast.variable.name
        if name in o.keys(): raise Redeclared(Parameter(), name)
        typ = ast.varType.accept(GetEnvi(), o)
        o[name] = {
            'type': typ,
            'kind': "instance",
            'init': "",
            'const': False}
        return o
    
class VisitStorageDecl(BaseVisitor):
    def visitVarDecl(self, ast: VarDecl, o: object):
        name = ast.variable.name
        if name in o['block'][0]: raise Redeclared(Variable(),name)
        typ = ast.varType.accept(GetEnvi(),o)
        init = ''
        if ast.varInit:
            init = ast.varInit.accept(GetTypeExp(),o)
            if GetTypeExp().matchType(typ,init,o) == False: raise TypeMismatchInStatement(ast)
            if init[0] == '[':
                arrType = init[:]
                while arrType[0] != ']': arrType = arrType[1:]
                arrType = arrType[1:]
                if not arrType in o['global'].keys():
                    init = typ
            elif not init in o['global'].keys(): init = typ
        o['block'][0][name] = {'type':typ,'kind':"instance",'init': init,'const':False}
        return o
    def visitConstDecl(self, ast: ConstDecl, o: object):
        '''
            make dictionary name with kind is instance
            dictionary constant form:
            o['field'][const_name] = {
                'type' : type of var
                'kind' : auto "instance" (can update to "static" late if this is attribute)
                'init' : "", wil assign to type of init value late, raise exception if don't have
                'const': True because this is constant
            }
        '''
        name = ast.constant.name
        if name in o['block'][0]: raise Redeclared(Constant(), name)
        typ = ast.constType.accept(GetEnvi(), o)
        if ast.value is None: raise IllegalConstantExpression(None)
        init = ast.value.accept(GetTypeConst(),o)
        if init[1] == 1: raise IllegalConstantExpression(ast.value)
        if GetTypeConst().matchType(typ, init[0],o) == False: raise TypeMismatchInConstant(ast)
        init = init[0]
        if init[0] == '[':
            arrType = init[:]
            while arrType[0] != ']': arrType = arrType[1:]
            arrType = arrType[1:]
            if not arrType in o['global'].keys():
                init = typ
        elif not init in o['global'].keys():
            init = typ
        o['block'][0][name] = {'type': typ,'kind': "instance", 'init': init, 'const': True}
        return o

class GetEnvi(BaseVisitor):
    '''
        CLASS TO GET CLASS NAME, ATTRIBUTE NAME, METHOD NAME
    '''
    def visitId(self, ast: Id, o: object): return ast.name
    def visitInstance(self, ast: Instance, o: object): return "instance"
    def visitStatic(self, ast: Static, o: object): return "static"
    def visitIntType(self, ast: IntType, o: object): return "int"
    def visitFloatType(self, ast: FloatType, o: object): return "float"
    def visitBoolType(self, ast: BoolType, o: object): return "bool"
    def visitStringType(self, ast: StringType, o: object): return "string"
    def visitArrayType(self, ast: ArrayType, o: object): return "[" + str(ast.size) + "]" + ast.eleType.accept(self,o)
    def visitClassType(self, ast: ClassType, o: object): return ast.classname.accept(self,o)
    def visitVoidType(self, ast: VoidType, o: object): return "void"
    def visitProgram(self, ast: Program, o: object):
        '''
            return dictionary with keys are class name
        '''
        o = {}
        for decl in ast.decl: decl.accept(self,o)
        return o
    def visitClassDecl(self, ast: ClassDecl, o: object):
        '''
            in dictionary class name
            dictionary form:
            o[class_name] = {
                'parent' : parent_name,
                'field'  : {dictionary of attribute}
                'method' : {dictionary of method}
            }
        '''
        name = ast.classname.name
        pa = ""
        if not ast.parentname is None:
            pa = ast.parentname.name
            if pa == name: raise Undeclared(Class(),name)
        if name in o: raise Redeclared(Class(),name)
        o[name] = {
            'parent': pa,
            'field' : {}}
        for mem in ast.memlist: mem.accept(self,o[name]['field'])
    def visitAttributeDecl(self, ast: AttributeDecl, o: object):
        '''
            in dictionary attribute name
                - update kind key: change to "static" or "instance"
        '''
        name = ast.decl.accept(self,o)
        o[name]['kind'] = ast.kind.accept(self,o)
    def visitVarDecl(self, ast: VarDecl, o: object):
        '''
            make dictionary name with kind is instance
            dictionary variable form:
            o['field'][var_name] = {
                'type' : type of var
                'kind' : auto "instance" (can update to "static" late if this is attribute)
                'init' : "", will assign to type of init value late if exist init value
                'const': False because this is variable
            }
        '''
        name = ast.variable.name
        if name in o: raise Redeclared(Attribute(),name)
        typ = ast.varType.accept(self,o)
        o[name] = {
            'type':typ,
            'kind':"instance",
            'init':"",
            'const':False}
        return name
    def visitConstDecl(self, ast: ConstDecl, o: object):
        '''
            make dictionary name with kind is instance
            dictionary constant form:
            o['field'][const_name] = {
                'type' : type of var
                'kind' : auto "instance" (can update to "static" late if this is attribute)
                'init' : "", wil assign to type of init value late, raise exception if don't have
                'const': True because this is constant
            }
        '''
        name = ast.constant.name
        if name in o: raise Redeclared(Attribute(), name)
        typ = ast.constType.accept(self, o)
        if ast.value is None: raise IllegalConstantExpression(None)
        o[name] = {
            'type':typ,
            'kind':"instance",
            'init':"",
            'const':True}
        return name
    def visitMethodDecl(self, ast: MethodDecl, o: object):
        '''
            in dictionary method name, contains:
            dictionary method form:
            o['method'][method_name] = {
                'field' : list dictionary {var decl}, use for method scope and block scope
                'type'  : return type of method, "" if this is special method constructor
                'kind'  : "instance" or "static"
                'param' : {list parameter}
            }
        '''
        name = ast.name.name
        typ = ""
        if not ast.returnType is None: typ = ast.returnType.accept(self,o)
        if name in o:
            if typ == "": raise Redeclared(Method(),name)
            raise Redeclared(Method(),name)
        o[name] = {
            'field':[{}],
            'type':typ,
            'kind':ast.kind.accept(self,o),
            'param' : {}
        }
        for par in ast.param:
            o[name]['param'] = CheckForLoop().visitParam(par,o[name]['param'])
    
class GetTypeExp(BaseVisitor):
    def getTypeDecl(self,name,o):
        if not 'const' in o[name]: return 'method'
        if o[name]['const'] == True: return 'const'
        return 'var'
    def matchType(self,lhs,rhs,o:object):
        # match type and class == nil
        if rhs == lhs: return True
        if lhs == 'float' and rhs in ['int','float']: return True
        if lhs in o['global'] and rhs == 'nil': return True
        # class child and class parent
        if rhs in o['global']:
            parent = o['global'][rhs]['parent']
            while parent != "":
                if parent == lhs: return True
                parent = o['global'][parent]['parent']
        # array type
        if rhs[0] == '[':
            rhs = rhs[1:]
            sizeRhs = ''
            while rhs[0] != ']':
                sizeRhs += rhs[0]
                rhs = rhs[1:]
            sizeLhs = ''
            lhs = lhs[1:]
            while lhs[0] != ']':
                sizeLhs += lhs[0]
                lhs = lhs[1:]
            if int(sizeRhs) == int(sizeLhs) and self.matchType(lhs[1:],rhs[1:],o):
                return True
        return False
    def visitId(self, ast: Id, o: object):
        name = ast.name
        if 'block' in o:
            for block in o['block']:
                if name in block:
                    typ = block[name]['type']
                    init = block[name]['init']
                    if init == '': return typ
                    return init
        raise Undeclared(Identifier(),name)
    def visitIntLiteral(self, ast: IntLiteral, o: object): return 'int'
    def visitFloatLiteral(self, ast: FloatLiteral, o: object): return 'float'
    def visitStringLiteral(self, ast: StringLiteral,o: object): return 'string'
    def visitBooleanLiteral(self, ast: BooleanLiteral,o: object): return 'bool'
    def visitNullLiteral(self, ast: NullLiteral, o: object): return 'nil'
    def visitSelfLiteral(self, ast: SelfLiteral, o: object):
        for key in o['global'].keys():
            if o['global'][key] == o['class']: return key
        raise Undeclared(Class(),"this")
    def visitArrayLiteral(self, ast: ArrayLiteral, o: object):
        list_type = [value.accept(self, o) for value in ast.value]
        if len(list_type) == 0: raise IllegalArrayLiteral(ast)
        typ = list_type[0]
        for type_value in list_type[1:]:
            if typ != type_value: raise IllegalArrayLiteral(ast)
        return "[" + str(len(list_type)) + "]" + typ
    def visitBinaryOp(self, ast: BinaryOp, o: object):
        left = ast.left.accept(self,o)
        right = ast.right.accept(self,o)
        op = ast.op
        if op == "^" and left == "string" and right == "string": return "string"
        if op in ['\\','%'] and left == 'int' and right == 'int': return 'int'
        if op == '/' and left in ['int','float'] and right in ['int','float']: return 'float'
        if op in ['&&','||'] and left == 'bool' and right == 'bool': return 'bool'
        if op in ['+','-','*']:
            if left == 'int' and right == 'int': return 'int'
            if left in ['int','float'] and right in ['int','float']: return 'float'
        if op in ['==','!='] and left == right and left in ['int','bool']: return 'bool'
        if op in ['>','<','>=','<='] and left in ['int','float'] and right in ['int','float']: return 'bool'
        raise TypeMismatchInExpression(ast)
    def visitUnaryOp(self, ast: UnaryOp, o: object):
        op = ast.op
        body = ast.body.accept(self,o)
        if op == "!" and body == "bool": return "bool"
        if op in ["+","-"] and body in ['int','float']: return body
        raise TypeMismatchInExpression(ast)
    def visitNewExpr(self, ast: NewExpr, o: object):
        classname = ast.classname.name
        if not classname in o['global']: raise Undeclared(Class(), classname)
        # don't have constructor
        if not '<init>' in o['global'][classname]['field']:
            if len(ast.param) == 0: return classname
            raise Undeclared(Method(), '<init>')
        # have constructor, check match param and value pass
        envi = o['global'][classname]['field']['<init>']['param']
        list_param = [envi[par]['type'] for par in envi]
        pass_param = [par.accept(self, o) for par in ast.param]
        if len(list_param) != len(pass_param): raise TypeMismatchInExpression(ast)
        for i in range(len(list_param)):
            if self.matchType(list_param[i], pass_param[i],o) == False: raise TypeMismatchInExpression(ast)
        return classname
    def visitArrayCell(self, ast: ArrayCell, o: object):
        arr = ast.arr.accept(self,o)
        idx = ast.idx.accept(self,o)
        if arr[0] != '[' or idx != 'int': raise TypeMismatchInExpression(ast)
        while arr[0] != ']': arr = arr[1:]
        return arr[1:]
    def visitCallExpr(self, ast: CallExpr, o: object):
        kind = 'instance'
        obj = ''
        if hasattr(ast.obj,'name'):
            # obj can be class name to static access
            name = ast.obj.name
            if 'block' in o:
                for scope in o['block']:
                    if name in scope:
                        if scope[name]['init'] != '':
                            obj = scope[name]['init']
                        else:
                            obj = scope[name]['type']
            if obj == '' and name in o['global']:
                obj = name
                kind = 'static'
            if obj == '': raise Undeclared(Identifier(),name)
        else: obj = ast.obj.accept(self, o)
        if obj in ['int','float','string','bool','nil'] or obj[0] == '[': 
            raise TypeMismatchInExpression(ast)
        if not obj in o['global']: raise Undeclared(Class(),obj)
        # FIND ENVIRONMENT HAVE THIS METHOD
        method = ast.method.name
        envi = o['global'][obj]
        while True:
            if method in envi['field']:
                if self.getTypeDecl(method,envi['field']) == 'method':
                    if envi['field'][method]['kind'] == kind: break
                    raise IllegalMemberAccess(ast)
                else:
                    raise TypeMismatchInExpression(ast)
            parent = o['global'][obj]['parent']
            if parent == '': raise Undeclared(Method(), method)
            envi = o['global'][parent]
        if envi['field'][method]['type'] == 'void': raise TypeMismatchInExpression(ast)
        # CHECK PARAM MATCH
        list_param = [envi['field'][method]['param'][par]['type'] for par in envi['field'][method]['param'].keys()]
        pass_value = [par.accept(self, o) for par in ast.param]
        if len(list_param) != len(pass_value): raise TypeMismatchInExpression(ast)
        for i in range(len(list_param)):
            if self.matchType(list_param[i], pass_value[i], o) == False: raise TypeMismatchInExpression(ast)
        return envi['field'][method]['type']
    def visitFieldAccess(self, ast: FieldAccess, o: object):
        kind = 'instance'
        obj = ''
        if hasattr(ast.obj,'name'):
            # obj can be class name to static access
            name = ast.obj.name
            if 'block' in o:
                for scope in o['block']:
                    if name in scope:
                        if scope[name]['init'] != '':
                            obj = scope[name]['init']
                        else:
                            obj = scope[name]['type']
            if obj == '' and name in o['global']:
                obj = name
                kind = 'static'
            if obj == '': raise Undeclared(Identifier(), name)
        else: obj = ast.obj.accept(self, o)
        if obj in ['int','float','string','bool','nil'] or obj[0] == '[': 
            raise TypeMismatchInExpression(ast)
        if not obj in o['global']: raise Undeclared(Class(),obj)
        # FIND LOCATION OF ATTRIBUTE
        fieldname = ast.fieldname.name
        envi = o['global'][obj]

        if kind == 'instance':
            class_scope = o['class']
            while class_scope != envi:
                parent = class_scope['parent']
                if parent == '': raise Undeclared(Attribute(), fieldname)
                class_scope = o['global'][parent]

        while True:
            if fieldname in envi['field']:
                if self.getTypeDecl(fieldname, envi['field']) != 'method':
                    if envi['field'][fieldname]['kind'] == kind:
                        if envi['field'][fieldname]['init'] != '':
                            return envi['field'][fieldname]['init']
                        return envi['field'][fieldname]['type']
                    raise IllegalMemberAccess(ast)
                else: 
                    raise TypeMismatchInExpression(ast)
            parent = o['global'][obj]['parent']
            if parent == '': raise Undeclared(Attribute(), fieldname)
            envi = o['global'][parent]

class GetTypeConst(BaseVisitor):
    def getTypeDecl(self,name,o):
        if not 'const' in o[name]: return 'method'
        if o[name]['const'] == True: return 'const'
        return 'var'
    def matchType(self,lhs,rhs,o:object):
        # match type and class == nil
        if rhs == lhs: return True
        if lhs == 'float' and rhs in ['int','float']: return True
        if lhs in o['global'] and rhs == 'nil': return True
        # class child and class parent
        if rhs in o['global']:
            parent = o['global'][rhs]['parent']
            while parent != "":
                if parent == lhs: return True
                parent = o['global'][parent]['parent']
        # array type
        if rhs[0] == '[':
            rhs = rhs[1:]
            sizeRhs = ''
            while rhs[0] != ']':
                sizeRhs += rhs[0]
                rhs = rhs[1:]
            sizeLhs = ''
            lhs = lhs[1:]
            while lhs[0] != ']':
                sizeLhs += lhs[0]
                lhs = lhs[1:]
            if int(sizeRhs) == int(sizeLhs) and self.matchType(lhs[1:],rhs[1:],o):
                return True
        return False
    def visitId(self, ast: Id, o: object):
        name = ast.name
        res = 0
        if 'block' in o:
            for block in o['block']:
                if name in block:
                    typ = block[name]['type']
                    init = block[name]['init']
                    if block[name]['const'] == False:
                        res = 1
                    if init == '': return (typ,res)
                    return (init,res)
        raise Undeclared(Identifier(),name)
    def visitIntLiteral(self, ast: IntLiteral, o: object): return ('int',0)
    def visitFloatLiteral(self, ast: FloatLiteral, o: object): return ('float',0)
    def visitStringLiteral(self, ast: StringLiteral,o: object): return ('string',0)
    def visitBooleanLiteral(self, ast: BooleanLiteral,o: object): return ('bool',0)
    def visitNullLiteral(self, ast: NullLiteral, o: object): return ('nil',0)
    def visitSelfLiteral(self, ast: SelfLiteral, o: object):
        for key in o['global'].keys():
            if o['global'][key] == o['class']: return (key,0)
        raise Undeclared(Class(),"this")
    def visitArrayLiteral(self, ast: ArrayLiteral, o: object):
        list_type = [value.accept(self, o)[0] for value in ast.value]
        if len(list_type) == 0: raise IllegalArrayLiteral(ast)
        typ = list_type[0]
        for type_value in list_type[1:]:
            if typ != type_value: raise IllegalArrayLiteral(ast)
        return (("[" + str(len(list_type)) + "]" + typ),1)
    def visitBinaryOp(self, ast: BinaryOp, o: object):
        left = ast.left.accept(self,o)
        right = ast.right.accept(self,o)
        res = 0
        if left[1] == 1 or right[1] == 1: res = 1
        left = left[0]
        right = right[0]
        op = ast.op
        if op == "^" and left == "string" and right == "string": return ("string",res)
        if op in ['\\','%'] and left == 'int' and right == 'int': return ('int',res)
        if op == '/' and left in ['int','float'] and right in ['int','float']: return ('float',res)
        if op in ['&&','||'] and left == 'bool' and right == 'bool': return ('bool',res)
        if op in ['+','-','*']:
            if left == 'int' and right == 'int': return ('int',res)
            if left in ['int','float'] and right in ['int','float']: return ('float',res)
        if op in ['==','!='] and left == right and left in ['int','bool']: return ('bool',res)
        if op in ['>','<','>=','<='] and left in ['int','float'] and right in ['int','float']: return ('bool',res)
        raise TypeMismatchInExpression(ast)
    def visitUnaryOp(self, ast: UnaryOp, o: object):
        op = ast.op
        body = ast.body.accept(self,o)
        res = body[1]
        body = body[0]
        if op == "!" and body == "bool": return ("bool",res)
        if op in ["+","-"] and body in ['int','float']: return (body,res)
        raise TypeMismatchInExpression(ast)
    def visitNewExpr(self, ast: NewExpr, o: object):
        classname = ast.classname.name
        if not classname in o['global']: raise Undeclared(Class(), classname)
        # don't have constructor
        if not '<init>' in o['global'][classname]['field']:
            if len(ast.param) == 0: return (classname,1)
            raise Undeclared(Method(), '<init>')
        # have constructor, check match param and value pass
        envi = o['global'][classname]['field']['<init>']['param']
        list_param = [envi[par]['type'] for par in envi]
        pass_param = [par.accept(self, o)[0] for par in ast.param]
        if len(list_param) != len(pass_param): raise TypeMismatchInExpression(ast)
        for i in range(len(list_param)):
            if self.matchType(list_param[i], pass_param[i],o) == False: raise TypeMismatchInExpression(ast)
        return (classname,1)
    def visitArrayCell(self, ast: ArrayCell, o: object):
        arr = ast.arr.accept(self,o)
        idx = ast.idx.accept(self,o)
        arr = arr[0]
        idx = idx[0]
        if arr[0] != '[' or idx != 'int': raise TypeMismatchInExpression(ast)
        while arr[0] != ']': arr = arr[1:]
        return (arr[1:],1)
    def visitCallExpr(self, ast: CallExpr, o: object):
        kind = 'instance'
        obj = ''
        if hasattr(ast.obj,'name'):
            # obj can be class name to static access
            name = ast.obj.name
            if 'block' in o:
                for scope in o['block']:
                    if name in scope:
                        if scope[name]['init'] != '':
                            obj = scope[name]['init']
                        else:
                            obj = scope[name]['type']
            if obj == '' and name in o['global']:
                obj = name
                kind = 'static'
            if obj == '': raise Undeclared(Identifier(),name)
        else: obj = ast.obj.accept(self, o)[0]
        if obj in ['int','float','string','bool','nil'] or obj[0] == '[': 
            raise TypeMismatchInExpression(ast)
        if not obj in o['global']: raise Undeclared(Class(),obj)
        # FIND ENVIRONMENT HAVE THIS METHOD
        method = ast.method.name
        envi = o['global'][obj]
        while True:
            if method in envi['field']:
                if self.getTypeDecl(method,envi['field']) == 'method':
                    if envi['field'][method]['kind'] == kind: break
                    raise IllegalMemberAccess(ast)
                else: raise TypeMismatchInExpression(ast)
            parent = o['global'][obj]['parent']
            if parent == '': raise Undeclared(Method(), method)
            envi = o['global'][parent]
        if envi['field'][method]['type'] == 'void': raise TypeMismatchInExpression(ast)
        # CHECK PARAM MATCH
        list_param = [envi['field'][method]['param'][par]['type'] for par in envi['field'][method]['param'].keys()]
        pass_value = [par.accept(self, o)[0] for par in ast.param]
        if len(list_param) != len(pass_value): raise TypeMismatchInExpression(ast)
        for i in range(len(list_param)):
            if self.matchType(list_param[i], pass_value[i], o) == False: raise TypeMismatchInExpression(ast)
        return (envi['field'][method]['type'],1)
    def visitFieldAccess(self, ast: FieldAccess, o: object):
        kind = 'instance'
        obj = ''
        res = 0
        if hasattr(ast.obj,'name'):
            # obj can be class name to static access
            name = ast.obj.name
            if 'block' in o:
                for scope in o['block']:
                    if name in scope:
                        if scope[name]['const'] == False: res = 1
                        if scope[name]['init'] != '':
                            obj = scope[name]['init']
                        else:
                            obj = scope[name]['type']
            if obj == '' and name in o['global']:
                obj = name
                kind = 'static'
            if obj == '': raise Undeclared(Identifier(), name)
        else:
            obj = ast.obj.accept(self, o)
            if obj[1] == 1: res = 1
            obj = obj[0]
        if obj in ['int','float','string','bool','nil'] or obj[0] == '[': 
            raise TypeMismatchInExpression(ast)
        if not obj in o['global']: raise Undeclared(Class(),obj)
        # FIND LOCATION OF ATTRIBUTE
        fieldname = ast.fieldname.name
        envi = o['global'][obj]

        if kind == 'instance':
            class_scope = o['class']
            while class_scope != envi:
                parent = class_scope['parent']
                if parent == '':
                    raise Undeclared(Attribute(), fieldname)
                class_scope = o['global'][parent]
        while True:
            if fieldname in envi['field']:
                if self.getTypeDecl(fieldname, envi['field']) != 'method':
                    if envi['field'][fieldname]['kind'] == kind:
                        if envi['field'][fieldname]['const'] == False: res = 1
                        if envi['field'][fieldname]['init'] != '':
                            return (envi['field'][fieldname]['init'],res)
                        return (envi['field'][fieldname]['type'],res)
                    raise IllegalMemberAccess(ast)
                else:
                    raise TypeMismatchInExpression(ast)
            parent = o['global'][obj]['parent']
            if parent == '': raise Undeclared(Attribute(), fieldname)
            envi = o['global'][parent]

class GetLHS(BaseVisitor):
    def getTypeDecl(self,name,o):
        if not 'const' in o[name]: return 'method'
        if o[name]['const'] == True: return 'const'
        return 'var'
    def matchType(self,lhs,rhs,o:object):
        # match type and class == nil
        if 'type' in rhs: rhs = rhs['type']
        if 'type' in lhs: lhs = lhs['type']
        if rhs == lhs: return True
        if lhs == 'float' and rhs in ['int','float']: return True
        if lhs in o['global'] and rhs == 'nil': return True
        # class child and class parent
        if rhs in o['global']:
            parent = o['global'][rhs]['parent']
            while parent != "":
                if parent == lhs: return True
                parent = o['global'][parent]['parent']
        # array type
        if rhs[0] == '[':
            rhs = rhs[1:]
            sizeRhs = ''
            while rhs[0] != ']':
                sizeRhs += rhs[0]
                rhs = rhs[1:]
            sizeLhs = ''
            lhs = lhs[1:]
            while lhs[0] != ']':
                sizeLhs += lhs[0]
                lhs = lhs[1:]
            if int(sizeRhs) == int(sizeLhs) and self.matchType(lhs[1:],rhs[1:],o):
                return True
        return False
    def visitId(self, ast: Id, o: object):
        name = ast.name
        if 'block' in o:
            for block in o['block']:
                if name in block:
                    return block[name]
        raise Undeclared(Identifier(),name)
    def visitIntLiteral(self, ast: IntLiteral, o: object): return 'int'
    def visitFloatLiteral(self, ast: FloatLiteral, o: object): return 'float'
    def visitStringLiteral(self, ast: StringLiteral,o: object): return 'string'
    def visitBooleanLiteral(self, ast: BooleanLiteral,o: object): return 'bool'
    def visitNullLiteral(self, ast: NullLiteral, o: object): return 'nil'
    def visitSelfLiteral(self, ast: SelfLiteral, o: object):
        for key in o['global'].keys():
            if o['global'][key] == o['class']: return key
        raise Undeclared(Class(),"this")
    def visitArrayLiteral(self, ast: ArrayLiteral, o: object):
        list_type = [value.accept(self, o) for value in ast.value]
        if len(list_type) == 0: raise IllegalArrayLiteral(ast)
        for i in range(len(list_type)):
            if 'type' in list_type[i]:
                list_type[i] = list_type[i]['type']
        typ = list_type[0]
        for type_value in list_type[1:]:
            if typ != type_value: raise IllegalArrayLiteral(ast)
        return "[" + str(len(list_type)) + "]" + typ
    def visitBinaryOp(self, ast: BinaryOp, o: object):
        left = ast.left.accept(self,o)
        right = ast.right.accept(self,o)
        if 'type' in left: left = left['type']
        if 'type' in right: right = right['type']
        op = ast.op
        if op == "^" and left == "string" and right == "string": return "string"
        if op in ['\\','%'] and left == 'int' and right == 'int': return 'int'
        if op == '/' and left in ['int','float'] and right in ['int','float']: return 'float'
        if op in ['&&','||'] and left == 'bool' and right == 'bool': return 'bool'
        if op in ['+','-','*']:
            if left == 'int' and right == 'int': return 'int'
            if left in ['int','float'] and right in ['int','float']: return 'float'
        if op in ['==','!='] and left == right and left in ['int','bool']: return 'bool'
        if op in ['>','<','>=','<='] and left in ['int','float'] and right in ['int','float']: return 'bool'
        raise TypeMismatchInExpression(ast)
    def visitUnaryOp(self, ast: UnaryOp, o: object):
        op = ast.op
        body = ast.body.accept(self,o)
        if 'type' in body: body = body['type']
        if op == "!" and body == "bool": return "bool"
        if op in ["+","-"] and body in ['int','float']: return body
        raise TypeMismatchInExpression(ast)
    def visitNewExpr(self, ast: NewExpr, o: object):
        classname = ast.classname.name
        if not classname in o['global']: raise Undeclared(Class(), classname)
        # don't have constructor
        if not '<init>' in o['global'][classname]['field']:
            if len(ast.param) == 0: return classname
            raise Undeclared(Method(), '<init>')
        # have constructor, check match param and value pass
        envi = o['global'][classname]['field']['<init>']['param']
        list_param = [envi[par]['type'] for par in envi]
        pass_param = [par.accept(self, o) for par in ast.param]
        if len(list_param) != len(pass_param): raise TypeMismatchInExpression(ast)
        for i in range(len(list_param)):
            if self.matchType(list_param[i], pass_param[i],o) == False: raise TypeMismatchInExpression(ast)
        return classname
    def visitArrayCell(self, ast: ArrayCell, o: object):
        arr = ast.arr.accept(self,o)
        idx = ast.idx.accept(self,o)
        if arr['type'][0] != '[' or idx != 'int': raise TypeMismatchInExpression(ast)
        typ = arr['type'][:]
        while typ[0] != ']': typ = typ[1:]
        init=arr['init']
        if init != '':
            while init[0] !=']': init = init[1:]
            init = init[1:]
        return {'type':typ[1:],'kind':arr['kind'],'init':init,'const':arr['const']}
    def visitCallExpr(self, ast: CallExpr, o: object):
        kind = 'instance'
        obj = ''
        if hasattr(ast.obj,'name'):
            # obj can be class name to static access
            name = ast.obj.name
            if 'block' in o:
                for scope in o['block']:
                    if name in scope:
                        if scope[name]['init'] != '':
                            obj = scope[name]['init']
                        else:
                            obj = scope[name]['type']
            if obj == '' and name in o['global']:
                obj = name
                kind = 'static'
            if obj == '': raise Undeclared(Identifier(),name)
        else: obj = ast.obj.accept(self, o)
        if obj in ['int','float','string','bool','nil'] or obj[0] == '[': 
            raise TypeMismatchInExpression(ast)
        if not obj in o['global']: raise Undeclared(Class(),obj)
        # FIND ENVIRONMENT HAVE THIS METHOD
        method = ast.method.name
        envi = o['global'][obj]
        while True:
            if method in envi['field']:
                if self.getTypeDecl(method,envi['field']) == 'method':
                    if envi['field'][method]['kind'] == kind: break
                    raise IllegalMemberAccess(ast)
                else:
                    raise TypeMismatchInExpression(ast)
            parent = o['global'][obj]['parent']
            if parent == '': raise Undeclared(Method(), method)
            envi = o['global'][parent]
        if envi['field'][method]['type'] == 'void': raise TypeMismatchInExpression(ast)
        # CHECK PARAM MATCH
        list_param = [envi['field'][method]['param'][par]['type'] for par in envi['field'][method]['param'].keys()]
        pass_value = [par.accept(self, o) for par in ast.param]
        if len(list_param) != len(pass_value): raise TypeMismatchInExpression(ast)
        for i in range(len(list_param)):
            if self.matchType(list_param[i], pass_value[i], o) == False: raise TypeMismatchInExpression(ast)
        return envi['field'][method]['type']
    def visitFieldAccess(self, ast: FieldAccess, o: object):
        kind = 'instance'
        obj = ''
        if hasattr(ast.obj,'name'):
            # obj can be class name to static access
            name = ast.obj.name
            if 'block' in o:
                for scope in o['block']:
                    if name in scope:
                        if scope[name]['init'] != '':
                            obj = scope[name]['init']
                        else:
                            obj = scope[name]['type']
            if obj == '' and name in o['global']:
                obj = name
                kind = 'static'
            if obj == '': raise Undeclared(Identifier(), name)
        else: obj = ast.obj.accept(self, o)
        if obj in ['int','float','string','bool','nil'] or obj[0] == '[': 
            raise TypeMismatchInExpression(ast)
        if not obj in o['global']: raise Undeclared(Class(),obj)
        # FIND LOCATION OF ATTRIBUTE
        fieldname = ast.fieldname.name
        envi = o['global'][obj]

        if kind == 'instance':
            class_scope = o['class']
            while class_scope != envi:
                parent = class_scope['parent']
                if parent == '':
                    raise Undeclared(Attribute(), fieldname)
                class_scope = o['global'][parent]

        while True:
            if fieldname in envi['field']:
                if self.getTypeDecl(fieldname, envi['field']) != 'method':
                    if envi['field'][fieldname]['kind'] == kind:
                        return envi['field'][fieldname]
                    raise IllegalMemberAccess(ast)
                else:
                    raise TypeMismatchInExpression(ast)
            parent = o['global'][obj]['parent']
            if parent == '': raise Undeclared(Attribute(), fieldname)
            envi = o['global'][parent]

class StaticChecker(BaseVisitor):
    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ] 
    def __init__(self,ast):
        self.ast = ast
    def check(self):
        return self.ast.accept(self, StaticChecker.global_envi)

    def visitInstance(self, ast: Instance, o: object): pass
    def visitStatic(self, ast: Static, o: object): pass
    def visitIntType(self, ast: IntType, o: object): pass
    def visitFloatType(self, ast: FloatType, o: object): pass
    def visitBoolType(self, ast: BoolType, o: object): pass
    def visitStringType(self, ast: StringType, o: object): pass
    def visitArrayType(self, ast: ArrayType, o: object): ast.eleType.accept(self,o)
    def visitClassType(self, ast: ClassType, o: object):
        name = ast.classname.name
        if name not in o['global']:
            raise Undeclared(Class(),name)
    def visitVoidType(self, ast: VoidType, o: object): pass
    def visitProgram(self, ast: Program, o: object):
        o = GetEnvi().visitProgram(ast,o)
        o = MakeIO().make(o)
        for decl in ast.decl: decl.accept(self, o)
        # return o
    def visitClassDecl(self, ast: ClassDecl, o: object):
        if ast.parentname:
            if not ast.parentname.name in o: raise Undeclared(Class(), ast.parentname.name)
        envi = {
            'global': o,
            'class' : o[ast.classname.name]
        }
        for mem in ast.memlist: mem.accept(self, envi)
    def visitAttributeDecl(self, ast: AttributeDecl, o: object):
        ast.decl.accept(self,o)
    def visitVarDecl(self, ast: VarDecl, o: object):
        name = ast.variable.name
        ast.varType.accept(self,o)
        typ = o['class']['field'][name]['type']
        if ast.varInit:
            init = ast.varInit.accept(GetTypeExp(),o)
            if GetTypeExp().matchType(typ,init,o) == False:
                raise TypeMismatchInStatement(ast)
            if init[0] == '[':
                arrType = init[1:]
                while arrType[0] != ']': arrType = arrType[1:]
                arrType = arrType[1:]
                if arrType in o['global'].keys():
                    o['class']['field'][name]['init'] = init
                else:
                    o['class']['field'][name]['init'] = typ
            elif init in o['global'].keys():
                o['class']['field'][name]['init'] = init
            else:
                o['class']['field'][name]['init'] = typ 
    def visitConstDecl(self, ast: ConstDecl, o: object):
        name = ast.constant.name
        ast.constType.accept(self,o)
        typ = o['class']['field'][name]['type']
        init = ast.value.accept(GetTypeConst(),o)
        if init[1] == 1:
            raise IllegalConstantExpression(ast.value)
        if GetTypeConst().matchType(typ, init[0],o) == False:
            raise TypeMismatchInConstant(ast)
        init = init[0]
        if init[0] == '[':
            arrType = init[:]
            while arrType[0] != ']': arrType = arrType[1:]
            arrType = arrType[1:]
            if arrType in o['global'].keys():
                o['class']['field'][name]['init'] = init
            else:
                o['class']['field'][name]['init'] = typ
        elif init in o['global'].keys():
            o['class']['field'][name]['init'] = init
        else:
            o['class']['field'][name]['init'] = typ
    def visitMethodDecl(self, ast: MethodDecl, o: object):
        CheckForLoop().visitBlock(ast.body,[])
        if ast.returnType: ast.returnType.accept(self,o)
        envi = {
            'global' : o['global'],
            'class'  : o['class'],
            'method' : o['class']['field'][ast.name.name],
            'block'  : o['class']['field'][ast.name.name]['field']
        }
        for key in envi['method']['param'].keys():
            envi['block'][0][key] = {
            'type': envi['method']['param'][key]['type'],
            'kind': "instance",
            'init': "",
            'const': False}
        ast.body.accept(self,envi)
    def visitAssign(self, ast: Assign, o: object):
        lhs = ast.lhs.accept(GetLHS(),o)
        rhs = ast.exp.accept(GetTypeExp(),o)
        if not 'const' in lhs:
            raise TypeMismatchInStatement(ast)
        if lhs['const'] == True:
            raise CannotAssignToConstant(ast)
        if lhs['type'] == 'void':
            raise TypeMismatchInStatement(ast)
        if GetTypeExp().matchType(lhs['type'],rhs,o) == False:
            raise TypeMismatchInStatement(ast)
        if rhs in o['global'].keys(): lhs['init'] = rhs
        elif rhs[0] == '[':
            arrType = rhs[1:]
            while arrType[0] != ']': arrType = arrType[1:]
            arrType = arrType[1:]
            if arrType in o['global'].keys(): lhs['init'] = rhs
            else: lhs['init'] = lhs['type']
        else: lhs['init'] = lhs['type']
    def visitIf(self, ast: If, o: object):
        # CHECK expr IS bool?
        expr = ast.expr.accept(GetTypeExp(),o)
        if expr != 'bool':
            raise TypeMismatchInStatement(ast)
        # VISIT thenStmt
        envi = {'global':o['global'],'class':o['class'], 'method':o['method'],'block':o['block']}
        if hasattr(ast.thenStmt,'decl') and hasattr(ast.thenStmt,'stmt'): envi['block'] = [{}] + envi['block']
        ast.thenStmt.accept(self,envi)
        # VISIT elseStmt
        if not ast.elseStmt is None:
            envi = {'global':o['global'],'class':o['class'], 'method':o['method'],'block':o['block']}
            if hasattr(ast.elseStmt,'decl') and hasattr(ast.elseStmt,'stmt'): envi['block'] = [{}] + envi['block']
            ast.elseStmt.accept(self,envi)
    def visitFor(self, ast: For, o: object):
        # CHECK id, expr1, expr2 IS int?
        id_name = ast.id.name
        id_dic = {}
        for block in o['block']:
            if id_name in block: id_dic = block[id_name]
        if id_dic == {}: raise Undeclared(Variable(),id_name)
        if id_dic['const'] == True: raise CannotAssignToConstant(Assign(ast.id,ast.expr1))
        expr1 = ast.expr1.accept(GetTypeExp(),o)
        expr2 = ast.expr2.accept(GetTypeExp(),o)
        if id_dic['type'] != 'int' or expr2 != 'int' or expr1 !='int': raise TypeMismatchInStatement(ast)
        # VISIT loop
        envi = {'global':o['global'],'class':o['class'], 'method':o['method'],'block':o['block']}
        envi['block'] = [{id_name: id_dic}] + envi['block']
        ast.loop.accept(self,envi)
    def visitBreak(self, ast: Break, o: object): pass
    def visitContinue(self, ast: Continue, o: object): pass
    def visitReturn(self, ast: Return, o: object):
        exp = ast.expr.accept(GetTypeExp(),o)
        #print(o['method']['type'] + " " + exp)
        if GetTypeExp().matchType(o['method']['type'],exp,o) == False:
            raise TypeMismatchInStatement(ast)
    def visitCallStmt(self, ast: CallStmt, o: object):  
        kind = 'instance'
        obj = ''
        if hasattr(ast.obj,'name'):
            # obj can be class name to static access
            name = ast.obj.name
            if 'block' in o:
                for scope in o['block']:
                    if name in scope:
                        if scope[name]['init'] != '':
                            obj = scope[name]['init']
                        else:
                            obj = scope[name]['type']
            if obj == '' and name in o['global']:
                obj = name
                kind = 'static'
            if obj == '': raise Undeclared(Identifier(),name)
        else: obj = ast.obj.accept(GetTypeExp(), o)
        if obj in ['int','float','string','bool','nil'] or obj[0] == '[': 
            raise TypeMismatchInStatement(ast)
        if not obj in o['global']: raise Undeclared(Class(),obj)
        # FIND ENVIRONMENT HAVE THIS METHOD
        method = ast.method.name
        envi = o['global'][obj]
        while True:
            if method in envi['field']:
                if GetTypeExp().getTypeDecl(method,envi['field']) == 'method':
                    if envi['field'][method]['kind'] == kind: break
                    raise IllegalMemberAccess(ast)
                else: raise TypeMismatchInStatement(ast)
            parent = o['global'][obj]['parent']
            if parent == '': raise Undeclared(Method(), method)
            envi = o['global'][parent]
        if envi['field'][method]['type'] != 'void': raise TypeMismatchInStatement(ast)
        # CHECK PARAM MATCH
        list_param = [envi['field'][method]['param'][par]['type'] for par in envi['field'][method]['param'].keys()]
        pass_value = [par.accept(GetTypeExp(), o) for par in ast.param]
        if len(list_param) != len(pass_value): raise TypeMismatchInStatement(ast)
        for i in range(len(list_param)):
            if GetTypeExp().matchType(list_param[i], pass_value[i], o) == False: raise TypeMismatchInStatement(ast)
    def visitBlock(self, ast: Block, o: object):
        for decl in ast.decl:
            o = decl.accept(VisitStorageDecl(), o)
        for stmt in ast.stmt:
            if hasattr(stmt,'decl') and hasattr(stmt,'stmt'): o['block'] = [{}] + o['block']
            stmt.accept(self,o)
