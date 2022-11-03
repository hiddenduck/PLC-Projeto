import re

def teste1(lista):
    return [[x] for x in lista]

colunas = []

print("Split de uma linha por virgulas")

input = open("teste1.csv", "r", encoding="utf-8")
primeira = input.readline()[:-1]
colunas = re.findall(r'(?<![^,])([^{^,]+)(?:{(\d+)(?:,(\d+))?})?(?:::([^,]+))?', primeira)


#será que é possível fazer sub(ou mesmo sub n) nesta string e construir logo algo super interessante, uma linha magica logo de estoura, evitando um for
print(colunas)

patern = r'^'
replace = r''
fun_str = ""
i = 1
fun_pos = 0
#colunas: 0 -> título; 1->min/único; 2->max; 3->função
for coluna in colunas:
    if coluna[1] == '':
        patern += r'([^{,]+),'    
        replace += r'%s:\%d\n' % (coluna[0],i)
    else:
        if coluna[2] == '':
            if coluna[3] == '':
                patern += r'([^,]+(?:,[^,]+){%d}),{0,%d},' % (int(coluna[1])-1, int(coluna[1])-1)
                replace += r'%s:[\%d]\n' % (coluna[0],i)
            else:
                patern += r'((?:[^\[\],]+)|(?:\[[^,]*(?:,[^,]*)*\])),'    
                replace += r'%s_%s:%s(\\%d)\n' % (coluna[0],coluna[3],coluna[3],i)
                fun_str += r'%s|' % (coluna[3])
        else:
            if coluna[3] == '':
                patern += r'([^,]+(?:,[^,]+){%d,%d}),{0,%d},' % (int(coluna[1])-1, int(coluna[2])-1,int(coluna[2])-1) 
                replace += r'%s:[\%d]\n' % (coluna[0],i)
            else:
                patern += r'((?:[^\[\],]+)|(?:\[[^,]*(?:,[^,]*)*\])),'    
                replace += r'%s_%s:%s(\\%d)\n' % (coluna[0],coluna[3],coluna[3],i)
                fun_str += r'%s|' % (coluna[3])
    i += 1

patern = patern[:-1] + '$'
fun_str = fun_str[:-1]
print(patern)
print(replace)
#o group de 0 é a linha sempre?
"""for linha in input:
    linha = linha[:-1]
    print(linha)
    teste = re.search(linha_magica, linha)
    for i in range(len(colunas)):
        if (colunas[i][1] != ''):
            lista = re.split(r',', teste.group(i+1))
            if (colunas[i][3] != ''):
                fun = eval(colunas[i][3])
                print(colunas[i][0] + "_" + colunas[i][3] + " : " + str(fun(map(int,lista))))
            else:
                print(colunas[i][0] + " : " + str(lista))
        else:
            print(colunas[i][0] + " : " + teste.group(i+1))"""

res = ''
for linha in input:
    linha = linha[:-1]
    print(linha)
    res += re.sub(patern,replace,linha)
    res += '\n'

print(res)

input.close()