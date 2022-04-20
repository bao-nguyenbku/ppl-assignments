# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_declares_list.
    def visitClass_declares_list(self, ctx:D96Parser.Class_declares_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_declare.
    def visitClass_declare(self, ctx:D96Parser.Class_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#extend.
    def visitExtend(self, ctx:D96Parser.ExtendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_members.
    def visitClass_members(self, ctx:D96Parser.Class_membersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member_list.
    def visitMember_list(self, ctx:D96Parser.Member_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#members.
    def visitMembers(self, ctx:D96Parser.MembersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member.
    def visitMember(self, ctx:D96Parser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor_method.
    def visitConstructor_method(self, ctx:D96Parser.Constructor_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor_method.
    def visitDestructor_method(self, ctx:D96Parser.Destructor_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_declare.
    def visitMethod_declare(self, ctx:D96Parser.Method_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#param_list.
    def visitParam_list(self, ctx:D96Parser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameters.
    def visitParameters(self, ctx:D96Parser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameter.
    def visitParameter(self, ctx:D96Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_statements.
    def visitBlock_statements(self, ctx:D96Parser.Block_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statements_list.
    def visitStatements_list(self, ctx:D96Parser.Statements_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statements.
    def visitStatements(self, ctx:D96Parser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statement.
    def visitStatement(self, ctx:D96Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_statement.
    def visitBreak_statement(self, ctx:D96Parser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_statement.
    def visitContinue_statement(self, ctx:D96Parser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_statement.
    def visitReturn_statement(self, ctx:D96Parser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_value.
    def visitExp_value(self, ctx:D96Parser.Exp_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_statement.
    def visitAssign_statement(self, ctx:D96Parser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_else_statement.
    def visitIf_else_statement(self, ctx:D96Parser.If_else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseif_stmt_list.
    def visitElseif_stmt_list(self, ctx:D96Parser.Elseif_stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseif_stmts.
    def visitElseif_stmts(self, ctx:D96Parser.Elseif_stmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseif_stmt.
    def visitElseif_stmt(self, ctx:D96Parser.Elseif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_stmt.
    def visitElse_stmt(self, ctx:D96Parser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#foreach_statement.
    def visitForeach_statement(self, ctx:D96Parser.Foreach_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#increment.
    def visitIncrement(self, ctx:D96Parser.IncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lhs.
    def visitLhs(self, ctx:D96Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_attr_call.
    def visitStatic_attr_call(self, ctx:D96Parser.Static_attr_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_method_call.
    def visitStatic_method_call(self, ctx:D96Parser.Static_method_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_attr_call.
    def visitInstance_attr_call(self, ctx:D96Parser.Instance_attr_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_method_call.
    def visitInstance_method_call(self, ctx:D96Parser.Instance_method_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_declare.
    def visitAttribute_declare(self, ctx:D96Parser.Attribute_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#dec_and_init_list1.
    def visitDec_and_init_list1(self, ctx:D96Parser.Dec_and_init_list1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#pair1.
    def visitPair1(self, ctx:D96Parser.Pair1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_declare.
    def visitVar_declare(self, ctx:D96Parser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#dec_and_init_list2.
    def visitDec_and_init_list2(self, ctx:D96Parser.Dec_and_init_list2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#pair2.
    def visitPair2(self, ctx:D96Parser.Pair2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx:D96Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_literal.
    def visitArray_literal(self, ctx:D96Parser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal_list.
    def visitLiteral_list(self, ctx:D96Parser.Literal_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literals.
    def visitLiterals(self, ctx:D96Parser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp.
    def visitExp(self, ctx:D96Parser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp0.
    def visitExp0(self, ctx:D96Parser.Exp0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp1.
    def visitExp1(self, ctx:D96Parser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp2.
    def visitExp2(self, ctx:D96Parser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp3.
    def visitExp3(self, ctx:D96Parser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp4.
    def visitExp4(self, ctx:D96Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp5.
    def visitExp5(self, ctx:D96Parser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp6.
    def visitExp6(self, ctx:D96Parser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp7.
    def visitExp7(self, ctx:D96Parser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp8.
    def visitExp8(self, ctx:D96Parser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp9.
    def visitExp9(self, ctx:D96Parser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp10.
    def visitExp10(self, ctx:D96Parser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp11.
    def visitExp11(self, ctx:D96Parser.Exp11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_exp.
    def visitList_exp(self, ctx:D96Parser.List_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exps.
    def visitExps(self, ctx:D96Parser.ExpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#normal_id_list.
    def visitNormal_id_list(self, ctx:D96Parser.Normal_id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#id_list.
    def visitId_list(self, ctx:D96Parser.Id_listContext):
        return self.visitChildren(ctx)



del D96Parser