# É necessário importar uma biblioteca;
# Importa a biblioteca 'os';

# Forma simples para remoção de arquivo:
import os
#os.remove("Modes de arquivos/test3.txt")
# Se tentar compilar o código novamente, vai dar erro, pois o arquivo não existe mais.

# Código para verificar se o arquivo existe ou não e, caso não existe, irá aparecer a mensagem após a comparação 'else'.
if os.path.exists("Modes_de_arquivos/test2.txt"):
    os.remove("Modes_de_arquivos/test2.txt")
    print("Teste excluído com sucesso!")
else:
    print("Arquivo inexistente!")