import random



def gerar_numeros_e_salvar(quantidade:int):
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


def ler_numeros_do_arquivo(nome_arquivo:str):
    """
    Lê números de um arquivo de texto, um por linha, e retorna uma lista de inteiros.
    
    Args:
        nome_arquivo (str): O nome do arquivo a ser lido.

    Returns:
        list: Uma lista de inteiros com os números do arquivo, ou uma lista vazia se houver um erro.
    """
    numeros_lidos = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                # Remove espaços em branco e quebras de linha, e converte para inteiro
                numeros_lidos.append(int(linha.strip()))
        print(f"Arquivo '{nome_arquivo}' lido com sucesso.")
        return numeros_lidos
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return []
    except ValueError:
        print(f"Erro: O arquivo '{nome_arquivo}' contém dados inválidos (não são números).")
        return []


def escrever_no_arquivo(nome_arquivo:str, conteudo:str):
    """
    Escreve o conteúdo fornecido em um arquivo de texto.

    Args:
        nome_arquivo (str): O nome do arquivo onde o conteúdo será escrito.
        conteudo (str): O conteúdo a ser escrito no arquivo.
    """
    try:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(conteudo)
        print(f"Conteúdo escrito com sucesso no arquivo '{nome_arquivo}'.")
    except Exception as e:
        print(f"Erro ao escrever no arquivo '{nome_arquivo}': {e}")


# if __name__ == "__main__":

#     lista = ler_numeros_do_arquivo('Arquivos_testes/crescentes_100.txt')

#     print("Números lidos do arquivo:", lista)
