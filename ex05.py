#Exercício de fila 
import fila as fi

#1  
fila = fi.Fila(5) 

print("Vamos imprimir em ordem os documentos da fila de impressão:")

print("Doc1")
fila.enfileirar(1)
print("Doc2")
fila.enfileirar(2) 
print("Doc3") 
fila.enfileirar(3)
print("Doc4") 
fila.enfileirar(4)

print('O primeiro doc da fila..: ',fila.primeiro())
print('================')
fila.visualizar()
fila.desenfileirar() 
print('O primeiro doc da fila..: ',fila.primeiro())
print('================')
fila.visualizar()

#2 
fila = fi.Fila(5) 

print("Vamos atender os clientes desta fila por ordem de chegada:")

print("Cliente1")
fila.enfileirar(9)
print("Cliente2")
fila.enfileirar(7) 
print("Cliente3") 
fila.enfileirar(3)
print("Cliente4") 
fila.enfileirar(1)

print('Ficha do primeiro do cliente da fila..: ',fila.primeiro())
print('================')
fila.visualizar()
fila.desenfileirar() 
print('Ficha do segundo da fila..: ',fila.primeiro())
print('================')
fila.visualizar() 

#3 
fila = fi.Fila(5)  

print("Vamos organizar a fila de pedidos com base na ordem em que foram feitos.") 

print("Pedido1")
fila.enfileirar(31)
print("Pedido2")
fila.enfileirar(32) 
print("Pedido3") 
fila.enfileirar(33)
print("Pedido4") 
fila.enfileirar(34)

print('Ficha primeiro do pedido da fila..: ',fila.primeiro())
print('================')
fila.visualizar()
fila.desenfileirar() 
print('Ficha do segundo pedido da fila..: ',fila.primeiro())
print('================')
fila.visualizar() 

#4 
fila = fi.Fila(5) 

print("Lista de tarefas:") 
print("Tarefa1")
fila.enfileirar(1)
print("Tarefa2")
fila.enfileirar(2) 
print("Tarefa3") 
fila.enfileirar(3)
print("Tarefa4") 
fila.enfileirar(4) 

print('Primeira tarefa a ser concluida..: ',fila.primeiro())
print('================')
fila.visualizar()
fila.desenfileirar() 
print('Segunda tarefa a ser concluida..: ',fila.primeiro())
print('================')
fila.visualizar() 

#5 

class FilaPedidos:
    def __init__(self):
        self.pedidos = []

    def enfileirar_pedido(self, pedido):
        self.pedidos.append(pedido)
        print(f"Pedido '{pedido}' adicionado à fila.")

    def desenfileirar_pedido(self):
        # Processa o próximo pedido na fila
        if self.pedidos:
            pedido = self.pedidos.pop(0)
            print(f"Processando pedido: '{pedido}'")
        else:
            print("A fila de pedidos está vazia. Não há pedidos para.de.")

    def visualizar_pedidos(self):
        # Exibe a lista de pedidos na fila
        if self.pedidos:
            print("Pedidos na fila:")
            for pedido in self.pedidos:
                print(pedido)
        else:
            print("A fila de pedidos está vazia.")


fila = FilaPedidos()

fila.enfileirar_pedido("Pedido 1")
fila.enfileirar_pedido("Pedido 2")
fila.enfileirar_pedido("Pedido 3")

fila.visualizar_pedidos()

fila.desenfileirar_pedido()
fila.desenfileirar_pedido()