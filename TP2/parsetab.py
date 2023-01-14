
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ADD AND COMMENT DIV ELSE EQUAL GEQ GREATER ID IF LARROW LEQ LESSER MUL NEG NUM OR POW PRINT RARROW READ STRING SUB SWAP SWITCHCASE SWITCHCOND WHILEStart : AxiomStart : Axiom : Axiom BlockAxiom : Axiom FunctionAxiom : Code : Code BlockCode : BlockBlock : FunCall ';'Block : Exp ';'Block : If Block : IfElse Block : While Block : Switch Body : '{' '}'Body : BlockBody : '{' Code '}'Function : ID FunScope FunCases BodyFunScope : ':'FunCases : FunExtra RARROW IDFunCases : RARROW IDFunCases : FunExtraFunCases : FunExtra : FunExtra ',' IDFunExtra : IDIfScope : IFIf : IfScope AtribOp BodyElseScope : ELSEIfElse : IfScope AtribOp Body ElseScope BodyWhileScope : WHILEWhile : WhileScope '(' AtribOp ')' BodySwitchScope : SWITCHCONDSwitchScope : SWITCHCASESwitch : SwitchScope Conds '{' Cases '}'Conds : Conds ',' CondConds : CondCond : ID '(' AtribOp ')'Cond : '(' AtribOp ')'Cases : Cases Case Cases : CaseCase : ID ':' BodyCase : ':' BodyExp : STRING PRINTExp : AtribExp : OpExp : DeclExp : DeclArrayExp : DeclAtribAtribOp : AtribNumAtribOp : OpDecl : ID IDDeclArray : ID ID DeclArraySizeDeclArraySize : DeclArraySize '[' NUM ']'DeclArraySize : '[' NUM ']'AtribArray : ID ArraySize LARROW AtribOpAtribArray : AtribOp RARROW ID ArraySizeArraySize : ArraySize '[' AtribOp ']'ArraySize : '[' AtribOp ']'DeclAtrib : ID ID LARROW AtribOpDeclAtrib : AtribOp RARROW ID IDAtribNum : ID LARROW AtribOpAtribNum : AtribOp RARROW IDAtribNum : AtribArrayAtrib : ID LARROW AtribOpAtrib : AtribOp RARROW IDAtrib : ID SWAP IDAtrib : AtribArrayOp : OpBinOpUno : NEG BaseOpUno : AccessArrayOpUno : SUB BaseOpUno : Base PRINTAccessArray : ID ArraySizeOpBin : OpBin OpLogico TermPlusOpBin : TermPlusTermPlus : TermPlus OpPlus TermMultTermPlus : TermMultTermMult : TermMult OpMult TermPowTermMult : TermPowTermPow : TermPow OpPow BaseTermPow : BaseBase : OpUnoBase : '(' AtribOp ')'Base : IDBase : NUMBase : FunCallBase : READFunCall : ID '(' FunArg ')'FunArg : FunRecFunArg : FunRec : FunRec ',' AtribOpFunRec : AtribOpOpLogico : ANDOpLogico : OROpLogico : LESSEROpLogico : GREATEROpLogico : LEQOpLogico : GEQOpLogico : EQUALOpPlus : ADDOpPlus : SUBOpMult : MULOpMult : DIVOpPow : POW"
    
