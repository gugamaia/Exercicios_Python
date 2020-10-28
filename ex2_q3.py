peixe = float(input("Informe o peso do peixe: "))
if peixe <= 50:
    print("Peso dentro do permitido! Informar o próximo")
else:
    print(f"Peso acima do permitido, sua multa será de R$ {(peixe - 50) * 4:.2f}")
