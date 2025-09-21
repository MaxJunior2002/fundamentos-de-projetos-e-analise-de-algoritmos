def max_min_select(arr):
    n = len(arr)

    if n == 1:
        return arr[0], arr[0]

    if n == 2:
        if arr[0] < arr[1]:
            return arr[0], arr[1]
        else:
            return arr[1], arr[0]

    meio = n // 2

    min_esq, max_esq = max_min_select(arr[:meio])
    min_dir, max_dir = max_min_select(arr[meio:])

    menor_final = min_esq if min_esq < min_dir else min_dir

    maior_final = max_esq if max_esq > max_dir else max_dir

    return menor_final, maior_final


lista = [15, 19, 73, 6, 8, 18, 31]

if not lista:
    print("A lista está vazia.")
else:
    menor, maior = max_min_select(lista)
    print(f"Menor: {menor}")
    print(f"Maior: {maior}")