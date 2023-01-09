
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ADD AND DIV ELSE EQUAL GEQ GREATER ID IF LARROW LEQ LESSER MUL NEG NUM OR POW PRINT RARROW READ SUB SWAP SWITCH WHILEStart : AxiomStart : Axiom : Axiom BlockAxiom : Axiom FunctionAxiom : Code : Code BlockCode : BlockBlock : FunCall ';'Block : Exp ';'Block : If Block : IfElse Block : While Block : Switch Body : '{' '}'Body : BlockBody : '{' Code '}'Function : ID FunScope FunCases BodyFunScope : ':'FunCases : FunExtra RARROW IDFunCases : RARROW IDFunCases : FunExtraFunCases : FunExtra : FunExtra ',' IDFunExtra : IDIfScope : IFIf : IfScope AtribOp BodyElseScope : ELSEIfElse : IfScope AtribOp Body ElseScope BodyWhileScope : WHILEWhile : WhileScope '(' AtribOp ')' BodySwitchScope : SWITCHSwitch : SwitchScope Conds '{' Cases '}'Conds : Conds ',' CondConds : CondCond : ID '(' AtribOp ')'Cond : '(' AtribOp ')'Cases : Cases Case Cases : CaseCase : ID ':' BodyCase : ':' BodyExp : AtribExp : OpExp : DeclExp : DeclArrayExp : DeclAtribAtribOp : AtribNumAtribOp : OpDecl : ID IDDeclArray : ID ID DeclArraySizeDeclArraySize : DeclArraySize '[' NUM ']'DeclArraySize : '[' NUM ']'AtribArray : ID ArraySize LARROW AtribOpAtribArray : AtribOp RARROW ID ArraySizeArraySize : ArraySize '[' AtribOp ']'ArraySize : '[' AtribOp ']'DeclAtrib : ID ID LARROW AtribOpDeclAtrib : AtribOp RARROW ID IDAtribNum : ID LARROW AtribOpAtribNum : AtribOp RARROW IDAtribNum : AtribArrayAtrib : ID LARROW AtribOpAtrib : AtribOp RARROW IDAtrib : ID SWAP IDAtrib : AtribArrayOp : OpBinOpUno : NEG BaseOpUno : AccessArrayOpUno : SUB BaseOpUno : Base PRINTAccessArray : ID ArraySizeOpBin : OpBin OpLogico TermPlusOpBin : TermPlusTermPlus : TermPlus OpPlus TermMultTermPlus : TermMultTermMult : TermMult OpMult TermPowTermMult : TermPowTermPow : TermPow OpPow BaseTermPow : BaseBase : OpUnoBase : '(' AtribOp ')'Base : IDBase : NUMBase : FunCallBase : READFunCall : ID '(' FunArg ')'FunArg : FunRecFunArg : FunRec : FunRec ',' AtribOpFunRec : AtribOpOpLogico : ANDOpLogico : OROpLogico : LESSEROpLogico : GREATEROpLogico : LEQOpLogico : GEQOpLogico : EQUALOpPlus : ADDOpPlus : SUBOpMult : MULOpMult : DIVOpPow : POW"
    
