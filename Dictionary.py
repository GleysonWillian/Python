# Coleção de chave e valor;
# Não são ordenados;
# Não aceita valores duplicados;
# É totalmente mutável;
# Utiliza chaves;
# Os valores podem ser de quaisquer tipos

meses = {
    "Jan" : "Janeiro",
    "Fev" : "Fevereiro",
    "Mar" : "Março",
    "Apr" : "Abril",
    "May" : "Maio",
    "Jun" : "Junho",
    "Jul" : "Julho",
    "Aug" : "Agosto",
    "Sep" : "Setembro",
    "Oct" : "Outubro",
    "Nov" : "Novembro",
    "Dec" : "Dezembro"
}

print(meses.get("Abc")) # Retorna um none, quando se quer obter um valor que não foi declarado no código
print(meses["Jan"]) # Retorna uma mensagem de erro quando se quer obter u valor que não foi declarado
print(meses.get("Abc", "Esse valor não existe")) # Coloca outro valor, o qual sempre aparecerá sempre que quiser um valor que não foi declarado
print(len(meses)) # A função 'len', pega a quantidade de valores dentro da coleção, neste caso, a quantidade de meses