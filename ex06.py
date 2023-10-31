import pilha as pi 

#6 

p1 = pi.Pilha() 
p1.empilhar("Página 1")
p1.empilhar("Página 2")
p1.empilhar("Página 3")
p1.empilhar("Página 4") 
print("Topo:", p1.topo())
p1.imprimir()

p1.desempilhar()  
p1.empilhar("Página 5") 
print("Topo:", p1.topo()) 
p1.imprimir() 

#7
class CalculadoraRPN:
    def __init__(self):
        self.pilha = []

    def avaliar_rpn(self, expressao):
        tokens = expressao.split()

        for token in tokens:
            if self.eh_numero(token):
                self.pilha.append(float(token))
            else:
                if len(self.pilha) < 2:
                    raise ValueError("Expressão RPN inválida. Não há operandos suficientes para o operador.")

                operand2 = self.pilha.pop()
                operand1 = self.pilha.pop()

                if token == '+':
                    resultado = operand1 + operand2
                elif token == '-':
                    resultado = operand1 - operand2
                elif token == '*':
                    resultado = operand1 * operand2
                elif token == '/':
                    resultado = operand1 / operand2
                else:
                    raise ValueError(f"Operador inválido: {token}")

                self.pilha.append(resultado)

        if len(self.pilha) != 1:
            raise ValueError("Expressão RPN inválida. Muitos operandos ou operadores.")

        return self.pilha[0]

    def eh_numero(self, token):
        try:
            float(token)
            return True
        except ValueError:
            return False

calculadora = CalculadoraRPN()

expressao_rpn = "3 4 + 2 *"
resultado = calculadora.avaliar_rpn(expressao_rpn)
print(f"Resultado da expressão RPN: {resultado}") 

#8 


#9 
expressao = '(2+3)*(8-9)/(7^3)'

n=len(expressao)

pi = pi.Pilha()

op1=True
op2=True
op3=True 
op4=True

for i in range(n):
    if (expressao[i]=='+' and op1) or (expressao[i]=='-' and op2) or (expressao[i]=='*' and op3) or (expressao[i]=='/' and op4):
        pi.empilhar(expressao[i])
        if (expressao[i]=='+'):
            op1=False
        elif (expressao[i]=='-'):
            op2=False
        elif (expressao[i]=='*'):
            op3=False 
        else: 
            op4=False


pi.imprimir()  

#10 
class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()

    def esta_vazia(self):
        return len(self.itens) == 0

def verifica_palindromo(frase):
    frase = frase.lower()  
    pilha = Pilha()

    for caractere in frase:
        if caractere.isalnum():  
            pilha.empilhar(caractere)

    frase_invertida = "".join(pilha.itens[::-1])

    return frase == frase_invertida

frase = input("Digite uma palavra ou frase: ")
if verifica_palindromo(frase):
    print(f"'{frase}' é um palíndromo!")
else:
    print(f"'{frase}' não é um palíndromo.")
 
