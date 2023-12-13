import time
print('='*40)
print('Caixa da loja')
print('='*40)

p = float(input('Digite o valor das compras: '))
print('Aguarde...')
time.sleep(3)
print('''Escolha uma das opcões de pagamento:
[ 1 ] Á vista (dinheiro ou cheque)
[ 2 ] Á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão ''')
o = int(input('Digite a opção de pagamento: '))
print('Calculando o valor final...')
time.sleep(3)

if o == 1:
    novo = p - (p * 10 / 100)
    print('Aplicando descontos...')
    time.sleep(3)
    print('O valor total da compra foi de {}' .format(novo))
elif o == 2:
    novo = p - (p * 5 / 100)
    print('Verificação de descontos...')
    time.sleep(3)
    print('O valor total da compra foi de {}' .format(novo))
elif o == 3:
    total = p
    parcelas = (total / 2)
    print('Sua compra sera parcelada em 2x de {}' .format(parcelas))
    print('O valor total da compra sera de {}' .format(total))
elif o == 4:
    total = p + (p * 20 / 100)
    total_parc = int(input('Quantas parcelas? '))
    parcela = total / total_parc
    print('Calculando...')
    time.sleep(3)
    print('Sua compra será parcelada em {}x de R$ {:.2f}'.format(total_parc, parcela))
