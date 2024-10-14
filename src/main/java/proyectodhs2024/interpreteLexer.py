# Generated from /home/joaquin/DHS/proyectodhs2024/src/main/java/proyectodhs2024/interprete.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,2,9,6,-1,2,0,7,0,2,1,7,1,1,0,1,0,1,1,1,1,0,0,2,1,1,3,2,1,0,2,
        2,0,65,90,97,122,1,0,48,57,8,0,1,1,0,0,0,0,3,1,0,0,0,1,5,1,0,0,0,
        3,7,1,0,0,0,5,6,7,0,0,0,6,2,1,0,0,0,7,8,7,1,0,0,8,4,1,0,0,0,1,0,
        0
    ]

class interpreteLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LETRA = 1
    DIGITO = 2

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "LETRA", "DIGITO" ]

    ruleNames = [ "LETRA", "DIGITO" ]

    grammarFileName = "interprete.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


