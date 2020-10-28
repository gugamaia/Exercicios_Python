ganho = int(input("Quanto você ganha por hora: "))
horas = int(input("Informe quantas horas trabalha por mês: "))
salario = ganho * horas
imposto = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
descontos = imposto + inss + sindicato
sal_liquido = salario - descontos
print(f"+Salário Bruto: R${salario:.2f}")
print(f"-IR (11%): R${imposto:.2f}")
print(f"-INSS (8%): R${inss:.2f}")
print(f"-Sindicato (5%): R${sindicato:.2f}")
print(f"=Salário Liquido: R${sal_liquido:.2f}")
#\t para dar um tab
#\n pular de linha
