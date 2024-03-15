# Exercícios
#
# 4. Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

lista_frutas = ["Morango", "Abacaxi", "Uva", "Mamão", "Banana", "Maçã", "Pêra", "Uva", "Morango", "Morango", "Abacaxi"]

def contador(lista):
    dic_repetido = {}
    for i in lista:
        if i not in dic_repetido:
            dic_repetido[i] = 1
        else:
            dic_repetido[i] += 1
    print(dic_repetido)

contador(lista_frutas)