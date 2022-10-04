tamanho = int(input('Tamanho em metros quadrados: '))
litros = tamanho / 3

if tamanho % 54 == 0:
	latas = tamanho / 54
else:
	latas = int(tamanho / 54) + 1

preco = latas * 80
print ('%d latas' %latas)
print ('R$ %.2f' %preco)

#Aqui utilizamlos uma formula para saber quantas latas iremos utilizar mediante a quantos metros quadrados
#O usuario quer pintar e sabendo o valor unitário de uma lata, fica fácil calcular o valor de várias depois
#De saber a quantidade nececessária