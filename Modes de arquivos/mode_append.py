# Adicionando coisas em um arquivo já existente:

arquivo = open("Modes de arquivos/Test2.txt", "w") 
# Quando coloca "a", adiciona já no arquivo existente.
# Quando coloca "w", deleta o que existia e começa um novo.

arquivo.write("HTLM\n")
arquivo.write("Java\n")
arquivo.write("Perl\n")

arquivo.close()