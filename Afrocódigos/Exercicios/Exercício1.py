# Exercícios
# 
# 1. Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Utilizando o método set, que significa que os dados devem ter valores únicos, excluindo os duplicados.
# importante ressaltar que após a transformação de uma lista em um set ela se torna um conjunto {}, portanto utilizamos list() para retornar uma lista

lista1 = [1, 2, 2, 3, 4, 4, 4, 5]

lista_sem_duplicatas = list(set(lista1))
print(f"Lista utilizando o set(): {lista_sem_duplicatas} | Tipo {type(lista_sem_duplicatas)}")

# Sem utilizar o set, criamos uma lista_sem_duplicadas para inserir os valores que ainda não foram inseridos.
# Lógica super simples, se o elemento não estiver na lista de valores únicos ele é inserido, o que configura a inserção apenas de valores únicos.

lista2 = [1, 2, 2, 3, 4, 4, 4, 5]
lista_sem_duplicatas_2 = []

for elemento in lista2:
    if elemento not in lista_sem_duplicatas_2:
        lista_sem_duplicatas_2.append(elemento)

print(f"Lista sem utilizar o set(): {lista_sem_duplicatas_2} | Tipo {type(lista_sem_duplicatas_2)}")

# Modificando a lista enquanto itera sobre ela. Causa comportamento estranho, mas interessante adicionar elementos em outra lista.
#for i in lista:
#    for j in lista:
#        if i == j:
#            lista.remove(j)
# print(lista)