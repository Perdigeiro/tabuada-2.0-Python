while True:
    print("-" * 50)
    print('''TABUADA
             [ 1 ] - SOMA
             [ 2 ] - SUBTRAIR
             [ 3 ] - DIVIDIR
             [ 4 ] - MULTIPLICAR
             [ 5 ] - Sair''')
    print("-"*50)
    op = input('Escolhe uma opção: ')
    if not op.isdigit():
        print('Ahh! Só é aceitavel números numa conta')
        continue

    op = int(op)

    if op == 1:
        soma = int(input('Qual valor você quer?: '))
        for s in range(1, 11):
            res = s + soma
            print("{} + {} = {}".format(soma, s, res))

    if op == 2:
        soma = int(input('Escolha um número: '))
        for s in range(1, 11):
            res = s - soma
            print("{} - {} = {}".format(soma, s, res))

    if op == 3:
        soma = int(input('Escolha um número: '))
        for s in range(1, 11):
            res = s / soma
            print("{} / {} = {}".format(soma, s, res))

    if op == 4:
        soma = int(input('Escolha um número: '))
        for s in range(1, 11):
            res = s * soma
            print("{} x {} = {}".format(soma, s, res))
    if op == 5:
        print("Fim")
        break

    else:
        print('Digite uma opção valida')


