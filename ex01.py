#1
notas = []
for i in range(3): 
    num = int(input("Digite um número: ")) 
    notas.append(num) 
    media = sum(notas) / 3 

print(f"A média da soma das suas notas é {media:.1f}.") 

#2 
num = int(input("Digite um número: ")) 
if num % 2 == 0:
    print("É par!")
else:
    print("É ímpar!")

#3
def numpar():
    try:
        num = int(input("Digite um número: ")) 
        print(f"Os números pares de 0 até {num} são:") 
        for c in range(0, num + 1, 2):
            print(c) 
    except:
        print("Este não é um número inteiro.") 
while True:
    numpar()
    continuar = input("Deseja verificar outro número? (s/n): ")
    if continuar.lower() != "s":
        break

#4 
lista = [10, 0, -1, 50, 8, 19, 26] 
maior_valor = max(lista) 
menor_valor = min(lista) 

print(f"O maior valor da lista é {maior_valor} e o menor valor é {menor_valor}")

#5
lista = [0, 5, 8 ,16, 15, 30, 12, 25, 20]
num_pares = [] 
for num in lista:
    if num % 2 ==0:
        num_pares.append(num) 
    media = sum(num_pares) / len(num_pares)
print(f"A média dos números pares dessa lista é {media:.1f}.")

#6 
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

#7
num = int(input("Digite um número inteiro: "))

fibonacci = [0, 1] 

while fibonacci[-1] + fibonacci[-2] <= num:
    novo_num = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(novo_num) 

print(fibonacci)


#8

#9
nomes = ["amanda", "ana", "luciana", "rafaela", "carol"]
nomes_a = []

for nome in nomes:
    if "a" in nome[0]:
        nomes_a.append(nome)
print(f"A lista de nomes completa é {nomes}, e a lista só com a letra 'a' é {nomes_a}.") 


#10 
import random 
jokenpo = ["pedra", "papel", "tesoura"]

while True:
    escolha = input("Digite pedra, papel ou tesoura: ").lower()
    computador = random.choice(jokenpo)
        
    if escolha not in jokenpo:
        print("Escolha inválida, tente novamente.")
        continue
        
    if escolha == computador:
        print("Empate!")
    elif escolha == "pedra" and computador == "papel":
        print("Computador venceu!")
    elif escolha == "papel" and computador == "tesoura":
        print("Computador venceu!")
    elif escolha == "tesoura" and computador == "pedra":
        print("Computador venceu!")
    else:
        print("Você venceu!")
            
    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != "s":
        break
