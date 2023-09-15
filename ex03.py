#1
notas = []
for i in range(1, 6): 
    num = int(input(f"Digite sua {i}ª nota: ")) 
    notas.append(num) 
    media = sum(notas) / 5 

print(f"A média da soma das suas notas é {media:.1f}.") 

#2

def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

def entrada():
    numero = int(input("Digite um número: ")) 
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}") 

entrada()
 
#3 
palavra = input("Digite uma palavra: ")

for letra in reversed(palavra):
    print(letra) 

palavra_invertida = "".join(reversed(palavra)) 

if palavra == palavra_invertida:
    print("É um palíndromo")
else:
    print("Não é um palíndromo.") 

#4
num = int(input("Digite um número: "))
if num < 0 :
    print("Digite um número positivo por favor.") 
else:
    string = str(num) 
    soma = 0
    for digito in string:
       soma += int(digito) 
print(soma) 

#5 
print("Vamos descobrir se um número é primo.")
num = int(input("Digite um número inteiro: ")) 

divisores = 0
for i in range(1, num +1):
    if num % i == 0:
        divisores += 1
if divisores == 2:
    print("É primo!")
else: 
    print("Não é primo!") 

#6 
string = input("Digite uma palavra: ") 
lista = ["a", "e", "i", "o", "u"]

vogais = 0
for digito in string:
    if digito in lista:
        vogais += 1
print(vogais)

#7
altura = float(input("Digite sua altura: ")) 
peso = float(input("Digite seu peso: "))
imc = peso / (altura*altura)
print(f"Seu imc é: {imc:.2f}")
 
#8
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

opcao = input("Escolha a conversão (Celsius para Fahrenheit - 'C' / Fahrenheit para Celsius - 'F'): ")

if opcao.upper() == 'C':
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"{celsius} graus Celsius equivalem a {fahrenheit:.2f} graus Fahrenheit.")
elif opcao.upper() == 'F':
    fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
    celsius = fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit} graus Fahrenheit equivalem a {celsius:.2f} graus Celsius.")
else:
    print("Opção inválida. Por favor, escolha 'C' ou 'F' para a conversão.")

#9
while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input("Digite um operador (+,-,/,*): ")
    resultado1 = (num1 + num2)
    resultado2 = (num1 - num2)
    resultado3 = (num1 / num2)
    resultado4 = (num1 * num2)
    operador_val = ["+", "-", "/", "*"]
    
    if operador not in operador_val:
        print("Este não é um operador válido, tente novamente.")
        continue

    if operador == "+":
        print(resultado1)
    elif operador == "-":
        print(resultado2) 
    elif operador == "/":
        print(resultado3)
    else:
        print(resultado4)

    pergunta = input("Deseja tentar novamente? ").lower() 
    if pergunta == "n":
        break

#10
num = int(input("Digite um número inteiro: "))

fibonacci = [0, 1] 

while fibonacci[-1] + fibonacci[-2] <= num:
    novo_num = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(novo_num) 

print(fibonacci)
