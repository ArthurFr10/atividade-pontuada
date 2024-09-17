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
    numeros_invertidos = len(lista_numeros)



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


def media(a):
    for numero in a:
        if numero != 0:
            soma = sum(a)
            media = soma / QUANTIDADE_NUMERO
            return media
        else:
            return 0

def media_par_impar(a):
    par = 0
    impar = 0
    quantidade_par = []
    quantidade_impar = []
    for numero in a:
        if numero % 2 == 0:
            par += 1
            quantidade_par.append(numero)
        else:
            impar += 1
            quantidade_impar.append(numero)
    return par, impar, quantidade_par, quantidade_impar

def positivo_negativo(a):
    contador_positivo = 0
    contador_negativo = 0
    for numero in a:
        if numero >= 0:
            contador_positivo += 1
        else:
            contador_negativo += 1
    return contador_positivo, contador_negativo

def traco():
    print("==" * 18)
    return print


# Atribuindo valores as variáveis

cont_impar, cont_par = pares_impares(lista_numeros)
media_total = media(lista_numeros)
par, impar, quantidade_par, quantidade_impar = media_par_impar(lista_numeros)
contador_positivo, contador_negativo = positivo_negativo(lista_numeros)
media_par = media(quantidade_par)
media_impar = media(quantidade_impar)

maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)


    

  




print("\n===== Estatísticas dos números =====")
print(f"Quantidade de pares: {cont_par}")
print(f"Quantidade de ímpares: {cont_impar}")
print(f"Quantidade de positivos: {contador_positivo}")
print(f"Quantidade de negativos: {contador_negativo}")
print(f"Quantidade de números inseridos: {QUANTIDADE_NUMERO}")
traco()
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
traco()
print(f"Média dos números pares: {media_par}")
print(f"Média dos números ímpares: {media_impar}")
print(f"Média de todos os números: {media_total}")
traco()
print(f"Todos os números em ordem inversa: ")
for i, numero in enumerate(reversed(lista_numeros)):
    print(f"{QUANTIDADE_NUMERO - i}ª Número: {numero}")