
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftXORleftANDnonassocLESSTHANGREATTHANleftPLUSMINUSleftTIMESDIVIDEnonassocNEWrightPRIVATEPROTECTEDPUBLICABSTRACT AND AND_ASSIGN ARRAYLIST BLOCK_COMMENT BOOLEAN BYTE CHAR COMA CONCA CONCAT DEFAULT DIVIDE DIVIDE_ASSIGN DOSCOMA DOUBLE DOUBLELINKEDLIST EQUAL EQUALS FINAL FLOAT GREATTHAN GREATTHANEQUAL INT INTEGER LCORCHETE LESSTHAN LESSTHANEQUAL LINKEDLIST LIST LLLAVE LONG LPAREN MINUS MINUSMINUS MINUS_ASSIGN MOD MOD_ASSIGN NEQUAL NEW NOT NULL OBJECT OR OR_ASSIGN PLUS PLUSPLUS PLUS_ASSIGN PRIVATE PROTECTED PUBLIC PUNTO PUNTOCOMA QUEUE RCORCHETE RLLAVE RPAREN SHORT STACK STATIC STRING TIMES TIMESTIMES TIMES_ASSIGN XOR XOR_ASSIGNempty :Type : INT\n            | BOOLEAN\n            | STRING\n            | SHORT\n            | FLOAT\n            | LONG\n            | DOUBLE\n            | CHAR\n            | BYTE\n            | OBJECT\n            | arraydeclaration\n            | empty\n            accessmodif : PUBLIC\n                    | PRIVATE\n                    | PROTECTED\n                    | DEFAULT\n                    | emptyfinalstatvar : FINAL\n                | STATIC\n                | FINAL STATIC\n                | emptydeclaration : accessmodif finalstatvar Type STRING endexpression\n            | accessmodif finalstatvar Type assign\n            arraydeclaration : accessmodif finalstatvar LIST GREATTHAN Type LESSTHAN  STRING endexpression\n            | accessmodif finalstatvar ARRAYLIST GREATTHAN Type LESSTHAN STRING endexpression\n            | accessmodif finalstatvar LINKEDLIST GREATTHAN Type LESSTHAN STRING endexpression\n            | accessmodif finalstatvar DOUBLELINKEDLIST GREATTHAN Type LESSTHAN STRING endexpression\n            | accessmodif finalstatvar QUEUE GREATTHAN Type LESSTHAN STRING endexpression\n            | accessmodif finalstatvar STACK GREATTHAN Type LESSTHAN STRING endexpression\n            | accessmodif finalstatvar LIST GREATTHAN Type LESSTHAN  assign\n            | accessmodif finalstatvar ARRAYLIST GREATTHAN Type LESSTHAN assign\n            | accessmodif finalstatvar LINKEDLIST GREATTHAN Type LESSTHAN assign\n            | accessmodif finalstatvar DOUBLELINKEDLIST GREATTHAN Type LESSTHAN assign\n            | accessmodif finalstatvar QUEUE GREATTHAN Type LESSTHAN assign\n            | accessmodif finalstatvar STACK GREATTHAN Type LESSTHAN assign\n            assign : STRING EQUALS expression endexpression\n            | STRING EQUALS expressionarray endexpressionendexpression : PUNTOCOMAexpression : expression PLUS expression\n           | expression MINUS expression\n           | expression TIMES expression\n           | expression DIVIDE expression\n           | expression MOD expression\n           | PLUSPLUS\n           | MINUSMINUS\n           | expression TIMESTIMES expression\n           | TIMES_ASSIGN expression\n           | MINUS_ASSIGN expression\n           | PLUS_ASSIGN expression\n           | DIVIDE_ASSIGN expression\n           | MOD_ASSIGN expression\n           | LPAREN expression RPAREN\n           | INTEGER\n           | emptyexpressionarray : NEW LIST GREATTHAN Type LESSTHAN LPAREN RPAREN\n           | NEW LINKEDLIST GREATTHAN Type LESSTHAN LPAREN RPAREN\n           | NEW DOUBLELINKEDLIST GREATTHAN Type LESSTHAN LPAREN RPAREN\n           | NEW QUEUE GREATTHAN Type LESSTHAN LPAREN RPAREN\n           | NEW STACK GREATTHAN Type LESSTHAN LPAREN RPAREN'
    
