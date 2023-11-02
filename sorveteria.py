print('Olá, seja bem-vindo a Sorveteria do Amaral') #mensagem de boas vindas e cardápio
print('---------------------------------------Cardápio----------------------------------------')
print('| Nº DE BOLAS | Sabor Tradicional (tr) | Sabor Premium (pr)  | Sabor Especial (es)    |')
print('|     1       |         R$ 6,00        |        R$ 7,00      |       R$ 8,00          |')
print('|     2       |         R$ 11,00       |        R$ 13,00     |       R$ 15,00         |')
print('|     3       |         R$ 15,00       |        R$ 18,00     |       R$ 21,00         |')
print('---------------------------------------------------------------------------------------')

preco_pedido = 0 #iniciar a variavel que contabiliza o valor do pedido

while True: #Utilização da estrutura while com atribuição "True" para gerar um loop

    sabor_sorvete = input('\nEntre com o sabor desejado (tr/ pr/ es): ') #entrada do sabor desejado do sorvete
    if(sabor_sorvete != 'tr' and sabor_sorvete != 'pr' and sabor_sorvete != 'es'): #validação da entrada para continuar ou não a elaboração do pedido
        print('Sabor inválido. Tente novamente')
        continue

    num_de_bolas_sorvete = input('Entre com o número de bolas de sorvete desejado (1/ 2/ 3): ') #entrada da quantidade desejada de bola(s) de sorvete
    if(num_de_bolas_sorvete != '1' and num_de_bolas_sorvete != '2' and num_de_bolas_sorvete != '3'): #validação da entrada para continuar ou não a elaboração do pedido, caso não retorna para a entrada acima
        print('Número de bolas de sorvete inválido. Tente novamente')
        continue

#especificar a categoria, preço por quantidade de bola(s) de sorvete
    if(sabor_sorvete == 'tr'):
        tipo = "Tradicional"
        preco_bola = 6
        if(num_de_bolas_sorvete == '2'):
            preco_bola = 11
        elif(num_de_bolas_sorvete == '3'):
            preco_bola = 15
    elif(sabor_sorvete == 'pr'):
        tipo = "Premium"
        preco_bola = 7
        if(num_de_bolas_sorvete == '2'):
            preco_bola = 13
        elif(num_de_bolas_sorvete == '3'):
            preco_bola = 18
    elif(sabor_sorvete == 'es'):
        tipo = "Especial"
        preco_bola = 8
        if(num_de_bolas_sorvete == '2'):
            preco_bola = 15
        elif(num_de_bolas_sorvete == '3'):
            preco_bola = 21

    preco_pedido += preco_bola #variável que soma o total do pedido

    if(num_de_bolas_sorvete == 1): #definir o tipo de print a ser realizado (bola / bola(s))
        print('Você pediu {} bola de sorvete no sabor {}: R${}'.format(num_de_bolas_sorvete, tipo, preco_bola))
    else:
        print('Você pediu {} bolas de sorvete no sabor {}: R${:.2f}'.format(num_de_bolas_sorvete, tipo, preco_bola))

    deseja_mais_sorvete = input('Deseja mais algum sorvete (s - Sim / n - Não): ') #perguntar ao usuário se deseja mais algum sorvete, se sim, retorna ao 1º bloco de comando
    if(deseja_mais_sorvete == 's'):
        continue
    else:
        print('\nO valor total a ser pago: R${:.2f}'.format(preco_pedido)) #caso não desejado mais nada, é feito o print do valor total a ser pago
        print('Pedido encerrado,')
        break #encerrar programa