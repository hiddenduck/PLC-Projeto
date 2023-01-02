
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ADD AND DIV ELSE EQUAL GEQ GREATER ID IF LARROW LEQ LESSER MUL NEG NUM OR POW RARROW SUB SWAP SWITCH WHILEStart : AxiomAxiom : Axiom CodeAxiom : Axiom FunctionAxiom : Code : Code BlockCode : BlockBlock : Exp ';'Block : If Block : IfElse Block : While Block : Switch Body : '{' '}'Body : BlockBody : '{' Code '}'Function : ID FunScope FunCases BodyFunScope : ':'FunCases : FunExtra RARROW IDFunCases : RARROW IDFunCases : FunExtraFunCases : FunExtra : FunExtra ',' IDFunExtra : IDIfScope : IFIf : IfScope AtribOp BodyElseScope : ELSEIfElse : IfScope AtribOp Body ElseScope BodyWhileScope : WHILEWhile : WhileScope '(' AtribOp ')' BodySwitchScope : SWITCHSwitch : SwitchScope Conds '{' Cases '}'Conds : Conds ',' CondConds : CondCond : ID '(' AtribOp ')'Cond : '(' AtribOp ')'Cases : Cases Case Cases : CaseCase : ID ':' BodyCase : ':' BodyExp : AtribExp : OpExp : DeclExp : DeclArrayExp : DeclAtribAtribOp : AtribNumAtribOp : OpDecl : ID IDDeclArray : ID ID DeclArraySizeDeclArraySize : DeclArraySize '[' NUM ']'DeclArraySize : AtribArray : ID ArraySize LARROW AtribOpAtribArray : AtribOp RARROW ID ArraySizeArraySize : ArraySize '[' AtribOp ']'ArraySize : '[' AtribOp ']'DeclAtrib : ID ID LARROW AtribOpDeclAtrib : AtribOp RARROW ID IDAtribNum : ID LARROW AtribOpAtribNum : AtribOp RARROW IDAtribNum : AtribArrayAtrib : ID LARROW AtribOpAtrib : AtribOp RARROW IDAtrib : ID SWAP IDAtrib : AtribArrayOp : OpUnoOp : OpBinOpUno : NEG AtribOpOpUno : AccessArrayOpUno : SUB AtribOpOpUno : '?' AtribOpAccessArray : ID ArraySizeOpBin : OpBin OpLogico TermPlusOpBin : TermPlusTermPlus : TermPlus OpPlus TermMultTermPlus : TermMultTermMult : TermMult OpMult TermPowTermMult : TermPowTermPow : TermPow OpPow BaseTermPow : BaseBase : '(' AtribOp ')'Base : IDBase : NUMBase : FunCallBase : '¿'FunCall : ID '(' FunArg ')'FunArg : FunRecFunArg : FunRec : FunRec ',' AtribOpFunRec : AtribOpOpLogico : ANDOpLogico : OROpLogico : LESSEROpLogico : GREATEROpLogico : LEQOpLogico : GEQOpLogico : EQUALOpPlus : ADDOpPlus : SUBOpMult : MULOpMult : DIVOpPow : POW"
    
