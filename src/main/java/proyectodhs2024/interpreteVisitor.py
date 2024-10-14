# Generated from /home/joaquin/DHS/proyectodhs2024/src/main/java/proyectodhs2024/interprete.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .interpreteParser import interpreteParser
else:
    from interpreteParser import interpreteParser

# This class defines a complete generic visitor for a parse tree produced by interpreteParser.

class interpreteVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by interpreteParser#s.
    def visitS(self, ctx:interpreteParser.SContext):
        return self.visitChildren(ctx)



del interpreteParser