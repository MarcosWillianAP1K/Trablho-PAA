def distancia_edicao_recursiva(s1:str, s2:str) -> int:
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)
    if s1[-1] == s2[-1]:
        custo = 0
    else:
        custo = 1
        
    remocao = distancia_edicao_recursiva(s1[:-1], s2) + 1
    
    insercao = distancia_edicao_recursiva(s1, s2[:-1]) + 1
    
    substituicao = distancia_edicao_recursiva(s1[:-1], s2[:-1]) + custo

    return min(remocao, insercao, substituicao)



def distancia_edicao_prog_dinamica(s1:str, s2:str) -> int:
    """
    Calcula a Distância de Edição entre s1 e s2 usando Programação Dinâmica.
    """
    m, n = len(s1), len(s2) # Tamanhos das strings
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
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


