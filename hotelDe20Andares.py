# Repetição For

print("Usando o laço de repetição FOR")

print("Hotel de 20 andares...")
print("Fazendo a contagem de baixo para cima...")

for i in range(20, 0, -1):
    if(i == 13):
        continue
    else:
        print("Hotel andar: " + str(i))

# Repetição While

print("------------------------------------------")

print("Usando o laço de repetição WHILE")

contador = 20

while(contador >= 0):
    if(contador != 13):
        print("Hotel andar: " + str(contador))
    contador -= 1
