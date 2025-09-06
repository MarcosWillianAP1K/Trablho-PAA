def cocktail_sort(lista):
    tamanho = len(lista)
    houve_troca = True
    inicio = 0
    fim = tamanho - 1

    while (houve_troca == True):
        # Reinicia o sinalizador para a próxima iteração
        houve_troca = False

        # Loop da esquerda para a direita
        for i in range(inicio, fim):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                houve_troca = True

        # Se não houve troca, a lista está ordenada
        if (houve_troca == False):
            break

        # Caso contrário, redefine o sinalizador para a próxima fase
        houve_troca = False

        # Move o 'fim' um passo para trás
        fim = fim - 1

        # Loop da direita para a esquerda
        for i in range(fim - 1, inicio - 1, -1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                houve_troca = True

        # Move o 'início' um passo para frente
        inicio = inicio + 1

# Exemplo de uso
if __name__ == '__main__':
    minha_lista = [5, 1, 4, 2, 8, 0, 2]
    print("Lista original:", minha_lista)
    cocktail_sort(minha_lista)
    print("Lista ordenada:", minha_lista)