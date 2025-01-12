# Range é um gerador de uma sequência de números usada em for.
# Esssa função tem 3 parâmetros:
# 1. start (opcional): número inicial da sequência (o padrão é 0.)
# 2. stop (obrigatório): limite da sequência.
# 3. step (opcional): intervalo entre os números da sequência (o padrão é 1).

# Sequência simples:
#for i in range(5):
    #print(i)

# Sequência com start e stop:
#for i in range(2,8):
    #print(i)

# Sequência decrescente:
#for i in range(10,0,-2):
    #print(i)

# Sequência completa (start, stop, step):
#for index in range (7,15,2):
    #print(index)


# Conversão para lista usando range:
#lista = list(range(5))
#print(lista)

# Iteração de índices:
#frutas = ["Maça", "Banana", "Cereja"]
#for i in range(len(frutas)):
    #print(frutas[i], "(Valor do índice)", i)

for i in range(5):
    if i == 0:
        print("Primeira linha")
    else:
        print(f"Outras linhas {i}")