_lr_action_items = {'ID':([0,2,3,4,5,6,8,9,10,11,17,20,21,23,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,84,85,86,89,90,95,96,97,98,99,100,102,103,104,105,107,108,109,110,111,114,115,116,117,118,120,121,122,123,124,125,126,127,128,130,131,132,133,135,140,141,142,144,145,146,147,148,149,150,153,],[-4,6,41,-3,-6,42,-8,-9,-10,-11,53,53,60,-63,-64,-23,-29,-44,53,-66,53,53,-71,-73,-75,-77,-80,-81,-82,-5,42,83,53,88,-69,53,-16,53,-7,41,-45,-79,-58,100,53,53,108,-88,-89,-90,-91,-92,-93,-94,-65,-67,-68,108,-95,-96,108,-97,-98,108,-99,53,-22,41,-19,117,53,53,-24,125,41,-13,53,129,-78,134,60,53,-70,-79,-72,-74,-76,-15,140,141,-18,-50,-83,53,-53,41,-25,-57,-12,41,-56,-51,41,134,-36,41,-17,-21,-52,-26,-14,-28,-30,-35,41,-38,-37,]),'IF':([0,2,3,4,5,8,9,10,11,23,24,28,30,33,34,35,36,37,38,39,40,43,46,48,50,51,52,53,54,70,71,72,83,84,85,95,97,98,102,107,108,109,110,111,114,117,118,120,122,123,124,125,126,127,128,130,131,135,140,141,142,144,145,146,147,149,],[-4,25,25,-3,-6,-8,-9,-10,-11,-63,-64,-44,-66,-71,-73,-75,-77,-80,-81,-82,-5,-20,-69,-16,-7,25,-45,-79,-58,-65,-67,-68,-22,25,-19,-24,25,-13,-78,-70,-79,-72,-74,-76,-15,-18,-50,-83,-53,25,-25,-57,-12,25,-56,-51,25,25,-17,-21,-52,-26,-14,-28,-30,25,]),'WHILE':([0,2,3,4,5,8,9,10,11,23,24,28,30,33,34,35,36,37,38,39,40,43,46,48,50,51,52,53,54,70,71,72,83,84,85,95,97,98,102,107,108,109,110,111,114,117,118,120,122,123,124,125,126,127,128,130,131,135,140,141,142,144,145,146,147,149,],[-4,26,26,-3,-6,-8,-9,-10,-11,-63,-64,-44,-66,-71,-73,-75,-77,-80,-81,-82,-5,-20,-69,-16,-7,26,-45,-79,-58,-65,-67,-68,-22,26,-19,-24,26,-13,-78,-70,-79,-72,-74,-76,-15,-18,-50,-83,-53,26,-25,-57,-12,26,-56,-51,26,26,-17,-21,-52,-26,-14,-28,-30,26,]),'SWITCH':([0,2,3,4,5,8,9,10,11,23,24,28,30,33,34,35,36,37,38,39,40,43,46,48,50,51,52,53,54,70,71,72,83,84,85,95,97,98,102,107,108,109,110,111,114,117,118,120,122,123,124,125,126,127,128,130,131,135,140,141,142,144,145,146,147,149,],[-4,27,27,-3,-6,-8,-9,-10,-11,-63,-64,-44,-66,-71,-73,-75,-77,-80,-81,-82,-5,-20,-69,-16,-7,27,-45,-79,-58,-65,-67,-68,-22,27,-19,-24,27,-13,-78,-70,-79,-72,-74,-76,-15,-18,-50,-83,-53,27,-25,-57,-12,27,-56,-51,27,27,-17,-21,-52,-26,-14,-28,-30,27,]),'NEG':([0,2,3,4,5,8,9,10,11,17,20,23,24,25,28,29,30,31,32,33,34,35,36,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,56,61,70,71,72,82,83,84,85,89,90,95,97,98,99,102,105,107,108,109,110,111,114,117,118,120,121,122,123,124,125,126,127,128,130,131,135,140,141,142,144,145,146,147,149,],[-4,29,29,-3,-6,-8,-9,-10,-11,29,29,-63,-64,-23,-44,29,-66,29,29,-71,-73,-75,-77,-80,-81,-82,-5,-20,29,-69,29,-16,29,-7,29,-45,-79,-58,29,29,-65,-67,-68,29,-22,29,-19,29,29,-24,29,-13,29,-78,29,-70,-79,-72,-74,-76,-15,-18,-50,-83,29,-53,29,-25,-57,-12,29,-56,-51,29,29,-17,-21,-52,-26,-14,-28,-30,29,]),'SUB':([0,2,3,4,5,6,8,9,10,11,17,20,23,24,25,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,46,47,48,49,50,51,52,53,54,56,61,70,71,72,82,83,84,85,89,90,95,97,98,99,102,105,107,108,109,110,111,114,117,118,120,121,122,123,124,125,126,127,128,130,131,135,140,141,142,144,145,146,147,149,],[-4,31,31,-3,-6,-79,-8,-9,-10,-11,31,31,-63,-64,-23,-44,31,-66,31,31,75,-73,-75,-77,-80,-81,-82,-5,-79,-20,31,-69,31,-16,31,-7,31,-45,-79,-58,31,31,-65,-67,-68,31,-22,31,-19,31,31,-24,31,-13,31,-78,31,75,-79,-72,-74,-76,-15,-18,-50,-83,31,-53,31,-25,-57,-12,31,-56,-51,31,31,-17,-21,-52,-26,-14,-28,-30,31,]),'?':([0,2,3,4,5,8,9,10,11,17,20,23,24,25,28,29,30,31,32,33,34,35,36,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,56,61,70,71,72,82,83,84,85,89,90,95,97,98,99,102,105,107,108,109,110,111,114,117,118,120,121,122,123,124,125,126,127,128,130,131,135,140,141,142,144,145,146,147,149,],[-4,32,32,-3,-6,-8,-9,-10,-11,32,32,-63,-64,-23,-44,32,-66,32,32,-71,-73,-75,-77,-80,-81,-82,-5,-20,32,-69,32,-16,32,-7,32,-45,-79,-58,32,32,-65,-67,-68,32,-22,32,-19,32,32,-24,32,-13,32,-78,32,-70,-79,-72,-74,-76,-15,-18,-50,-83,32,-53,32,-25,-57,-12,32,-56,-51,32,32,-17,-21,-52,-26,-14,-28,-30,32,]),'(':([0,2,3,4,5,6,8,9,10,11,17,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,46,47,48,49,50,51,52,53,54,56,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,84,85,89,90,95,97,98,99,102,104,105,107,108,109,110,111,114,117,118,120,121,122,123,124,125,126,127,128,130,131,135,140,141,142,144,145,146,147,149,],[-4,20,20,-3,-6,47,-8,-9,-10,-11,20,56,20,61,-63,-64,-23,-27,-29,-44,20,-66,20,20,-71,-73,-75,-77,-80,-81,-82,-5,47,-20,20,-69,20,-16,20,-7,20,-45,47,-58,20,105,20,20,-88,-89,-90,-91,-92,-93,-94,-65,-67,-68,20,-95,-96,20,-97,-98,20,-99,20,-22,20,-19,20,20,-24,20,-13,20,-78,61,20,-70,47,-72,-74,-76,-15,-18,-50,-83,20,-53,20,-25,-57,-12,20,-56,-51,20,20,-17,-21,-52,-26,-14,-28,-30,20,]),'NUM':([0,2,3,4,5,8,9,10,11,17,20,23,24,25,28,29,30,31,32,33,34,35,36,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,56,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,84,85,89,90,95,97,98,99,102,105,107,108,109,110,111,112,114,117,118,120,121,122,123,124,125,126,127,128,130,131,135,140,141,142,144,145,146,147,149,],[-4,37,37,-3,-6,-8,-9,-10,-11,37,37,-63,-64,-23,-44,37,-66,37,37,-71,-73,-75,-77,-80,-81,-82,-5,-20,37,-69,37,-16,37,-7,37,-45,-79,-58,37,37,37,-88,-89,-90,-91,-92,-93,-94,-65,-67,-68,37,-95,-96,37,-97,-98,37,-99,37,-22,37,-19,37,37,-24,37,-13,37,-78,37,-70,-79,-72,-74,-76,139,-15,-18,-50,-83,37,-53,37,-25,-57,-12,37,-56,-51,37,37,-17,-21,-52,-26,-14,-28,-30,37,]),'�':([0,2,3,4,5,8,9,10,11,17,20,23,24,25,28,29,30,31,32,33,34,35,36,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,56,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,84,85,89,90,95,97,98,99,102,105,107,108,109,110,111,114,117,118,120,121,122,123,124,125,126,127,128,130,131,135,140,141,142,144,145,146,147,149,],[-4,39,39,-3,-6,-8,-9,-10,-11,39,39,-63,-64,-23,-44,39,-66,39,39,-71,-73,-75,-77,-80,-81,-82,-5,-20,39,-69,39,-16,39,-7,39,-45,-79,-58,39,39,39,-88,-89,-90,-91,-92,-93,-94,-65,-67,-68,39,-95,-96,39,-97,-98,39,-99,39,-22,39,-19,39,39,-24,39,-13,39,-78,39,-70,-79,-72,-74,-76,-15,-18,-50,-83,39,-53,39,-25,-57,-12,39,-56,-51,39,39,-17,-21,-52,-26,-14,-28,-30,39,]),'$end':([0,1,2,3,4,5,8,9,10,11,40,50,95,98,114,126,144,145,146,147,],[-4,0,-1,-2,-3,-6,-8,-9,-10,-11,-5,-7,-24,-13,-15,-12,-26,-14,-28,-30,]),'}':([5,8,9,10,11,40,50,95,97,98,126,127,132,133,144,145,146,147,148,150,153,],[-6,-8,-9,-10,-11,-5,-7,-24,126,-13,-12,145,147,-36,-26,-14,-28,-30,-35,-38,-37,]),'LARROW':([6,41,42,46,53,122,142,],[44,44,82,89,99,-53,-52,]),'SWAP':([6,41,],[45,45,]),'POW':([6,35,36,37,38,39,41,53,102,108,110,111,120,],[-79,80,-77,-80,-81,-82,-79,-79,-78,-79,80,-76,-83,]),'MUL':([6,34,35,36,37,38,39,41,53,102,108,109,110,111,120,],[-79,77,-75,-77,-80,-81,-82,-79,-79,-78,-79,77,-74,-76,-83,]),'DIV':([6,34,35,36,37,38,39,41,53,102,108,109,110,111,120,],[-79,78,-75,-77,-80,-81,-82,-79,-79,-78,-79,78,-74,-76,-83,]),'ADD':([6,33,34,35,36,37,38,39,41,53,102,107,108,109,110,111,120,],[-79,74,-73,-75,-77,-80,-81,-82,-79,-79,-78,74,-79,-72,-74,-76,-83,]),'AND':([6,24,33,34,35,36,37,38,39,41,53,102,107,108,109,110,111,120,],[-79,63,-71,-73,-75,-77,-80,-81,-82,-79,-79,-78,-70,-79,-72,-74,-76,-83,]),'OR':([6,24,33,34,35,36,37,38,39,41,53,102,107,108,109,110,111,120,],[-79,64,-71,-73,-75,-77,-80,-81,-82,-79,-79,-78,-70,-79,-72,-74,-76,-83,]),'LESSER':([6,24,33,34,35,36,37,38,39,41,53,102,107,108,109,110,111,120,],[-79,65,-71,-73,-75,-77,-80,-81,-82,-79,-79,-78,-70,-79,-72,-74,-76,-83,]),'GREATER':([6,24,33,34,35,36,37,38,39,41,53,102,107,108,109,110,111,120,],[-79,66,-71,-73,-75,-77,-80,-81,-82,-79,-79,-78,-70,-79,-72,-74,-76,-83,]),'LEQ':([6,24,33,34,35,36,37,38,39,41,53,102,107,108,109,110,111,120,],[-79,67,-71,-73,-75,-77,-80,-81,-82,-79,-79,-78,-70,-79,-72,-74,-76,-83,]),'GEQ':([6,24,33,34,35,36,37,38,39,41,53,102,107,108,109,110,111,120,],[-79,68,-71,-73,-75,-77,-80,-81,-82,-79,-79,-78,-70,-79,-72,-74,-76,-83,]),'EQUAL':([6,24,33,34,35,36,37,38,39,41,53,102,107,108,109,110,111,120,],[-79,69,-71,-73,-75,-77,-80,-81,-82,-79,-79,-78,-70,-79,-72,-74,-76,-83,]),';':([6,7,12,13,14,15,16,22,23,24,28,30,33,34,35,36,37,38,39,41,42,46,52,53,54,70,71,72,81,87,88,100,102,107,108,109,110,111,113,118,120,122,125,128,129,130,142,152,],[-79,50,-39,-40,-41,-42,-43,-62,-63,-64,-44,-66,-71,-73,-75,-77,-80,-81,-82,-79,-46,-69,-45,-79,-58,-65,-67,-68,-47,-59,-61,-60,-78,-70,-79,-72,-74,-76,-54,-50,-83,-53,-57,-56,-55,-51,-52,-48,]),'RARROW':([6,13,18,22,23,24,28,30,33,34,35,36,37,38,39,41,43,46,48,51,52,53,54,57,70,71,72,83,85,87,93,94,100,101,102,106,107,108,109,110,111,113,118,119,120,122,125,128,130,137,141,142,143,],[-79,-45,55,-58,-63,-64,-44,-66,-71,-73,-75,-77,-80,-81,-82,-79,86,-69,-16,96,-45,-79,-58,96,96,96,96,-22,115,96,96,96,-57,96,-78,96,-70,-79,-72,-74,-76,96,96,96,-83,-53,-57,96,-51,96,-21,-52,96,]),':':([6,8,9,10,11,50,95,98,103,126,132,133,134,144,145,146,147,148,150,153,],[48,-8,-9,-10,-11,-7,-24,-13,135,-12,135,-36,149,-26,-14,-28,-30,-35,-38,-37,]),'[':([6,41,42,46,53,81,100,122,125,130,142,152,],[49,49,-49,90,49,112,49,-53,49,90,-52,-48,]),'ELSE':([8,9,10,11,50,95,98,126,144,145,146,147,],[-8,-9,-10,-11,-7,124,-13,-12,-26,-14,-28,-30,]),'{':([23,24,28,30,33,34,35,36,37,38,39,43,46,48,51,52,53,54,58,59,70,71,72,83,84,85,102,107,108,109,110,111,117,118,120,122,123,124,125,128,130,131,135,136,138,140,141,142,149,151,],[-63,-64,-44,-66,-71,-73,-75,-77,-80,-81,-82,-20,-69,-16,97,-45,-79,-58,103,-32,-65,-67,-68,-22,97,-19,-78,-70,-79,-72,-74,-76,-18,-50,-83,-53,97,-25,-57,-56,-51,97,97,-31,-34,-17,-21,-52,97,-33,]),')':([23,24,28,30,33,34,35,36,37,38,39,46,47,52,53,54,57,70,71,72,91,92,93,101,102,106,107,108,109,110,111,118,120,122,125,128,130,137,142,143,],[-63,-64,-44,-66,-71,-73,-75,-77,-80,-81,-82,-69,-85,-45,-79,-58,102,-65,-67,-68,120,-84,-87,131,-78,138,-70,-79,-72,-74,-76,-50,-83,-53,-57,-56,-51,151,-52,-86,]),',':([23,24,28,30,33,34,35,36,37,38,39,46,52,53,54,58,59,70,71,72,83,85,92,93,102,107,108,109,110,111,118,120,122,125,128,130,136,138,141,142,143,151,],[-63,-64,-44,-66,-71,-73,-75,-77,-80,-81,-82,-69,-45,-79,-58,104,-32,-65,-67,-68,-22,116,121,-87,-78,-70,-79,-72,-74,-76,-50,-83,-53,-57,-56,-51,-31,-34,-21,-52,-86,-33,]),']':([23,24,28,30,33,34,35,36,37,38,39,46,52,53,54,70,71,72,94,102,107,108,109,110,111,118,119,120,122,125,128,130,139,142,],[-63,-64,-44,-66,-71,-73,-75,-77,-80,-81,-82,-69,-45,-79,-58,-65,-67,-68,122,-78,-70,-79,-72,-74,-76,-50,142,-83,-53,-57,-56,-51,152,-52,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Start':([0,],[1,]),'Axiom':([0,],[2,]),'Code':([2,97,],[3,127,]),'Function':([2,],[4,]),'Block':([2,3,51,84,97,123,127,131,135,149,],[5,40,98,98,5,98,40,98,98,98,]),'Exp':([2,3,51,84,97,123,127,131,135,149,],[7,7,7,7,7,7,7,7,7,7,]),'If':([2,3,51,84,97,123,127,131,135,149,],[8,8,8,8,8,8,8,8,8,8,]),'IfElse':([2,3,51,84,97,123,127,131,135,149,],[9,9,9,9,9,9,9,9,9,9,]),'While':([2,3,51,84,97,123,127,131,135,149,],[10,10,10,10,10,10,10,10,10,10,]),'Switch':([2,3,51,84,97,123,127,131,135,149,],[11,11,11,11,11,11,11,11,11,11,]),'Atrib':([2,3,51,84,97,123,127,131,135,149,],[12,12,12,12,12,12,12,12,12,12,]),'Op':([2,3,17,20,29,31,32,44,47,49,51,56,61,82,84,89,90,97,99,105,121,123,127,131,135,149,],[13,13,52,52,52,52,52,52,52,52,13,52,52,52,13,52,52,13,52,52,52,13,13,13,13,13,]),'Decl':([2,3,51,84,97,123,127,131,135,149,],[14,14,14,14,14,14,14,14,14,14,]),'DeclArray':([2,3,51,84,97,123,127,131,135,149,],[15,15,15,15,15,15,15,15,15,15,]),'DeclAtrib':([2,3,51,84,97,123,127,131,135,149,],[16,16,16,16,16,16,16,16,16,16,]),'IfScope':([2,3,51,84,97,123,127,131,135,149,],[17,17,17,17,17,17,17,17,17,17,]),'AtribOp':([2,3,17,20,29,31,32,44,47,49,51,56,61,82,84,89,90,97,99,105,121,123,127,131,135,149,],[18,18,51,57,70,71,72,87,93,94,18,101,106,113,18,118,119,18,128,137,143,18,18,18,18,18,]),'WhileScope':([2,3,51,84,97,123,127,131,135,149,],[19,19,19,19,19,19,19,19,19,19,]),'SwitchScope':([2,3,51,84,97,123,127,131,135,149,],[21,21,21,21,21,21,21,21,21,21,]),'AtribArray':([2,3,17,20,29,31,32,44,47,49,51,56,61,82,84,89,90,97,99,105,121,123,127,131,135,149,],[22,22,54,54,54,54,54,54,54,54,22,54,54,54,22,54,54,22,54,54,54,22,22,22,22,22,]),'OpUno':([2,3,17,20,29,31,32,44,47,49,51,56,61,82,84,89,90,97,99,105,121,123,127,131,135,149,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'OpBin':([2,3,17,20,29,31,32,44,47,49,51,56,61,82,84,89,90,97,99,105,121,123,127,131,135,149,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'AtribNum':([2,3,17,20,29,31,32,44,47,49,51,56,61,82,84,89,90,97,99,105,121,123,127,131,135,149,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'AccessArray':([2,3,17,20,29,31,32,44,47,49,51,56,61,82,84,89,90,97,99,105,121,123,127,131,135,149,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'TermPlus':([2,3,17,20,29,31,32,44,47,49,51,56,61,62,82,84,89,90,97,99,105,121,123,127,131,135,149,],[33,33,33,33,33,33,33,33,33,33,33,33,33,107,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'TermMult':([2,3,17,20,29,31,32,44,47,49,51,56,61,62,73,82,84,89,90,97,99,105,121,123,127,131,135,149,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,109,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'TermPow':([2,3,17,20,29,31,32,44,47,49,51,56,61,62,73,76,82,84,89,90,97,99,105,121,123,127,131,135,149,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,110,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'Base':([2,3,17,20,29,31,32,44,47,49,51,56,61,62,73,76,79,82,84,89,90,97,99,105,121,123,127,131,135,149,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,111,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'FunCall':([2,3,17,20,29,31,32,44,47,49,51,56,61,62,73,76,79,82,84,89,90,97,99,105,121,123,127,131,135,149,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'FunScope':([6,],[43,]),'ArraySize':([6,41,53,100,125,],[46,46,46,130,130,]),'Conds':([21,],[58,]),'Cond':([21,104,],[59,136,]),'OpLogico':([24,],[62,]),'OpPlus':([33,107,],[73,73,]),'OpMult':([34,109,],[76,76,]),'OpPow':([35,110,],[79,79,]),'DeclArraySize':([42,],[81,]),'FunCases':([43,],[84,]),'FunExtra':([43,],[85,]),'FunArg':([47,],[91,]),'FunRec':([47,],[92,]),'Body':([51,84,123,131,135,149,],[95,114,144,146,150,153,]),'ElseScope':([95,],[123,]),'Cases':([103,],[132,]),'Case':([103,132,],[133,148,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Start","S'",1,None,None,None),
  ('Start -> Axiom','Start',1,'p_start','yacc.py',11),
  ('Axiom -> Axiom Code','Axiom',2,'p_axiom_code','yacc.py',17),
  ('Axiom -> Axiom Function','Axiom',2,'p_axiom_function','yacc.py',23),
  ('Axiom -> <empty>','Axiom',0,'p_axiom_empty','yacc.py',29),
  ('Code -> Code Block','Code',2,'p_code_block','yacc.py',34),
  ('Code -> Block','Code',1,'p_code_empty','yacc.py',39),
  ('Block -> Exp ;','Block',2,'p_block_exp','yacc.py',44),
  ('Block -> If','Block',1,'p_block_if','yacc.py',49),
  ('Block -> IfElse','Block',1,'p_block_ifelse','yacc.py',54),
  ('Block -> While','Block',1,'p_block_while','yacc.py',59),
  ('Block -> Switch','Block',1,'p_block_switch','yacc.py',64),
  ('Body -> { }','Body',2,'p_body_empty','yacc.py',73),
  ('Body -> Block','Body',1,'p_body_block','yacc.py',78),
  ('Body -> { Code }','Body',3,'p_body_code','yacc.py',83),
  ('Function -> ID FunScope FunCases Body','Function',4,'p_function','yacc.py',88),
  ('FunScope -> :','FunScope',1,'p_funscope','yacc.py',117),
  ('FunCases -> FunExtra RARROW ID','FunCases',3,'p_funcases_funextra_rarrow','yacc.py',123),
  ('FunCases -> RARROW ID','FunCases',2,'p_funcases_rarrow','yacc.py',139),
  ('FunCases -> FunExtra','FunCases',1,'p_funcases_funextra','yacc.py',149),
  ('FunCases -> <empty>','FunCases',0,'p_funcases_empty','yacc.py',154),
  ('FunExtra -> FunExtra , ID','FunExtra',3,'p_funextra_rec','yacc.py',159),
  ('FunExtra -> ID','FunExtra',1,'p_funextra_empty','yacc.py',165),
  ('IfScope -> IF','IfScope',1,'p_if_scope','yacc.py',170),
  ('If -> IfScope AtribOp Body','If',3,'p_if','yacc.py',176),
  ('ElseScope -> ELSE','ElseScope',1,'p_else_scope','yacc.py',188),
  ('IfElse -> IfScope AtribOp Body ElseScope Body','IfElse',5,'p_ifelse','yacc.py',196),
  ('WhileScope -> WHILE','WhileScope',1,'p_while_scope','yacc.py',211),
  ('While -> WhileScope ( AtribOp ) Body','While',5,'p_while','yacc.py',217),
  ('SwitchScope -> SWITCH','SwitchScope',1,'p_switch_scope','yacc.py',232),
  ('Switch -> SwitchScope Conds { Cases }','Switch',5,'p_switch','yacc.py',244),
  ('Conds -> Conds , Cond','Conds',3,'p_conds_rec','yacc.py',284),
  ('Conds -> Cond','Conds',1,'p_conds_base','yacc.py',290),
  ('Cond -> ID ( AtribOp )','Cond',4,'p_cond_id','yacc.py',295),
  ('Cond -> ( AtribOp )','Cond',3,'p_cond_empty','yacc.py',301),
  ('Cases -> Cases Case','Cases',2,'p_cases_rec','yacc.py',307),
  ('Cases -> Case','Cases',1,'p_cases_base','yacc.py',313),
  ('Case -> ID : Body','Case',3,'p_case_id','yacc.py',318),
  ('Case -> : Body','Case',2,'p_case_empty','yacc.py',325),
  ('Exp -> Atrib','Exp',1,'p_exp_atrib','yacc.py',332),
  ('Exp -> Op','Exp',1,'p_exp_op','yacc.py',337),
  ('Exp -> Decl','Exp',1,'p_exp_decl','yacc.py',342),
  ('Exp -> DeclArray','Exp',1,'p_exp_declarray','yacc.py',347),
  ('Exp -> DeclAtrib','Exp',1,'p_exp_declatrib','yacc.py',352),
  ('AtribOp -> AtribNum','AtribOp',1,'p_atribop_atribnum','yacc.py',357),
  ('AtribOp -> Op','AtribOp',1,'p_atribop_op','yacc.py',362),
  ('Decl -> ID ID','Decl',2,'p_decl','yacc.py',367),
  ('DeclArray -> ID ID DeclArraySize','DeclArray',3,'p_declarray','yacc.py',387),
  ('DeclArraySize -> DeclArraySize [ NUM ]','DeclArraySize',4,'p_declarraysize_rec','yacc.py',411),
  ('DeclArraySize -> <empty>','DeclArraySize',0,'p_declarraysize_empty','yacc.py',417),
  ('AtribArray -> ID ArraySize LARROW AtribOp','AtribArray',4,'p_atribarray_Leftatribop','yacc.py',422),
  ('AtribArray -> AtribOp RARROW ID ArraySize','AtribArray',4,'p_atribarray_Rightatribop','yacc.py',445),
  ('ArraySize -> ArraySize [ AtribOp ]','ArraySize',4,'p_arraysize_rec','yacc.py',473),
  ('ArraySize -> [ AtribOp ]','ArraySize',3,'p_arraysize_empty','yacc.py',478),
  ('DeclAtrib -> ID ID LARROW AtribOp','DeclAtrib',4,'p_declatrib_left','yacc.py',483),
  ('DeclAtrib -> AtribOp RARROW ID ID','DeclAtrib',4,'p_declatrib_right','yacc.py',504),
  ('AtribNum -> ID LARROW AtribOp','AtribNum',3,'p_atribnum_left','yacc.py',525),
  ('AtribNum -> AtribOp RARROW ID','AtribNum',3,'p_atribnum_right','yacc.py',530),
  ('AtribNum -> AtribArray','AtribNum',1,'p_atribnum_array','yacc.py',536),
  ('Atrib -> ID LARROW AtribOp','Atrib',3,'p_atrib_left','yacc.py',541),
  ('Atrib -> AtribOp RARROW ID','Atrib',3,'p_atrib_right','yacc.py',546),
  ('Atrib -> ID SWAP ID','Atrib',3,'p_atrib_equiv','yacc.py',551),
  ('Atrib -> AtribArray','Atrib',1,'p_atrib_array','yacc.py',574),
  ('Op -> OpUno','Op',1,'p_op_opuno','yacc.py',579),
  ('Op -> OpBin','Op',1,'p_op_opbin','yacc.py',584),
  ('OpUno -> NEG AtribOp','OpUno',2,'p_opuno_neg','yacc.py',589),
  ('OpUno -> AccessArray','OpUno',1,'p_opuno_accessarray','yacc.py',594),
  ('OpUno -> SUB AtribOp','OpUno',2,'p_opuno_minus','yacc.py',599),
  ('OpUno -> ? AtribOp','OpUno',2,'p_opuno_print','yacc.py',604),
  ('AccessArray -> ID ArraySize','AccessArray',2,'p_accessarray','yacc.py',610),
  ('OpBin -> OpBin OpLogico TermPlus','OpBin',3,'p_opbin_rec','yacc.py',625),
  ('OpBin -> TermPlus','OpBin',1,'p_opbin_base','yacc.py',630),
  ('TermPlus -> TermPlus OpPlus TermMult','TermPlus',3,'p_termplus_rec','yacc.py',635),
  ('TermPlus -> TermMult','TermPlus',1,'p_termplus_base','yacc.py',640),
  ('TermMult -> TermMult OpMult TermPow','TermMult',3,'p_termmult_rec','yacc.py',645),
  ('TermMult -> TermPow','TermMult',1,'p_termmult_base','yacc.py',650),
  ('TermPow -> TermPow OpPow Base','TermPow',3,'p_termpow_rec','yacc.py',655),
  ('TermPow -> Base','TermPow',1,'p_termpow_base','yacc.py',660),
  ('Base -> ( AtribOp )','Base',3,'p_base_exp','yacc.py',665),
  ('Base -> ID','Base',1,'p_base_id','yacc.py',670),
  ('Base -> NUM','Base',1,'p_base_num','yacc.py',683),
  ('Base -> FunCall','Base',1,'p_base_funcall','yacc.py',688),
  ('Base -> �','Base',1,'p_base_read','yacc.py',693),
  ('FunCall -> ID ( FunArg )','FunCall',4,'p_funcall','yacc.py',698),
  ('FunArg -> FunRec','FunArg',1,'p_funarg_funrec','yacc.py',710),
  ('FunArg -> <empty>','FunArg',0,'p_funarg_empty','yacc.py',715),
  ('FunRec -> FunRec , AtribOp','FunRec',3,'p_funrec_rec','yacc.py',720),
  ('FunRec -> AtribOp','FunRec',1,'p_funrec_base','yacc.py',725),
  ('OpLogico -> AND','OpLogico',1,'p_oplogico_and','yacc.py',730),
  ('OpLogico -> OR','OpLogico',1,'p_oplogico_or','yacc.py',735),
  ('OpLogico -> LESSER','OpLogico',1,'p_oplogico_lesser','yacc.py',740),
  ('OpLogico -> GREATER','OpLogico',1,'p_oplogico_greater','yacc.py',745),
  ('OpLogico -> LEQ','OpLogico',1,'p_oplogico_leq','yacc.py',750),
  ('OpLogico -> GEQ','OpLogico',1,'p_oplogico_geq','yacc.py',755),
  ('OpLogico -> EQUAL','OpLogico',1,'p_oplogico_equal','yacc.py',760),
  ('OpPlus -> ADD','OpPlus',1,'p_opplus_add','yacc.py',765),
  ('OpPlus -> SUB','OpPlus',1,'p_opplus_sub','yacc.py',770),
  ('OpMult -> MUL','OpMult',1,'p_opmult_mul','yacc.py',775),
  ('OpMult -> DIV','OpMult',1,'p_opmult_div','yacc.py',780),
  ('OpPow -> POW','OpPow',1,'p_oppow','yacc.py',785),
]