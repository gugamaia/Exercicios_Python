area = int(input("Informe quantos metros² serão pintados: "))
litros = area / 3
lata = 80
num_latas = area / 54
preco = round(num_latas+0.5) * lata
print(f"Total de latas usadas {round(num_latas+0.5)}")
print(f"Valor total das latas R${round(preco+0.5)}")

#m= int(input("Metros"))
#if m % 54 == 0:
#   latas = m / 54
#else:
#   latas = int(m / 54) + 1
#
#valor = latas * 80
#print (f'{latas} latas')
#print (f'Total: R$ {valor:.2f}')
