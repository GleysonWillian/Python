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
except ZeroDivisionError:
    print("Divisão por zero não é possível!")
except ValueError:
    print("Digite um valor válido!")
except:
    print("Erro inesperado!") #Erro de uma variável inexistente
finally:
    print("Sempre executa!")

# A função do 'finally' é fechar um arquivo para que possa ser aberto novamente.
# O finally é executado se o código der erro ou não.
# Muito usado em manipulação de arquivos.