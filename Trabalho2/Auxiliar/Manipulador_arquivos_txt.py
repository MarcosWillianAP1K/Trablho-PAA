import random
import os


class Arquivo_txt:
    
    def __init__(self, diretorio_arquivo:str):
        self.diretorio_arquivo = diretorio_arquivo

    def escrever_no_arquivo(self, conteudo:str):
        """
        Verifica se o arquivo existe. Se existir, escreve no arquivo existente;
    caso contrário, cria um novo arquivo.

    Args:
        nome_arquivo (str): O nome do arquivo onde o conteúdo será escrito.
        conteudo (str): O conteúdo a ser escrito no arquivo.
    """
        try:
            mode = 'a' if os.path.exists(self.diretorio_arquivo) else 'w'
            with open(self.diretorio_arquivo, mode) as arquivo:
                arquivo.write(conteudo)
            if mode == 'a':
                print(f"Conteúdo adicionado ao arquivo existente '{self.diretorio_arquivo}'.")
            else:
                print(f"Novo arquivo '{self.diretorio_arquivo}' criado e conteúdo escrito com sucesso.")
        except Exception as e:
            print(f"Erro ao escrever no arquivo '{self.diretorio_arquivo}': {e}")


    def apagar_arquivo(self):
        """
        Apaga o arquivo especificado, se ele existir.

        Args:
            nome_arquivo (str): O nome do arquivo a ser apagado.
        """
        try:
            if os.path.exists(self.diretorio_arquivo):
                os.remove(self.diretorio_arquivo)
                print(f"Arquivo '{self.diretorio_arquivo}' apagado com sucesso.")
            else:
                print(f"O arquivo '{self.diretorio_arquivo}' não existe.")
        except Exception as e:
            print(f"Erro ao apagar o arquivo '{self.diretorio_arquivo}': {e}")


    def limpar_arquivo(self):
            """
            Limpa o conteúdo do arquivo especificado, se ele existir.
            Se o arquivo não existir, cria um novo arquivo vazio.

            Args:
                nome_arquivo (str): O nome do arquivo a ser limpo ou criado.
            """
            try:
                if os.path.exists(self.diretorio_arquivo):
                    with open(self.diretorio_arquivo, 'w') as arquivo:
                        arquivo.truncate(0)
                        
            except Exception as e:
                pass


