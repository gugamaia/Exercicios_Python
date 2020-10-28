a = int(input("Informe o lado A do triangulo: "))
b = int(input("Informe o lado B do triangulo: "))
c = int(input("Informe o lado C do triangulo: "))
if a == b == c:
    print("Triângulo Equilátero")
elif a == b != c:
    print("Triângulo é Isóceles")
elif a != b == c:
    print("Triângulo é Isóceles")
else:
    print("Triângulo é Escaleno")
