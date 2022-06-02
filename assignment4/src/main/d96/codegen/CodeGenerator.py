'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from pprint import pprint

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType([], IntType()), CName(self.libName)),
                Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    
                Symbol("getFloat", MType([], FloatType()), CName(self.libName)),
                Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                
                Symbol("getBool", MType([], BoolType()), CName(self.libName)),
                Symbol("putBool", MType([BoolType()],VoidType()), CName(self.libName)),
                Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                
                Symbol("getStr", MType([], StringType()), CName(self.libName)),
                Symbol("putStr", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("putStrLn", MType([StringType()], VoidType()), CName(self.libName)),]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

class StringType(Type):
    
    def __str__(self):
        return "StringType"

    def accept(self, v, param):
        return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None
        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "Program"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, o):
        #ast: Program
        #c: Any
        # print(c)
        # self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        # e = SubBody(None, self.env)
        for x in ast.decl:
            self.visit(x, o)
        # # generate default constructor
        # self.genMETHOD(FuncDecl(Id("<init>"), list(), None, Block(list(), list())), c, Frame("<init>", VoidType))
        # self.emit.emitEPILOG()
        return o
    def visitClassDecl(self,ast,o):
        self.className = ast.classname.name
        self.emit = Emitter(self.path+"/" + self.className + ".j")
        parent_class = ast.parentname.name if ast.parentname else ""
        self.emit.printout(self.emit.emitPROLOG(self.className, parent_class))

        # [map(lambda x: self.visit(x,o) ,filter(lambda x: type(x) is AttributeDecl,ast.memlist))]
        # mem=list(filter(lambda x: x.value.value==ast.classname.name,self.env))
        # init=self.lookup("Constructor",mem,lambda x: x.name)
        # if not init:
        #     self.genMETHOD(MethodDecl(Instance(),Id("Constructor"), [],Block([])), self.env, Frame("Constructor", VoidType() ))
        [self.visit(ele, SubBody(Frame(ele.name, VoidType()), self.env)) for ele in ast.memlist if type(ele) == MethodDecl]
        self.emit.emitEPILOG()
        return o

    def visitMethodDecl(self, ast, o):
        self.genMETHOD(ast, o.sym, o.frame)

    def genMETHOD(self, consdecl, o, frame):
        #included default init and init
        isInit = True
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0
        returnType = VoidType()
        # methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else list(map(lambda x: x.varType,consdecl.param))
        mtype = MType(intype, returnType)
        isStatic = type(consdecl.kind) is Static
        self.emit.printout(self.emit.emitMETHOD(consdecl.name.name, mtype, isStatic ,frame))
        frame.enterScope(True)
        glenv = o
        # Generate code for parameter declarations
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(),frame))
        # else:
        #     if isInit:
        #         self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(),frame))
            
        # local = list(map(lambda x: self.visit(x,SubBody(frame,glenv)),consdecl.param))
        # glenv=local+glenv
            
        # body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        # if isInit:
        #     self.emit.printout(self.emit.emitREADVAR("this", ClassType(Id(self.className)), 0, frame))
        #     self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
    
        # list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.decl))
        # local = list(map(lambda x: self.visit(x,SubBody(frame,glenv)),body.inst))
        # glenv = local + glenv
    
        # list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.inst))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitContinue(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))
    
    def visitBreak(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))
    def visitIntLiteral(self,ast,o):
        return self.emit.emitPUSHICONST(ast.value,o.frame),IntType()

    def visitFloatLiteral(self,ast,o):
        return self.emit.emitPUSHFCONST(str(ast.value),o.frame),FloatType()

    def visitStringLiteral(self,ast,o):
        return self.emit.emitPUSHCONST(ast.value,StringType(),o.frame),StringType()

    def visitBooleanLiteral(self,ast,o):
        if ast.value: code = self.emit.emitPUSHICONST("true",o.frame)
        else: code = self.emit.emitPUSHICONST("false",o.frame)
        return code,BoolType()

    def visitNullLiteral(self, ast, o):
        return None

    
