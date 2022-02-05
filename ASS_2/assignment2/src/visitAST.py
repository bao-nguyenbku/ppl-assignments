from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return None

    def visitClass_declares_list(self, ctx: D96Parser.Class_declares_listContext):
        return None

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
        return None

    def visitParam_list(self, ctx: D96Parser.Param_listContext):
        return None

    def visitParameters(self, ctx: D96Parser.ParametersContext):
        return None

    def visitParameter(self, ctx: D96Parser.ParameterContext):
        return None

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

    def visitAttribute_declare(self, ctx: D96Parser.Attribute_declareContext):
        return None

    def visitDec_and_init_list1(self, ctx: D96Parser.Dec_and_init_list1Context):
        return None

    def visitPair1(self, ctx: D96Parser.Pair1Context):
        return None

    def visitVar_declare(self, ctx: D96Parser.Var_declareContext):
        return None

    def visitDec_and_init_list2(self, ctx: D96Parser.Dec_and_init_list2Context):
        return None

    def visitPair2(self, ctx: D96Parser.Pair2Context):
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
        return None

    def visitExp0(self, ctx: D96Parser.Exp0Context):
        return None

    def visitExp1(self, ctx: D96Parser.Exp1Context):
        return None

    def visitExp2(self, ctx: D96Parser.Exp2Context):
        return None

    def visitExp3(self, ctx: D96Parser.Exp3Context):
        return None

    def visitExp4(self, ctx: D96Parser.Exp4Context):
        return None

    def visitExp5(self, ctx: D96Parser.Exp5Context):
        return None

    def visitExp6(self, ctx: D96Parser.Exp6Context):
        return None

    def visitExp7(self, ctx: D96Parser.Exp7Context):
        return None

    def visitExp8(self, ctx: D96Parser.Exp8Context):
        return None

    def visitExp9(self, ctx: D96Parser.Exp9Context):
        return None

    def visitExp10(self, ctx: D96Parser.Exp10Context):
        return None

    def visitExp11(self, ctx: D96Parser.Exp11Context):
        return None

    def visitList_exp(self, ctx: D96Parser.List_expContext):
        return None

    def visitExps(self, ctx: D96Parser.ExpsContext):
        return None

    def visitNormal_id_list(self, ctx: D96Parser.Normal_id_listContext):
        return None

    def visitId_list(self, ctx: D96Parser.Id_listContext):
        return None

    