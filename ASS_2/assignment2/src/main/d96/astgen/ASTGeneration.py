from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        classDeclList = self.visit(ctx.class_declares_list())
        # If a method named "main" with no parameter in Program Class, this is entry point of D96
        for classDecl in classDeclList:
            if classDecl.classname.name == 'Program':
                for mem in classDecl.memlist:
                    if isinstance(mem, MethodDecl):
                        if mem.name.name == 'main' and len(mem.param) == 0:
                            mem.kind = Static()
        
        return Program(classDeclList)

    def visitClass_declares_list(self, ctx: D96Parser.Class_declares_listContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.class_declare())
        else:
            singleClass = self.visit(ctx.class_declare())
            multiClass = self.visit(ctx.class_declares_list())
        return singleClass + multiClass

    def visitClass_declare(self, ctx: D96Parser.Class_declareContext):
        classId = Id(ctx.NORMAL_ID().getText())
        memList = self.visit(ctx.class_members())
        parentName = self.visit(ctx.extend())
        return [ClassDecl(classId, memList, parentName)]

    def visitExtend(self, ctx: D96Parser.ExtendContext):
        if ctx.getChildCount() == 0:
            return None
        return Id(ctx.NORMAL_ID().getText())
    def visitClass_members(self, ctx: D96Parser.Class_membersContext):
        return self.visit(ctx.member_list())

    def visitMember_list(self, ctx: D96Parser.Member_listContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.members())

    def visitMembers(self, ctx: D96Parser.MembersContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.member())
        singleMember = self.visit(ctx.member())
        multiMember = self.visit(ctx.members())
        return singleMember + multiMember

    def visitMember(self, ctx: D96Parser.MemberContext):
        if ctx.method_declare():
            return [self.visit(ctx.method_declare())]

        if ctx.constructor_method():
            return [self.visit(ctx.constructor_method())]

        if ctx.destructor_method():
            return [self.visit(ctx.destructor_method())]

        if ctx.attribute_declare():
            return self.visit(ctx.attribute_declare())

    def visitConstructor_method(self, ctx: D96Parser.Constructor_methodContext):
        methodName = Id(ctx.CONSTRUCTOR().getText())
        paramList = self.visit(ctx.param_list())
        blockStmt = self.visit(ctx.block_statements())
        return MethodDecl(Instance(), methodName, paramList, blockStmt)

    def visitDestructor_method(self, ctx: D96Parser.Destructor_methodContext):
        methodName = Id(ctx.DESTRUCTOR().getText())
        blockStmt = self.visit(ctx.block_statements())
        return MethodDecl(Instance(), methodName, [], blockStmt)

    def visitMethod_declare(self, ctx: D96Parser.Method_declareContext):
        if ctx.NORMAL_ID():
            methodName = ctx.NORMAL_ID().getText()
            kind = Instance()
        if ctx.DOLLAR_ID():
            methodName = ctx.DOLLAR_ID().getText()
            kind = Static()
        
        paramList = self.visit(ctx.param_list())
        blockStmt = self.visit(ctx.block_statements())

        return MethodDecl(kind, Id(methodName), paramList, blockStmt)

    def visitParam_list(self, ctx: D96Parser.Param_listContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.parameters())


    def visitParameters(self, ctx: D96Parser.ParametersContext):
        if ctx.SEMI():
            param = self.visit(ctx.parameter())
            params = self.visit(ctx.parameters())
            return param + params
        return self.visit(ctx.parameter())

    def visitParameter(self, ctx: D96Parser.ParameterContext):
        idList = self.visit(ctx.normal_id_list())
        typ = ''
        if ctx.BOOLEAN():
            typ = BoolType()
        elif ctx.INT_TYPE():
            typ = IntType()
        elif ctx.FLOAT_TYPE():
            typ = FloatType()
        elif ctx.STRING():
            typ = StringType()
        elif ctx.NORMAL_ID():
            typ = ClassType(Id(ctx.NORMAL_ID().getText()))
        elif ctx.array_type():
            typ = self.visit(ctx.array_type())

        return [VarDecl(elementId, typ) for elementId in idList]
    def visitBlock_statements(self, ctx: D96Parser.Block_statementsContext):
        return Block(self.visit(ctx.statements_list()))

    def visitStatements_list(self, ctx: D96Parser.Statements_listContext):
        if ctx.getChildCount() == 0:
            return []
        # print(self.visit(ctx.statements()))
        return self.visit(ctx.statements())
        
    def visitStatements(self, ctx: D96Parser.StatementsContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.statement())

        singleStmt = self.visit(ctx.statement())
        multiStmt = self.visit(ctx.statements())
        return singleStmt + multiStmt

    def visitStatement(self, ctx: D96Parser.StatementContext):
        if ctx.assign_statement():
            return [self.visit(ctx.assign_statement())]
        if ctx.var_declare():
            return self.visit(ctx.var_declare())
        if ctx.break_statement():
            return [self.visit(ctx.break_statement())]
        if ctx.continue_statement():
            return [self.visit(ctx.continue_statement())]
        if ctx.return_statement():
            return [self.visit(ctx.return_statement())]
        if ctx.static_method_call():
            return [self.visit(ctx.static_method_call())]
        if ctx.instance_method_call():
            return [self.visit(ctx.instance_method_call())]
        if ctx.if_else_statement():
            return [self.visit(ctx.if_else_statement())]
        if ctx.foreach_statement():
            return [self.visit(ctx.foreach_statement())]

    def visitBreak_statement(self, ctx: D96Parser.Break_statementContext):
        return Break()

    def visitContinue_statement(self, ctx: D96Parser.Continue_statementContext):
        return Continue()

    def visitReturn_statement(self, ctx: D96Parser.Return_statementContext):
        return Return(self.visit(ctx.exp_value()))

    def visitExp_value(self, ctx: D96Parser.Exp_valueContext):
        return self.visit(ctx.exp()) if ctx.exp() else None

    def visitAssign_statement(self, ctx: D96Parser.Assign_statementContext):
        lhs = self.visit(ctx.lhs())
        myExp = self.visit(ctx.exp())
        return Assign(lhs, myExp)

    def visitIf_else_statement(self, ctx: D96Parser.If_else_statementContext):
        myExp = self.visit(ctx.exp())
        blockStmt = self.visit(ctx.block_statements())
        if ctx.elseif_stmt_list():
            # This statement will return a list of "elseif statements"
            elseIfStmtList = self.visit(ctx.elseif_stmt_list())
        if ctx.else_stmt():
            # This statement will return block of statements in "else"
            elseStmt = self.visit(ctx.else_stmt())
        
        if len(elseIfStmtList) == 0:
            return If(myExp, blockStmt, elseStmt) if elseStmt else If(myExp, blockStmt)
        else:
            listLen = len(elseIfStmtList)
            elseIfExp = elseIfStmtList[listLen - 1][0]
            elseIfBlock = elseIfStmtList[listLen - 1][1]
            lastElseIf = If(elseIfExp, elseIfBlock, elseStmt) if elseStmt else If(elseIfExp, elseIfBlock)

            for idx in range(listLen - 1):
                lastElseIf = If(elseIfStmtList[listLen - idx - 2][0], elseIfStmtList[listLen - idx - 2][1], lastElseIf)

            return If(myExp, blockStmt, lastElseIf)  
            


    def visitElseif_stmt_list(self, ctx:  D96Parser.Elseif_stmt_listContext):
        return self.visit(ctx.elseif_stmts()) if ctx.elseif_stmts() else []

    def visitElseif_stmts(self, ctx: D96Parser.Elseif_stmtsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.elseif_stmt())]
        elseifStmt = [self.visit(ctx.elseif_stmt())]
        elseifStmts = self.visit(ctx.elseif_stmts())
        return elseifStmt + elseifStmts
        
    def visitElseif_stmt(self, ctx: D96Parser.Elseif_stmtContext):
        myExp = self.visit(ctx.exp())
        blockStmt = self.visit(ctx.block_statements())
        return (myExp, blockStmt)


    def visitElse_stmt(self, ctx: D96Parser.Else_stmtContext):
        return None if ctx.getChildCount() == 0 else self.visit(ctx.block_statements())

    # TODO: visit foreach statement
    def visitForeach_statement(self, ctx: D96Parser.Foreach_statementContext):
        if ctx.NORMAL_ID():
            myId = Id(ctx.NORMAL_ID().getText())
        
        if ctx.static_attr_call():
            myId = self.visit(ctx.static_attr_call()).fieldname
        if ctx.instance_attr_call():
            myId = self.visit(ctx.instance_attr_call()).fieldname

        exp1 = self.visit(ctx.exp(0))
        exp2 = self.visit(ctx.exp(1))
        exp3 = self.visit(ctx.increment())
        blockStmt = self.visit(ctx.block_statements())
        return For(myId, exp1, exp2, blockStmt, exp3)

    def visitIncrement(self, ctx: D96Parser.IncrementContext):
        if ctx.getChildCount() == 0:
            return None
        return self.visit(ctx.exp())
    def visitLhs(self, ctx: D96Parser.LhsContext):
        if ctx.NORMAL_ID():
            return Id(ctx.NORMAL_ID().getText())
        if ctx.exp6():
            return self.visit(ctx.exp6())
        if ctx.static_attr_call():
            return self.visit(ctx.static_attr_call())
        if ctx.instance_attr_call():
            return self.visit(ctx.instance_attr_call())


    def visitStatic_attr_call(self, ctx: D96Parser.Static_attr_callContext):
        myId = Id(ctx.NORMAL_ID().getText())
        myAttribute = Id(ctx.DOLLAR_ID().getText())
        return FieldAccess(myId, myAttribute)

    def visitStatic_method_call(self, ctx: D96Parser.Static_method_callContext):
        obj = Id(ctx.NORMAL_ID().getText())
        method = Id(ctx.DOLLAR_ID().getText())
        listExp = self.visit(ctx.list_exp())
        return CallStmt(obj, method, listExp)

    def visitInstance_attr_call(self, ctx: D96Parser.Instance_attr_callContext):
        myExp = self.visit(ctx.exp7())
        myAttribute = Id(ctx.NORMAL_ID().getText())
        return FieldAccess(myExp, myAttribute)
    def visitInstance_method_call(self, ctx: D96Parser.Instance_method_callContext):
        obj = self.visit(ctx.exp7())
        method = Id(ctx.NORMAL_ID().getText())
        listExp = self.visit(ctx.list_exp())
        return CallStmt(obj, method, listExp)

    def visitAttribute_declare(self, ctx: D96Parser.Attribute_declareContext):
        components = self.visit(ctx.dec_and_init_list1())
        typ = components[1][0]
        declList = components[1][1]

        if components[0] == 'no init':
            if ctx.VAR():
                varDeclList = [VarDecl(decl, typ) for decl in declList]
                varOrConstDecl = varDeclList
            if ctx.VAL():
                constDeclList = [ConstDecl(decl, typ) for decl in declList]
                varOrConstDecl = constDeclList
        
        elif components[0] == 'init':
            if ctx.VAR():
                varDeclList = [VarDecl(declList[idx], typ, declList[idx + int(len(declList) / 2)]) for idx in range(int(len(declList) / 2))]
                varOrConstDecl = varDeclList
            if ctx.VAL():
                constDeclList = [ConstDecl(declList[idx], typ, declList[idx + int(len(declList) / 2)]) for idx in range(int(len(declList) / 2))]
                varOrConstDecl = constDeclList
        
        attrDeclList = []
        for decl in varOrConstDecl:
            if isinstance(decl, VarDecl):
                tmp = AttributeDecl(Static(), decl) if decl.variable.name.startswith('$') else AttributeDecl(Instance(), decl)
            if isinstance(decl, ConstDecl):
                tmp = AttributeDecl(Static(), decl) if decl.constant.name.startswith('$') else AttributeDecl(Instance(), decl)
            attrDeclList.append(tmp)        

        return attrDeclList


    def visitDec_and_init_list1(self, ctx: D96Parser.Dec_and_init_list1Context):
        if ctx.COLON():
            if ctx.BOOLEAN():
                typ = BoolType()
            elif ctx.INT_TYPE():
                typ = IntType()
            elif ctx.FLOAT_TYPE():
                typ = FloatType()
            elif ctx.STRING():
                typ = StringType()
            elif ctx.NORMAL_ID():
                typ = ClassType(Id(ctx.NORMAL_ID().getText()))
            elif ctx.array_type():
                typ = self.visit(ctx.array_type())

            if ctx.id_list():
                listId = self.visit(ctx.id_list())
            if ctx.normal_id_list():
                listId = self.visit(ctx.normal_id_list())
            return ('no init', [typ, listId])
        else:
            if ctx.NORMAL_ID():
                firstId = Id(ctx.NORMAL_ID().getText())
            if ctx.DOLLAR_ID():
                firstId = Id(ctx.DOLLAR_ID().getText())
            lastExp = self.visit(ctx.exp())
            pair1 = self.visit(ctx.pair1())
            if len(pair1) == 1:
                return ('init', [pair1[0], [firstId, lastExp]])
            else:
                typ = pair1[int(len(pair1) / 2)]
                newPair = pair1[:int(len(pair1) / 2)] + pair1[int(len(pair1) / 2) + 1:]
                # [Id, Id, Id, Id, Exp, Exp, Exp, Exp]
                declList = [firstId] + newPair + [lastExp]
                    
            # return [VarDecl(declList[idx], typ, declList[idx + int(len(declList) / 2)]) for idx in range(int(len(declList) / 2))]
                return ('init', [typ, declList])

    def visitPair1(self, ctx: D96Parser.Pair1Context):
        if ctx.COLON():
            if ctx.BOOLEAN():
                typ = BoolType()
            elif ctx.INT_TYPE():
                typ = IntType()
            elif ctx.FLOAT_TYPE():
                typ = FloatType()
            elif ctx.STRING():
                typ = StringType()
            elif ctx.NORMAL_ID():
                typ = ClassType(Id(ctx.NORMAL_ID().getText()))
            elif ctx.array_type():
                typ = self.visit(ctx.array_type())
            return [typ]

        if ctx.NORMAL_ID():
            myId = Id(ctx.NORMAL_ID().getText())
        if ctx.DOLLAR_ID():
            myId = Id(ctx.DOLLAR_ID().getText())

        pair1 = self.visit(ctx.pair1())
        myExp = self.visit(ctx.exp())
        return [myId] + pair1 + [myExp]
    
    
    def visitVar_declare(self, ctx: D96Parser.Var_declareContext):
        components = self.visit(ctx.dec_and_init_list2())
        typ = components[1][0]
        declList = components[1][1]

        if components[0] == 'no init':
            if ctx.VAR():
                varDeclList = [VarDecl(decl, typ) for decl in declList]
                varOrConstDecl = varDeclList
            if ctx.VAL():
                constDeclList = [ConstDecl(decl, typ) for decl in declList]
                varOrConstDecl = constDeclList
        
        elif components[0] == 'init':
            if ctx.VAR():
                varDeclList = [VarDecl(declList[idx], typ, declList[idx + int(len(declList) / 2)]) for idx in range(int(len(declList) / 2))]
                varOrConstDecl = varDeclList
            if ctx.VAL():
                constDeclList = [ConstDecl(declList[idx], typ, declList[idx + int(len(declList) / 2)]) for idx in range(int(len(declList) / 2))]
                varOrConstDecl = constDeclList
    
        return varOrConstDecl

    def visitDec_and_init_list2(self, ctx: D96Parser.Dec_and_init_list2Context):
        if ctx.COLON():
            if ctx.BOOLEAN():
                typ = BoolType()
            elif ctx.INT_TYPE():
                typ = IntType()
            elif ctx.FLOAT_TYPE():
                typ = FloatType()
            elif ctx.STRING():
                typ = StringType()
            elif ctx.NORMAL_ID():
                typ = ClassType(Id(ctx.NORMAL_ID().getText()))
            elif ctx.array_type():
                typ = self.visit(ctx.array_type())

            if ctx.normal_id_list():
                listId = self.visit(ctx.normal_id_list())
            return ('no init', [typ, listId])
        else:
            if ctx.NORMAL_ID():
                firstId = Id(ctx.NORMAL_ID().getText())
            lastExp = self.visit(ctx.exp())
            pair2 = self.visit(ctx.pair2())
            if len(pair2) == 1:
                return ('init', [pair2[0], [firstId, lastExp]])
            else:
                typ = pair2[int(len(pair2) / 2)]
                newPair = pair2[:int(len(pair2) / 2)] + pair2[int(len(pair2) / 2) + 1:]
                # [Id, Id, Id, Id, Exp, Exp, Exp, Exp]
                declList = [firstId] + newPair + [lastExp]

            return ('init', [typ, declList])

    def visitPair2(self, ctx: D96Parser.Pair2Context):
        if ctx.COLON():
            if ctx.BOOLEAN():
                typ = BoolType()
            elif ctx.INT_TYPE():
                typ = IntType()
            elif ctx.FLOAT_TYPE():
                typ = FloatType()
            elif ctx.STRING():
                typ = StringType()
            elif ctx.NORMAL_ID():
                typ = ClassType(Id(ctx.NORMAL_ID().getText()))
            elif ctx.array_type():
                typ = self.visit(ctx.array_type())
            return [typ]

        if ctx.NORMAL_ID():
            myId = Id(ctx.NORMAL_ID().getText())

        pair2 = self.visit(ctx.pair2())
        myExp = self.visit(ctx.exp())
        return [myId] + pair2 + [myExp]

    def visitArray_type(self, ctx: D96Parser.Array_typeContext):
        sizeStr = ctx.ARRAY_SIZE().getText()
        if sizeStr.startswith('0b') or sizeStr.startswith('0B'):
            size = int(sizeStr, 2)
        elif sizeStr.startswith('0x') or sizeStr.startswith('0X'):
            size = int(sizeStr, 16)
        elif sizeStr.startswith('0') and len(sizeStr) > 1:
            size = int(sizeStr, 8)
        else:
            size = int(sizeStr, 10)

        if ctx.BOOLEAN():
            typ = BoolType()

        elif ctx.INT_TYPE():
            typ = IntType()

        elif ctx.FLOAT_TYPE():
            typ = FloatType()

        elif ctx.array_type():
            typ = self.visit(ctx.array_type())

        elif ctx.STRING():
            typ = StringType()
        return ArrayType(size, typ)
    def visitArray_literal(self, ctx: D96Parser.Array_literalContext):
        return ArrayLiteral(self.visit(ctx.list_exp()))


    # def visitLiteral_list(self, ctx: D96Parser.Literal_listContext):
    #     if ctx.getChildCount() == 0:
    #         return []
    #     return self.visit(ctx.literals())
        

    # def visitLiterals(self, ctx: D96Parser.LiteralsContext):
    #     if ctx.COMMA():
    #         myExp = self.visit(ctx.exp())
    #         myLiterals = self.visit(ctx.literals())
    #         return [myExp] + myLiterals
    #     else:
    #         return [self.visit(ctx.exp())]

    def visitExp(self, ctx: D96Parser.ExpContext):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.exp0(0))
            right = self.visit(ctx.exp0(1))
            if ctx.EQUAL_STR():
                return BinaryOp(ctx.EQUAL_STR().getText(), left, right)
            elif ctx.ADD_STR():
                return BinaryOp(ctx.ADD_STR().getText(), left, right)
        return self.visit(ctx.exp0(0))


    def visitExp0(self, ctx: D96Parser.Exp0Context):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.exp1(0))
            right = self.visit(ctx.exp1(1))
            if ctx.LT():
                return BinaryOp(ctx.LT().getText(), left, right)

            elif ctx.LTE():
                return BinaryOp(ctx.LTE().getText(), left, right)

            elif ctx.GT():
                return BinaryOp(ctx.GT().getText(), left, right)

            elif ctx.GTE():
                return BinaryOp(ctx.GTE().getText(), left, right)

            elif ctx.EQUAL():
                return BinaryOp(ctx.EQUAL().getText(), left, right)

            elif ctx.NOTEQUAL():
                return BinaryOp(ctx.NOTEQUAL().getText(), left, right)
        return self.visit(ctx.exp1(0))

    def visitExp1(self, ctx: D96Parser.Exp1Context):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.exp1())
            right = self.visit(ctx.exp2())
            if ctx.AND():
                return BinaryOp(ctx.AND().getText(), left, right)

            elif ctx.OR():
                return BinaryOp(ctx.OR().getText(), left, right)

        return self.visit(ctx.exp2())

    def visitExp2(self, ctx: D96Parser.Exp2Context):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.exp2())
            right = self.visit(ctx.exp3())
            if ctx.ADD():
                return BinaryOp(ctx.ADD().getText(), left, right)

            elif ctx.SUB():
                return BinaryOp(ctx.SUB().getText(), left, right)

        return self.visit(ctx.exp3())

    def visitExp3(self, ctx: D96Parser.Exp3Context):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.exp3())
            right = self.visit(ctx.exp4())
            if ctx.MUL():
                return BinaryOp(ctx.MUL().getText(), left, right)

            elif ctx.DIV():
                return BinaryOp(ctx.DIV().getText(), left, right)

            elif ctx.MOD():
                return BinaryOp(ctx.MOD().getText(), left, right)

        return self.visit(ctx.exp4())

    def visitExp4(self, ctx: D96Parser.Exp4Context):
        if ctx.NOT():
            operand = self.visit(ctx.exp4())
            return UnaryOp(ctx.NOT().getText(), operand)

        return self.visit(ctx.exp5())

    def visitExp5(self, ctx: D96Parser.Exp5Context):
        if ctx.SUB():
            operand = self.visit(ctx.exp5())
            return UnaryOp(ctx.SUB().getText(), operand)
        return self.visit(ctx.exp6())

    def visitExp6(self, ctx: D96Parser.Exp6Context):
        if ctx.exp6():
            myExp = self.visit(ctx.exp6())
            idx = self.visit(ctx.index_operators())
            return ArrayCell(myExp, idx)
        
        return self.visit(ctx.exp7())
    def visitIndex_operators(self, ctx: D96Parser.Index_operatorsContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.exp())]
        nextIdxExp = self.visit(ctx.index_operators())
        idxExp = self.visit(ctx.exp())
        return nextIdxExp + [idxExp]

    def visitExp7(self, ctx: D96Parser.Exp7Context):
        if ctx.LP() and ctx.RP():
            myExp = self.visit(ctx.exp7())
            listExp = self.visit(ctx.list_exp())
            return CallExpr(myExp, Id(ctx.NORMAL_ID().getText()), listExp)

        elif ctx.NORMAL_ID():
            myExp = self.visit(ctx.exp7())
            return FieldAccess(myExp, Id(ctx.NORMAL_ID().getText()))

        else:
            return self.visit(ctx.exp8())


    def visitExp8(self, ctx: D96Parser.Exp8Context):
        if ctx.NORMAL_ID():
            className = Id(ctx.NORMAL_ID().getText())
            staticField = Id(ctx.DOLLAR_ID().getText())
            if ctx.LP() and ctx.RP():
                listExp = self.visit(ctx.list_exp())
                return CallExpr(className, staticField, listExp)
            else:
                return FieldAccess(className, staticField)
        else:
            return self.visit(ctx.exp9())

    def visitExp9(self, ctx: D96Parser.Exp9Context):
        if ctx.NORMAL_ID():
            myId = Id(ctx.NORMAL_ID().getText())
            listExp = self.visit(ctx.list_exp())
            return NewExpr(myId, listExp)
        return self.visit(ctx.exp10())

    def visitExp10(self, ctx: D96Parser.Exp10Context):
        if ctx.ARRAY_SIZE() or ctx.INTEGER_LITERAL():
            number = ctx.ARRAY_SIZE().getText() if ctx.ARRAY_SIZE() else ctx.INTEGER_LITERAL().getText()
            if number.startswith('0x') or number.startswith('0X'):
                return IntLiteral(int(number, 16))

            if number.startswith('0b') or number.startswith('0B'):
                return IntLiteral(int(number, 2))

            if number.startswith('0') and len(number) > 1:
                return IntLiteral(int(number, 8))
            
            return IntLiteral(int(number, 10))

        if ctx.BOOL_LITERAL():
            return BooleanLiteral(ctx.BOOL_LITERAL().getText() == 'True')

        if ctx.REAL_LITERAL():
            floatNum = ctx.REAL_LITERAL().getText()
            if floatNum.endswith('.'):
                return FloatLiteral(float(floatNum + '0'))
            elif floatNum.startswith('.'):
                return FloatLiteral(float('0' + floatNum))
            return FloatLiteral(float(floatNum))
            
        if ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())

        if ctx.NORMAL_ID():
            return Id(ctx.NORMAL_ID().getText())

        if ctx.SELF():
            return SelfLiteral()

        if ctx.NULL():
            return NullLiteral()
        
        if ctx.array_literal():
            return self.visit(ctx.array_literal())
        
        if ctx.exp11():
            return self.visit(ctx.exp11())
        

    def visitExp11(self, ctx: D96Parser.Exp11Context):
        return self.visit(ctx.exp())

    def visitList_exp(self, ctx: D96Parser.List_expContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.exps())

    def visitExps(self, ctx: D96Parser.ExpsContext):
        if ctx.COMMA():
            singleExp = [self.visit(ctx.exp())]
            nextExps = self.visit(ctx.exps())
            return singleExp + nextExps
        else:
            return [self.visit(ctx.exp())]

    def visitNormal_id_list(self, ctx: D96Parser.Normal_id_listContext):
        if ctx.COMMA():
            nextIds = self.visit(ctx.normal_id_list())
            return [Id(ctx.NORMAL_ID().getText())] + nextIds
        return [Id(ctx.NORMAL_ID().getText())]

    def visitId_list(self, ctx: D96Parser.Id_listContext):
        if ctx.COMMA():
            nextIds = self.visit(ctx.id_list())
            if ctx.NORMAL_ID():
                return [Id(ctx.NORMAL_ID().getText())] + nextIds
            if ctx.DOLLAR_ID():
                return [Id(ctx.DOLLAR_ID().getText())] + nextIds

        elif ctx.NORMAL_ID():
            return [Id(ctx.NORMAL_ID().getText())]

        elif ctx.DOLLAR_ID():
            return [Id(ctx.DOLLAR_ID().getText())]

    