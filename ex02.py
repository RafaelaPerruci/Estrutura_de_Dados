#1
from math import pi
class Circulo:
    def __init__(self, raio): 
        self.raio = raio
    def calcular_area(self):
        area = pi * self.raio ** 2
        return area

a1 = Circulo(5)
print(f"A área do círculo de raio 5 é {a1.calcular_area():.2f}") 

#2
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo 
        self.autor = autor 

    def detalhes(self):
        info = f"Título: {self.titulo}, Autor: {self.autor}" 
        return info 
    
livro1 = Livro("O alquimista", "Paulo Coelho") 
print(livro1.detalhes()) 

#3 
class Retangulo:
    def __init__(self, base, altura):
        self.altura = altura
        self.base = base 
    
    def calcular_area(self):
        area = self.base * self.altura 
        return f"A área deste retângulo é {area}" 
    
r1 = Retangulo(5, 3)
print(r1.calcular_area()) 

#4

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.saldo = saldo 
        self.titular = titular

    def depositar(self, valor): 
        print(f"O valor atual da sua conta é {self.saldo} reais.")
        self.saldo = valor
        print(f"No entanto foi depositado o valor de {valor} reais, logo você está {valor} reais mais rico.") 
        saldo = f"Seu saldo atual é de {self.saldo}."
        return saldo
    
    def sacar(self, valor):
        self.saldo -= valor
        print(f"Você acabou de sacar {valor} reais, agora seu saldo é {self.saldo} reais.")
        saldo = f"Seu saldo atual é de {self.saldo}."
        return saldo

conta = ContaBancaria("Maria")
print(conta.depositar(100))
print(conta.sacar(50)) 

#5

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 

    def falar(self):
        return f"Olá meu nome é {self.nome} e eu tenho {self.idade} anos."

p1 = Pessoa("Rafa", 26)
print(p1.falar())

#6

class Produto: 
    def __init__(self, nome, preco, quantidade):
        self.nome = nome  
        self.preco = preco 
        self.quantidade = quantidade 

    def calcular_total(self):
        total = self.preco * self.quantidade
        return f"O valor total da sua compra é de {total}" 

product = Produto("vinho rose", 40, 2) 
print(product.calcular_total()) 

#7
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        string = f"O meu carro é um {self.marca} {self.modelo}, de {self.ano}."
        return string
    
c1 = Carro("NISSAN", "Kicks", 2019)
print(c1.detalhes())

#8 
class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome 
        self.notas = notas

    def calcular_media(self):
        media = sum(self.notas)/3
        return f"A media do aluno {self.nome} é de {media:.2f}."

a1 = Aluno("João", [10,5,7])
print(a1.calcular_media()) 

#9
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_perimetro(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        return perimetro 
    
triangulo = Triangulo(3, 4, 5)
print(f"Perímetro do triângulo: {triangulo.calcular_perimetro()}") 

#10
class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def aumentar_salario(self, percentual):
        aumento = (self.salario * percentual) / 100
        self.salario += aumento
        return f"Novo salário do(a) {self.nome}: {self.salario}" 
    
funcionario = Funcionario("João", 5000, "Analista")
print(funcionario.aumentar_salario(10))