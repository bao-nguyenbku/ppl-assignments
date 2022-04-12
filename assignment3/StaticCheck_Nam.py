from AST import * 
from Visitor import *
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
class EnvGlobal(BaseVisitor):
    def visitProgram(self, ctx, param):
        param={}
        [self.visit(x,param) for x in ctx.decl]
        return param

    #  variable : Id    varType : Type    varInit : Expr = None
    def visitVarDecl(self, ast, param):
        if ast.variable.name in param:
            raise Redeclared(Attribute(),ast.variable.name)
        param[ast.variable.name] = [self.visit(ast.varType,param),"var"]
        return ast.variable.name

    #constant : Id     constType : Type     value : Expr
    def visitConstDecl(self, ast, param):
        if ast.constant.name in param:
            raise Redeclared(Attribute(),ast.constant.name)
        if ast.value is None:
            raise  IllegalConstantExpression(None)
        param[ast.constant.name] = [self.visit(ast.constType,param),"const"]
        return ast.constant.name

    # classname : Id    parentname : Id = None    memlist : List[MemDecl]
    def visitClassDecl(self, ast, param):
        if ast.classname.name in param:
            raise Redeclared(Class(),ast.classname.name)
        param[ast.classname.name] = {}
        [self.visit(x,param[ast.classname.name]) for x in ast.memlist]

    # name: Id    returnType: Type   kind: SIKind   param: List[VarDecl]   body: Block
    def visitMethodDecl(self, ast, param):
        if ast.name.name in param:
            raise Redeclared(Method(),ast.name.name)
        typ = self.visit(ast.returnType,param) if ast.returnType else None
        param[ast.name.name] = [typ,'Method',str(ast.kind),[]]
        
    # decl: StoreDecl       kind: SIKind
    def visitAttributeDecl(self, ast, param):
        name = self.visit(ast.decl,param)  
        param[name] +=[str(ast.kind)]

    #name:str
    def visitId(self, ast, param): 
        if ast.name in param['global']:
            return ast.name 
        if param['local'] is not None:
            if ast.name in param['local'][-1]:
                return param['local'][-1][ast.name]
        raise Undeclared(Identifier(),ast.name)

    def visitFieldAccess(self, ast, param):
        #print(ast.obj)
        obj = EnvGlobal().visit(ast.obj,param)
        # this.a
        if obj == 6:  
            if ast.fieldname.name in param['global'][param['curent']]:
                if param['global'][param['curent']][ast.fieldname.name][1] == 'Method': 
                    raise Undeclared(Attribute(),ast.fieldname.name)
            else: raise Undeclared(Attribute(),ast.fieldname.name)
            if param['global'][param['curent']][ast.fieldname.name][2] == 'Static':
                raise IllegalMemberAccess(ast)
            #print(param['global'][param['curent']][ast.fieldname.name])
            return param['global'][param['curent']][ast.fieldname.name]
        

        # classtype: x.a    instance attr
        if type(obj) is list: 
            if obj[0] in param['global']:
                if ast.fieldname.name in param['global'][obj[0]] and (param['parent'] == obj[0] or param['curent'] == obj[0]):
                    if param['global'][obj[0]][ast.fieldname.name][1] == 'Method': 
                        raise Undeclared(Attribute(),ast.fieldname.name)
                else: raise Undeclared(Attribute(),ast.fieldname.name)
            else: raise Undeclared(Class(),obj[0])

            if param['global'][obj[0]][ast.fieldname.name][2] == 'Static':
                raise IllegalMemberAccess(ast)
            return param['global'][obj[0]][ast.fieldname.name]

        # class: X.a        static attr 
        elif obj in param['global']:
            if ast.fieldname.name in param['global'][obj]:
                if param['global'][obj][ast.fieldname.name][1] == 'Method': 
                    raise Undeclared(Attribute(),ast.fieldname.name)
            else: raise Undeclared(Attribute(),ast.fieldname.name)
    
            if param['global'][obj][ast.fieldname.name][2] == 'Instance':
                raise IllegalMemberAccess(ast)
            return param['global'][obj][ast.fieldname.name]  
            
    def visitIntType(self, ast, param): return 1
    def visitFloatType(self, ast, param): return 2
    def visitBoolType(self, ast, param): return 3
    def visitStringType(self, ast, param): return 4
    def visitVoidType(self, ast, param): return 0
    def visitArrayType(self, ast, param): 
        typ = self.visit(ast.eleType,param)
        if type(typ) is str:
            return '5' + typ
        return 50 + typ
    def visitClassType(self, ast, param): return ast.classname.name

    def visitIntLiteral(self, ast, param): return 1
    def visitFloatLiteral(self, ast, param):  return 2
    def visitBooleanLiteral(self, ast, param): return 3
    def visitStringLiteral(self, ast, param): return 4
    def visitArrayLiteral(self, ast, param): return 5
    def visitSelfLiteral(self, ast, param): return 6
    def visitNullLiteral(self, ast, param): return 7
