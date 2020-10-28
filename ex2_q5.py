a = int(input("Informe primeiro número: "))
b = int(input("Informe segundo número: "))
c = int(input("Informe último número: "))
if a < b and a < c:
        print(f"O menor número é {a}")
if b < a and b < c:
        print(f"O menor número é {b}")
if c < a and c < b:
    print(f"O menor número é {c}")
