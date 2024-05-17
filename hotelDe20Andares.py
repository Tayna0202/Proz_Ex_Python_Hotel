# Repetição For

print("Usando o laço de repetição FOR")

print("Hotel de 20 andares...")
print("Fazendo a contagem de baixo para cima...")

for i in range(20, 13, -1):
    print("Hotel andar: " + str(i))

for i in range(12, 0, -1):
    print("Hotel andar: " + str(i))

# Repetição While

print("------------------------------------------")

print("Usando o laço de repetição WHILE")

andar = 20

while(andar > 0):
    print("Hotel andar: " + str(andar))
    andar -= 1
    if(andar <= 13):
        andar -= 1 
        break

while(andar > 0):
    print("Hotel andar: " + str(andar))
    andar -= 1
    if(andar <= 0): 
        break
     