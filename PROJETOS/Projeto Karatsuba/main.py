def karatsuba(num1, num2):
    if len(num1) < 5 or len(num2) < 5:
        return int(num1) * int(num2)

    tamanho = max(len(num1), len(num2))
    num1 = num1.zfill(tamanho)
    num2 = num2.zfill(tamanho)

    meio = tamanho // 2

    a = num1[:meio]
    b = num1[meio:]
    c = num2[:meio]
    d = num2[meio:]

    p1 = karatsuba(a, c)
    p2 = karatsuba(b, d)
    p3 = karatsuba(str(int(a) + int(b)), str(int(c) + int(d)))

    resultado_meio = p3 - p1 - p2

    return p1 * (10**(2 * (tamanho - meio))) + resultado_meio * (10**(tamanho - meio)) + p2

num1 = "148779635"
num2 = "259863347"

resultado = karatsuba(num1, num2)
print(f"Resultado: {resultado}")