# Try e Except: usado para aparecer uma mensagem informando que o valor inserido não é válido
# Sintaxe:
#try:
    #código
    #print("")
#except:
    #print("Mensagem desejada!")

try:

    numero = int(input("Digite um número: "))
    print(numero)

except:
    print("Digite um valor válido: ")

# Sintaxe para erro genérico