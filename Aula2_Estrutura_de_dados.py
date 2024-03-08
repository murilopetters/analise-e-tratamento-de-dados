# Criando uma lista chamada animais
animais = [1, 2, 3]
print("Lista de animais inicial:", animais)

# Atualizando a lista com diferentes tipos de elementos
animais = ["cachorro", "gato", 12345, 6.5]
print("Lista de animais atualizada:", animais)

# Imprimindo elementos específicos da lista
print("Primeiro elemento da lista:", animais[0])
print("Quarto elemento da lista:", animais[3])

# Substituindo o primeiro elemento da lista
animais[0] = "papagaio"
print("Lista após substituição:", animais)

# Removendo "gato" da lista
animais.remove("gato")
print("Lista após remoção de 'gato':", animais)

# Obtendo o comprimento da lista
comprimento_lista = len(animais)
print("Comprimento da lista:", comprimento_lista)

# Verificando se "gato" está na lista
verificar_gato = "gato" in animais
print("A presença de 'gato' na lista é:", verificar_gato)

# Trabalhando com uma lista numérica
lista_numerica = [500, 30, 300, 80, 10]
print("Lista numérica original:", lista_numerica)

# Encontrando o máximo e o mínimo na lista
maximo_lista = max(lista_numerica)
minimo_lista = min(lista_numerica)
print("Máximo da lista numérica:", maximo_lista)
print("Mínimo da lista numérica:", minimo_lista)

# Adicionando novos elementos à lista "animais"
animais.append(["leão", "Cachorro"])
print("Lista após append:", animais)

# Extendendo a lista "animais" com novos elementos
animais.extend(["cobra", 6])
print("Lista após extend:", animais)

# Contando ocorrências de "leão" na lista
ocorrencias_leao = animais.count("leão")
print("Ocorrências de 'leão' na lista:", ocorrencias_leao)

# Ordenando a lista numérica
lista_numerica.sort()
print("Lista numérica ordenada:", lista_numerica)


# Trabalhando com tuplas
tp = ("Banana", "Maçã", 10, 50)
print("Tupla original:", tp)

# Acessando elementos da tupla
primeiro_elemento_tupla = tp[0]
print("Primeiro elemento da tupla:", primeiro_elemento_tupla)

# Tentativa de alterar elemento da tupla (resultará em erro)
# tp[0] = "Laranja"

# Contando ocorrências de "Maçã" na tupla
ocorrencias_maca_tupla = tp.count("Maçã")
print("Ocorrências de 'Maçã' na tupla:", ocorrencias_maca_tupla)

# Acessando uma fatia da tupla
fatia_tupla = tp[0:2]
print("Fatia da tupla:", fatia_tupla)


# Trabalhando com dicionários
dc = {"Maçã": 20, "Banana": 10, "Laranja": 15, "Uva": 5}
print("Dicionário original:", dc)

# Acessando o valor de uma chave no dicionário
valor_maca = dc["Maçã"]
print("Valor correspondente à chave 'Maçã':", valor_maca)

# Atualizando o valor da chave 'Maçã'
dc["Maçã"] = 25
print("Dicionário após atualização:", dc)

# Retornando todas as chaves e valores do dicionário
chaves_dicionario = dc.keys()
valores_dicionario = dc.values()
print("Chaves do dicionário:", chaves_dicionario)
print("Valores do dicionário:", valores_dicionario)

# Verificando e inserindo uma nova chave no dicionário
dc.setdefault("Limão", 22)
print("Dicionário após setdefault:", dc)