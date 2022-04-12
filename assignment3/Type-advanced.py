class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        o = {}
        for x in ctx.decl:
            self.visit(x, o)
        for x in ctx.stmts:
            self.visit(x, o)

    def visitVarDecl(self,ctx:VarDecl,o):
        o[ctx.name] = 0
        
    def visitAssign(self,ctx:Assign,o):
        # o = {}
        left = self.visit(ctx.lhs, o)
        right = self.visit(ctx.rhs, o)
        if left == 0 and ctx.lhs.name not in o:
            raise UndeclaredIdentifier(ctx.lhs.name)
        if right == 0 and left == 0:
            raise TypeCannotBeInferred(ctx)
        elif right == 0 and left != 0:
            o[ctx.rhs.name] = left
        elif right != 0 and left == 0:
            o[ctx.lhs.name] = right
        elif right != left:
            raise TypeMismatchInStatement(ctx)

    def visitBinOp(self,ctx:BinOp,o):
        t1 = self.visit(ctx.e1, o)
        t2 = self.visit(ctx.e2, o)
        if t1 == 0 and ctx.e1.name not in o:
            raise UndeclaredIdentifier(ctx.e1.name)
        if t2 == 0 and ctx.e2.name not in o:
            raise UndeclaredIdentifier(ctx.e2.name)
            
        if ctx.op == "+" or ctx.op == "-" or ctx.op == "*" or ctx.op == "/":
            if t1 == 0:
                o[ctx.e1.name] = 1
                t1 = 1
            if t2 == 0:
                o[ctx.e2.name] = 1
                t2 = 1
            
            if (t1 != 1) or (t2 != 1):
                raise TypeMismatchInExpression(ctx)
            return 1
        elif ctx.op == "+." or ctx.op == "-." or ctx.op == "*." or ctx.op == "/.":
            if t1 == 0:
                o[ctx.e1.name] = 2
                t1 = 2
            if t2 == 0:
                o[ctx.e2.name] = 2
                t2 = 2
            
            if (t1 != 2) or (t2 != 2):
                raise TypeMismatchInExpression(ctx)
            return 2
        elif ctx.op == "!" or ctx.op == "||" or ctx.op == "&&" or ctx.op == ">b" or ctx.op == "=b":
            if t1 == 0:
                o[ctx.e1.name] = 3
                t1 = 3
            if t2 == 0:
                o[ctx.e2.name] = 3
                t2 = 3
            
            if (t1 != 3) or (t2 != 3):
                raise TypeMismatchInExpression(ctx)
            return 3
        elif ctx.op == ">" or ctx.op == "=":
            if t1 == 0:
                o[ctx.e1.name] = 1
                t1 = 1
            if t2 == 0:
                o[ctx.e2.name] = 1
                t2 = 1
            
            if (t1 != 1) or (t2 != 1):
                raise TypeMismatchInExpression(ctx)
            return 3
        elif ctx.op == ">." or ctx.op == "=.":
            if t1 == 0:
                o[ctx.e1.name] = 2
                t1 = 2
            if t2 == 0:
                o[ctx.e2.name] = 2
                t2 = 2
            
            if (t1 != 2) or (t2 != 2):
                raise TypeMismatchInExpression(ctx)
            return 3
                
    def visitUnOp(self,ctx:UnOp,o):
        t = self.visit(ctx.e, o)
        # t == 0 mean t is a Id
        if t == 0 and ctx.e.name not in o:
            raise UndeclaredIdentifier(ctx.e.name)
        if ctx.op == "-":
            if t == 0:
                o[ctx.e.name] = 1
                t = 1
                
            if t != 1:
                raise TypeMismatchInExpression(ctx)
            return 1
        elif ctx.op == "-.":
            if t == 0:
                o[ctx.e.name] = 2
                t = 2
            
            if t != 2:
                raise TypeMismatchInExpression(ctx)
            return 2
        elif ctx.op == "!":
            if t == 0:
                o[ctx.e.name] = 3
                t = 3
            
            if t != 3:
                raise TypeMismatchInExpression(ctx)
            return 3
        elif ctx.op == "i2f":
            if t == 0:
                o[ctx.e.name] = 1
                t = 1
            
            if t != 1:
                raise TypeMismatchInExpression(ctx)
            return 2
        elif ctx.op == "floor":
            if t == 0:
                o[ctx.e.name] = 2
                t = 2
            
            if t != 2:
                raise TypeMismatchInExpression(ctx)
            return 1
        
    def visitIntLit(self,ctx:IntLit,o):
        return 1
    def visitFloatLit(self,ctx,o):
        return 2
    def visitBoolLit(self,ctx,o):
        return 3
    def visitId(self,ctx,o):
        if ctx.name in o:
            return o[ctx.name]
        return 0


Assign(
    Id("x"), = UnOp("!",BinOp("=",Id("z"),BinOp("*",Id("y"),Id("x"))))
    )