#1
notas = []
for i in range(1, 6): 
    num = int(input(f"Digite sua {i}ª nota: ")) 
    notas.append(num) 
    media = sum(notas) / 5 

print(f"A média da soma das suas notas é {media:.1f}.") 

