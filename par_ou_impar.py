import time
import os
import random
def limpar_tela():
    os.system('cls')
while True:
    while True:
        p_i = input('Usuário, você escolhe par ou ímpar?\n a)Par\n b)Ímpar\n').lower().strip()
        if p_i in ['a', 'b']:
            break
        else:
            print('Resposta inválida. Tente novamente.')
    lista = []
    for c in range (1, 11):
        lista.append(c)
    n = random.choice(lista)
    print('Por fim, após a contagem, digite um número.')
    for b in range (3, 0, -1):
        print (b)
        time.sleep(0.5)
    n1 = int(input('Digite o seu número: '))
    print(f'O número escolhido pela máquina foi {n}')
    time.sleep(1)
    if p_i == 'a':
        if (n + n1)%2 == 0:
            print('Parabéns usuário, você é o vencedor.')
            print('Vamos jogar novamente!! ')
            time.sleep(1.3)
            limpar_tela()
        else:
            print('Você perdeu!')
            break
    else:
        if (n + n1)%2 != 0:
            print('Parabéns usuário, você é o vencedor!')
            print('Vamos jogar novamente!! ')
            time.sleep(1.3)
            limpar_tela()
        else:
            print('Você perdeu!')
            break



