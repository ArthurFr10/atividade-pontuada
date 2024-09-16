import os
os.system("cls || clear")

# Variáveis para armazenar os números
lista_numeros = []
QUANTIDADE_NUMERO = 5
maior_numero = 0
menor_numero = 0
for i in range(QUANTIDADE_NUMERO):
    numero = int(input(f"Digite o {i +1}ª número: "))
    lista_numeros.append(numero)



# Processando todos os números
def pares_impares(a):
    contador_impar = 0
    contador_par = 0
    for numero in a:
        if numero % 2 == 0:
            contador_par += 1

        else:
            contador_impar += 1
    return contador_impar, contador_par

cont_impar, cont_par = pares_impares(lista_numeros)

def media(a):

    for numero in a:
        if numero % 2 == 0:
            soma1 = sum(lista_numeros)
            media_par = soma1 / cont_par
        else:
            soma2 = sum(lista_numeros)
            media_impar = soma2 / cont_impar
    return media_par, media_impar

med_par, med_impar = media(lista_numeros)

numeros_invertidos = reversed(lista_numeros)
maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)


    

  




print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {cont_par}")
print(f"Quantidade de ímpares: {cont_impar}")
print(f"Quantidade de positivos: ")
print(f"Quantidade de negativos: ")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos números pares: {med_par}")
print(f"Média dos números ímpares: {med_impar}")
print(f"Média de todos os números: ")
print(f"Números na ordem inversa: {numeros_invertidos} ")