_lr_action_items = {'$end':([0,1,2,3,4,7,8,9,10,38,39,98,101,116,129,148,149,151,152,],[-2,0,-1,-3,-4,-10,-11,-12,-13,-8,-9,-26,-15,-17,-14,-28,-16,-30,-32,]),'ID':([0,2,3,4,7,8,9,10,11,12,18,21,23,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,49,50,51,52,53,54,55,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,83,84,85,86,92,93,95,96,97,98,99,100,101,102,104,105,106,108,109,110,111,112,116,117,118,119,120,121,122,124,125,126,127,128,129,130,131,133,134,135,136,138,144,145,147,148,149,150,151,152,153,154,155,158,],[-5,11,-3,-4,-10,-11,-12,-13,40,50,50,58,-65,-25,-31,-46,-72,-74,-76,-78,-79,-82,-84,78,-67,78,-8,-9,83,50,50,91,-70,-18,50,-47,-81,-60,-83,99,102,50,50,78,-90,-91,-92,-93,-94,-95,-96,78,-97,-98,78,-99,-100,78,-101,-69,-66,-81,-68,50,-24,99,-21,119,50,50,-80,125,50,-26,40,99,-15,132,137,58,50,-71,-73,-75,-77,-70,-17,144,145,-20,-85,50,-52,-55,-59,-58,99,-27,-14,99,-7,-53,99,137,-38,99,-19,-23,-54,-28,-16,-6,-30,-32,-37,99,-40,-39,]),'IF':([0,2,3,4,7,8,9,10,23,27,28,29,30,31,32,33,34,36,38,39,41,45,46,49,50,51,52,53,76,77,78,79,83,84,85,95,98,100,101,108,109,110,111,112,116,119,120,122,124,125,126,127,128,129,130,131,133,134,138,144,145,147,148,149,150,151,152,154,],[-5,24,-3,-4,-10,-11,-12,-13,-65,-46,-72,-74,-76,-78,-79,-82,-84,-67,-8,-9,-22,-70,-18,-47,-81,-60,-83,24,-69,-66,-81,-68,-24,24,-21,-80,-26,24,-15,-71,-73,-75,-77,-70,-17,-20,-85,-52,-55,-59,-58,24,-27,-14,24,-7,-53,24,24,-19,-23,-54,-28,-16,-6,-30,-32,24,]),'WHILE':([0,2,3,4,7,8,9,10,23,27,28,29,30,31,32,33,34,36,38,39,41,45,46,49,50,51,52,53,76,77,78,79,83,84,85,95,98,100,101,108,109,110,111,112,116,119,120,122,124,125,126,127,128,129,130,131,133,134,138,144,145,147,148,149,150,151,152,154,],[-5,25,-3,-4,-10,-11,-12,-13,-65,-46,-72,-74,-76,-78,-79,-82,-84,-67,-8,-9,-22,-70,-18,-47,-81,-60,-83,25,-69,-66,-81,-68,-24,25,-21,-80,-26,25,-15,-71,-73,-75,-77,-70,-17,-20,-85,-52,-55,-59,-58,25,-27,-14,25,-7,-53,25,25,-19,-23,-54,-28,-16,-6,-30,-32,25,]),'SWITCH':([0,2,3,4,7,8,9,10,23,27,28,29,30,31,32,33,34,36,38,39,41,45,46,49,50,51,52,53,76,77,78,79,83,84,85,95,98,100,101,108,109,110,111,112,116,119,120,122,124,125,126,127,128,129,130,131,133,134,138,144,145,147,148,149,150,151,152,154,],[-5,26,-3,-4,-10,-11,-12,-13,-65,-46,-72,-74,-76,-78,-79,-82,-84,-67,-8,-9,-22,-70,-18,-47,-81,-60,-83,26,-69,-66,-81,-68,-24,26,-21,-80,-26,26,-15,-71,-73,-75,-77,-70,-17,-20,-85,-52,-55,-59,-58,26,-27,-14,26,-7,-53,26,26,-19,-23,-54,-28,-16,-6,-30,-32,26,]),'(':([0,2,3,4,7,8,9,10,11,12,18,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,45,46,47,49,50,51,52,53,55,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,83,84,85,92,93,95,97,98,99,100,101,105,106,108,109,110,111,112,116,119,120,121,122,124,125,126,127,128,129,130,131,133,134,138,144,145,147,148,149,150,151,152,154,],[-5,12,-3,-4,-10,-11,-12,-13,42,12,12,55,59,-65,-25,-29,-31,-46,-72,-74,-76,-78,-79,-82,-84,12,-67,12,-8,-9,-22,12,12,-70,-18,12,-47,42,-60,-83,12,12,106,12,12,-90,-91,-92,-93,-94,-95,-96,12,-97,-98,12,-99,-100,12,-101,-69,-66,42,-68,12,-24,12,-21,12,12,-80,12,-26,42,12,-15,59,12,-71,-73,-75,-77,-70,-17,-20,-85,12,-52,-55,-59,-58,12,-27,-14,12,-7,-53,12,12,-19,-23,-54,-28,-16,-6,-30,-32,12,]),'NUM':([0,2,3,4,7,8,9,10,12,18,23,24,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,45,46,47,49,50,51,52,53,55,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,92,93,95,97,98,100,101,106,108,109,110,111,112,113,116,119,120,121,122,124,125,126,127,128,129,130,131,133,134,138,144,145,147,148,149,150,151,152,154,],[-5,33,-3,-4,-10,-11,-12,-13,33,33,-65,-25,-46,-72,-74,-76,-78,-79,-82,-84,33,-67,33,-8,-9,-22,33,33,-70,-18,33,-47,-81,-60,-83,33,33,33,33,-90,-91,-92,-93,-94,-95,-96,33,-97,-98,33,-99,-100,33,-101,-69,-66,-81,-68,33,115,-24,33,-21,33,33,-80,33,-26,33,-15,33,-71,-73,-75,-77,-70,142,-17,-20,-85,33,-52,-55,-59,-58,33,-27,-14,33,-7,-53,33,33,-19,-23,-54,-28,-16,-6,-30,-32,33,]),'READ':([0,2,3,4,7,8,9,10,12,18,23,24,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,45,46,47,49,50,51,52,53,55,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,83,84,85,92,93,95,97,98,100,101,106,108,109,110,111,112,116,119,120,121,122,124,125,126,127,128,129,130,131,133,134,138,144,145,147,148,149,150,151,152,154,],[-5,34,-3,-4,-10,-11,-12,-13,34,34,-65,-25,-46,-72,-74,-76,-78,-79,-82,-84,34,-67,34,-8,-9,-22,34,34,-70,-18,34,-47,-81,-60,-83,34,34,34,34,-90,-91,-92,-93,-94,-95,-96,34,-97,-98,34,-99,-100,34,-101,-69,-66,-81,-68,34,-24,34,-21,34,34,-80,34,-26,34,-15,34,-71,-73,-75,-77,-70,-17,-20,-85,34,-52,-55,-59,-58,34,-27,-14,34,-7,-53,34,34,-19,-23,-54,-28,-16,-6,-30,-32,34,]),'NEG':([0,2,3,4,7,8,9,10,12,18,23,24,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,45,46,47,49,50,51,52,53,55,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,83,84,85,92,93,95,97,98,100,101,106,108,109,110,111,112,116,119,120,121,122,124,125,126,127,128,129,130,131,133,134,138,144,145,147,148,149,150,151,152,154,],[-5,35,-3,-4,-10,-11,-12,-13,35,35,-65,-25,-46,-72,-74,-76,-78,-79,-82,-84,35,-67,35,-8,-9,-22,35,35,-70,-18,35,-47,-81,-60,-83,35,35,35,35,-90,-91,-92,-93,-94,-95,-96,35,-97,-98,35,-99,-100,35,-101,-69,-66,-81,-68,35,-24,35,-21,35,35,-80,35,-26,35,-15,35,-71,-73,-75,-77,-70,-17,-20,-85,35,-52,-55,-59,-58,35,-27,-14,35,-7,-53,35,35,-19,-23,-54,-28,-16,-6,-30,-32,35,]),'SUB':([0,2,3,4,5,7,8,9,10,11,12,18,23,24,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,45,46,47,49,50,51,52,53,55,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,83,84,85,92,93,95,97,98,99,100,101,106,108,109,110,111,112,116,119,120,121,122,124,125,126,127,128,129,130,131,133,134,138,144,145,147,148,149,150,151,152,154,],[-5,37,-3,-4,-83,-10,-11,-12,-13,-81,37,37,-65,-25,-46,70,-74,-76,-78,-79,-82,-84,37,-67,37,-8,-9,-22,37,37,-70,-18,37,-47,-81,-60,-83,37,37,37,37,-90,-91,-92,-93,-94,-95,-96,37,-97,-98,37,-99,-100,37,-101,-69,-66,-81,-68,37,-24,37,-21,37,37,-80,37,-26,-81,37,-15,37,70,-73,-75,-77,-70,-17,-20,-85,37,-52,-55,-59,-58,37,-27,-14,37,-7,-53,37,37,-19,-23,-54,-28,-16,-6,-30,-32,37,]),';':([5,6,11,13,14,15,16,17,22,23,27,28,29,30,31,32,33,34,36,40,45,49,50,51,52,76,77,78,79,80,90,91,95,99,102,108,109,110,111,112,114,120,122,124,125,126,132,133,143,147,157,],[38,39,-81,-41,-42,-43,-44,-45,-64,-65,-46,-72,-74,-76,-78,-79,-82,-84,-67,-48,-70,-47,-81,-60,-83,-69,-66,-81,-68,-49,-61,-63,-80,-81,-62,-71,-73,-75,-77,-70,-56,-85,-52,-55,-59,-58,-57,-53,-51,-54,-50,]),'PRINT':([5,11,31,32,33,34,36,45,50,52,76,77,78,79,95,99,111,112,120,124,147,],[-83,-81,76,-79,-82,-84,-67,-70,-81,-83,-69,76,-81,76,-80,-81,76,-70,-85,-55,-54,]),'POW':([5,11,30,31,32,33,34,36,45,50,52,76,77,78,79,95,99,110,111,112,120,124,147,],[-83,-81,75,-78,-79,-82,-84,-67,-70,-81,-83,-69,-66,-81,-68,-80,-81,75,-77,-70,-85,-55,-54,]),'MUL':([5,11,29,30,31,32,33,34,36,45,50,52,76,77,78,79,95,99,109,110,111,112,120,124,147,],[-83,-81,72,-76,-78,-79,-82,-84,-67,-70,-81,-83,-69,-66,-81,-68,-80,-81,72,-75,-77,-70,-85,-55,-54,]),'DIV':([5,11,29,30,31,32,33,34,36,45,50,52,76,77,78,79,95,99,109,110,111,112,120,124,147,],[-83,-81,73,-76,-78,-79,-82,-84,-67,-70,-81,-83,-69,-66,-81,-68,-80,-81,73,-75,-77,-70,-85,-55,-54,]),'ADD':([5,11,28,29,30,31,32,33,34,36,45,50,52,76,77,78,79,95,99,108,109,110,111,112,120,124,147,],[-83,-81,69,-74,-76,-78,-79,-82,-84,-67,-70,-81,-83,-69,-66,-81,-68,-80,-81,69,-73,-75,-77,-70,-85,-55,-54,]),'AND':([5,11,23,28,29,30,31,32,33,34,36,45,50,52,76,77,78,79,95,99,108,109,110,111,112,120,124,147,],[-83,-81,61,-72,-74,-76,-78,-79,-82,-84,-67,-70,-81,-83,-69,-66,-81,-68,-80,-81,-71,-73,-75,-77,-70,-85,-55,-54,]),'OR':([5,11,23,28,29,30,31,32,33,34,36,45,50,52,76,77,78,79,95,99,108,109,110,111,112,120,124,147,],[-83,-81,62,-72,-74,-76,-78,-79,-82,-84,-67,-70,-81,-83,-69,-66,-81,-68,-80,-81,-71,-73,-75,-77,-70,-85,-55,-54,]),'LESSER':([5,11,23,28,29,30,31,32,33,34,36,45,50,52,76,77,78,79,95,99,108,109,110,111,112,120,124,147,],[-83,-81,63,-72,-74,-76,-78,-79,-82,-84,-67,-70,-81,-83,-69,-66,-81,-68,-80,-81,-71,-73,-75,-77,-70,-85,-55,-54,]),'GREATER':([5,11,23,28,29,30,31,32,33,34,36,45,50,52,76,77,78,79,95,99,108,109,110,111,112,120,124,147,],[-83,-81,64,-72,-74,-76,-78,-79,-82,-84,-67,-70,-81,-83,-69,-66,-81,-68,-80,-81,-71,-73,-75,-77,-70,-85,-55,-54,]),'LEQ':([5,11,23,28,29,30,31,32,33,34,36,45,50,52,76,77,78,79,95,99,108,109,110,111,112,120,124,147,],[-83,-81,65,-72,-74,-76,-78,-79,-82,-84,-67,-70,-81,-83,-69,-66,-81,-68,-80,-81,-71,-73,-75,-77,-70,-85,-55,-54,]),'GEQ':([5,11,23,28,29,30,31,32,33,34,36,45,50,52,76,77,78,79,95,99,108,109,110,111,112,120,124,147,],[-83,-81,66,-72,-74,-76,-78,-79,-82,-84,-67,-70,-81,-83,-69,-66,-81,-68,-80,-81,-71,-73,-75,-77,-70,-85,-55,-54,]),'EQUAL':([5,11,23,28,29,30,31,32,33,34,36,45,50,52,76,77,78,79,95,99,108,109,110,111,112,120,124,147,],[-83,-81,67,-72,-74,-76,-78,-79,-82,-84,-67,-70,-81,-83,-69,-66,-81,-68,-80,-81,-71,-73,-75,-77,-70,-85,-55,-54,]),'RARROW':([5,11,14,19,22,23,27,28,29,30,31,32,33,34,36,41,45,46,48,49,50,51,52,53,76,77,78,79,83,85,89,90,94,95,99,102,103,107,108,109,110,111,112,114,120,122,123,124,125,126,133,140,145,146,147,],[-83,-81,-47,54,-60,-65,-46,-72,-74,-76,-78,-79,-82,-84,-67,86,-70,-18,96,-47,-81,-60,-83,96,-69,-66,-81,-68,-24,117,96,96,96,-80,-81,-59,96,96,-71,-73,-75,-77,-70,96,-85,96,96,-55,-59,96,-53,96,-23,96,-54,]),'ELSE':([7,8,9,10,38,39,98,101,129,148,149,151,152,],[-10,-11,-12,-13,-8,-9,128,-15,-14,-28,-16,-30,-32,]),'}':([7,8,9,10,38,39,98,100,101,129,130,131,135,136,148,149,150,151,152,153,155,158,],[-10,-11,-12,-13,-8,-9,-26,129,-15,-14,149,-7,152,-38,-28,-16,-6,-30,-32,-37,-40,-39,]),':':([7,8,9,10,11,38,39,98,101,104,129,135,136,137,148,149,151,152,153,155,158,],[-10,-11,-12,-13,46,-8,-9,-26,-15,138,-14,138,-38,154,-28,-16,-30,-32,-37,-40,-39,]),'LARROW':([11,40,45,50,99,124,147,],[43,81,92,97,43,-55,-54,]),'SWAP':([11,99,],[44,44,]),'[':([11,40,45,50,78,80,99,102,112,124,125,133,143,147,157,],[47,82,93,47,47,113,47,47,93,-55,47,93,-51,-54,-50,]),')':([23,27,28,29,30,31,32,33,34,36,42,45,48,49,50,51,52,76,77,78,79,87,88,89,95,103,107,108,109,110,111,112,120,122,124,125,126,133,140,146,147,],[-65,-46,-72,-74,-76,-78,-79,-82,-84,-67,-87,-70,95,-47,-81,-60,-83,-69,-66,-81,-68,120,-86,-89,-80,134,141,-71,-73,-75,-77,-70,-85,-52,-55,-59,-58,-53,156,-88,-54,]),'{':([23,27,28,29,30,31,32,33,34,36,41,45,46,49,50,51,52,53,56,57,76,77,78,79,83,84,85,95,108,109,110,111,112,119,120,122,124,125,126,127,128,133,134,138,139,141,144,145,147,154,156,],[-65,-46,-72,-74,-76,-78,-79,-82,-84,-67,-22,-70,-18,-47,-81,-60,-83,100,104,-34,-69,-66,-81,-68,-24,100,-21,-80,-71,-73,-75,-77,-70,-20,-85,-52,-55,-59,-58,100,-27,-53,100,100,-33,-36,-19,-23,-54,100,-35,]),',':([23,27,28,29,30,31,32,33,34,36,45,49,50,51,52,56,57,76,77,78,79,83,85,88,89,95,108,109,110,111,112,120,122,124,125,126,133,139,141,145,146,147,156,],[-65,-46,-72,-74,-76,-78,-79,-82,-84,-67,-70,-47,-81,-60,-83,105,-34,-69,-66,-81,-68,-24,118,121,-89,-80,-71,-73,-75,-77,-70,-85,-52,-55,-59,-58,-53,-33,-36,-23,-88,-54,-35,]),']':([23,27,28,29,30,31,32,33,34,36,45,49,50,51,52,76,77,78,79,94,95,108,109,110,111,112,115,120,122,123,124,125,126,133,142,147,],[-65,-46,-72,-74,-76,-78,-79,-82,-84,-67,-70,-47,-81,-60,-83,-69,-66,-81,-68,124,-80,-71,-73,-75,-77,-70,143,-85,-52,147,-55,-59,-58,-53,157,-54,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Start':([0,],[1,]),'Axiom':([0,],[2,]),'Block':([2,53,84,100,127,130,134,138,154,],[3,101,101,131,101,150,101,101,101,]),'Function':([2,],[4,]),'FunCall':([2,12,18,35,37,42,43,47,53,55,59,60,68,71,74,81,84,92,93,97,100,106,121,127,130,134,138,154,],[5,52,52,52,52,52,52,52,5,52,52,52,52,52,52,52,5,52,52,52,5,52,52,5,5,5,5,5,]),'Exp':([2,53,84,100,127,130,134,138,154,],[6,6,6,6,6,6,6,6,6,]),'If':([2,53,84,100,127,130,134,138,154,],[7,7,7,7,7,7,7,7,7,]),'IfElse':([2,53,84,100,127,130,134,138,154,],[8,8,8,8,8,8,8,8,8,]),'While':([2,53,84,100,127,130,134,138,154,],[9,9,9,9,9,9,9,9,9,]),'Switch':([2,53,84,100,127,130,134,138,154,],[10,10,10,10,10,10,10,10,10,]),'Atrib':([2,53,84,100,127,130,134,138,154,],[13,13,13,13,13,13,13,13,13,]),'Op':([2,12,18,42,43,47,53,55,59,81,84,92,93,97,100,106,121,127,130,134,138,154,],[14,49,49,49,49,49,14,49,49,49,14,49,49,49,14,49,49,14,14,14,14,14,]),'Decl':([2,53,84,100,127,130,134,138,154,],[15,15,15,15,15,15,15,15,15,]),'DeclArray':([2,53,84,100,127,130,134,138,154,],[16,16,16,16,16,16,16,16,16,]),'DeclAtrib':([2,53,84,100,127,130,134,138,154,],[17,17,17,17,17,17,17,17,17,]),'IfScope':([2,53,84,100,127,130,134,138,154,],[18,18,18,18,18,18,18,18,18,]),'AtribOp':([2,12,18,42,43,47,53,55,59,81,84,92,93,97,100,106,121,127,130,134,138,154,],[19,48,53,89,90,94,19,103,107,114,19,122,123,126,19,140,146,19,19,19,19,19,]),'WhileScope':([2,53,84,100,127,130,134,138,154,],[20,20,20,20,20,20,20,20,20,]),'SwitchScope':([2,53,84,100,127,130,134,138,154,],[21,21,21,21,21,21,21,21,21,]),'AtribArray':([2,12,18,42,43,47,53,55,59,81,84,92,93,97,100,106,121,127,130,134,138,154,],[22,51,51,51,51,51,22,51,51,51,22,51,51,51,22,51,51,22,22,22,22,22,]),'OpBin':([2,12,18,42,43,47,53,55,59,81,84,92,93,97,100,106,121,127,130,134,138,154,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'AtribNum':([2,12,18,42,43,47,53,55,59,81,84,92,93,97,100,106,121,127,130,134,138,154,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'TermPlus':([2,12,18,42,43,47,53,55,59,60,81,84,92,93,97,100,106,121,127,130,134,138,154,],[28,28,28,28,28,28,28,28,28,108,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'TermMult':([2,12,18,42,43,47,53,55,59,60,68,81,84,92,93,97,100,106,121,127,130,134,138,154,],[29,29,29,29,29,29,29,29,29,29,109,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'TermPow':([2,12,18,42,43,47,53,55,59,60,68,71,81,84,92,93,97,100,106,121,127,130,134,138,154,],[30,30,30,30,30,30,30,30,30,30,30,110,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'Base':([2,12,18,35,37,42,43,47,53,55,59,60,68,71,74,81,84,92,93,97,100,106,121,127,130,134,138,154,],[31,31,31,77,79,31,31,31,31,31,31,31,31,31,111,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'OpUno':([2,12,18,35,37,42,43,47,53,55,59,60,68,71,74,81,84,92,93,97,100,106,121,127,130,134,138,154,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'AccessArray':([2,12,18,35,37,42,43,47,53,55,59,60,68,71,74,81,84,92,93,97,100,106,121,127,130,134,138,154,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'FunScope':([11,],[41,]),'ArraySize':([11,50,78,99,102,125,],[45,45,112,45,133,133,]),'Conds':([21,],[56,]),'Cond':([21,105,],[57,139,]),'OpLogico':([23,],[60,]),'OpPlus':([28,108,],[68,68,]),'OpMult':([29,109,],[71,71,]),'OpPow':([30,110,],[74,74,]),'DeclArraySize':([40,],[80,]),'FunCases':([41,],[84,]),'FunExtra':([41,],[85,]),'FunArg':([42,],[87,]),'FunRec':([42,],[88,]),'Body':([53,84,127,134,138,154,],[98,116,148,151,155,158,]),'ElseScope':([98,],[127,]),'Code':([100,],[130,]),'Cases':([104,],[135,]),'Case':([104,135,],[136,153,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Start","S'",1,None,None,None),
  ('Start -> Axiom','Start',1,'p_start_axiom','yacc.py',11),
  ('Start -> <empty>','Start',0,'p_start_empty','yacc.py',17),
  ('Axiom -> Axiom Block','Axiom',2,'p_axiom_code','yacc.py',22),
  ('Axiom -> Axiom Function','Axiom',2,'p_axiom_function','yacc.py',28),
  ('Axiom -> <empty>','Axiom',0,'p_axiom_empty','yacc.py',34),
  ('Code -> Code Block','Code',2,'p_code_block','yacc.py',39),
  ('Code -> Block','Code',1,'p_code_empty','yacc.py',44),
  ('Block -> FunCall ;','Block',2,'p_block_funcall','yacc.py',49),
  ('Block -> Exp ;','Block',2,'p_block_exp','yacc.py',57),
  ('Block -> If','Block',1,'p_block_if','yacc.py',62),
  ('Block -> IfElse','Block',1,'p_block_ifelse','yacc.py',67),
  ('Block -> While','Block',1,'p_block_while','yacc.py',72),
  ('Block -> Switch','Block',1,'p_block_switch','yacc.py',77),
  ('Body -> { }','Body',2,'p_body_empty','yacc.py',86),
  ('Body -> Block','Body',1,'p_body_block','yacc.py',91),
  ('Body -> { Code }','Body',3,'p_body_code','yacc.py',96),
  ('Function -> ID FunScope FunCases Body','Function',4,'p_function','yacc.py',101),
  ('FunScope -> :','FunScope',1,'p_funscope','yacc.py',130),
  ('FunCases -> FunExtra RARROW ID','FunCases',3,'p_funcases_funextra_rarrow','yacc.py',136),
  ('FunCases -> RARROW ID','FunCases',2,'p_funcases_rarrow','yacc.py',156),
  ('FunCases -> FunExtra','FunCases',1,'p_funcases_funextra','yacc.py',166),
  ('FunCases -> <empty>','FunCases',0,'p_funcases_empty','yacc.py',180),
  ('FunExtra -> FunExtra , ID','FunExtra',3,'p_funextra_rec','yacc.py',185),
  ('FunExtra -> ID','FunExtra',1,'p_funextra_empty','yacc.py',191),
  ('IfScope -> IF','IfScope',1,'p_if_scope','yacc.py',196),
  ('If -> IfScope AtribOp Body','If',3,'p_if','yacc.py',202),
  ('ElseScope -> ELSE','ElseScope',1,'p_else_scope','yacc.py',214),
  ('IfElse -> IfScope AtribOp Body ElseScope Body','IfElse',5,'p_ifelse','yacc.py',222),
  ('WhileScope -> WHILE','WhileScope',1,'p_while_scope','yacc.py',237),
  ('While -> WhileScope ( AtribOp ) Body','While',5,'p_while','yacc.py',243),
  ('SwitchScope -> SWITCH','SwitchScope',1,'p_switch_scope','yacc.py',258),
  ('Switch -> SwitchScope Conds { Cases }','Switch',5,'p_switch','yacc.py',270),
  ('Conds -> Conds , Cond','Conds',3,'p_conds_rec','yacc.py',310),
  ('Conds -> Cond','Conds',1,'p_conds_base','yacc.py',316),
  ('Cond -> ID ( AtribOp )','Cond',4,'p_cond_id','yacc.py',321),
  ('Cond -> ( AtribOp )','Cond',3,'p_cond_empty','yacc.py',327),
  ('Cases -> Cases Case','Cases',2,'p_cases_rec','yacc.py',333),
  ('Cases -> Case','Cases',1,'p_cases_base','yacc.py',339),
  ('Case -> ID : Body','Case',3,'p_case_id','yacc.py',344),
  ('Case -> : Body','Case',2,'p_case_empty','yacc.py',351),
  ('Exp -> Atrib','Exp',1,'p_exp_atrib','yacc.py',366),
  ('Exp -> Op','Exp',1,'p_exp_op','yacc.py',371),
  ('Exp -> Decl','Exp',1,'p_exp_decl','yacc.py',376),
  ('Exp -> DeclArray','Exp',1,'p_exp_declarray','yacc.py',381),
  ('Exp -> DeclAtrib','Exp',1,'p_exp_declatrib','yacc.py',386),
  ('AtribOp -> AtribNum','AtribOp',1,'p_atribop_atribnum','yacc.py',391),
  ('AtribOp -> Op','AtribOp',1,'p_atribop_op','yacc.py',396),
  ('Decl -> ID ID','Decl',2,'p_decl','yacc.py',401),
  ('DeclArray -> ID ID DeclArraySize','DeclArray',3,'p_declarray','yacc.py',424),
  ('DeclArraySize -> DeclArraySize [ NUM ]','DeclArraySize',4,'p_declarraysize_rec','yacc.py',448),
  ('DeclArraySize -> [ NUM ]','DeclArraySize',3,'p_declarraysize_empty','yacc.py',454),
  ('AtribArray -> ID ArraySize LARROW AtribOp','AtribArray',4,'p_atribarray_Leftatribop','yacc.py',459),
  ('AtribArray -> AtribOp RARROW ID ArraySize','AtribArray',4,'p_atribarray_Rightatribop','yacc.py',494),
  ('ArraySize -> ArraySize [ AtribOp ]','ArraySize',4,'p_arraysize_rec','yacc.py',522),
  ('ArraySize -> [ AtribOp ]','ArraySize',3,'p_arraysize_empty','yacc.py',527),
  ('DeclAtrib -> ID ID LARROW AtribOp','DeclAtrib',4,'p_declatrib_left','yacc.py',532),
  ('DeclAtrib -> AtribOp RARROW ID ID','DeclAtrib',4,'p_declatrib_right','yacc.py',553),
  ('AtribNum -> ID LARROW AtribOp','AtribNum',3,'p_atribnum_left','yacc.py',574),
  ('AtribNum -> AtribOp RARROW ID','AtribNum',3,'p_atribnum_right','yacc.py',579),
  ('AtribNum -> AtribArray','AtribNum',1,'p_atribnum_array','yacc.py',585),
  ('Atrib -> ID LARROW AtribOp','Atrib',3,'p_atrib_left','yacc.py',590),
  ('Atrib -> AtribOp RARROW ID','Atrib',3,'p_atrib_right','yacc.py',595),
  ('Atrib -> ID SWAP ID','Atrib',3,'p_atrib_equiv','yacc.py',600),
  ('Atrib -> AtribArray','Atrib',1,'p_atrib_array','yacc.py',625),
  ('Op -> OpBin','Op',1,'p_op_opbin','yacc.py',635),
  ('OpUno -> NEG Base','OpUno',2,'p_opuno_neg','yacc.py',640),
  ('OpUno -> AccessArray','OpUno',1,'p_opuno_accessarray','yacc.py',645),
  ('OpUno -> SUB Base','OpUno',2,'p_opuno_minus','yacc.py',650),
  ('OpUno -> Base PRINT','OpUno',2,'p_opuno_print','yacc.py',655),
  ('AccessArray -> ID ArraySize','AccessArray',2,'p_accessarray','yacc.py',661),
  ('OpBin -> OpBin OpLogico TermPlus','OpBin',3,'p_opbin_rec','yacc.py',676),
  ('OpBin -> TermPlus','OpBin',1,'p_opbin_base','yacc.py',681),
  ('TermPlus -> TermPlus OpPlus TermMult','TermPlus',3,'p_termplus_rec','yacc.py',686),
  ('TermPlus -> TermMult','TermPlus',1,'p_termplus_base','yacc.py',691),
  ('TermMult -> TermMult OpMult TermPow','TermMult',3,'p_termmult_rec','yacc.py',696),
  ('TermMult -> TermPow','TermMult',1,'p_termmult_base','yacc.py',701),
  ('TermPow -> TermPow OpPow Base','TermPow',3,'p_termpow_rec','yacc.py',706),
  ('TermPow -> Base','TermPow',1,'p_termpow_base','yacc.py',711),
  ('Base -> OpUno','Base',1,'p_base_opuno','yacc.py',716),
  ('Base -> ( AtribOp )','Base',3,'p_base_exp','yacc.py',721),
  ('Base -> ID','Base',1,'p_base_id','yacc.py',726),
  ('Base -> NUM','Base',1,'p_base_num','yacc.py',739),
  ('Base -> FunCall','Base',1,'p_base_funcall','yacc.py',744),
  ('Base -> READ','Base',1,'p_base_read','yacc.py',754),
  ('FunCall -> ID ( FunArg )','FunCall',4,'p_funcall','yacc.py',759),
  ('FunArg -> FunRec','FunArg',1,'p_funarg_funrec','yacc.py',780),
  ('FunArg -> <empty>','FunArg',0,'p_funarg_empty','yacc.py',785),
  ('FunRec -> FunRec , AtribOp','FunRec',3,'p_funrec_rec','yacc.py',790),
  ('FunRec -> AtribOp','FunRec',1,'p_funrec_base','yacc.py',796),
  ('OpLogico -> AND','OpLogico',1,'p_oplogico_and','yacc.py',801),
  ('OpLogico -> OR','OpLogico',1,'p_oplogico_or','yacc.py',806),
  ('OpLogico -> LESSER','OpLogico',1,'p_oplogico_lesser','yacc.py',811),
  ('OpLogico -> GREATER','OpLogico',1,'p_oplogico_greater','yacc.py',816),
  ('OpLogico -> LEQ','OpLogico',1,'p_oplogico_leq','yacc.py',821),
  ('OpLogico -> GEQ','OpLogico',1,'p_oplogico_geq','yacc.py',826),
  ('OpLogico -> EQUAL','OpLogico',1,'p_oplogico_equal','yacc.py',831),
  ('OpPlus -> ADD','OpPlus',1,'p_opplus_add','yacc.py',836),
  ('OpPlus -> SUB','OpPlus',1,'p_opplus_sub','yacc.py',841),
  ('OpMult -> MUL','OpMult',1,'p_opmult_mul','yacc.py',846),
  ('OpMult -> DIV','OpMult',1,'p_opmult_div','yacc.py',851),
  ('OpPow -> POW','OpPow',1,'p_oppow','yacc.py',856),
]
