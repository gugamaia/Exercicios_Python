minutos = int(input("Informe quantos minutos você usou seu telefone: "))
if minutos < 200:
    preco = 0.2
else:
    if minutos <= 400:
      preco = 0.18
    if minutos > 600:
        preco = 0.15
    elif minutos > 800:
        preco = 0.08
print(f"Sua conta de telefone é R$ {preco*minutos:.2f}")
