import pilha as pi 

expressao1 = '(a+b)*{a+b}'
expressa2 = '(a+b)*{(a+b)*(c+d)a+b}'
expressao = '(a+(b)*(a}+b)'
expressao4 = '(a+b}*(a+b}'
expressao5 = '(a+b)-(k-l)'
expressao6 = '(a+b)-(k-l))'
expressao7 = '(a+b)-((k-l)' 

n=len(expressao)
pilha = pi.Pilha() 

for i in range(n):
    if (expressao[i]=='(') or (expressao[i]=='{'):
        pilha.empilhar(expressao[i])
    elif (expressao[i]==')') or (expressao[i]=='}'):
            if not pilha.is_vazia():
                if (expressao[i]==')' and pilha.topo()=='(') or (expressao[i]=='}' and pilha.topo()=='{'):
                    pilha.desempilhar()
            else:
                pilha.empilhar('x')

if pilha.is_vazia():
    print('Expressão correta!')
else:
    print('Expressão com problema.')