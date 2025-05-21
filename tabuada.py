import os
import time
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    n = int(input('Olá, usuário, digite um número: '))
    if n < 0:
        print('Programa encerrado!')
        break
    for c in range (0, 11):
        print (f'{n} X {c} = {n*c}')
    time.sleep(2)
    limpar_tela()
        
