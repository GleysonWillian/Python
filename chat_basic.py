import os

mensagens = []

nome = input ("Nome: ")

while True:

    os.system ('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'],":", m['texto'])

    print("_________________")

    texto = input ("mensagens: ")
    if texto == "fim":
        break

    mensagens.append({
        "nome": nome,
        "texto": texto
    })