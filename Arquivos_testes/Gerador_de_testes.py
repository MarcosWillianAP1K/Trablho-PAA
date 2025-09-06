import random

def gerar_numeros_e_salvar(quantidade):
    """
    Gera e salva três arquivos de texto com números:
    - um com números crescentes
    - um com decrescentes
    - um com números aleatórios (embaralhando a sequência de 1 a N)

    O nome de cada arquivo inclui a quantidade de números gerados.

    Args:
        quantidade (int): A quantidade de números a serem gerados em cada arquivo.
    """
    
    # --- Gerar e salvar números crescentes ---
    nome_arquivo_crescente = f'Arquivos_testes/crescentes_{quantidade}.txt'
    print(f"Gerando {quantidade} números crescentes e salvando em '{nome_arquivo_crescente}'...")
    with open(nome_arquivo_crescente, 'w') as arquivo:
        for i in range(1, quantidade + 1):
            arquivo.write(f"{i}\n")

    # --- Gerar e salvar números decrescentes ---
    nome_arquivo_decrescente = f'Arquivos_testes/decrescentes_{quantidade}.txt'
    print(f"Gerando {quantidade} números decrescentes e salvando em '{nome_arquivo_decrescente}'...")
    with open(nome_arquivo_decrescente, 'w') as arquivo:
        for i in range(quantidade, 0, -1):
            arquivo.write(f"{i}\n")

    # --- Gerar e salvar números aleatórios (embaralhados) ---
    nome_arquivo_aleatorio = f'Arquivos_testes/aleatorios_{quantidade}.txt'
    print(f"Gerando {quantidade} números aleatórios (embaralhados) e salvando em '{nome_arquivo_aleatorio}'...")

    # 1. Cria uma lista com todos os números de 1 até a quantidade
    numeros = list(range(1, quantidade + 1))
    
    # 2. Embaralha a lista de forma aleatória
    random.shuffle(numeros)
    
    # 3. Salva a lista embaralhada no arquivo
    with open(nome_arquivo_aleatorio, 'w') as arquivo:
        for numero in numeros:
            arquivo.write(f"{numero}\n")
    
    print("\nTodos os três arquivos foram gerados com sucesso!")





