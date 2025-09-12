import random
import os



def gerar_numeros_e_salvar(quantidade:int):
    """
    Gera e salva três arquivos de texto com números apenas se os arquivos não existirem:
    - um com números crescentes
    - um com decrescentes
    - um com números aleatórios (embaralhando a sequência de 1 a N)

    O nome de cada arquivo inclui a quantidade de números gerados.

    Args:
        quantidade (int): A quantidade de números a serem gerados em cada arquivo.
    """
    
    # --- Gerar e salvar números crescentes ---
    nome_arquivo_crescente = f'Arquivos_testes/crescentes_{quantidade}.txt'
    if os.path.exists(nome_arquivo_crescente):
        print(f"Arquivo '{nome_arquivo_crescente}' já existe. Pulando geração.")
    else:
        print(f"Gerando {quantidade} números crescentes e salvando em '{nome_arquivo_crescente}'...")
        with open(nome_arquivo_crescente, 'w') as arquivo:
            for i in range(1, quantidade + 1):
                arquivo.write(f"{i}\n")

    # --- Gerar e salvar números decrescentes ---
    nome_arquivo_decrescente = f'Arquivos_testes/decrescentes_{quantidade}.txt'
    if os.path.exists(nome_arquivo_decrescente):
        print(f"Arquivo '{nome_arquivo_decrescente}' já existe. Pulando geração.")
    else:
        print(f"Gerando {quantidade} números decrescentes e salvando em '{nome_arquivo_decrescente}'...")
        with open(nome_arquivo_decrescente, 'w') as arquivo:
            for i in range(quantidade, 0, -1):
                arquivo.write(f"{i}\n")

    # --- Gerar e salvar números aleatórios (embaralhados) ---
    nome_arquivo_aleatorio = f'Arquivos_testes/aleatorios_{quantidade}.txt'
    if os.path.exists(nome_arquivo_aleatorio):
        print(f"Arquivo '{nome_arquivo_aleatorio}' já existe. Pulando geração.")
    else:
        print(f"Gerando {quantidade} números aleatórios (embaralhados) e salvando em '{nome_arquivo_aleatorio}'...")

        # 1. Cria uma lista com todos os números de 1 até a quantidade
        numeros = list(range(1, quantidade + 1))
        
        # 2. Embaralha a lista de forma aleatória
        random.shuffle(numeros)
        
        # 3. Salva a lista embaralhada no arquivo
        with open(nome_arquivo_aleatorio, 'w') as arquivo:
            for numero in numeros:
                arquivo.write(f"{numero}\n")
    
    print("\nOperação concluída!")

#funçao especifica para gerar 10mil numeros com 5 digitos para o radix sort
def gerar_10mil_numeros_com_5_digitos_e_salvar():
    
    
    
     # --- Gerar e salvar números crescentes ---
    nome_arquivo_crescente = f'Arquivos_testes/crescentes_radix.txt'
    if os.path.exists(nome_arquivo_crescente):
        print(f"Arquivo '{nome_arquivo_crescente}' já existe. Pulando geração.")
    else:
        
        with open(nome_arquivo_crescente, 'w') as arquivo:
            for i in range(10000, 100000):
                arquivo.write(f"{i}\n")

    # --- Gerar e salvar números decrescentes ---
    nome_arquivo_decrescente = f'Arquivos_testes/decrescentes_radix.txt'
    if os.path.exists(nome_arquivo_decrescente):
        print(f"Arquivo '{nome_arquivo_decrescente}' já existe. Pulando geração.")
    else:
        
        with open(nome_arquivo_decrescente, 'w') as arquivo:
            for i in range(10000, 100000):
                arquivo.write(f"{i}\n")

    # --- Gerar e salvar números aleatórios (embaralhados) ---
    nome_arquivo_aleatorio = f'Arquivos_testes/aleatorios_radix.txt'
    if os.path.exists(nome_arquivo_aleatorio):
        print(f"Arquivo '{nome_arquivo_aleatorio}' já existe. Pulando geração.")
    else:

        # 1. Cria uma lista com todos os números de 1 até a quantidade
        numeros = list(range(10000, 100000))

        # 2. Embaralha a lista de forma aleatória
        random.shuffle(numeros)
        
        # 3. Salva a lista embaralhada no arquivo
        with open(nome_arquivo_aleatorio, 'w') as arquivo:
            for numero in numeros:
                arquivo.write(f"{numero}\n")
    
    print("\nOperação concluída!")
    

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
    Verifica se o arquivo existe. Se existir, escreve no arquivo existente;
    caso contrário, cria um novo arquivo.

    Args:
        nome_arquivo (str): O nome do arquivo onde o conteúdo será escrito.
        conteudo (str): O conteúdo a ser escrito no arquivo.
    """
    try:
        mode = 'a' if os.path.exists(nome_arquivo) else 'w'
        with open(nome_arquivo, mode) as arquivo:
            arquivo.write(conteudo)
        if mode == 'a':
            print(f"Conteúdo adicionado ao arquivo existente '{nome_arquivo}'.")
        else:
            print(f"Novo arquivo '{nome_arquivo}' criado e conteúdo escrito com sucesso.")
    except Exception as e:
        print(f"Erro ao escrever no arquivo '{nome_arquivo}': {e}")


def apagar_arquivo(nome_arquivo:str):
    """
    Apaga o arquivo especificado, se ele existir.

    Args:
        nome_arquivo (str): O nome do arquivo a ser apagado.
    """
    try:
        if os.path.exists(nome_arquivo):
            os.remove(nome_arquivo)
            print(f"Arquivo '{nome_arquivo}' apagado com sucesso.")
        else:
            print(f"O arquivo '{nome_arquivo}' não existe.")
    except Exception as e:
        print(f"Erro ao apagar o arquivo '{nome_arquivo}': {e}")

def limpar_arquivo(nome_arquivo:str):
    """
    Limpa o conteúdo do arquivo especificado, se ele existir.
    Se o arquivo não existir, cria um novo arquivo vazio.

    Args:
        nome_arquivo (str): O nome do arquivo a ser limpo ou criado.
    """
    try:
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'w') as arquivo:
                arquivo.truncate(0)
                
    except Exception as e:
        pass


# if __name__ == "__main__":

#     lista = ler_numeros_do_arquivo('Arquivos_testes/crescentes_100.txt')

#     print("Números lidos do arquivo:", lista)
