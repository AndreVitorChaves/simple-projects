import os
import time
def limpar_tela():
    os.system('cls')
lista = []
lista1 = []
lista2 = []
while True:
    print('-'*45)
    print('CADASTRE UMA PESSOA')
    print('-'*45)
    idad = int(input('Idade: '))
    if idad >= 18:
        lista.append(idad)
    sex = input('Sexo: [M/F] ').lower() .strip()
    if sex == 'm':
        lista1.append(sex)
    elif sex == 'f' and idad < 20:
        lista2.append("mulher < 20")
    print('-'*45)
    cont = input('Deseja continuar? [S/N] ').lower() .strip()
    if cont =='n':
        break
    else:
        time.sleep(0.5)
        limpar_tela()
dimaior = len(lista)
homens = len(lista1)
mu_20 = len(lista2)
print(f'Total de pessoas maiores de idade: {dimaior}')
print(f'A quantidade de homens cadastrados foram: {homens}')
print(f'A quantidade de mulheres com menos de 20 anos foi: {mu_20}')