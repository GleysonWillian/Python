#open("caminho", "r")

# Mode
# R -> leitura
# A -> Append / incrementar
# W -> Escrita
# X -> Create arquivo
# R+ -> Leitura + escrita


# Função para verificar se o arquivo pode ser lido ou não:
arquivo = open("Aula sobre arquivos/Test.txt", "r")

#print(arquivo.readable())
#print(arquivo.read())

# readline para ler a primieira linha do arquivo
# readline's seguidos vai ser linha por linha
#print(arquivo.readline()) 
#print(arquivo.readline()) 
#print(arquivo.readline())
#print(arquivo.readline())

# readlines pega todas as linhas e transforma em uma lista:
lista = arquivo.readlines()
print(lista)

print(lista[3])

arquivo.close()