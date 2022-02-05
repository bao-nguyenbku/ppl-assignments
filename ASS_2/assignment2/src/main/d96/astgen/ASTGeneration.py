from ast import LtE, expr
from ctypes.wintypes import FLOAT
from logging import StringTemplateStyle
from tkinter.font import NORMAL
from turtle import right
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return None

    def visitClass_declares_list(self, ctx: D96Parser.Class_declares_listContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.class_declare())
        else:
            singleClass = self.visit(ctx.class_declare())
            multiClass = self.visit(ctx.class_declares_list())


    def visitClass_declare(self, ctx: D96Parser.Class_declareContext):
        return None

    def visitExtend(self, ctx: D96Parser.ExtendContext):
        return None

    def visitClass_members(self, ctx: D96Parser.Class_membersContext):
        return None

    def visitMember_list(self, ctx: D96Parser.Member_listContext):
        return None

    def visitMembers(self, ctx: D96Parser.MembersContext):
        return None

    def visitMember(self, ctx: D96Parser.MemberContext):
        return None

    def visitConstructor_method(self, ctx: D96Parser.Constructor_methodContext):
        return None

    def visitDestructor_method(self, ctx: D96Parser.Destructor_methodContext):
        return None

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
        return None

    def visitStatements_list(self, ctx: D96Parser.Statements_listContext):
        return None

    def visitStatements(self, ctx: D96Parser.StatementsContext):
        return None

    def visitStatement(self, ctx: D96Parser.StatementContext):
        return None

    def visitBreak_statement(self, ctx: D96Parser.Break_statementContext):
        return None

    def visitContinue_statement(self, ctx: D96Parser.Continue_statementContext):
        return None

    def visitReturn_statement(self, ctx: D96Parser.Return_statementContext):
        return None

    def visitExp_value(self, ctx: D96Parser.Exp_valueContext):
        return None

    def visitAssign_statement(self, ctx: D96Parser.Assign_statementContext):
        return None

    def visitIf_else_statement(self, ctx: D96Parser.If_else_statementContext):
        return None

    def visitElseif_stmt_list(self, ctx: D96Parser.Elseif_stmt_listContext):
        return None

    def visitElseif_stmts(self, ctx: D96Parser.Elseif_stmtsContext):
        return None

    def visitElseif_stmt(self, ctx: D96Parser.Elseif_stmtContext):
        return None

    def visitElse_stmt(self, ctx: D96Parser.Else_stmtContext):
        return None

    def visitForeach_statement(self, ctx: D96Parser.Foreach_statementContext):
        return None

    def visitIncrement(self, ctx: D96Parser.IncrementContext):
        return None

    def visitLhs(self, ctx: D96Parser.LhsContext):
        return None

    def visitStatic_attr_call(self, ctx: D96Parser.Static_attr_callContext):
        return None

    def visitStatic_method_call(self, ctx: D96Parser.Static_method_callContext):
        return None

    def visitInstance_attr_call(self, ctx: D96Parser.Instance_attr_callContext):
        return None

    def visitInstance_method_call(self, ctx: D96Parser.Instance_method_callContext):
        return None

    def visitVar_attribute_declare(self, ctx: D96Parser.Var_attribute_declareContext):
        return self.visit(ctx.dec_and_init_list1())

    def visitDec_and_init_list1(self, ctx: D96Parser.Dec_and_init_list1Context):
        if ctx.COLON():
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

            if ctx.id_list():
                listId = self.visit(ctx.id_list())
            return [VarDecl(elementId, typ) for elementId in listId]
        else:
            if ctx.NORMAL_ID():
                firstId = Id(ctx.NORMAL_ID().getText())
            if ctx.DOLLAR_ID():
                firstId = Id(ctx.DOLLAR_ID().getText())

    def visitPair1(self, ctx: D96Parser.Pair1Context):
        return None

    def visitConst_attribute_declare(self, ctx: D96Parser.Const_attribute_declareContext):
        return None

    def visitDec_and_init_list2(self, ctx: D96Parser.Dec_and_init_list2Context):
        return None

    def visitPair2(self, ctx: D96Parser.Pair2Context):
        return None

    def visitVar_declare(self, ctx: D96Parser.Var_declareContext):
        return None

    def visitDec_and_init_list3(self, ctx: D96Parser.Dec_and_init_list3Context):
        return None

    def visitPair3(self, ctx: D96Parser.Pair3Context):
        return None

    def visitConst_declare(self, ctx: D96Parser.Const_declareContext):
        return None

    def visitDec_and_init_list4(self, ctx: D96Parser.Dec_and_init_list4Context):
        return None

    def visitPair4(self, ctx: D96Parser.Pair4Context):
        return None

    def visitArray_type(self, ctx: D96Parser.Array_typeContext):
        return None

    def visitArray_literal(self, ctx: D96Parser.Array_literalContext):
        return None

    def visitLiteral_list(self, ctx: D96Parser.Literal_listContext):
        return None

    def visitLiterals(self, ctx: D96Parser.LiteralsContext):
        return None

    def visitExp(self, ctx: D96Parser.ExpContext):
        if ctx.getChildCount() == 2:
            left = self.visit(ctx.exp0(0))
            right = self.visit(ctx.exp0(1))
            if ctx.EQUAL_STR():
                return BinaryOp(ctx.EQUAL_STR().getText(), left, right)
            elif ctx.ADD_STR():
                return BinaryOp(ctx.ADD_STR().getText(), left, right)
        return self.visit(ctx.exp0())


    def visitExp0(self, ctx: D96Parser.Exp0Context):
        if ctx.getChildCount() == 2:
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
        return self.visit(ctx.exp1())

    def visitExp1(self, ctx: D96Parser.Exp1Context):
        if ctx.getChildCount() == 2:
            left = self.visit(ctx.exp1())
            right = self.visit(ctx.exp2())
            if ctx.AND():
                return BinaryOp(ctx.AND().getText(), left, right)

            elif ctx.OR():
                return BinaryOp(ctx.OR().getText(), left, right)

        return self.visit(ctx.exp2())

    def visitExp2(self, ctx: D96Parser.Exp2Context):
        if ctx.getChildCount() == 2:
            left = self.visit(ctx.exp2())
            right = self.visit(ctx.exp3())
            if ctx.ADD():
                return BinaryOp(ctx.ADD().getText(), left, right)

            elif ctx.SUB():
                return BinaryOp(ctx.SUB().getText(), left, right)

        return self.visit(ctx.exp3())

    def visitExp3(self, ctx: D96Parser.Exp3Context):
        if ctx.getChildCount() == 2:
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
        return self.visit(ctx.exp7())

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
        return self.visit(ctx.exp9())

    def visitExp9(self, ctx: D96Parser.Exp9Context):
        myId = ctx.NORMAL_ID().getText()
        listExp = self.visit(ctx.list_exp())
        return NewExpr(Id(myId), listExp)
    def visitExp10(self, ctx: D96Parser.Exp10Context):
        if ctx.ARRAY_SIZE():
            return IntLiteral(int(ctx.ARRAY_SIZE().getText()))

        if ctx.INTEGER_LITERAL():
            return IntLiteral(int(ctx.INTEGER_LITERAL().getText()))

        if ctx.BOOL_LITERAL():
            return BooleanLiteral(ctx.BOOL_LITERAL().getText() == 'True')

        if ctx.FLOAT_LITERAL():
            return FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))

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
            nextIds = self.visit(ctx.normal_id_list())
            if ctx.NORMAL_ID():
                return [Id(ctx.NORMAL_ID().getText())] + nextIds
            if ctx.DOLLAR_ID():
                return [Id(ctx.DOLLAR_ID().getText())] + nextIds

        elif ctx.NORMAL_ID():
            return [Id(ctx.NORMAL_ID().getText())]

        elif ctx.DOLLAR_ID():
            return [Id(ctx.DOLLAR_ID().getText())]

    