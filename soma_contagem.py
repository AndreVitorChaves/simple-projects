n = 0
n2 = 0
while True:
    n1 = int(input('Digite um número: '))
    if n1 == 999:
        break
    n += n1
    n2 += 1
print(f'A quantidade de números digitados foi {n2}. Enquanto a soma total desses números foi de {n}.')
