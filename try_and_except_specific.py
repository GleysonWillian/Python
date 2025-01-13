# Try e Except: usado para aparecer uma mensagem informando que o valor inserido não é válido
# Sintaxe:
# try:
    #código
    #print("")
# except:
    #print("Mensagem desejada!")

try:
    numero = int(input("Digite um número: "))
    print(numero)

    10/0
except ZeroDivisionError:
    print("Divisão por zero não é possível!")
except ValueError:
    print("Digite um valor válido!")
except:
    print("Erro inesperado!") #Erro de uma variável inexistente

# Sintaxe para erro específico