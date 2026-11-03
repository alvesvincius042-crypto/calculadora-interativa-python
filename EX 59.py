n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
menu = 0
while menu != 5:
    print('''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair''')
    menu = int(input('Qual é a sua opção? '))
    if menu == 1:
        print('A soma entre {} e {} vale {}'.format(n1, n2, n1 + n2))
    elif menu == 2:
        print('A multiplicação entre {} e {} vale {}'.format(n1, n2, n1 * n2))
    elif menu == 3:
        if n1 > n2:
            print('O maior número é {} e o menor é {}'.format(n1, n2))
        elif n2 > n1:
            print('O maior número é {} e o menor é {}'.format(n2, n1))
        else:
            print('Os dois números são iguais')
    elif menu == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif menu == 5:
        print('Fim do programa')
    else:
        print('Opção inválida. Tente novamente.')