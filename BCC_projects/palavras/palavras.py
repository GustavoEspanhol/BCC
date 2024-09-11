from collections import Counter

# Letras que devem ser usadas (número exato de cada letra)
letras = "aaabcc"
letras_contador = Counter(letras)

# Função para verificar se uma palavra pode ser formada com as letras fornecidas
def pode_formar(palavra, letras_contador):
    return Counter(palavra) == letras_contador

# Abrindo o dicionário de palavras (substitua pelo caminho correto do arquivo do dicionário)
with open("dicionario.txt", "r", encoding="utf-8") as arquivo:
    palavras = arquivo.read().splitlines()

# Listando todas as palavras que podem ser formadas
palavras_formadas = [palavra for palavra in palavras if pode_formar(palavra, letras_contador)]

# Exibindo as palavras encontradas
for palavra in palavras_formadas:
    print(palavra)
else:
    print("não tem")