#-----------------------------------------------------------------------------------------------------
class EnvPara(BaseVisitor):
    def visitProgram(self, ast, param):
        param = EnvGlobal().visit(ast, param)
        [self.visit(x,param) for x in ast.decl]
        return param

    #  variable : Id    varType : Type    varInit : Expr = None
    def visitVarDecl(self, ast, param):
        for i in range(0,len(param[3])):
            if ast.variable.name == param[3][i][1]:
                raise Redeclared(Parameter(),ast.variable.name)
        param[3] += [(EnvGlobal().visit(ast.varType,param),ast.variable.name)]

    # classname : Id    parentname : Id = None    memlist : List[MemDecl]
    def visitClassDecl(self, ast, param):
        [self.visit(x,param[ast.classname.name]) for x in ast.memlist]

    # name: Id    returnType: Type   kind: SIKind   param: List[VarDecl]   body: Block
    def visitMethodDecl(self, ast, param):
        param[ast.name.name][3] = []
        [self.visit(x,param[ast.name.name]) for x in ast.param]
#-----------------------------------------------------------------------------------------------------
class EnvAttr(BaseVisitor):
    def visitProgram(self, ast, param):
        param = EnvPara().visit(ast,param)
        [self.visit(x,param) for x in ast.decl]
        return param

    #  variable : Id    varType : Type    varInit : Expr = None
    def visitVarDecl(self, ast, param):
        if type(ast.varType) is ClassType:
            if ast.varType.classname.name not in param["global"]:
                raise Undeclared(Class(),ast.varType.classname.name)
        if type(ast.varType) is ArrayType:
            if type(ast.varType.eleType) is ClassType:
                if ast.varType.eleType.classname.name not in param["global"]:
                    raise Undeclared(Class(),ast.varType.eleType.classname.name)
        if ast.varInit is not None: 
            self.visit(ast.varInit,param)
        
    #constant : Id     constType : Type     value : Expr
    def visitConstDecl(self, ast, param):
        if type(ast.constType) is ClassType:
            if ast.constType.classname.name not in param["global"]:
                raise Undeclared(Class(),ast.constType.classname.name)
        val = self.visit(ast.value,param)
        if type(val) is int:
            if val < 6: 
                if val != param["global"][param['curent']][ast.constant.name][0]:
                    raise TypeMismatchInConstant(ast)
            else: raise TypeMismatchInConstant(ast)           # final int a = 1.2; final int a =1 + 1.2;
        elif type(val) is list:
            if val[1] != 'const':
                raise IllegalConstantExpression(ast.value)          # final int a = m.method() + 1;
            if val[0] != param["global"][param['curent']][ast.constant.name][0]:
                raise TypeMismatchInConstant(ast)               # final float b = 1; final int a = this.b;

    # decl: StoreDecl       kind: SIKind
    def visitAttributeDecl(self, ast, param):
        self.visit(ast.decl,param)    

    # classname : Id    parentname : Id = None    memlist : List[MemDecl]
    def visitClassDecl(self, ast, param):
        if ast.parentname is not None: 
            if ast.parentname.name not in param:
                raise Undeclared(Class(),ast.parentname.name)
        env = {}
        env["curent"] = ast.classname.name   # class_a
        env["parent"] = ast.parentname.name if ast.parentname else None  
        env["global"] = param               # class_a, class_b,class_c
        [self.visit(x,env) for x in ast.memlist]

    # op:str    left: Expr     right: Expr
    def visitBinaryOp(self, ast, param):
        g1 = self.visit(ast.left,param)
        g2 = self.visit(ast.right,param)
        e1 = 0
        e2 = 0
        r = [1,'const','Instance']
        if type(g1) is list:            # attr: [type, var/const/method, Instance/Static]
            e1 = g1[0]
            r[1] = g1[1]
            r[2] = g1[2]
        elif type(g1) is int:           
            if g1 > 7: 
                e1 = g1%10              # array index:   int[7]  a    =>   51
                r[1] = 'var'
            else: e1 = g1

        if type(g2) is list:            # attr: [type, var/const/method, Instance/Static]
            e2 = g2[0]
            r[1] = g2[1]
            r[2] = g2[2]
        elif type(g2) is int:           
            if g2 > 7: 
                e2 = g2%10              # array index:   int[7]  a    =>   51
                r[1] = 'var'
            else: e2 = g2

        e2 = g2[0] if type(g2) is list else  g2
        if type(g2) is list:
            if g2[1] == 'Method': r[1] = g2[1]
        if ast.op in ['+', '-', '*', '/']:
            if (e1 != 1 and e1 != 2) or (e2 != 1 and e2 != 2):
                raise TypeMismatchInExpression(ast)
            if e1 == 1 and e2 == 1 and ast.op != '/':
                return r
            r[0] = 2
            return r

        if ast.op in ['<', '<=', '>', '>=']:
            if (e1 != 1 and e1 != 2) or (e2 != 1 and e2 != 2):
                raise TypeMismatchInExpression(ast)
            r[0] = 3
            return r

        if ast.op in ['\\', '%']:
            if e1 != 1 or e2 != 1:
                raise TypeMismatchInExpression(ast)  
            return r

        if ast.op in ['==', '!=']:
            if e1 != e2 or (e1 != 3 and e1 != 1): 
                raise TypeMismatchInExpression(ast)  
            r[0] = 3
            return r

        if ast.op in ['&&', '||']:
            if e1 != 3 or e2 != 3: 
                raise TypeMismatchInExpression(ast)  
            r[0] = 3
            return r

        if ast.op == '^':
            if e1 != 4 or e2 != 4:
                raise TypeMismatchInExpression(ast)  
            r[0] = 4
            return r         

    # op:str    body:Expr    
    def visitUnaryOp(self, ast, param):
        g1 = self.visit(ast.body,param)
        e = 0
        r = [1,'const','Instance']
        if type(g1) is list:            # attr: [type, var/const/method, Instance/Static]
            e = g1[0]
            r[1] = g1[1]
            r[2] = g1[2]
        elif type(g1) is int:           
            if g1 > 7: 
                e = g1%10              # array index:   int[7]  a    =>   51
                r[1] = 'var'
            else: e = g1
            
        if ast.op in ['+','-']:
            if e != 1 and e != 2:
                raise TypeMismatchInExpression(ast)  
            r[0] = e
            return r

        if ast.op == '!':
            if e != 3:
                raise TypeMismatchInExpression(ast)  
            r[0] = 3
            return r

    #obj: Expr    method:Id      param:List[Expr]
    def visitCallExpr(self, ast, param):
        obj = EnvGlobal().visit(ast.obj,param)
        method = None
        # this.a
        if obj == 6:  
            if ast.method.name in param['global'][param['curent']]:
                if param['global'][param['curent']][ast.method.name][1] != 'Method': 
                    raise Undeclared(Method(),ast.method.name)
            else: raise Undeclared(Method(),ast.method.name)
            method = param['global'][param['curent']][ast.method.name]
            if method[2] == 'Static':
                raise IllegalMemberAccess(ast)

        # classtype: x.a
        if type(obj) is list: 
            if obj[0] in param['global']:
                if ast.method.name in param['global'][obj[0]]:
                    if param['global'][obj[0]][ast.method.name][1] != 'Method': 
                        raise Undeclared(Method(),ast.method.name)
                else: raise Undeclared(Method(),ast.method.name)
            else: raise Undeclared(Class(),obj[0])
            method = param['global'][obj[0]][ast.method.name]
            if method[2] == 'Static':
                raise IllegalMemberAccess(ast)

        # class: X.a
        elif obj in param['global']:
            if ast.method.name in param['global'][obj]:
                if param['global'][obj][ast.method.name][1] != 'Method': 
                    raise Undeclared(Method(),ast.method.name)
            else: raise Undeclared(Method(),ast.method.name)
            method =param['global'][obj][ast.method.name]
            if method[2] == 'Instance':
                raise IllegalMemberAccess(ast)
        # Check method
        if method is not None: 
            if method[0] != 0: # return type != void 
                if len(ast.param) == len(method[3]):
                    for i in range(0,len(ast.param)):
                        para = self.visit(ast.param[i],param)
                        if type(para) is list:
                            if para[0] != method[3][i][0]:
                                raise TypeMismatchInExpression(ast)
                        else: 
                            if para != method[3][i][0]:
                                raise TypeMismatchInExpression(ast)
                else: raise TypeMismatchInExpression(ast)
            else: raise TypeMismatchInExpression(ast)
        return method
        
    # classname:Id      param:List[Expr]     
    def visitNewExpr(self, ast, param):
        if ast.classname.name not in param['global']:
            raise Undeclared(Class(),ast.classname)
        return 7
        
    #name:str
    def visitId(self, ast, param): 
        raise Undeclared(Identifier(),ast.name)
        
    # arr:Expr      idx:Expr                a[1]
    def visitArrayCell(self, ast, param):
        typ = self.visit(ast.arr,param)
        if (type(typ) is int and typ[0] < 10) or (type(typ) is str and typ[0]!='5'):  # not arr type
            raise TypeMismatchInExpression(ast) 
        idx = self.visit(ast.idx,param)
        if idx != 1: 
            raise TypeMismatchInExpression(ast)
        return typ 

    # obj:Expr      fieldname:Id
    def visitFieldAccess(self, ast, param):
        obj = EnvGlobal().visit(ast.obj,param)
        # this.a
        if obj == 6:  
            if ast.fieldname.name in param['global'][param['curent']]:
                if param['global'][param['curent']][ast.fieldname.name][1] == 'Method': 
                    raise Undeclared(Attribute(),ast.fieldname.name)
            else: raise Undeclared(Attribute(),ast.fieldname.name)
            if param['global'][param['curent']][ast.fieldname.name][2] == 'Static':
                raise IllegalMemberAccess(ast)
            #print(param['global'][param['curent']][ast.fieldname.name])
            return param['global'][param['curent']][ast.fieldname.name]
       

        # classtype: x.a    instance attr
        if type(obj) is list: 
            if obj[0] in param['global']:
                if ast.fieldname.name in param['global'][obj[0]] and (param['parent'] == obj[0] or param['curent'] == obj[0]):
                    if param['global'][obj[0]][ast.fieldname.name][1] == 'Method': 
                        raise Undeclared(Attribute(),ast.fieldname.name)
                else: raise Undeclared(Attribute(),ast.fieldname.name)
            else: raise Undeclared(Class(),obj[0])

            if param['global'][obj[0]][ast.fieldname.name][2] == 'Static':
                raise IllegalMemberAccess(ast)
            return param['global'][obj[0]][ast.fieldname.name]

        # class: X.a        static attr 
        elif obj in param['global']:
            if ast.fieldname.name in param['global'][obj]:
                if param['global'][obj][ast.fieldname.name][1] == 'Method': 
                    raise Undeclared(Attribute(),ast.fieldname.name)
            else: raise Undeclared(Attribute(),ast.fieldname.name)
    
            if param['global'][obj][ast.fieldname.name][2] == 'Instance':
                raise IllegalMemberAccess(ast)
            return param['global'][obj][ast.fieldname.name]          

    def visitIntLiteral(self, ast, param): return 1
    def visitFloatLiteral(self, ast, param): return 2
    def visitBooleanLiteral(self, ast, param): return 3
    def visitStringLiteral(self, ast, param): return 4
    def visitArrayLiteral(self, ast, param):
        if len(ast.value) >1:
            typ = self.visit(ast.value[0],param)
            for i in range(1,len(ast.value)):
                if(typ != self.visit(ast.value[i],param)):
                    raise IllegalArrayLiteral(ast)
        return 5
    def visitSelfLiteral(self, ast, param): return 6
    def visitNullLiteral(self, ast, param): return 7
    


