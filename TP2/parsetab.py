
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ADD AND DIFF DIV ELSE EQUAL GEQ GREATER ID IF LARROW LEQ LESSER MOD MUL NEG NUM OR POW PRINT RARROW READ STRING SUB SWAP SWITCHCASE SWITCHCOND WHILEAxiom : StartAxiom : Start : Start BlockStart : Start FunctionStart : Code : Code BlockCode : BlockBlock : FunCall ';'Block : Exp ';'Block : If Block : IfElse Block : While Block : Switch Body : '{' '}'Body : BlockBody : '{' Code '}'FunctionHeader : ID FunScope FunCasesFunction : FunctionHeader BodyFunScope : ':'FunCases : FunExtra RARROW IDFunCases : RARROW IDFunCases : FunExtraFunCases : FunExtra : FunExtra ',' IDFunExtra : IDIfScope : IFIf : IfScope AtribOp BodyElseScope : ELSEIfElse : IfScope AtribOp Body ElseScope BodyWhileScope : WHILEWhile : WhileScope '(' AtribOp ')' BodySwitchScope : SWITCHCONDSwitchScope : SWITCHCASESwitch : SwitchScope Conds '{' Cases '}'Conds : Conds ',' CondConds : CondCond : ID '(' AtribOp ')'Cond : '(' AtribOp ')'Cases : Cases Case Cases : CaseCase : ID ':' BodyCase : ':' BodyExp : Str PRINTStr : '(' STRING ')'Str : STRINGExp : AtribExp : OpExp : DeclExp : DeclArrayExp : DeclAtribAtribOp : AtribNumAtribOp : OpDecl : ID IDDeclArray : ID ID DeclArraySizeDeclArraySize : DeclArraySize '[' NUM ']'DeclArraySize : '[' NUM ']'AtribArray : ID ArraySize LARROW AtribOpAtribArray : AtribOp RARROW ID ArraySizeAccessArray : ID ArraySizeArraySize : ArraySize '[' AtribOp ']'ArraySize : '[' AtribOp ']'DeclAtrib : ID ID LARROW AtribOpDeclAtrib : AtribOp RARROW ID IDAtribNum : ID LARROW AtribOpAtribNum : AtribOp RARROW IDAtribNum : AtribArrayAtrib : ID LARROW AtribOpAtrib : AtribOp RARROW IDAtrib : ID SWAP IDAtrib : AtribArrayOp : OpBinOpUno : NEG BaseOpUno : AccessArrayOpUno : SUB BaseOpUno : Base PRINTOpBin : OpBin OpLogico TermModOpBin : TermModTermMod : TermMod OpMod TermPlusTermMod : TermPlusTermPlus : TermPlus OpPlus TermMultTermPlus : TermMultTermMult : TermMult OpMult TermPowTermMult : TermPowTermPow : TermPow OpPow BaseTermPow : BaseBase : OpUnoBase : '(' AtribOp ')'Base : IDBase : NUMBase : FunCallBase : READFunCall : ID '(' FunArg ')'FunArg : FunRecFunArg : FunRec : FunRec ',' AtribOpFunRec : AtribOpOpLogico : DIFFOpLogico : ANDOpLogico : OROpLogico : LESSEROpLogico : GREATEROpLogico : LEQOpLogico : GEQOpLogico : EQUALOpMod : MODOpPlus : ADDOpPlus : SUBOpMult : MULOpMult : DIVOpPow : POW"
    
