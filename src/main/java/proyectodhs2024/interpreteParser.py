# Generated from /home/joaquin/DHS/proyectodhs2024/src/main/java/proyectodhs2024/interprete.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,2,9,2,0,7,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,7,0,2,1,
        0,0,0,2,3,5,2,0,0,3,4,3,0,0,0,4,5,5,1,0,0,5,6,3,0,0,0,6,7,5,0,0,
        1,7,1,1,0,0,0,0
    ]

class interpreteParser ( Parser ):

    grammarFileName = "interprete.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "LETRA", "DIGITO" ]

    RULE_s = 0

    ruleNames =  [ "s" ]

    EOF = Token.EOF
    LETRA=1
    DIGITO=2

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGITO(self):
            return self.getToken(interpreteParser.DIGITO, 0)

        def s(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(interpreteParser.SContext)
            else:
                return self.getTypedRuleContext(interpreteParser.SContext,i)


        def LETRA(self):
            return self.getToken(interpreteParser.LETRA, 0)

        def EOF(self):
            return self.getToken(interpreteParser.EOF, 0)

        def getRuleIndex(self):
            return interpreteParser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS" ):
                return visitor.visitS(self)
            else:
                return visitor.visitChildren(self)




    def s(self):

        localctx = interpreteParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(interpreteParser.DIGITO)
            self.state = 3
            self.s()
            self.state = 4
            self.match(interpreteParser.LETRA)
            self.state = 5
            self.s()
            self.state = 6
            self.match(interpreteParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