_lr_action_items = {'$end':([0,1,],[-1,0,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'empty':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> empty","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','Yacc.py',19),
  ('Type -> INT','Type',1,'p_Type','Yacc.py',23),
  ('Type -> BOOLEAN','Type',1,'p_Type','Yacc.py',24),
  ('Type -> STRING','Type',1,'p_Type','Yacc.py',25),
  ('Type -> SHORT','Type',1,'p_Type','Yacc.py',26),
  ('Type -> FLOAT','Type',1,'p_Type','Yacc.py',27),
  ('Type -> LONG','Type',1,'p_Type','Yacc.py',28),
  ('Type -> DOUBLE','Type',1,'p_Type','Yacc.py',29),
  ('Type -> CHAR','Type',1,'p_Type','Yacc.py',30),
  ('Type -> BYTE','Type',1,'p_Type','Yacc.py',31),
  ('Type -> OBJECT','Type',1,'p_Type','Yacc.py',32),
  ('Type -> arraydeclaration','Type',1,'p_Type','Yacc.py',33),
  ('Type -> empty','Type',1,'p_Type','Yacc.py',34),
  ('accessmodif -> PUBLIC','accessmodif',1,'p_accessmodif','Yacc.py',39),
  ('accessmodif -> PRIVATE','accessmodif',1,'p_accessmodif','Yacc.py',40),
  ('accessmodif -> PROTECTED','accessmodif',1,'p_accessmodif','Yacc.py',41),
  ('accessmodif -> DEFAULT','accessmodif',1,'p_accessmodif','Yacc.py',42),
  ('accessmodif -> empty','accessmodif',1,'p_accessmodif','Yacc.py',43),
  ('finalstatvar -> FINAL','finalstatvar',1,'p_finalstatvar','Yacc.py',47),
  ('finalstatvar -> STATIC','finalstatvar',1,'p_finalstatvar','Yacc.py',48),
  ('finalstatvar -> FINAL STATIC','finalstatvar',2,'p_finalstatvar','Yacc.py',49),
  ('finalstatvar -> empty','finalstatvar',1,'p_finalstatvar','Yacc.py',50),
  ('declaration -> accessmodif finalstatvar Type STRING endexpression','declaration',5,'p_declaration','Yacc.py',54),
  ('declaration -> accessmodif finalstatvar Type assign','declaration',4,'p_declaration','Yacc.py',55),
  ('arraydeclaration -> accessmodif finalstatvar LIST GREATTHAN Type LESSTHAN STRING endexpression','arraydeclaration',8,'p_arraydeclaration','Yacc.py',60),
  ('arraydeclaration -> accessmodif finalstatvar ARRAYLIST GREATTHAN Type LESSTHAN STRING endexpression','arraydeclaration',8,'p_arraydeclaration','Yacc.py',61),
  ('arraydeclaration -> accessmodif finalstatvar LINKEDLIST GREATTHAN Type LESSTHAN STRING endexpression','arraydeclaration',8,'p_arraydeclaration','Yacc.py',62),
  ('arraydeclaration -> accessmodif finalstatvar DOUBLELINKEDLIST GREATTHAN Type LESSTHAN STRING endexpression','arraydeclaration',8,'p_arraydeclaration','Yacc.py',63),
  ('arraydeclaration -> accessmodif finalstatvar QUEUE GREATTHAN Type LESSTHAN STRING endexpression','arraydeclaration',8,'p_arraydeclaration','Yacc.py',64),
  ('arraydeclaration -> accessmodif finalstatvar STACK GREATTHAN Type LESSTHAN STRING endexpression','arraydeclaration',8,'p_arraydeclaration','Yacc.py',65),
  ('arraydeclaration -> accessmodif finalstatvar LIST GREATTHAN Type LESSTHAN assign','arraydeclaration',7,'p_arraydeclaration','Yacc.py',66),
  ('arraydeclaration -> accessmodif finalstatvar ARRAYLIST GREATTHAN Type LESSTHAN assign','arraydeclaration',7,'p_arraydeclaration','Yacc.py',67),
  ('arraydeclaration -> accessmodif finalstatvar LINKEDLIST GREATTHAN Type LESSTHAN assign','arraydeclaration',7,'p_arraydeclaration','Yacc.py',68),
  ('arraydeclaration -> accessmodif finalstatvar DOUBLELINKEDLIST GREATTHAN Type LESSTHAN assign','arraydeclaration',7,'p_arraydeclaration','Yacc.py',69),
  ('arraydeclaration -> accessmodif finalstatvar QUEUE GREATTHAN Type LESSTHAN assign','arraydeclaration',7,'p_arraydeclaration','Yacc.py',70),
  ('arraydeclaration -> accessmodif finalstatvar STACK GREATTHAN Type LESSTHAN assign','arraydeclaration',7,'p_arraydeclaration','Yacc.py',71),
  ('assign -> STRING EQUALS expression endexpression','assign',4,'p_assign','Yacc.py',76),
  ('assign -> STRING EQUALS expressionarray endexpression','assign',4,'p_assign','Yacc.py',77),
  ('endexpression -> PUNTOCOMA','endexpression',1,'p_endexpression','Yacc.py',81),
  ('expression -> expression PLUS expression','expression',3,'p_expression','Yacc.py',85),
  ('expression -> expression MINUS expression','expression',3,'p_expression','Yacc.py',86),
  ('expression -> expression TIMES expression','expression',3,'p_expression','Yacc.py',87),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','Yacc.py',88),
  ('expression -> expression MOD expression','expression',3,'p_expression','Yacc.py',89),
  ('expression -> PLUSPLUS','expression',1,'p_expression','Yacc.py',90),
  ('expression -> MINUSMINUS','expression',1,'p_expression','Yacc.py',91),
  ('expression -> expression TIMESTIMES expression','expression',3,'p_expression','Yacc.py',92),
  ('expression -> TIMES_ASSIGN expression','expression',2,'p_expression','Yacc.py',93),
  ('expression -> MINUS_ASSIGN expression','expression',2,'p_expression','Yacc.py',94),
  ('expression -> PLUS_ASSIGN expression','expression',2,'p_expression','Yacc.py',95),
  ('expression -> DIVIDE_ASSIGN expression','expression',2,'p_expression','Yacc.py',96),
  ('expression -> MOD_ASSIGN expression','expression',2,'p_expression','Yacc.py',97),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','Yacc.py',98),
  ('expression -> INTEGER','expression',1,'p_expression','Yacc.py',99),
  ('expression -> empty','expression',1,'p_expression','Yacc.py',100),
  ('expressionarray -> NEW LIST GREATTHAN Type LESSTHAN LPAREN RPAREN','expressionarray',7,'p_expressionarray','Yacc.py',130),
  ('expressionarray -> NEW LINKEDLIST GREATTHAN Type LESSTHAN LPAREN RPAREN','expressionarray',7,'p_expressionarray','Yacc.py',131),
  ('expressionarray -> NEW DOUBLELINKEDLIST GREATTHAN Type LESSTHAN LPAREN RPAREN','expressionarray',7,'p_expressionarray','Yacc.py',132),
  ('expressionarray -> NEW QUEUE GREATTHAN Type LESSTHAN LPAREN RPAREN','expressionarray',7,'p_expressionarray','Yacc.py',133),
  ('expressionarray -> NEW STACK GREATTHAN Type LESSTHAN LPAREN RPAREN','expressionarray',7,'p_expressionarray','Yacc.py',134),
]