_lr_action_items = {'$end':([0,1,2,3,4,7,8,9,10,43,44,45,47,95,117,130,163,164,165,],[-2,0,-1,-3,-4,-10,-11,-12,-13,-8,-9,-18,-15,-14,-27,-16,-29,-31,-34,]),'ID':([0,2,3,4,7,8,9,10,11,12,13,20,23,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,54,55,56,57,60,61,62,63,65,66,67,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,104,105,106,107,110,111,114,115,116,117,118,120,121,122,124,125,126,127,128,129,130,131,135,136,137,138,139,140,142,143,144,145,146,148,149,150,151,153,160,161,162,163,164,165,166,167,168,171,],[-5,12,-3,-4,-10,-11,-12,-13,48,49,61,61,70,-71,-26,-32,-33,-51,-77,-79,-81,-83,-85,-86,-89,-91,93,-73,93,-8,-9,-18,48,-15,49,61,104,61,109,-59,-19,61,61,-52,-88,-66,-90,48,118,61,61,93,-97,-98,-99,-100,-101,-102,-103,-104,93,-105,93,-106,-107,93,-108,-109,93,-110,-75,-72,-88,-74,-14,48,-7,61,-25,-17,-22,139,61,61,-87,143,61,-27,147,152,70,61,-76,-78,-80,-82,-84,-59,-16,-6,-92,61,160,161,-21,-57,-61,-65,-64,48,-28,-58,48,152,-40,48,-20,-24,-60,-29,-31,-34,-39,48,-42,-41,]),'(':([0,2,3,4,7,8,9,10,11,12,13,20,22,23,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,54,55,56,57,60,61,62,63,65,67,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,104,105,106,110,111,114,116,117,121,122,124,125,126,127,128,129,130,131,135,136,139,140,142,143,144,145,146,148,149,153,160,161,162,163,164,165,167,],[-5,13,-3,-4,-10,-11,-12,-13,13,50,57,57,67,71,-71,-26,-30,-32,-33,-51,-77,-79,-81,-83,-85,-86,-89,-91,57,-73,57,-8,-9,-18,13,-15,50,57,-23,57,-59,-19,57,57,-52,50,-66,-90,13,57,122,57,57,-97,-98,-99,-100,-101,-102,-103,-104,57,-105,57,-106,-107,57,-108,-109,57,-110,-75,-72,50,-74,-14,13,-7,57,-25,-17,-22,57,57,-87,57,-27,71,57,-76,-78,-80,-82,-84,-59,-16,-6,-92,57,-21,-57,-61,-65,-64,13,-28,-58,13,13,-20,-24,-60,-29,-31,-34,13,]),'STRING':([0,2,3,4,7,8,9,10,11,13,26,31,32,33,34,35,36,37,38,39,41,43,44,45,46,47,51,54,55,60,61,62,63,65,91,92,93,94,95,96,97,104,105,106,114,117,124,125,126,127,128,129,130,131,135,139,140,142,143,144,145,146,148,149,153,160,161,162,163,164,165,167,],[-5,24,-3,-4,-10,-11,-12,-13,24,58,-71,-51,-77,-79,-81,-83,-85,-86,-89,-91,-73,-8,-9,-18,24,-15,-23,-59,-19,-52,-88,-66,-90,24,-75,-72,-88,-74,-14,24,-7,-25,-17,-22,-87,-27,-76,-78,-80,-82,-84,-59,-16,-6,-92,-21,-57,-61,-65,-64,24,-28,-58,24,24,-20,-24,-60,-29,-31,-34,24,]),'IF':([0,2,3,4,7,8,9,10,11,26,31,32,33,34,35,36,37,38,39,41,43,44,45,46,47,51,54,55,60,61,62,63,65,91,92,93,94,95,96,97,104,105,106,114,117,124,125,126,127,128,129,130,131,135,139,140,142,143,144,145,146,148,149,153,160,161,162,163,164,165,167,],[-5,27,-3,-4,-10,-11,-12,-13,27,-71,-51,-77,-79,-81,-83,-85,-86,-89,-91,-73,-8,-9,-18,27,-15,-23,-59,-19,-52,-88,-66,-90,27,-75,-72,-88,-74,-14,27,-7,-25,-17,-22,-87,-27,-76,-78,-80,-82,-84,-59,-16,-6,-92,-21,-57,-61,-65,-64,27,-28,-58,27,27,-20,-24,-60,-29,-31,-34,27,]),'WHILE':([0,2,3,4,7,8,9,10,11,26,31,32,33,34,35,36,37,38,39,41,43,44,45,46,47,51,54,55,60,61,62,63,65,91,92,93,94,95,96,97,104,105,106,114,117,124,125,126,127,128,129,130,131,135,139,140,142,143,144,145,146,148,149,153,160,161,162,163,164,165,167,],[-5,28,-3,-4,-10,-11,-12,-13,28,-71,-51,-77,-79,-81,-83,-85,-86,-89,-91,-73,-8,-9,-18,28,-15,-23,-59,-19,-52,-88,-66,-90,28,-75,-72,-88,-74,-14,28,-7,-25,-17,-22,-87,-27,-76,-78,-80,-82,-84,-59,-16,-6,-92,-21,-57,-61,-65,-64,28,-28,-58,28,28,-20,-24,-60,-29,-31,-34,28,]),'SWITCHCOND':([0,2,3,4,7,8,9,10,11,26,31,32,33,34,35,36,37,38,39,41,43,44,45,46,47,51,54,55,60,61,62,63,65,91,92,93,94,95,96,97,104,105,106,114,117,124,125,126,127,128,129,130,131,135,139,140,142,143,144,145,146,148,149,153,160,161,162,163,164,165,167,],[-5,29,-3,-4,-10,-11,-12,-13,29,-71,-51,-77,-79,-81,-83,-85,-86,-89,-91,-73,-8,-9,-18,29,-15,-23,-59,-19,-52,-88,-66,-90,29,-75,-72,-88,-74,-14,29,-7,-25,-17,-22,-87,-27,-76,-78,-80,-82,-84,-59,-16,-6,-92,-21,-57,-61,-65,-64,29,-28,-58,29,29,-20,-24,-60,-29,-31,-34,29,]),'SWITCHCASE':([0,2,3,4,7,8,9,10,11,26,31,32,33,34,35,36,37,38,39,41,43,44,45,46,47,51,54,55,60,61,62,63,65,91,92,93,94,95,96,97,104,105,106,114,117,124,125,126,127,128,129,130,131,135,139,140,142,143,144,145,146,148,149,153,160,161,162,163,164,165,167,],[-5,30,-3,-4,-10,-11,-12,-13,30,-71,-51,-77,-79,-81,-83,-85,-86,-89,-91,-73,-8,-9,-18,30,-15,-23,-59,-19,-52,-88,-66,-90,30,-75,-72,-88,-74,-14,30,-7,-25,-17,-22,-87,-27,-76,-78,-80,-82,-84,-59,-16,-6,-92,-21,-57,-61,-65,-64,30,-28,-58,30,30,-20,-24,-60,-29,-31,-34,30,]),'NUM':([0,2,3,4,7,8,9,10,11,13,20,26,27,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,50,51,52,54,55,56,57,60,61,62,63,65,67,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,100,104,105,106,110,111,114,116,117,122,124,125,126,127,128,129,130,131,132,135,136,139,140,142,143,144,145,146,148,149,153,160,161,162,163,164,165,167,],[-5,38,-3,-4,-10,-11,-12,-13,38,38,38,-71,-26,-51,-77,-79,-81,-83,-85,-86,-89,-91,38,-73,38,-8,-9,-18,38,-15,38,-23,38,-59,-19,38,38,-52,-88,-66,-90,38,38,38,38,-97,-98,-99,-100,-101,-102,-103,-104,38,-105,38,-106,-107,38,-108,-109,38,-110,-75,-72,-88,-74,-14,38,-7,38,134,-25,-17,-22,38,38,-87,38,-27,38,-76,-78,-80,-82,-84,-59,-16,-6,157,-92,38,-21,-57,-61,-65,-64,38,-28,-58,38,38,-20,-24,-60,-29,-31,-34,38,]),'READ':([0,2,3,4,7,8,9,10,11,13,20,26,27,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,50,51,52,54,55,56,57,60,61,62,63,65,67,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,104,105,106,110,111,114,116,117,122,124,125,126,127,128,129,130,131,135,136,139,140,142,143,144,145,146,148,149,153,160,161,162,163,164,165,167,],[-5,39,-3,-4,-10,-11,-12,-13,39,39,39,-71,-26,-51,-77,-79,-81,-83,-85,-86,-89,-91,39,-73,39,-8,-9,-18,39,-15,39,-23,39,-59,-19,39,39,-52,-88,-66,-90,39,39,39,39,-97,-98,-99,-100,-101,-102,-103,-104,39,-105,39,-106,-107,39,-108,-109,39,-110,-75,-72,-88,-74,-14,39,-7,39,-25,-17,-22,39,39,-87,39,-27,39,-76,-78,-80,-82,-84,-59,-16,-6,-92,39,-21,-57,-61,-65,-64,39,-28,-58,39,39,-20,-24,-60,-29,-31,-34,39,]),'NEG':([0,2,3,4,7,8,9,10,11,13,20,26,27,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,50,51,52,54,55,56,57,60,61,62,63,65,67,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,104,105,106,110,111,114,116,117,122,124,125,126,127,128,129,130,131,135,136,139,140,142,143,144,145,146,148,149,153,160,161,162,163,164,165,167,],[-5,40,-3,-4,-10,-11,-12,-13,40,40,40,-71,-26,-51,-77,-79,-81,-83,-85,-86,-89,-91,40,-73,40,-8,-9,-18,40,-15,40,-23,40,-59,-19,40,40,-52,-88,-66,-90,40,40,40,40,-97,-98,-99,-100,-101,-102,-103,-104,40,-105,40,-106,-107,40,-108,-109,40,-110,-75,-72,-88,-74,-14,40,-7,40,-25,-17,-22,40,40,-87,40,-27,40,-76,-78,-80,-82,-84,-59,-16,-6,-92,40,-21,-57,-61,-65,-64,40,-28,-58,40,40,-20,-24,-60,-29,-31,-34,40,]),'SUB':([0,2,3,4,5,7,8,9,10,11,12,13,20,26,27,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,54,55,56,57,60,61,62,63,65,67,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,104,105,106,110,111,114,116,117,122,124,125,126,127,128,129,130,131,135,136,139,140,142,143,144,145,146,148,149,153,160,161,162,163,164,165,167,],[-5,42,-3,-4,-90,-10,-11,-12,-13,42,-88,42,42,-71,-26,-51,-77,85,-81,-83,-85,-86,-89,-91,42,-73,42,-8,-9,-18,42,-15,-88,42,-23,42,-59,-19,42,42,-52,-88,-66,-90,42,42,42,42,-97,-98,-99,-100,-101,-102,-103,-104,42,-105,42,-106,-107,42,-108,-109,42,-110,-75,-72,-88,-74,-14,42,-7,42,-25,-17,-22,42,42,-87,42,-27,42,-76,85,-80,-82,-84,-59,-16,-6,-92,42,-21,-57,-61,-65,-64,42,-28,-58,42,42,-20,-24,-60,-29,-31,-34,42,]),';':([5,6,12,15,16,17,18,19,25,26,31,32,33,34,35,36,37,38,39,41,48,49,54,60,61,62,63,64,91,92,93,94,98,108,109,114,118,124,125,126,127,128,129,133,135,140,142,143,144,147,148,158,162,170,],[43,44,-88,-46,-47,-48,-49,-50,-70,-71,-51,-77,-79,-81,-83,-85,-86,-89,-91,-73,-88,-53,-59,-52,-88,-66,-90,-43,-75,-72,-88,-74,-54,-67,-69,-87,-68,-76,-78,-80,-82,-84,-59,-62,-92,-57,-61,-65,-64,-63,-58,-56,-60,-55,]),'PRINT':([5,12,14,24,36,37,38,39,41,48,54,61,63,91,92,93,94,113,114,128,129,135,142,162,],[-90,-88,64,-45,91,-86,-89,-91,-73,-88,-59,-88,-90,-75,91,-88,91,-44,-87,91,-59,-92,-61,-60,]),'POW':([5,12,35,36,37,38,39,41,48,54,61,63,91,92,93,94,114,127,128,129,135,142,162,],[-90,-88,90,-85,-86,-89,-91,-73,-88,-59,-88,-90,-75,-72,-88,-74,-87,90,-84,-59,-92,-61,-60,]),'MUL':([5,12,34,35,36,37,38,39,41,48,54,61,63,91,92,93,94,114,126,127,128,129,135,142,162,],[-90,-88,87,-83,-85,-86,-89,-91,-73,-88,-59,-88,-90,-75,-72,-88,-74,-87,87,-82,-84,-59,-92,-61,-60,]),'DIV':([5,12,34,35,36,37,38,39,41,48,54,61,63,91,92,93,94,114,126,127,128,129,135,142,162,],[-90,-88,88,-83,-85,-86,-89,-91,-73,-88,-59,-88,-90,-75,-72,-88,-74,-87,88,-82,-84,-59,-92,-61,-60,]),'ADD':([5,12,33,34,35,36,37,38,39,41,48,54,61,63,91,92,93,94,114,125,126,127,128,129,135,142,162,],[-90,-88,84,-81,-83,-85,-86,-89,-91,-73,-88,-59,-88,-90,-75,-72,-88,-74,-87,84,-80,-82,-84,-59,-92,-61,-60,]),'MOD':([5,12,32,33,34,35,36,37,38,39,41,48,54,61,63,91,92,93,94,114,124,125,126,127,128,129,135,142,162,],[-90,-88,82,-79,-81,-83,-85,-86,-89,-91,-73,-88,-59,-88,-90,-75,-72,-88,-74,-87,82,-78,-80,-82,-84,-59,-92,-61,-60,]),'DIFF':([5,12,26,32,33,34,35,36,37,38,39,41,48,54,61,63,91,92,93,94,114,124,125,126,127,128,129,135,142,162,],[-90,-88,73,-77,-79,-81,-83,-85,-86,-89,-91,-73,-88,-59,-88,-90,-75,-72,-88,-74,-87,-76,-78,-80,-82,-84,-59,-92,-61,-60,]),'AND':([5,12,26,32,33,34,35,36,37,38,39,41,48,54,61,63,91,92,93,94,114,124,125,126,127,128,129,135,142,162,],[-90,-88,74,-77,-79,-81,-83,-85,-86,-89,-91,-73,-88,-59,-88,-90,-75,-72,-88,-74,-87,-76,-78,-80,-82,-84,-59,-92,-61,-60,]),'OR':([5,12,26,32,33,34,35,36,37,38,39,41,48,54,61,63,91,92,93,94,114,124,125,126,127,128,129,135,142,162,],[-90,-88,75,-77,-79,-81,-83,-85,-86,-89,-91,-73,-88,-59,-88,-90,-75,-72,-88,-74,-87,-76,-78,-80,-82,-84,-59,-92,-61,-60,]),'LESSER':([5,12,26,32,33,34,35,36,37,38,39,41,48,54,61,63,91,92,93,94,114,124,125,126,127,128,129,135,142,162,],[-90,-88,76,-77,-79,-81,-83,-85,-86,-89,-91,-73,-88,-59,-88,-90,-75,-72,-88,-74,-87,-76,-78,-80,-82,-84,-59,-92,-61,-60,]),'GREATER':([5,12,26,32,33,34,35,36,37,38,39,41,48,54,61,63,91,92,93,94,114,124,125,126,127,128,129,135,142,162,],[-90,-88,77,-77,-79,-81,-83,-85,-86,-89,-91,-73,-88,-59,-88,-90,-75,-72,-88,-74,-87,-76,-78,-80,-82,-84,-59,-92,-61,-60,]),'LEQ':([5,12,26,32,33,34,35,36,37,38,39,41,48,54,61,63,91,92,93,94,114,124,125,126,127,128,129,135,142,162,],[-90,-88,78,-77,-79,-81,-83,-85,-86,-89,-91,-73,-88,-59,-88,-90,-75,-72,-88,-74,-87,-76,-78,-80,-82,-84,-59,-92,-61,-60,]),'GEQ':([5,12,26,32,33,34,35,36,37,38,39,41,48,54,61,63,91,92,93,94,114,124,125,126,127,128,129,135,142,162,],[-90,-88,79,-77,-79,-81,-83,-85,-86,-89,-91,-73,-88,-59,-88,-90,-75,-72,-88,-74,-87,-76,-78,-80,-82,-84,-59,-92,-61,-60,]),'EQUAL':([5,12,26,32,33,34,35,36,37,38,39,41,48,54,61,63,91,92,93,94,114,124,125,126,127,128,129,135,142,162,],[-90,-88,80,-77,-79,-81,-83,-85,-86,-89,-91,-73,-88,-59,-88,-90,-75,-72,-88,-74,-87,-76,-78,-80,-82,-84,-59,-92,-61,-60,]),'RARROW':([5,12,16,21,25,26,31,32,33,34,35,36,37,38,39,41,48,51,54,55,59,60,61,62,63,65,91,92,93,94,103,104,106,108,112,114,118,119,123,124,125,126,127,128,129,133,135,140,141,142,143,144,148,155,159,161,162,],[-90,-88,-52,66,-66,-71,-51,-77,-79,-81,-83,-85,-86,-89,-91,-73,-88,107,-59,-19,115,-52,-88,-66,-90,115,-75,-72,-88,-74,115,-25,137,115,115,-87,-65,115,115,-76,-78,-80,-82,-84,-59,115,-92,115,115,-61,-65,115,-58,115,115,-24,-60,]),'}':([7,8,9,10,43,44,46,47,95,96,97,117,130,131,150,151,163,164,165,166,168,171,],[-10,-11,-12,-13,-8,-9,95,-15,-14,130,-7,-27,-16,-6,165,-40,-29,-31,-34,-39,-42,-41,]),'ELSE':([7,8,9,10,43,44,47,95,117,130,163,164,165,],[-10,-11,-12,-13,-8,-9,-15,-14,146,-16,-29,-31,-34,]),':':([7,8,9,10,12,43,44,47,95,117,120,130,150,151,152,163,164,165,166,168,171,],[-10,-11,-12,-13,55,-8,-9,-15,-14,-27,153,-16,153,-40,167,-29,-31,-34,-39,-42,-41,]),'{':([11,26,31,32,33,34,35,36,37,38,39,41,51,54,55,60,61,62,63,65,68,69,91,92,93,94,104,105,106,114,124,125,126,127,128,129,135,139,140,142,143,144,145,146,148,149,153,154,156,160,161,162,167,169,],[46,-71,-51,-77,-79,-81,-83,-85,-86,-89,-91,-73,-23,-59,-19,-52,-88,-66,-90,46,120,-36,-75,-72,-88,-74,-25,-17,-22,-87,-76,-78,-80,-82,-84,-59,-92,-21,-57,-61,-65,-64,46,-28,-58,46,46,-35,-38,-20,-24,-60,46,-37,]),'LARROW':([12,48,49,54,61,142,162,],[52,52,99,110,116,-61,-60,]),'SWAP':([12,48,],[53,53,]),'[':([12,48,49,54,61,93,98,118,129,142,143,148,158,162,170,],[56,56,100,111,56,56,132,56,111,-61,56,111,-56,-60,-55,]),')':([26,31,32,33,34,35,36,37,38,39,41,50,54,58,59,60,61,62,63,91,92,93,94,101,102,103,114,119,123,124,125,126,127,128,129,135,140,142,143,144,148,155,159,162,],[-71,-51,-77,-79,-81,-83,-85,-86,-89,-91,-73,-94,-59,113,114,-52,-88,-66,-90,-75,-72,-88,-74,135,-93,-96,-87,149,156,-76,-78,-80,-82,-84,-59,-92,-57,-61,-65,-64,-58,169,-95,-60,]),',':([26,31,32,33,34,35,36,37,38,39,41,54,60,61,62,63,68,69,91,92,93,94,102,103,104,106,114,124,125,126,127,128,129,135,140,142,143,144,148,154,156,159,161,162,169,],[-71,-51,-77,-79,-81,-83,-85,-86,-89,-91,-73,-59,-52,-88,-66,-90,121,-36,-75,-72,-88,-74,136,-96,-25,138,-87,-76,-78,-80,-82,-84,-59,-92,-57,-61,-65,-64,-58,-35,-38,-95,-24,-60,-37,]),']':([26,31,32,33,34,35,36,37,38,39,41,54,60,61,62,63,91,92,93,94,112,114,124,125,126,127,128,129,134,135,140,141,142,143,144,148,157,162,],[-71,-51,-77,-79,-81,-83,-85,-86,-89,-91,-73,-59,-52,-88,-66,-90,-75,-72,-88,-74,142,-87,-76,-78,-80,-82,-84,-59,158,-92,-57,162,-61,-65,-64,-58,170,-60,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Axiom':([0,],[1,]),'Start':([0,],[2,]),'Block':([2,11,46,65,96,145,149,153,167,],[3,47,97,47,131,47,47,47,47,]),'Function':([2,],[4,]),'FunCall':([2,11,13,20,40,42,46,50,52,56,57,65,67,71,72,81,83,86,89,96,99,110,111,116,122,136,145,149,153,167,],[5,5,63,63,63,63,5,63,63,63,63,5,63,63,63,63,63,63,63,5,63,63,63,63,63,63,5,5,5,5,]),'Exp':([2,11,46,65,96,145,149,153,167,],[6,6,6,6,6,6,6,6,6,]),'If':([2,11,46,65,96,145,149,153,167,],[7,7,7,7,7,7,7,7,7,]),'IfElse':([2,11,46,65,96,145,149,153,167,],[8,8,8,8,8,8,8,8,8,]),'While':([2,11,46,65,96,145,149,153,167,],[9,9,9,9,9,9,9,9,9,]),'Switch':([2,11,46,65,96,145,149,153,167,],[10,10,10,10,10,10,10,10,10,]),'FunctionHeader':([2,],[11,]),'Str':([2,11,46,65,96,145,149,153,167,],[14,14,14,14,14,14,14,14,14,]),'Atrib':([2,11,46,65,96,145,149,153,167,],[15,15,15,15,15,15,15,15,15,]),'Op':([2,11,13,20,46,50,52,56,57,65,67,71,96,99,110,111,116,122,136,145,149,153,167,],[16,16,60,60,16,60,60,60,60,16,60,60,16,60,60,60,60,60,60,16,16,16,16,]),'Decl':([2,11,46,65,96,145,149,153,167,],[17,17,17,17,17,17,17,17,17,]),'DeclArray':([2,11,46,65,96,145,149,153,167,],[18,18,18,18,18,18,18,18,18,]),'DeclAtrib':([2,11,46,65,96,145,149,153,167,],[19,19,19,19,19,19,19,19,19,]),'IfScope':([2,11,46,65,96,145,149,153,167,],[20,20,20,20,20,20,20,20,20,]),'AtribOp':([2,11,13,20,46,50,52,56,57,65,67,71,96,99,110,111,116,122,136,145,149,153,167,],[21,21,59,65,21,103,108,112,59,21,119,123,21,133,140,141,144,155,159,21,21,21,21,]),'WhileScope':([2,11,46,65,96,145,149,153,167,],[22,22,22,22,22,22,22,22,22,]),'SwitchScope':([2,11,46,65,96,145,149,153,167,],[23,23,23,23,23,23,23,23,23,]),'AtribArray':([2,11,13,20,46,50,52,56,57,65,67,71,96,99,110,111,116,122,136,145,149,153,167,],[25,25,62,62,25,62,62,62,62,25,62,62,25,62,62,62,62,62,62,25,25,25,25,]),'OpBin':([2,11,13,20,46,50,52,56,57,65,67,71,96,99,110,111,116,122,136,145,149,153,167,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'AtribNum':([2,11,13,20,46,50,52,56,57,65,67,71,96,99,110,111,116,122,136,145,149,153,167,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'TermMod':([2,11,13,20,46,50,52,56,57,65,67,71,72,96,99,110,111,116,122,136,145,149,153,167,],[32,32,32,32,32,32,32,32,32,32,32,32,124,32,32,32,32,32,32,32,32,32,32,32,]),'TermPlus':([2,11,13,20,46,50,52,56,57,65,67,71,72,81,96,99,110,111,116,122,136,145,149,153,167,],[33,33,33,33,33,33,33,33,33,33,33,33,33,125,33,33,33,33,33,33,33,33,33,33,33,]),'TermMult':([2,11,13,20,46,50,52,56,57,65,67,71,72,81,83,96,99,110,111,116,122,136,145,149,153,167,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,126,34,34,34,34,34,34,34,34,34,34,34,]),'TermPow':([2,11,13,20,46,50,52,56,57,65,67,71,72,81,83,86,96,99,110,111,116,122,136,145,149,153,167,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,127,35,35,35,35,35,35,35,35,35,35,35,]),'Base':([2,11,13,20,40,42,46,50,52,56,57,65,67,71,72,81,83,86,89,96,99,110,111,116,122,136,145,149,153,167,],[36,36,36,36,92,94,36,36,36,36,36,36,36,36,36,36,36,36,128,36,36,36,36,36,36,36,36,36,36,36,]),'OpUno':([2,11,13,20,40,42,46,50,52,56,57,65,67,71,72,81,83,86,89,96,99,110,111,116,122,136,145,149,153,167,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'AccessArray':([2,11,13,20,40,42,46,50,52,56,57,65,67,71,72,81,83,86,89,96,99,110,111,116,122,136,145,149,153,167,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'Body':([11,65,145,149,153,167,],[45,117,163,164,168,171,]),'FunScope':([12,],[51,]),'ArraySize':([12,48,61,93,118,143,],[54,54,54,129,148,148,]),'Conds':([23,],[68,]),'Cond':([23,121,],[69,154,]),'OpLogico':([26,],[72,]),'OpMod':([32,124,],[81,81,]),'OpPlus':([33,125,],[83,83,]),'OpMult':([34,126,],[86,86,]),'OpPow':([35,127,],[89,89,]),'Code':([46,],[96,]),'DeclArraySize':([49,],[98,]),'FunArg':([50,],[101,]),'FunRec':([50,],[102,]),'FunCases':([51,],[105,]),'FunExtra':([51,],[106,]),'ElseScope':([117,],[145,]),'Cases':([120,],[150,]),'Case':([120,150,],[151,166,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Axiom","S'",1,None,None,None),
  ('Axiom -> Start','Axiom',1,'p_axiom_start','yacc.py',7),
  ('Axiom -> <empty>','Axiom',0,'p_start_empty','yacc.py',15),
  ('Start -> Start Block','Start',2,'p_axiom_code','yacc.py',20),
  ('Start -> Start Function','Start',2,'p_axiom_function','yacc.py',26),
  ('Start -> <empty>','Start',0,'p_axiom_empty','yacc.py',32),
  ('Code -> Code Block','Code',2,'p_code_block','yacc.py',37),
  ('Code -> Block','Code',1,'p_code_empty','yacc.py',42),
  ('Block -> FunCall ;','Block',2,'p_block_funcall','yacc.py',47),
  ('Block -> Exp ;','Block',2,'p_block_exp','yacc.py',55),
  ('Block -> If','Block',1,'p_block_if','yacc.py',60),
  ('Block -> IfElse','Block',1,'p_block_ifelse','yacc.py',65),
  ('Block -> While','Block',1,'p_block_while','yacc.py',70),
  ('Block -> Switch','Block',1,'p_block_switch','yacc.py',75),
  ('Body -> { }','Body',2,'p_body_empty','yacc.py',84),
  ('Body -> Block','Body',1,'p_body_block','yacc.py',89),
  ('Body -> { Code }','Body',3,'p_body_code','yacc.py',94),
  ('FunctionHeader -> ID FunScope FunCases','FunctionHeader',3,'p_function_header','yacc.py',98),
  ('Function -> FunctionHeader Body','Function',2,'p_function','yacc.py',117),
  ('FunScope -> :','FunScope',1,'p_funscope','yacc.py',140),
  ('FunCases -> FunExtra RARROW ID','FunCases',3,'p_funcases_funextra_rarrow','yacc.py',146),
  ('FunCases -> RARROW ID','FunCases',2,'p_funcases_rarrow','yacc.py',167),
  ('FunCases -> FunExtra','FunCases',1,'p_funcases_funextra','yacc.py',177),
  ('FunCases -> <empty>','FunCases',0,'p_funcases_empty','yacc.py',193),
  ('FunExtra -> FunExtra , ID','FunExtra',3,'p_funextra_rec','yacc.py',199),
  ('FunExtra -> ID','FunExtra',1,'p_funextra_empty','yacc.py',205),
  ('IfScope -> IF','IfScope',1,'p_if_scope','yacc.py',210),
  ('If -> IfScope AtribOp Body','If',3,'p_if','yacc.py',216),
  ('ElseScope -> ELSE','ElseScope',1,'p_else_scope','yacc.py',228),
  ('IfElse -> IfScope AtribOp Body ElseScope Body','IfElse',5,'p_ifelse','yacc.py',237),
  ('WhileScope -> WHILE','WhileScope',1,'p_while_scope','yacc.py',253),
  ('While -> WhileScope ( AtribOp ) Body','While',5,'p_while','yacc.py',259),
  ('SwitchScope -> SWITCHCOND','SwitchScope',1,'p_switch_scopecond','yacc.py',277),
  ('SwitchScope -> SWITCHCASE','SwitchScope',1,'p_switch_scopecase','yacc.py',289),
  ('Switch -> SwitchScope Conds { Cases }','Switch',5,'p_switch','yacc.py',302),
  ('Conds -> Conds , Cond','Conds',3,'p_conds_rec','yacc.py',343),
  ('Conds -> Cond','Conds',1,'p_conds_base','yacc.py',349),
  ('Cond -> ID ( AtribOp )','Cond',4,'p_cond_id','yacc.py',354),
  ('Cond -> ( AtribOp )','Cond',3,'p_cond_empty','yacc.py',360),
  ('Cases -> Cases Case','Cases',2,'p_cases_rec','yacc.py',366),
  ('Cases -> Case','Cases',1,'p_cases_base','yacc.py',372),
  ('Case -> ID : Body','Case',3,'p_case_id','yacc.py',377),
  ('Case -> : Body','Case',2,'p_case_empty','yacc.py',387),
  ('Exp -> Str PRINT','Exp',2,'p_exp_print','yacc.py',396),
  ('Str -> ( STRING )','Str',3,'p_Str_Aspas','yacc.py',401),
  ('Str -> STRING','Str',1,'p_Str_SemAspas','yacc.py',405),
  ('Exp -> Atrib','Exp',1,'p_exp_atrib','yacc.py',409),
  ('Exp -> Op','Exp',1,'p_exp_op','yacc.py',414),
  ('Exp -> Decl','Exp',1,'p_exp_decl','yacc.py',419),
  ('Exp -> DeclArray','Exp',1,'p_exp_declarray','yacc.py',424),
  ('Exp -> DeclAtrib','Exp',1,'p_exp_declatrib','yacc.py',429),
  ('AtribOp -> AtribNum','AtribOp',1,'p_atribop_atribnum','yacc.py',434),
  ('AtribOp -> Op','AtribOp',1,'p_atribop_op','yacc.py',439),
  ('Decl -> ID ID','Decl',2,'p_decl','yacc.py',444),
  ('DeclArray -> ID ID DeclArraySize','DeclArray',3,'p_declarray','yacc.py',469),
  ('DeclArraySize -> DeclArraySize [ NUM ]','DeclArraySize',4,'p_declarraysize_rec','yacc.py',498),
  ('DeclArraySize -> [ NUM ]','DeclArraySize',3,'p_declarraysize_empty','yacc.py',504),
  ('AtribArray -> ID ArraySize LARROW AtribOp','AtribArray',4,'p_atribarray_Leftatribop','yacc.py',509),
  ('AtribArray -> AtribOp RARROW ID ArraySize','AtribArray',4,'p_atribarray_Rightatribop','yacc.py',544),
  ('AccessArray -> ID ArraySize','AccessArray',2,'p_accessarray','yacc.py',584),
  ('ArraySize -> ArraySize [ AtribOp ]','ArraySize',4,'p_arraysize_rec','yacc.py',608),
  ('ArraySize -> [ AtribOp ]','ArraySize',3,'p_arraysize_empty','yacc.py',613),
  ('DeclAtrib -> ID ID LARROW AtribOp','DeclAtrib',4,'p_declatrib_left','yacc.py',618),
  ('DeclAtrib -> AtribOp RARROW ID ID','DeclAtrib',4,'p_declatrib_right','yacc.py',640),
  ('AtribNum -> ID LARROW AtribOp','AtribNum',3,'p_atribnum_left','yacc.py',662),
  ('AtribNum -> AtribOp RARROW ID','AtribNum',3,'p_atribnum_right','yacc.py',667),
  ('AtribNum -> AtribArray','AtribNum',1,'p_atribnum_array','yacc.py',673),
  ('Atrib -> ID LARROW AtribOp','Atrib',3,'p_atrib_left','yacc.py',678),
  ('Atrib -> AtribOp RARROW ID','Atrib',3,'p_atrib_right','yacc.py',683),
  ('Atrib -> ID SWAP ID','Atrib',3,'p_atrib_equiv','yacc.py',688),
  ('Atrib -> AtribArray','Atrib',1,'p_atrib_array','yacc.py',730),
  ('Op -> OpBin','Op',1,'p_op_opbin','yacc.py',740),
  ('OpUno -> NEG Base','OpUno',2,'p_opuno_neg','yacc.py',745),
  ('OpUno -> AccessArray','OpUno',1,'p_opuno_accessarray','yacc.py',750),
  ('OpUno -> SUB Base','OpUno',2,'p_opuno_minus','yacc.py',755),
  ('OpUno -> Base PRINT','OpUno',2,'p_opuno_print','yacc.py',760),
  ('OpBin -> OpBin OpLogico TermMod','OpBin',3,'p_opbin_rec','yacc.py',767),
  ('OpBin -> TermMod','OpBin',1,'p_opbin_base','yacc.py',772),
  ('TermMod -> TermMod OpMod TermPlus','TermMod',3,'p_opmod_rec','yacc.py',777),
  ('TermMod -> TermPlus','TermMod',1,'p_opmod_base','yacc.py',782),
  ('TermPlus -> TermPlus OpPlus TermMult','TermPlus',3,'p_termplus_rec','yacc.py',787),
  ('TermPlus -> TermMult','TermPlus',1,'p_termplus_base','yacc.py',792),
  ('TermMult -> TermMult OpMult TermPow','TermMult',3,'p_termmult_rec','yacc.py',797),
  ('TermMult -> TermPow','TermMult',1,'p_termmult_base','yacc.py',802),
  ('TermPow -> TermPow OpPow Base','TermPow',3,'p_termpow_rec','yacc.py',807),
  ('TermPow -> Base','TermPow',1,'p_termpow_base','yacc.py',812),
  ('Base -> OpUno','Base',1,'p_base_opuno','yacc.py',817),
  ('Base -> ( AtribOp )','Base',3,'p_base_exp','yacc.py',822),
  ('Base -> ID','Base',1,'p_base_id','yacc.py',827),
  ('Base -> NUM','Base',1,'p_base_num','yacc.py',841),
  ('Base -> FunCall','Base',1,'p_base_funcall','yacc.py',846),
  ('Base -> READ','Base',1,'p_base_read','yacc.py',856),
  ('FunCall -> ID ( FunArg )','FunCall',4,'p_funcall','yacc.py',861),
  ('FunArg -> FunRec','FunArg',1,'p_funarg_funrec','yacc.py',882),
  ('FunArg -> <empty>','FunArg',0,'p_funarg_empty','yacc.py',887),
  ('FunRec -> FunRec , AtribOp','FunRec',3,'p_funrec_rec','yacc.py',892),
  ('FunRec -> AtribOp','FunRec',1,'p_funrec_base','yacc.py',898),
  ('OpLogico -> DIFF','OpLogico',1,'p_oplogico_diff','yacc.py',903),
  ('OpLogico -> AND','OpLogico',1,'p_oplogico_and','yacc.py',907),
  ('OpLogico -> OR','OpLogico',1,'p_oplogico_or','yacc.py',912),
  ('OpLogico -> LESSER','OpLogico',1,'p_oplogico_lesser','yacc.py',917),
  ('OpLogico -> GREATER','OpLogico',1,'p_oplogico_greater','yacc.py',922),
  ('OpLogico -> LEQ','OpLogico',1,'p_oplogico_leq','yacc.py',927),
  ('OpLogico -> GEQ','OpLogico',1,'p_oplogico_geq','yacc.py',932),
  ('OpLogico -> EQUAL','OpLogico',1,'p_oplogico_equal','yacc.py',937),
  ('OpMod -> MOD','OpMod',1,'p_opmod_mod','yacc.py',941),
  ('OpPlus -> ADD','OpPlus',1,'p_opplus_add','yacc.py',945),
  ('OpPlus -> SUB','OpPlus',1,'p_opplus_sub','yacc.py',950),
  ('OpMult -> MUL','OpMult',1,'p_opmult_mul','yacc.py',955),
  ('OpMult -> DIV','OpMult',1,'p_opmult_div','yacc.py',960),
  ('OpPow -> POW','OpPow',1,'p_oppow','yacc.py',965),
]
