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