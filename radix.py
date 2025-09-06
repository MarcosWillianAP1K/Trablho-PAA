def obter_maximo(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

def ordenacao_contagem(arr, exp):
    """
    Realiza a ordenação por contagem no array com base no dígito representado por exp.

    Args:
        arr (lista de int): O array de inteiros a ser ordenado.
        exp (int): O expoente correspondente à posição do dígito (1 para unidades, 10 para dezenas, 100 para centenas, etc.).

    Returns:
        None: O array de entrada é ordenado in-place com base no dígito atual.
    """
    n = len(arr)
    saida = [0] * n
    contagem = [0] * 10

    # Conta a ocorrência de cada dígito
    for i in range(n):
        indice = arr[i] // exp
        contagem[indice % 10] += 1

    # Atualiza contagem para armazenar as posições finais
    for i in range(1, 10):
        contagem[i] += contagem[i - 1]

    # Constroi o array de saída
    i = n - 1
    while i >= 0:
        indice = arr[i] // exp
        saida[contagem[indice % 10] - 1] = arr[i]
        contagem[indice % 10] -= 1
        i -= 1

    # Copia o resultado para arr
    for i in range(n):
        arr[i] = saida[i]

def ordenacao_radix(arr):
    if not arr:
        return arr

    max_val = obter_maximo(arr)
    
    exp = 1
    while max_val // exp > 0:
        ordenacao_contagem(arr, exp)
        exp *= 10

# Exemplo de uso
if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Array original:", arr)
    ordenacao_radix(arr)
    print("Array ordenado:", arr)