#--------------------------------------------------------------------------------------------


class StaticChecker(BaseVisitor):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
               
    def __init__(self,ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, param): 
        param = EnvAttr().visit(ast,param)
        [self.visit(x,param) for x in ast.decl]
        return param
    # classname : Id    parentname : Id = None    memlist : List[MemDecl]
    def visitClassDecl(self, ast, param):
        env = {}
        env["curent"] = ast.classname.name   # class_a
        env["parent"] = ast.parentname.name if ast.parentname else None  
        env["global"] = param 
        [self.visit(x,env) for x in ast.memlist]
        # env{curent:class_a, parent:class_b ,global: {..,...} }

    # decl: StoreDecl       kind: SIKind
    # def visitAttributeDecl(self, ast, param):
    #     self.visit(ast.decl,param)

     # varType : Type   variable : Id    varInit : Expr = None
    def visitVarDecl(self, ast, param):
        #param {x:inttype,y:floattype}
        if len(param['local']) == 2:
            if ast.variable.name in param['local'][0]:
                raise Redeclared(Variable(),ast.variable.name)
        else:
            if ast.variable.name in param['local'][-1]:
                raise Redeclared(Variable(),ast.variable.name)
        param['local'][-1][ast.variable.name] = [self.visit(ast.varType,param),"var"]
        if ast.varInit is not None: 
            self.visit(ast.varInit,param)

    #constant : Id     constType : Type     value : Expr
    def visitConstDecl(self, ast, param):
        #param {x:inttype,y:floattype}
        if len(param['local']) == 2:
            if ast.constant.name in param['local'][0]:
                raise Redeclared(Constant(),ast.constant.name)
        else:
            if ast.constant.name in param['local'][-1]:
                raise Redeclared(Constant(),ast.constant.name)
        param['local'][-1][ast.constant.name] = [self.visit(ast.constType,param),"const"]
        val = self.visit(ast.value,param)
        if type(val) is int:
            if val < 6: 
                if val != param['local'][-1][ast.constant.name][0]:
                    raise TypeMismatchInConstant(ast)
            else: raise TypeMismatchInConstant(ast)           # final int a = 1.2; final int a =1 + 1.2;
        elif type(val) is list:
            if val[1] != 'const':
                raise IllegalConstantExpression(ast.value)          # final int a = m.method() + 1;
            if val[0] != param['local'][-1][ast.constant.name][0]:
                raise TypeMismatchInConstant(ast)               # final float b = 1; final int a = this.b;

    # name: Id    returnType: Type   kind: SIKind   param: List[VarDecl]   body: Block
    def visitMethodDecl(self, ast, param):
        env = {}
        env["global"] = param["global"]     # class_a, class_b,class_c
        env["curent"] = param["curent"]    # class_a
        env["parent"] = param["parent"]
        env['method'] = ast.name.name
        env["local"] = [{}]
        x = env["global"][env["curent"]][ast.name.name][3]
        for i in range(0,len(x)):
            env['local'][0][x[i][1]] = [x[i][0],'var']
        self.visit(ast.body,env)
        # env{curent:class_a, parent:class_b ,global: {..,...}, local: {x:inttype,y:floattype} }

    # stmt:List[Stmt]   decl:List[StoreDecl]
    def visitBlock(self, ast, param):
        env = {}
        env["global"] = param["global"]     # class_a, class_b,class_c
        env["curent"] = param["curent"]    # class_a
        env["parent"] = param["parent"]
        env["local"] = param["local"]
        env['method'] = param['method']
        env["local"].append({})
        [self.visit(stmt,env) for stmt in ast.decl]        
        [self.visit(stmt,env) for stmt in ast.stmt] 
        param['local'].pop(-1)
    
    # op:str    left: Expr     right: Expr
    def visitBinaryOp(self, ast, param):
        g1 = self.visit(ast.left,param)
        g2 = self.visit(ast.right,param)
        e1 = 0
        e2 = 0
        r = [1,'const','Instance']
        if type(g1) is list:            # attr: [type, var/const/method, Instance/Static]
            e1 = g1[0]
            r[1] = g1[1]
            r[2] = g1[2]
        elif type(g1) is int:           
            if g1 > 7: 
                e1 = g1%10              # array index:   int[7]  a    =>   51
                r[1] = 'var'
            else: e1 = g1

        if type(g2) is list:            # attr: [type, var/const/method, Instance/Static]
            e2 = g2[0]
            r[1] = g2[1]
            r[2] = g2[2]
        elif type(g2) is int:           
            if g2 > 7: 
                e2 = g2%10              # array index:   int[7]  a    =>   51
                r[1] = 'var'
            else: e2 = g2

        e2 = g2[0] if type(g2) is list else  g2
        if type(g2) is list:
            if g2[1] == 'Method': r[1] = g2[1]
        if ast.op in ['+', '-', '*', '/']:
            if (e1 != 1 and e1 != 2) or (e2 != 1 and e2 != 2):
                raise TypeMismatchInExpression(ast)
            if e1 == 1 and e2 == 1 and ast.op != '/':
                return r
            r[0] = 2
            return r

        if ast.op in ['<', '<=', '>', '>=']:
            if (e1 != 1 and e1 != 2) or (e2 != 1 and e2 != 2):
                raise TypeMismatchInExpression(ast)
            r[0] = 3
            return r

        if ast.op in ['\\', '%']:
            if e1 != 1 or e2 != 1:
                raise TypeMismatchInExpression(ast)  
            return r

        if ast.op in ['==', '!=']:
            if e1 != e2 or (e1 != 3 and e1 != 1): 
                raise TypeMismatchInExpression(ast)  
            r[0] = 3
            return r

        if ast.op in ['&&', '||']:
            if e1 != 3 or e2 != 3: 
                raise TypeMismatchInExpression(ast)  
            r[0] = 3
            return r

        if ast.op == '^':
            if e1 != 4 or e2 != 4:
                raise TypeMismatchInExpression(ast)  
            r[0] = 4
            return r         

    # op:str    body:Expr    
    def visitUnaryOp(self, ast, param):
        g1 = self.visit(ast.body,param)
        e = 0
        r = [1,'const','Instance']
        if type(g1) is list:            # attr: [type, var/const/method, Instance/Static]
            e = g1[0]
            r[1] = g1[1]
            r[2] = g1[2]
        elif type(g1) is int:           
            if g1 > 7: 
                e = g1%10              # array index:   int[7]  a    =>   51
                r[1] = 'var'
            else: e = g1
            
        if ast.op in ['+','-']:
            if e != 1 and e != 2:
                raise TypeMismatchInExpression(ast)  
            r[0] = e
            return r

        if ast.op == '!':
            if e != 3:
                raise TypeMismatchInExpression(ast)  
            r[0] = 3
            return r

    #obj: Expr    method:Id      param:List[Expr]
    def visitCallExpr(self, ast, param):
        obj = EnvGlobal().visit(ast.obj,param)
        method = None
        # this.a
        if obj == 6:  
            if ast.method.name in param['global'][param['curent']]:
                if param['global'][param['curent']][ast.method.name][1] != 'Method': 
                    raise Undeclared(Method(),ast.method.name)
            else: raise Undeclared(Method(),ast.method.name)
            method = param['global'][param['curent']][ast.method.name]
            if method[2] == 'Static':
                raise IllegalMemberAccess(ast)

        # classtype: x.a
        if type(obj) is list: 
            if obj[0] in param['global']:
                if ast.method.name in param['global'][obj[0]]:
                    if param['global'][obj[0]][ast.method.name][1] != 'Method': 
                        raise Undeclared(Method(),ast.method.name)
                else: raise Undeclared(Method(),ast.method.name)
            else: raise Undeclared(Class(),obj[0])
            method = param['global'][obj[0]][ast.method.name]
            if method[2] == 'Static':
                raise IllegalMemberAccess(ast)

        # class: X.a
        elif obj in param['global']:
            if ast.method.name in param['global'][obj]:
                if param['global'][obj][ast.method.name][1] != 'Method': 
                    raise Undeclared(Method(),ast.method.name)
            else: raise Undeclared(Method(),ast.method.name)
            method =param['global'][obj][ast.method.name]
            if method[2] == 'Instance':
                raise IllegalMemberAccess(ast)
        # Check method
        if method is not None: 
            if method[0] != 0: # return type != void 
                if len(ast.param) == len(method[3]):
                    for i in range(0,len(ast.param)):
                        para = self.visit(ast.param[i],param)
                        if type(para) is list:
                            if para[0] != method[3][i][0]:
                                raise TypeMismatchInExpression(ast)
                        else: 
                            if para != method[3][i][0]:
                                raise TypeMismatchInExpression(ast)
                else: raise TypeMismatchInExpression(ast)
            else: raise TypeMismatchInExpression(ast)
        return method
        

    # classname:Id      param:List[Expr]     
    def visitNewExpr(self, ast, param):
        if ast.classname.name not in param['global']:
            raise Undeclared(Class(),ast.classname)
        return 7

    #name:str
    def visitId(self, ast, param):
        for i in range(0, len(param['local'])):
            if ast.name in param['local'][i]:
                return param['local'][i][ast.name]
        raise Undeclared(Identifier(),ast.name)

    # arr:Expr      idx:Expr
    def visitArrayCell(self, ast, param):
        typ = self.visit(ast.arr,param)
        if (type(typ) is int and typ[0] < 10) or (type(typ) is str and typ[0]!='5'):   # not arr type
            raise TypeMismatchInExpression(ast) 
        idx = self.visit(ast.idx,param)
        if idx != 1: 
            raise TypeMismatchInExpression(ast)
        return typ 

    # obj:Expr      fieldname:Id
    def visitFieldAccess(self, ast, param):
        #print(ast.obj)
        obj = EnvGlobal().visit(ast.obj,param)
        # this.a
        if obj == 6:  
            if ast.fieldname.name in param['global'][param['curent']]:
                if param['global'][param['curent']][ast.fieldname.name][1] == 'Method': 
                    raise Undeclared(Attribute(),ast.fieldname.name)
            else: raise Undeclared(Attribute(),ast.fieldname.name)
            if param['global'][param['curent']][ast.fieldname.name][2] == 'Static':
                raise IllegalMemberAccess(ast)
            #print(param['global'][param['curent']][ast.fieldname.name])
            return param['global'][param['curent']][ast.fieldname.name]
        

        # classtype: x.a    instance attr
        if type(obj) is list: 
            if obj[0] in param['global']:
                if ast.fieldname.name in param['global'][obj[0]] and (param['parent'] == obj[0] or param['curent'] == obj[0]):
                    if param['global'][obj[0]][ast.fieldname.name][1] == 'Method': 
                        raise Undeclared(Attribute(),ast.fieldname.name)
                else: raise Undeclared(Attribute(),ast.fieldname.name)
            else: raise Undeclared(Class(),obj[0])

            if param['global'][obj[0]][ast.fieldname.name][2] == 'Static':
                raise IllegalMemberAccess(ast)
            return param['global'][obj[0]][ast.fieldname.name]

        # class: X.a        static attr 
        elif obj in param['global']:
            if ast.fieldname.name in param['global'][obj]:
                if param['global'][obj][ast.fieldname.name][1] == 'Method': 
                    raise Undeclared(Attribute(),ast.fieldname.name)
            else: raise Undeclared(Attribute(),ast.fieldname.name)
    
            if param['global'][obj][ast.fieldname.name][2] == 'Instance':
                raise IllegalMemberAccess(ast)
            return param['global'][obj][ast.fieldname.name]       

    #expr:Expr , thenStmt:Stmt , elseStmt: Stmt = None
    def visitIf(self, ast, param):
        exp = self.visit(ast.expr, param)
        if type(exp) is list:
            if exp[0] != 3:
                raise TypeMismatchInStatement(ast)
        elif exp != 3: raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt,param)

        if ast.elseStmt: 
            self.visit(ast.elseStmt,param)
        

    #id:Id , expr1:Expr, expr2:Expr, up: bool , loop: Stmt
    def visitFor(self, ast, param):
        exp1 = self.visit(ast.expr1,param)
        exp2 = self.visit(ast.expr2,param)
        a1 = exp1 if type(exp1) is not list else exp1[0]
        a2 = exp2 if type(exp2) is not list else exp2[0]
        if a1 != 1 or a2 != 1:
            raise TypeMismatchInStatement(ast)
        id = self.visit(ast.id,param)
        if id[1] == 'const':
            raise CannotAssignToConstant(Assign(ast.id,ast.expr1))
        if id[0] not in [1,2]: raise TypeMismatchInStatement(ast)
        param['local'].append('for')
        self.visit(ast.loop,param)
        param['local'].remove('for')


    def visitContinue(self, ast, param):
        if 'for' not in param['local']:
            raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        if 'for' not in param['local']:
            raise MustInLoop(ast)

    # expr: Expr
    def visitReturn(self, ast, param):
        expr = self.visit(ast.expr,param)
        if type(expr) is list:
            expr = expr[0]
            if type(expr) is int:
                if expr>10: expr = expr%10
            elif type(expr) is str:
                expr=6  
        elif type(expr) is str:
            expr=6
        elif type(expr) is int:
            if expr>10: expr = expr%10
        
        x = param['global'][param['curent']][param['method']][0]
        if expr != x:
            if expr ==1 and x ==2: pass
            else: raise TypeMismatchInStatement(ast)

    # lhs:Expr,  exp:Expr  
    def visitAssign(self, ast, param):
        lhs = self.visit(ast.lhs,param)
        #---------------------------
        #print(param['local'])
        if type(lhs) is list:
            if lhs[0] == 0:
                raise TypeMismatchInStatement(ast)
        elif lhs == 0: raise TypeMismatchInStatement(ast)
        exp = self.visit(ast.exp,param)

        if type(lhs) is list:
            lhs = lhs[0]
            if type(lhs) is int:
                if lhs>10: lhs = lhs%10
            elif type(lhs) is str:
                lhs=6  
        elif type(lhs) is str:
            lhs=6
        elif type(lhs) is int:
            if lhs>10: lhs = lhs%10

        if type(exp) is list:
            exp = exp[0]
            if type(exp) is int:
                if exp>10: exp = exp%10
            elif type(exp) is str:
                exp=6
        elif type(exp) is str:
            exp=6
        elif type(exp) is int:
            if exp>10: exp = exp%10
        # print(lhs)
        # print(exp)
        if lhs != exp:
            if lhs ==2 and exp == 1:pass
            elif (lhs ==6 and exp ==7):pass
            else: raise TypeMismatchInStatement(ast)
                
    # obj: Expr, method:Id, param:List[Expr
    def visitCallStmt(self, ast, param):
        obj = EnvGlobal().visit(ast.obj,param)
        #print(obj)

        method = None
        # this.a
        if obj == 6:  
            if ast.method.name in param['global'][param['curent']]:
                if param['global'][param['curent']][ast.method.name][1] != 'Method': 
                    raise Undeclared(Method(),ast.method.name)
            else: raise Undeclared(Method(),ast.method.name)
            method = param['global'][param['curent']][ast.method.name]
            if method[2] == 'Static':
                raise IllegalMemberAccess(ast)

        # classtype: x.a
        if type(obj) is list: 
            if obj[0] in param['global']:
                if ast.method.name in param['global'][obj[0]]:
                    if param['global'][obj[0]][ast.method.name][1] != 'Method': 
                        raise Undeclared(Method(),ast.method.name)
                else: raise Undeclared(Method(),ast.method.name)
            else: raise Undeclared(Class(),obj[0])
            method = param['global'][obj[0]][ast.method.name]
            if method[2] == 'Static':
                raise IllegalMemberAccess(ast)

        # class: X.a
        elif obj in param['global']:
            if ast.method.name in param['global'][obj]:
                if param['global'][obj][ast.method.name][1] != 'Method': 
                    raise Undeclared(Method(),ast.method.name)
            else: raise Undeclared(Method(),ast.method.name)
            method =param['global'][obj][ast.method.name]
            if method[2] == 'Instance':
                raise IllegalMemberAccess(ast)
        # Check method
        if method is not None: 
            if method[0] != 0: # return type != void 
                if len(ast.param) == len(method[3]):
                    for i in range(0,len(ast.param)):
                        para = self.visit(ast.param[i],param)
                        if type(para) is list:
                            if para[0] != method[3][i][0]:
                                raise TypeMismatchInExpression(ast)
                        else: 
                            if para != method[3][i][0]:
                                raise TypeMismatchInExpression(ast)
                else: raise TypeMismatchInExpression(ast)
            else: raise TypeMismatchInExpression(ast)
        return method
    
    def visitIntType(self, ast, param): return 1
    def visitFloatType(self, ast, param): return 2
    def visitBoolType(self, ast, param): return 3
    def visitStringType(self, ast, param): return 4
    def visitVoidType(self, ast, param): return 0
    def visitArrayType(self, ast, param): 
        typ = self.visit(ast.eleType,param)
        if type(typ) is str:
            return '5' + typ
        return 50 + typ
    def visitClassType(self, ast, param): return ast.classname.name

    def visitIntLiteral(self, ast, param): return 1
    def visitFloatLiteral(self, ast, param): return 2
    def visitBooleanLiteral(self, ast, param): return 3
    def visitStringLiteral(self, ast, param): return 4
    def visitArrayLiteral(self, ast, param):
        if len(ast.value) >1:
            typ = self.visit(ast.value[0],param)
            for i in range(1,len(ast.value)):
                if(typ != self.visit(ast.value[i],param)):
                    raise IllegalArrayLiteral(ast)
        return 5
    def visitSelfLiteral(self, ast, param): return 6
    def visitNullLiteral(self, ast, param): return 7


