import os
os.system("cls || clear")

# Componentes da equipe:
# Arthur Fraga de Oliveira
# Heloisa Lima de Oliveira
# Júlia vitória dos Santos Azevedo Jesus
#Iran Ferreira


lista_numero = []
contador= 0
QUANTIDADE_NUMERO = 5


for i in range(QUANTIDADE_NUMERO):
    numero = int(input(f"Digite o {i + 1}ª número: "))
    lista_numero.append(numero)
    contador += 1

def par_impar(a):
    par = 0
    impar = 0
    lista_par = []
    lista_impar = []
    for numero in a:
        if numero % 2 == 0:
            par += 1
            lista_par.append(numero)
        else:
            impar += 1
            lista_impar.append(numero)

    return lista_par, lista_impar 

lista_par, lista_impar = par_impar(lista_numero)

def verifificar_numeros_positivos_negativos(a):
    positivo= 0
    negativo= 0

    for numero in a:
        if numero < 0:
            negativo += 1
        else:
            positivo += 1

    return positivo,negativo

numero_positivo, numero_negativo = verifificar_numeros_positivos_negativos(lista_numero)

def media(a):
    for numero in a:
        if numero != 0:
            soma = sum(a)
            media = soma / QUANTIDADE_NUMERO
    return media

media_total = media(lista_numero)

def media_pares_impares(a):
    QUANTIDADE = len(a)
    soma = sum(a)
    for numero in a:
       if numero <= 0 or numero >=0:
        media = soma /QUANTIDADE
        return media
       else:
        return 0

media_par = media_pares_impares (lista_par)
media_impar = media_pares_impares (lista_impar)
maior_numero = max (lista_numero)
menor_numero = min (lista_numero)


for i, numero in enumerate(reversed(lista_numero)):
    print(f"Ordem reversa: {len(lista_numero)-i}º {numero}")
print(f"Quantidade de números pares: {len(lista_par)}")
print(f"Quantidade de números ímpares: {len(lista_impar)}")
print (f"Quantidade de números positivos: {numero_positivo}")
print(f"Quantidade de números negativos: {numero_negativo}")
print(f"Quantidade de números inseridos: {contador}")
print (f"Maior número: {maior_numero} ")
print (f"Menor número: {menor_numero} ")
print(f"Média: {media_total}")
print(f"Média de numeros pares: {media_par}")
print(f"Média de numeros ímpares: {media_impar}")