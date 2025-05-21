total = 0
lista = []
lista1 = []
print('-'*45)
print('LOJA DO DEKO')
print('-'*45)
while True: 
    nome = input('Nome do produto: ')
    val = float(input('Preço: R$'))
    total += val
    if val > 1000:
        lista.append(val)
    lista1.append(val)
    menor_valor = min(lista1)
    cont = input('Deseja continuar? [S/N] ').lower().strip()
    if cont == 'n':
        break
maisdemil = len(lista)
print(f'O valor total gasto em sua compra foi: R${total}')
print(f'O total de itens custando mais de mil reais foi: {maisdemil}')
print(f'O menor valor gasto foi: {menor_valor}')