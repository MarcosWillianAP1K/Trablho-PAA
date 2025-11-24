

def distancia_edicao_gulosa(s1: str, s2: str) -> int:
    """
    Calcula a Distância de Edição usando uma abordagem GULOSA.
    
    Estratégia gulosa: A cada passo, escolhe a operação que parece mais vantajosa
    localmente (compara caracteres da esquerda para direita e faz a escolha imediata).
    
    ATENÇÃO: Esta abordagem NÃO garante a solução ótima, pois o problema de 
    distância de edição não possui a propriedade de escolha gulosa.
    """
    i, j = 0, 0
    operacoes = 0
    
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            # Caracteres iguais, avança sem custo
            i += 1
            j += 1
        else:
            # Caracteres diferentes: escolhe gulosa a operação que avança mais
            # Sempre escolhe substituição (avança ambos os índices)
            operacoes += 1
            i += 1
            j += 1
    
    # Adiciona operações para caracteres restantes
    operacoes += (len(s1) - i)  # Remoções restantes
    operacoes += (len(s2) - j)  # Inserções restantes
    
    return operacoes


def distancia_edicao_backtracking(s1: str, s2: str) -> int:
    """
    Calcula a Distância de Edição usando BACKTRACKING.
    
    Explora todas as possibilidades de forma sistemática, fazendo escolhas
    e voltando atrás (backtrack) quando necessário para encontrar a solução ótima.
    
    Esta abordagem é similar à recursiva, mas com uma estrutura explícita de
    exploração de todas as possibilidades.
    """
    def backtrack(i: int, j: int) -> int:
        """
        Função auxiliar de backtracking.
        
        Args:
            i: Índice atual na string s1
            j: Índice atual na string s2
        
        Returns:
            Distância mínima de edição para os sufixos s1[i:] e s2[j:]
        """
        # Casos base
        if i == len(s1):
            return len(s2) - j  # Inserir caracteres restantes de s2
        
        if j == len(s2):
            return len(s1) - i  # Remover caracteres restantes de s1
        
        # Se caracteres são iguais, não há custo
        if s1[i] == s2[j]:
            return backtrack(i + 1, j + 1)
        
        # Explora todas as três possibilidades (backtracking)
        # 1. Inserir caractere de s2
        insercao = 1 + backtrack(i, j + 1)
        
        # 2. Remover caractere de s1
        remocao = 1 + backtrack(i + 1, j)
        
        # 3. Substituir caractere
        substituicao = 1 + backtrack(i + 1, j + 1)
        
        # Retorna o mínimo das três opções
        return min(insercao, remocao, substituicao)
    
    return backtrack(0, 0)


def distancia_edicao_backtracking_com_poda(s1: str, s2: str) -> int:
    """
    Versão otimizada do backtracking com PODA (pruning).
    
    Mantém track da melhor solução encontrada até o momento e poda
    ramos que não podem levar a uma solução melhor.
    """
    melhor_custo = [float('inf')]  # Usando lista para permitir modificação em função aninhada
    
    def backtrack_poda(i: int, j: int, custo_atual: int) -> int:
        """
        Backtracking com poda.
        
        Args:
            i: Índice atual na string s1
            j: Índice atual na string s2
            custo_atual: Custo acumulado até agora
        
        Returns:
            Distância mínima de edição
        """
        # Poda: se o custo atual já é maior que o melhor, abandona este ramo
        if custo_atual >= melhor_custo[0]:
            return melhor_custo[0]
        
        # Casos base
        if i == len(s1):
            custo_final = custo_atual + (len(s2) - j)
            melhor_custo[0] = min(melhor_custo[0], custo_final)
            return custo_final
        
        if j == len(s2):
            custo_final = custo_atual + (len(s1) - i)
            melhor_custo[0] = min(melhor_custo[0], custo_final)
            return custo_final
        
        # Se caracteres são iguais
        if s1[i] == s2[j]:
            return backtrack_poda(i + 1, j + 1, custo_atual)
        
        # Explora as três possibilidades
        resultado_minimo = float('inf')
        
        # 1. Inserção
        resultado_minimo = min(resultado_minimo, backtrack_poda(i, j + 1, custo_atual + 1))
        
        # 2. Remoção
        resultado_minimo = min(resultado_minimo, backtrack_poda(i + 1, j, custo_atual + 1))
        
        # 3. Substituição
        resultado_minimo = min(resultado_minimo, backtrack_poda(i + 1, j + 1, custo_atual + 1))
        
        return resultado_minimo
    
    return backtrack_poda(0, 0, 0)



