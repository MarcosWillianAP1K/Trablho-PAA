import random
import os




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
