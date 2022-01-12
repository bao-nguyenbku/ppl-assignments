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


    # Visit a parse tree produced by D96Parser#mptype.
    def visitMptype(self, ctx:D96Parser.MptypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#body.
    def visitBody(self, ctx:D96Parser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp.
    def visitExp(self, ctx:D96Parser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#funcall.
    def visitFuncall(self, ctx:D96Parser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_declare.
    def visitClass_declare(self, ctx:D96Parser.Class_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member.
    def visitMember(self, ctx:D96Parser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_declare.
    def visitVar_declare(self, ctx:D96Parser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_list.
    def visitArray_list(self, ctx:D96Parser.Array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx:D96Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitive_type.
    def visitPrimitive_type(self, ctx:D96Parser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp0.
    def visitExp0(self, ctx:D96Parser.Exp0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp1.
    def visitExp1(self, ctx:D96Parser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp4.
    def visitExp4(self, ctx:D96Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_exp.
    def visitList_exp(self, ctx:D96Parser.List_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#id_list.
    def visitId_list(self, ctx:D96Parser.Id_listContext):
        return self.visitChildren(ctx)



del D96Parser