_lr_action_items = {'$end':([0,1,2,3,4,7,8,9,10,40,41,101,104,119,132,151,152,154,155,],[-2,0,-1,-3,-4,-10,-11,-12,-13,-8,-9,-26,-15,-17,-14,-28,-16,-30,-33,]),'ID':([0,2,3,4,7,8,9,10,11,12,19,22,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,45,46,47,48,49,51,52,53,54,56,57,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,86,87,88,89,95,96,98,99,100,101,102,103,104,105,107,108,109,111,112,113,114,115,119,120,121,122,123,124,125,127,128,129,130,131,132,133,134,136,137,138,139,141,147,148,150,151,152,153,154,155,156,157,158,161,],[-5,11,-3,-4,-10,-11,-12,-13,42,52,52,61,-67,-25,-31,-32,-48,-74,-76,-78,-80,-81,-84,-86,81,-69,81,-8,-9,86,52,52,94,-72,-18,52,-49,-83,-62,-85,102,105,52,52,81,-92,-93,-94,-95,-96,-97,-98,81,-99,-100,81,-101,-102,81,-103,-71,-68,-83,-70,52,-24,102,-21,122,52,52,-82,128,52,-26,42,102,-15,135,140,61,52,-73,-75,-77,-79,-72,-17,147,148,-20,-87,52,-54,-57,-61,-60,102,-27,-14,102,-7,-55,102,140,-39,102,-19,-23,-56,-28,-16,-6,-30,-33,-38,102,-41,-40,]),'STRING':([0,2,3,4,7,8,9,10,24,29,30,31,32,33,34,35,36,38,40,41,43,47,48,51,52,53,54,56,79,80,81,82,86,87,88,98,101,103,104,111,112,113,114,115,119,122,123,125,127,128,129,130,131,132,133,134,136,137,141,147,148,150,151,152,153,154,155,157,],[-5,13,-3,-4,-10,-11,-12,-13,-67,-48,-74,-76,-78,-80,-81,-84,-86,-69,-8,-9,-22,-72,-18,-49,-83,-62,-85,13,-71,-68,-83,-70,-24,13,-21,-82,-26,13,-15,-73,-75,-77,-79,-72,-17,-20,-87,-54,-57,-61,-60,13,-27,-14,13,-7,-55,13,13,-19,-23,-56,-28,-16,-6,-30,-33,13,]),'IF':([0,2,3,4,7,8,9,10,24,29,30,31,32,33,34,35,36,38,40,41,43,47,48,51,52,53,54,56,79,80,81,82,86,87,88,98,101,103,104,111,112,113,114,115,119,122,123,125,127,128,129,130,131,132,133,134,136,137,141,147,148,150,151,152,153,154,155,157,],[-5,25,-3,-4,-10,-11,-12,-13,-67,-48,-74,-76,-78,-80,-81,-84,-86,-69,-8,-9,-22,-72,-18,-49,-83,-62,-85,25,-71,-68,-83,-70,-24,25,-21,-82,-26,25,-15,-73,-75,-77,-79,-72,-17,-20,-87,-54,-57,-61,-60,25,-27,-14,25,-7,-55,25,25,-19,-23,-56,-28,-16,-6,-30,-33,25,]),'WHILE':([0,2,3,4,7,8,9,10,24,29,30,31,32,33,34,35,36,38,40,41,43,47,48,51,52,53,54,56,79,80,81,82,86,87,88,98,101,103,104,111,112,113,114,115,119,122,123,125,127,128,129,130,131,132,133,134,136,137,141,147,148,150,151,152,153,154,155,157,],[-5,26,-3,-4,-10,-11,-12,-13,-67,-48,-74,-76,-78,-80,-81,-84,-86,-69,-8,-9,-22,-72,-18,-49,-83,-62,-85,26,-71,-68,-83,-70,-24,26,-21,-82,-26,26,-15,-73,-75,-77,-79,-72,-17,-20,-87,-54,-57,-61,-60,26,-27,-14,26,-7,-55,26,26,-19,-23,-56,-28,-16,-6,-30,-33,26,]),'SWITCHCOND':([0,2,3,4,7,8,9,10,24,29,30,31,32,33,34,35,36,38,40,41,43,47,48,51,52,53,54,56,79,80,81,82,86,87,88,98,101,103,104,111,112,113,114,115,119,122,123,125,127,128,129,130,131,132,133,134,136,137,141,147,148,150,151,152,153,154,155,157,],[-5,27,-3,-4,-10,-11,-12,-13,-67,-48,-74,-76,-78,-80,-81,-84,-86,-69,-8,-9,-22,-72,-18,-49,-83,-62,-85,27,-71,-68,-83,-70,-24,27,-21,-82,-26,27,-15,-73,-75,-77,-79,-72,-17,-20,-87,-54,-57,-61,-60,27,-27,-14,27,-7,-55,27,27,-19,-23,-56,-28,-16,-6,-30,-33,27,]),'SWITCHCASE':([0,2,3,4,7,8,9,10,24,29,30,31,32,33,34,35,36,38,40,41,43,47,48,51,52,53,54,56,79,80,81,82,86,87,88,98,101,103,104,111,112,113,114,115,119,122,123,125,127,128,129,130,131,132,133,134,136,137,141,147,148,150,151,152,153,154,155,157,],[-5,28,-3,-4,-10,-11,-12,-13,-67,-48,-74,-76,-78,-80,-81,-84,-86,-69,-8,-9,-22,-72,-18,-49,-83,-62,-85,28,-71,-68,-83,-70,-24,28,-21,-82,-26,28,-15,-73,-75,-77,-79,-72,-17,-20,-87,-54,-57,-61,-60,28,-27,-14,28,-7,-55,28,28,-19,-23,-56,-28,-16,-6,-30,-33,28,]),'(':([0,2,3,4,7,8,9,10,11,12,19,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,45,47,48,49,51,52,53,54,56,58,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,86,87,88,95,96,98,100,101,102,103,104,108,109,111,112,113,114,115,119,122,123,124,125,127,128,129,130,131,132,133,134,136,137,141,147,148,150,151,152,153,154,155,157,],[-5,12,-3,-4,-10,-11,-12,-13,44,12,12,58,62,-67,-25,-29,-31,-32,-48,-74,-76,-78,-80,-81,-84,-86,12,-69,12,-8,-9,-22,12,12,-72,-18,12,-49,44,-62,-85,12,12,109,12,12,-92,-93,-94,-95,-96,-97,-98,12,-99,-100,12,-101,-102,12,-103,-71,-68,44,-70,12,-24,12,-21,12,12,-82,12,-26,44,12,-15,62,12,-73,-75,-77,-79,-72,-17,-20,-87,12,-54,-57,-61,-60,12,-27,-14,12,-7,-55,12,12,-19,-23,-56,-28,-16,-6,-30,-33,12,]),'NUM':([0,2,3,4,7,8,9,10,12,19,24,25,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,45,47,48,49,51,52,53,54,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,87,88,95,96,98,100,101,103,104,109,111,112,113,114,115,116,119,122,123,124,125,127,128,129,130,131,132,133,134,136,137,141,147,148,150,151,152,153,154,155,157,],[-5,35,-3,-4,-10,-11,-12,-13,35,35,-67,-25,-48,-74,-76,-78,-80,-81,-84,-86,35,-69,35,-8,-9,-22,35,35,-72,-18,35,-49,-83,-62,-85,35,35,35,35,-92,-93,-94,-95,-96,-97,-98,35,-99,-100,35,-101,-102,35,-103,-71,-68,-83,-70,35,118,-24,35,-21,35,35,-82,35,-26,35,-15,35,-73,-75,-77,-79,-72,145,-17,-20,-87,35,-54,-57,-61,-60,35,-27,-14,35,-7,-55,35,35,-19,-23,-56,-28,-16,-6,-30,-33,35,]),'READ':([0,2,3,4,7,8,9,10,12,19,24,25,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,45,47,48,49,51,52,53,54,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,86,87,88,95,96,98,100,101,103,104,109,111,112,113,114,115,119,122,123,124,125,127,128,129,130,131,132,133,134,136,137,141,147,148,150,151,152,153,154,155,157,],[-5,36,-3,-4,-10,-11,-12,-13,36,36,-67,-25,-48,-74,-76,-78,-80,-81,-84,-86,36,-69,36,-8,-9,-22,36,36,-72,-18,36,-49,-83,-62,-85,36,36,36,36,-92,-93,-94,-95,-96,-97,-98,36,-99,-100,36,-101,-102,36,-103,-71,-68,-83,-70,36,-24,36,-21,36,36,-82,36,-26,36,-15,36,-73,-75,-77,-79,-72,-17,-20,-87,36,-54,-57,-61,-60,36,-27,-14,36,-7,-55,36,36,-19,-23,-56,-28,-16,-6,-30,-33,36,]),'NEG':([0,2,3,4,7,8,9,10,12,19,24,25,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,45,47,48,49,51,52,53,54,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,86,87,88,95,96,98,100,101,103,104,109,111,112,113,114,115,119,122,123,124,125,127,128,129,130,131,132,133,134,136,137,141,147,148,150,151,152,153,154,155,157,],[-5,37,-3,-4,-10,-11,-12,-13,37,37,-67,-25,-48,-74,-76,-78,-80,-81,-84,-86,37,-69,37,-8,-9,-22,37,37,-72,-18,37,-49,-83,-62,-85,37,37,37,37,-92,-93,-94,-95,-96,-97,-98,37,-99,-100,37,-101,-102,37,-103,-71,-68,-83,-70,37,-24,37,-21,37,37,-82,37,-26,37,-15,37,-73,-75,-77,-79,-72,-17,-20,-87,37,-54,-57,-61,-60,37,-27,-14,37,-7,-55,37,37,-19,-23,-56,-28,-16,-6,-30,-33,37,]),'SUB':([0,2,3,4,5,7,8,9,10,11,12,19,24,25,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,45,47,48,49,51,52,53,54,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,86,87,88,95,96,98,100,101,102,103,104,109,111,112,113,114,115,119,122,123,124,125,127,128,129,130,131,132,133,134,136,137,141,147,148,150,151,152,153,154,155,157,],[-5,39,-3,-4,-85,-10,-11,-12,-13,-83,39,39,-67,-25,-48,73,-76,-78,-80,-81,-84,-86,39,-69,39,-8,-9,-22,39,39,-72,-18,39,-49,-83,-62,-85,39,39,39,39,-92,-93,-94,-95,-96,-97,-98,39,-99,-100,39,-101,-102,39,-103,-71,-68,-83,-70,39,-24,39,-21,39,39,-82,39,-26,-83,39,-15,39,73,-75,-77,-79,-72,-17,-20,-87,39,-54,-57,-61,-60,39,-27,-14,39,-7,-55,39,39,-19,-23,-56,-28,-16,-6,-30,-33,39,]),';':([5,6,11,14,15,16,17,18,23,24,29,30,31,32,33,34,35,36,38,42,47,51,52,53,54,55,79,80,81,82,83,93,94,98,102,105,111,112,113,114,115,117,123,125,127,128,129,135,136,146,150,160,],[40,41,-83,-43,-44,-45,-46,-47,-66,-67,-48,-74,-76,-78,-80,-81,-84,-86,-69,-50,-72,-49,-83,-62,-85,-42,-71,-68,-83,-70,-51,-63,-65,-82,-83,-64,-73,-75,-77,-79,-72,-58,-87,-54,-57,-61,-60,-59,-55,-53,-56,-52,]),'PRINT':([5,11,13,33,34,35,36,38,47,52,54,79,80,81,82,98,102,114,115,123,127,150,],[-85,-83,55,79,-81,-84,-86,-69,-72,-83,-85,-71,79,-83,79,-82,-83,79,-72,-87,-57,-56,]),'POW':([5,11,32,33,34,35,36,38,47,52,54,79,80,81,82,98,102,113,114,115,123,127,150,],[-85,-83,78,-80,-81,-84,-86,-69,-72,-83,-85,-71,-68,-83,-70,-82,-83,78,-79,-72,-87,-57,-56,]),'MUL':([5,11,31,32,33,34,35,36,38,47,52,54,79,80,81,82,98,102,112,113,114,115,123,127,150,],[-85,-83,75,-78,-80,-81,-84,-86,-69,-72,-83,-85,-71,-68,-83,-70,-82,-83,75,-77,-79,-72,-87,-57,-56,]),'DIV':([5,11,31,32,33,34,35,36,38,47,52,54,79,80,81,82,98,102,112,113,114,115,123,127,150,],[-85,-83,76,-78,-80,-81,-84,-86,-69,-72,-83,-85,-71,-68,-83,-70,-82,-83,76,-77,-79,-72,-87,-57,-56,]),'ADD':([5,11,30,31,32,33,34,35,36,38,47,52,54,79,80,81,82,98,102,111,112,113,114,115,123,127,150,],[-85,-83,72,-76,-78,-80,-81,-84,-86,-69,-72,-83,-85,-71,-68,-83,-70,-82,-83,72,-75,-77,-79,-72,-87,-57,-56,]),'AND':([5,11,24,30,31,32,33,34,35,36,38,47,52,54,79,80,81,82,98,102,111,112,113,114,115,123,127,150,],[-85,-83,64,-74,-76,-78,-80,-81,-84,-86,-69,-72,-83,-85,-71,-68,-83,-70,-82,-83,-73,-75,-77,-79,-72,-87,-57,-56,]),'OR':([5,11,24,30,31,32,33,34,35,36,38,47,52,54,79,80,81,82,98,102,111,112,113,114,115,123,127,150,],[-85,-83,65,-74,-76,-78,-80,-81,-84,-86,-69,-72,-83,-85,-71,-68,-83,-70,-82,-83,-73,-75,-77,-79,-72,-87,-57,-56,]),'LESSER':([5,11,24,30,31,32,33,34,35,36,38,47,52,54,79,80,81,82,98,102,111,112,113,114,115,123,127,150,],[-85,-83,66,-74,-76,-78,-80,-81,-84,-86,-69,-72,-83,-85,-71,-68,-83,-70,-82,-83,-73,-75,-77,-79,-72,-87,-57,-56,]),'GREATER':([5,11,24,30,31,32,33,34,35,36,38,47,52,54,79,80,81,82,98,102,111,112,113,114,115,123,127,150,],[-85,-83,67,-74,-76,-78,-80,-81,-84,-86,-69,-72,-83,-85,-71,-68,-83,-70,-82,-83,-73,-75,-77,-79,-72,-87,-57,-56,]),'LEQ':([5,11,24,30,31,32,33,34,35,36,38,47,52,54,79,80,81,82,98,102,111,112,113,114,115,123,127,150,],[-85,-83,68,-74,-76,-78,-80,-81,-84,-86,-69,-72,-83,-85,-71,-68,-83,-70,-82,-83,-73,-75,-77,-79,-72,-87,-57,-56,]),'GEQ':([5,11,24,30,31,32,33,34,35,36,38,47,52,54,79,80,81,82,98,102,111,112,113,114,115,123,127,150,],[-85,-83,69,-74,-76,-78,-80,-81,-84,-86,-69,-72,-83,-85,-71,-68,-83,-70,-82,-83,-73,-75,-77,-79,-72,-87,-57,-56,]),'EQUAL':([5,11,24,30,31,32,33,34,35,36,38,47,52,54,79,80,81,82,98,102,111,112,113,114,115,123,127,150,],[-85,-83,70,-74,-76,-78,-80,-81,-84,-86,-69,-72,-83,-85,-71,-68,-83,-70,-82,-83,-73,-75,-77,-79,-72,-87,-57,-56,]),'RARROW':([5,11,15,20,23,24,29,30,31,32,33,34,35,36,38,43,47,48,50,51,52,53,54,56,79,80,81,82,86,88,92,93,97,98,102,105,106,110,111,112,113,114,115,117,123,125,126,127,128,129,136,143,148,149,150,],[-85,-83,-49,57,-62,-67,-48,-74,-76,-78,-80,-81,-84,-86,-69,89,-72,-18,99,-49,-83,-62,-85,99,-71,-68,-83,-70,-24,120,99,99,99,-82,-83,-61,99,99,-73,-75,-77,-79,-72,99,-87,99,99,-57,-61,99,-55,99,-23,99,-56,]),'ELSE':([7,8,9,10,40,41,101,104,132,151,152,154,155,],[-10,-11,-12,-13,-8,-9,131,-15,-14,-28,-16,-30,-33,]),'}':([7,8,9,10,40,41,101,103,104,132,133,134,138,139,151,152,153,154,155,156,158,161,],[-10,-11,-12,-13,-8,-9,-26,132,-15,-14,152,-7,155,-39,-28,-16,-6,-30,-33,-38,-41,-40,]),':':([7,8,9,10,11,40,41,101,104,107,132,138,139,140,151,152,154,155,156,158,161,],[-10,-11,-12,-13,48,-8,-9,-26,-15,141,-14,141,-39,157,-28,-16,-30,-33,-38,-41,-40,]),'LARROW':([11,42,47,52,102,127,150,],[45,84,95,100,45,-57,-56,]),'SWAP':([11,102,],[46,46,]),'[':([11,42,47,52,81,83,102,105,115,127,128,136,146,150,160,],[49,85,96,49,49,116,49,49,96,-57,49,96,-53,-56,-52,]),')':([24,29,30,31,32,33,34,35,36,38,44,47,50,51,52,53,54,79,80,81,82,90,91,92,98,106,110,111,112,113,114,115,123,125,127,128,129,136,143,149,150,],[-67,-48,-74,-76,-78,-80,-81,-84,-86,-69,-89,-72,98,-49,-83,-62,-85,-71,-68,-83,-70,123,-88,-91,-82,137,144,-73,-75,-77,-79,-72,-87,-54,-57,-61,-60,-55,159,-90,-56,]),'{':([24,29,30,31,32,33,34,35,36,38,43,47,48,51,52,53,54,56,59,60,79,80,81,82,86,87,88,98,111,112,113,114,115,122,123,125,127,128,129,130,131,136,137,141,142,144,147,148,150,157,159,],[-67,-48,-74,-76,-78,-80,-81,-84,-86,-69,-22,-72,-18,-49,-83,-62,-85,103,107,-35,-71,-68,-83,-70,-24,103,-21,-82,-73,-75,-77,-79,-72,-20,-87,-54,-57,-61,-60,103,-27,-55,103,103,-34,-37,-19,-23,-56,103,-36,]),',':([24,29,30,31,32,33,34,35,36,38,47,51,52,53,54,59,60,79,80,81,82,86,88,91,92,98,111,112,113,114,115,123,125,127,128,129,136,142,144,148,149,150,159,],[-67,-48,-74,-76,-78,-80,-81,-84,-86,-69,-72,-49,-83,-62,-85,108,-35,-71,-68,-83,-70,-24,121,124,-91,-82,-73,-75,-77,-79,-72,-87,-54,-57,-61,-60,-55,-34,-37,-23,-90,-56,-36,]),']':([24,29,30,31,32,33,34,35,36,38,47,51,52,53,54,79,80,81,82,97,98,111,112,113,114,115,118,123,125,126,127,128,129,136,145,150,],[-67,-48,-74,-76,-78,-80,-81,-84,-86,-69,-72,-49,-83,-62,-85,-71,-68,-83,-70,127,-82,-73,-75,-77,-79,-72,146,-87,-54,150,-57,-61,-60,-55,160,-56,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Start':([0,],[1,]),'Axiom':([0,],[2,]),'Block':([2,56,87,103,130,133,137,141,157,],[3,104,104,134,104,153,104,104,104,]),'Function':([2,],[4,]),'FunCall':([2,12,19,37,39,44,45,49,56,58,62,63,71,74,77,84,87,95,96,100,103,109,124,130,133,137,141,157,],[5,54,54,54,54,54,54,54,5,54,54,54,54,54,54,54,5,54,54,54,5,54,54,5,5,5,5,5,]),'Exp':([2,56,87,103,130,133,137,141,157,],[6,6,6,6,6,6,6,6,6,]),'If':([2,56,87,103,130,133,137,141,157,],[7,7,7,7,7,7,7,7,7,]),'IfElse':([2,56,87,103,130,133,137,141,157,],[8,8,8,8,8,8,8,8,8,]),'While':([2,56,87,103,130,133,137,141,157,],[9,9,9,9,9,9,9,9,9,]),'Switch':([2,56,87,103,130,133,137,141,157,],[10,10,10,10,10,10,10,10,10,]),'Atrib':([2,56,87,103,130,133,137,141,157,],[14,14,14,14,14,14,14,14,14,]),'Op':([2,12,19,44,45,49,56,58,62,84,87,95,96,100,103,109,124,130,133,137,141,157,],[15,51,51,51,51,51,15,51,51,51,15,51,51,51,15,51,51,15,15,15,15,15,]),'Decl':([2,56,87,103,130,133,137,141,157,],[16,16,16,16,16,16,16,16,16,]),'DeclArray':([2,56,87,103,130,133,137,141,157,],[17,17,17,17,17,17,17,17,17,]),'DeclAtrib':([2,56,87,103,130,133,137,141,157,],[18,18,18,18,18,18,18,18,18,]),'IfScope':([2,56,87,103,130,133,137,141,157,],[19,19,19,19,19,19,19,19,19,]),'AtribOp':([2,12,19,44,45,49,56,58,62,84,87,95,96,100,103,109,124,130,133,137,141,157,],[20,50,56,92,93,97,20,106,110,117,20,125,126,129,20,143,149,20,20,20,20,20,]),'WhileScope':([2,56,87,103,130,133,137,141,157,],[21,21,21,21,21,21,21,21,21,]),'SwitchScope':([2,56,87,103,130,133,137,141,157,],[22,22,22,22,22,22,22,22,22,]),'AtribArray':([2,12,19,44,45,49,56,58,62,84,87,95,96,100,103,109,124,130,133,137,141,157,],[23,53,53,53,53,53,23,53,53,53,23,53,53,53,23,53,53,23,23,23,23,23,]),'OpBin':([2,12,19,44,45,49,56,58,62,84,87,95,96,100,103,109,124,130,133,137,141,157,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'AtribNum':([2,12,19,44,45,49,56,58,62,84,87,95,96,100,103,109,124,130,133,137,141,157,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'TermPlus':([2,12,19,44,45,49,56,58,62,63,84,87,95,96,100,103,109,124,130,133,137,141,157,],[30,30,30,30,30,30,30,30,30,111,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'TermMult':([2,12,19,44,45,49,56,58,62,63,71,84,87,95,96,100,103,109,124,130,133,137,141,157,],[31,31,31,31,31,31,31,31,31,31,112,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'TermPow':([2,12,19,44,45,49,56,58,62,63,71,74,84,87,95,96,100,103,109,124,130,133,137,141,157,],[32,32,32,32,32,32,32,32,32,32,32,113,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'Base':([2,12,19,37,39,44,45,49,56,58,62,63,71,74,77,84,87,95,96,100,103,109,124,130,133,137,141,157,],[33,33,33,80,82,33,33,33,33,33,33,33,33,33,114,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'OpUno':([2,12,19,37,39,44,45,49,56,58,62,63,71,74,77,84,87,95,96,100,103,109,124,130,133,137,141,157,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'AccessArray':([2,12,19,37,39,44,45,49,56,58,62,63,71,74,77,84,87,95,96,100,103,109,124,130,133,137,141,157,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'FunScope':([11,],[43,]),'ArraySize':([11,52,81,102,105,128,],[47,47,115,47,136,136,]),'Conds':([22,],[59,]),'Cond':([22,108,],[60,142,]),'OpLogico':([24,],[63,]),'OpPlus':([30,111,],[71,71,]),'OpMult':([31,112,],[74,74,]),'OpPow':([32,113,],[77,77,]),'DeclArraySize':([42,],[83,]),'FunCases':([43,],[87,]),'FunExtra':([43,],[88,]),'FunArg':([44,],[90,]),'FunRec':([44,],[91,]),'Body':([56,87,130,137,141,157,],[101,119,151,154,158,161,]),'ElseScope':([101,],[130,]),'Code':([103,],[133,]),'Cases':([107,],[138,]),'Case':([107,138,],[139,156,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Start","S'",1,None,None,None),
  ('Start -> Axiom','Start',1,'p_start_axiom','yacc.py',11),
  ('Start -> <empty>','Start',0,'p_start_empty','yacc.py',19),
  ('Axiom -> Axiom Block','Axiom',2,'p_axiom_code','yacc.py',24),
  ('Axiom -> Axiom Function','Axiom',2,'p_axiom_function','yacc.py',30),
  ('Axiom -> <empty>','Axiom',0,'p_axiom_empty','yacc.py',36),
  ('Code -> Code Block','Code',2,'p_code_block','yacc.py',41),
  ('Code -> Block','Code',1,'p_code_empty','yacc.py',46),
  ('Block -> FunCall ;','Block',2,'p_block_funcall','yacc.py',51),
  ('Block -> Exp ;','Block',2,'p_block_exp','yacc.py',59),
  ('Block -> If','Block',1,'p_block_if','yacc.py',64),
  ('Block -> IfElse','Block',1,'p_block_ifelse','yacc.py',69),
  ('Block -> While','Block',1,'p_block_while','yacc.py',74),
  ('Block -> Switch','Block',1,'p_block_switch','yacc.py',79),
  ('Body -> { }','Body',2,'p_body_empty','yacc.py',88),
  ('Body -> Block','Body',1,'p_body_block','yacc.py',93),
  ('Body -> { Code }','Body',3,'p_body_code','yacc.py',98),
  ('Function -> ID FunScope FunCases Body','Function',4,'p_function','yacc.py',103),
  ('FunScope -> :','FunScope',1,'p_funscope','yacc.py',140),
  ('FunCases -> FunExtra RARROW ID','FunCases',3,'p_funcases_funextra_rarrow','yacc.py',146),
  ('FunCases -> RARROW ID','FunCases',2,'p_funcases_rarrow','yacc.py',166),
  ('FunCases -> FunExtra','FunCases',1,'p_funcases_funextra','yacc.py',176),
  ('FunCases -> <empty>','FunCases',0,'p_funcases_empty','yacc.py',190),
  ('FunExtra -> FunExtra , ID','FunExtra',3,'p_funextra_rec','yacc.py',195),
  ('FunExtra -> ID','FunExtra',1,'p_funextra_empty','yacc.py',201),
  ('IfScope -> IF','IfScope',1,'p_if_scope','yacc.py',206),
  ('If -> IfScope AtribOp Body','If',3,'p_if','yacc.py',212),
  ('ElseScope -> ELSE','ElseScope',1,'p_else_scope','yacc.py',224),
  ('IfElse -> IfScope AtribOp Body ElseScope Body','IfElse',5,'p_ifelse','yacc.py',232),
  ('WhileScope -> WHILE','WhileScope',1,'p_while_scope','yacc.py',247),
  ('While -> WhileScope ( AtribOp ) Body','While',5,'p_while','yacc.py',253),
  ('SwitchScope -> SWITCHCOND','SwitchScope',1,'p_switch_scopecond','yacc.py',268),
  ('SwitchScope -> SWITCHCASE','SwitchScope',1,'p_switch_scopecase','yacc.py',280),
  ('Switch -> SwitchScope Conds { Cases }','Switch',5,'p_switch','yacc.py',293),
  ('Conds -> Conds , Cond','Conds',3,'p_conds_rec','yacc.py',335),
  ('Conds -> Cond','Conds',1,'p_conds_base','yacc.py',341),
  ('Cond -> ID ( AtribOp )','Cond',4,'p_cond_id','yacc.py',346),
  ('Cond -> ( AtribOp )','Cond',3,'p_cond_empty','yacc.py',352),
  ('Cases -> Cases Case','Cases',2,'p_cases_rec','yacc.py',358),
  ('Cases -> Case','Cases',1,'p_cases_base','yacc.py',364),
  ('Case -> ID : Body','Case',3,'p_case_id','yacc.py',369),
  ('Case -> : Body','Case',2,'p_case_empty','yacc.py',376),
  ('Exp -> STRING PRINT','Exp',2,'p_exp_print','yacc.py',390),
  ('Exp -> Atrib','Exp',1,'p_exp_atrib','yacc.py',395),
  ('Exp -> Op','Exp',1,'p_exp_op','yacc.py',400),
  ('Exp -> Decl','Exp',1,'p_exp_decl','yacc.py',405),
  ('Exp -> DeclArray','Exp',1,'p_exp_declarray','yacc.py',410),
  ('Exp -> DeclAtrib','Exp',1,'p_exp_declatrib','yacc.py',415),
  ('AtribOp -> AtribNum','AtribOp',1,'p_atribop_atribnum','yacc.py',420),
  ('AtribOp -> Op','AtribOp',1,'p_atribop_op','yacc.py',425),
  ('Decl -> ID ID','Decl',2,'p_decl','yacc.py',430),
  ('DeclArray -> ID ID DeclArraySize','DeclArray',3,'p_declarray','yacc.py',453),
  ('DeclArraySize -> DeclArraySize [ NUM ]','DeclArraySize',4,'p_declarraysize_rec','yacc.py',477),
  ('DeclArraySize -> [ NUM ]','DeclArraySize',3,'p_declarraysize_empty','yacc.py',483),
  ('AtribArray -> ID ArraySize LARROW AtribOp','AtribArray',4,'p_atribarray_Leftatribop','yacc.py',488),
  ('AtribArray -> AtribOp RARROW ID ArraySize','AtribArray',4,'p_atribarray_Rightatribop','yacc.py',523),
  ('ArraySize -> ArraySize [ AtribOp ]','ArraySize',4,'p_arraysize_rec','yacc.py',551),
  ('ArraySize -> [ AtribOp ]','ArraySize',3,'p_arraysize_empty','yacc.py',556),
  ('DeclAtrib -> ID ID LARROW AtribOp','DeclAtrib',4,'p_declatrib_left','yacc.py',561),
  ('DeclAtrib -> AtribOp RARROW ID ID','DeclAtrib',4,'p_declatrib_right','yacc.py',582),
  ('AtribNum -> ID LARROW AtribOp','AtribNum',3,'p_atribnum_left','yacc.py',603),
  ('AtribNum -> AtribOp RARROW ID','AtribNum',3,'p_atribnum_right','yacc.py',608),
  ('AtribNum -> AtribArray','AtribNum',1,'p_atribnum_array','yacc.py',614),
  ('Atrib -> ID LARROW AtribOp','Atrib',3,'p_atrib_left','yacc.py',619),
  ('Atrib -> AtribOp RARROW ID','Atrib',3,'p_atrib_right','yacc.py',624),
  ('Atrib -> ID SWAP ID','Atrib',3,'p_atrib_equiv','yacc.py',629),
  ('Atrib -> AtribArray','Atrib',1,'p_atrib_array','yacc.py',654),
  ('Op -> OpBin','Op',1,'p_op_opbin','yacc.py',664),
  ('OpUno -> NEG Base','OpUno',2,'p_opuno_neg','yacc.py',669),
  ('OpUno -> AccessArray','OpUno',1,'p_opuno_accessarray','yacc.py',674),
  ('OpUno -> SUB Base','OpUno',2,'p_opuno_minus','yacc.py',679),
  ('OpUno -> Base PRINT','OpUno',2,'p_opuno_print','yacc.py',684),
  ('AccessArray -> ID ArraySize','AccessArray',2,'p_accessarray','yacc.py',690),
  ('OpBin -> OpBin OpLogico TermPlus','OpBin',3,'p_opbin_rec','yacc.py',705),
  ('OpBin -> TermPlus','OpBin',1,'p_opbin_base','yacc.py',710),
  ('TermPlus -> TermPlus OpPlus TermMult','TermPlus',3,'p_termplus_rec','yacc.py',715),
  ('TermPlus -> TermMult','TermPlus',1,'p_termplus_base','yacc.py',720),
  ('TermMult -> TermMult OpMult TermPow','TermMult',3,'p_termmult_rec','yacc.py',725),
  ('TermMult -> TermPow','TermMult',1,'p_termmult_base','yacc.py',730),
  ('TermPow -> TermPow OpPow Base','TermPow',3,'p_termpow_rec','yacc.py',735),
  ('TermPow -> Base','TermPow',1,'p_termpow_base','yacc.py',740),
  ('Base -> OpUno','Base',1,'p_base_opuno','yacc.py',745),
  ('Base -> ( AtribOp )','Base',3,'p_base_exp','yacc.py',750),
  ('Base -> ID','Base',1,'p_base_id','yacc.py',755),
  ('Base -> NUM','Base',1,'p_base_num','yacc.py',769),
  ('Base -> FunCall','Base',1,'p_base_funcall','yacc.py',774),
  ('Base -> READ','Base',1,'p_base_read','yacc.py',784),
  ('FunCall -> ID ( FunArg )','FunCall',4,'p_funcall','yacc.py',789),
  ('FunArg -> FunRec','FunArg',1,'p_funarg_funrec','yacc.py',810),
  ('FunArg -> <empty>','FunArg',0,'p_funarg_empty','yacc.py',815),
  ('FunRec -> FunRec , AtribOp','FunRec',3,'p_funrec_rec','yacc.py',820),
  ('FunRec -> AtribOp','FunRec',1,'p_funrec_base','yacc.py',826),
  ('OpLogico -> AND','OpLogico',1,'p_oplogico_and','yacc.py',831),
  ('OpLogico -> OR','OpLogico',1,'p_oplogico_or','yacc.py',836),
  ('OpLogico -> LESSER','OpLogico',1,'p_oplogico_lesser','yacc.py',841),
  ('OpLogico -> GREATER','OpLogico',1,'p_oplogico_greater','yacc.py',846),
  ('OpLogico -> LEQ','OpLogico',1,'p_oplogico_leq','yacc.py',851),
  ('OpLogico -> GEQ','OpLogico',1,'p_oplogico_geq','yacc.py',856),
  ('OpLogico -> EQUAL','OpLogico',1,'p_oplogico_equal','yacc.py',861),
  ('OpPlus -> ADD','OpPlus',1,'p_opplus_add','yacc.py',866),
  ('OpPlus -> SUB','OpPlus',1,'p_opplus_sub','yacc.py',871),
  ('OpMult -> MUL','OpMult',1,'p_opmult_mul','yacc.py',876),
  ('OpMult -> DIV','OpMult',1,'p_opmult_div','yacc.py',881),
  ('OpPow -> POW','OpPow',1,'p_oppow','yacc.py',886),
]
