def distancia_edicao_recursiva(s1:str, s2:str) -> int:
    """
    Calcula a Distância de Edição entre s1 e s2 usando uma abordagem recursiva pura.
    """
    # Caso base 1: se a primeira string é vazia, o custo é inserir todos os caracteres da segunda.
    if not s1:
        return len(s2)

    # Caso base 2: se a segunda string é vazia, o custo é remover todos os caracteres da primeira.
    if not s2:
        return len(s1)

    # Se os últimos caracteres são iguais, não há custo.
    # O problema é reduzido para as strings sem o último caractere.
    if s1[-1] == s2[-1]:
        custo = 0
    # Se são diferentes, o custo da operação é 1.
    else:
        custo = 1

    # Chamadas recursivas para as três operações possíveis
    # 1. Remover o último caractere de s1
    remocao = distancia_edicao_recursiva(s1[:-1], s2) + 1
    
    # 2. Inserir o último caractere de s2 em s1
    insercao = distancia_edicao_recursiva(s1, s2[:-1]) + 1
    
    # 3. Substituir (ou manter, se os caracteres forem iguais)
    substituicao = distancia_edicao_recursiva(s1[:-1], s2[:-1]) + custo

    # Retorna o custo mínimo entre as três operações
    return min(remocao, insercao, substituicao)



def distancia_edicao_dp(s1:str, s2:str) -> int:
    """
    Calcula a Distância de Edição entre s1 e s2 usando Programação Dinâmica.
    """
    m, n = len(s1), len(s2)

    # Cria uma matriz (m+1)x(n+1) para armazenar os resultados.
    # A linha/coluna extra é para lidar com strings vazias.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Preenche a primeira linha e a primeira coluna da matriz.
    # Custo de transformar uma string vazia em outra.
    for i in range(m + 1):
        dp[i][0] = i  # Custo de 'i' remoções
    for j in range(n + 1):
        dp[0][j] = j  # Custo de 'j' inserções

    # Preenche o resto da matriz
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # O índice da string é i-1 e j-1 porque a matriz tem tamanho m+1, n+1
            if s1[i-1] == s2[j-1]:
                custo = 0
            else:
                custo = 1

            # Pega o valor mínimo das células vizinhas (que representam as operações)
            remocao = dp[i-1][j] + 1
            insercao = dp[i][j-1] + 1
            substituicao = dp[i-1][j-1] + custo
            
            dp[i][j] = min(remocao, insercao, substituicao)
    
    # O resultado final está na última célula da matriz
    return dp[m][n]


if __name__ == "__main__":
    # --- Exemplo 1: Simples ---
    palavra1 = "BOLO"
    palavra2 = "BOLA"
    
    print(f"--- Comparando '{palavra1}' e '{palavra2}' ---")
    dist_dp = distancia_edicao_dp(palavra1, palavra2)
    dist_recursivo = distancia_edicao_recursiva(palavra1, palavra2)
    print(f"Distância (Programação Dinâmica): {dist_dp}")
    print(f"Distância (Recursiva): {dist_recursivo}")
    # A versão recursiva seria rápida aqui, pois as strings são pequenas
    # dist_rec = distancia_edicao_recursiva(palavra1, palavra2) 
    # print(f"Distância (Recursiva): {dist_rec}")
    print("-" * 30)

    # --- Exemplo 2: Mais complexo ---
    palavra3 = "SÁBADO"
    palavra4 = "DOMINGO"

    print(f"--- Comparando '{palavra3}' e '{palavra4}' ---")
    dist_dp_2 = distancia_edicao_dp(palavra3, palavra4)
    dist_rec_2 = distancia_edicao_recursiva(palavra3, palavra4)
    print(f"Distância (Programação Dinâmica): {dist_dp_2}")
    print(f"Distância (Recursiva): {dist_rec_2}")
    
    # AVISO: A versão recursiva para este exemplo já será BEM LENTA.
    # Descomente a linha abaixo por sua conta e risco para ver a diferença!
    # dist_rec_2 = distancia_edicao_recursiva(palavra3, palavra4)
    # print(f"Distância (Recursiva): {dist_rec_2}")
    print("-" * 30)