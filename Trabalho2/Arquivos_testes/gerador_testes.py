import Auxiliar.Manipulador_arquivos_txt as txt

class Gerador_testes:
    
    def __init__(self, diretorio_base:str = ""):

        self.diretorio_base = diretorio_base
    
    def gerar_testes_strings_tamanhos_iguais(self, tamanho_inicial:int, tamanho_final:int):
    
        def gerar_testes_strings_iguais(self, tamanho_inicial:int, tamanho_final:int):
            """
            Gera um arquivo de teste com duas strings iguais de tamanho 'tamanho'.
            """
            nome_arquivo = f"{self.diretorio_base}/tam_igual_strings_iguais_{tamanho_inicial}_a_{tamanho_final}.txt"
            arquivo = txt.Arquivo_txt(nome_arquivo)
            
            for tamanho in range(tamanho_inicial, tamanho_final + 1):
                s = 'a' * tamanho
                conteudo = f"{s}\n{s}\n"
                arquivo.escrever_no_arquivo(conteudo)
    
        def gerar_testes_strings_diferentes(self, tamanho_inicial:int, tamanho_final:int):
            """
            Gera um arquivo de teste com duas strings diferentes de tamanho 'tamanho'.
            """
            nome_arquivo = f"{self.diretorio_base}/tam_igual_strings_diferentes_{tamanho_inicial}_a_{tamanho_final}.txt"
            arquivo = txt.Arquivo_txt(nome_arquivo)
            
            
            for tamanho in range(tamanho_inicial, tamanho_final + 1):
                

                s1 = 'a' * tamanho
                s2 = 'b' * tamanho
                conteudo = f"{s1}\n{s2}\n"
                arquivo.escrever_no_arquivo(conteudo)
            
        def gerar_testes_strings_parciais(self, tamanho_inicial:int, tamanho_final:int):
            """
            Gera um arquivo de teste com duas strings que diferem em 'diferenca' caracteres.
            """
            nome_arquivo = f"{self.diretorio_base}/tam_igual_strings_parciais_{tamanho_inicial}_a_{tamanho_final}.txt"
            arquivo = txt.Arquivo_txt(nome_arquivo)
            
            for tamanho in range(tamanho_inicial, tamanho_final + 1):

                s1 = 'a' * tamanho
                s2 = 'a' * (tamanho // 2) + ('b' * (tamanho // 2) if tamanho % 2 == 0 else 'b' * (tamanho // 2 + 1))
                conteudo = f"{s1}\n{s2}\n"
                arquivo.escrever_no_arquivo(conteudo)
            
        def gerar_testes_strings_aleatorias(self, tamanho_inicial:int, tamanho_final:int):
            """
            Gera um arquivo de teste com duas strings aleatórias de tamanho 'tamanho'.
            """
            import random
            import string
            
            nome_arquivo = f"{self.diretorio_base}/tam_igual_strings_aleatorias_{tamanho_inicial}_a_{tamanho_final}.txt"
            arquivo = txt.Arquivo_txt(nome_arquivo)

            for tamanho in range(tamanho_inicial, tamanho_final + 1):
                

                s1 = ''.join(random.choices(string.ascii_lowercase, k=tamanho))
                s2 = ''.join(random.choices(string.ascii_lowercase, k=tamanho))
                conteudo = f"{s1}\n{s2}\n"
                arquivo.escrever_no_arquivo(conteudo)

        gerar_testes_strings_iguais(self, tamanho_inicial, tamanho_final)
        gerar_testes_strings_diferentes(self, tamanho_inicial, tamanho_final)
        gerar_testes_strings_parciais(self, tamanho_inicial, tamanho_final)
        gerar_testes_strings_aleatorias(self, tamanho_inicial, tamanho_final)
    
    def gerar_testes_strings_tamanhos_diferentes(self, tamanho1_inicial:int, tamanho1_final:int):
        
        def gerar_testes_strings_iguais(self, tamanho_inicial:int, tamanho_final:int):
            """
            Gera um arquivo de teste com duas strings iguais de tamanho 'tamanho'.
            """
            nome_arquivo = f"{self.diretorio_base}/tam_dif_strings_iguais_{tamanho_inicial}_a_{tamanho_final}.txt"
            arquivo = txt.Arquivo_txt(nome_arquivo)
            
            for tamanho in range(tamanho_inicial, tamanho_final + 1):
                s = 'a' * tamanho
                conteudo = f"{s}\n"
                arquivo.escrever_no_arquivo(conteudo)
    
        def gerar_testes_strings_diferentes(self, tamanho_inicial:int, tamanho_final:int):
            """
            Gera um arquivo de teste com duas strings diferentes de tamanho 'tamanho'.
            """

            nome_arquivo = f"{self.diretorio_base}/tam_dif_strings_diferentes_{tamanho_inicial}_a_{tamanho_final}.txt"
            arquivo = txt.Arquivo_txt(nome_arquivo)
            #Caso base
            s1 = 'a' * tamanho_inicial
            conteudo = f"{s1}\n"
            arquivo.escrever_no_arquivo(conteudo)
            
            #proximas strings a serem comparadas
            for tamanho in range(tamanho_inicial + 1, tamanho_final + 1):
                

                s2 = 'b' * tamanho
                conteudo = f"{s2}\n"
                arquivo.escrever_no_arquivo(conteudo)
            
        def gerar_testes_strings_parciais(self, tamanho_inicial:int, tamanho_final:int):
            """
            Gera um arquivo de teste com duas strings que diferem em 'diferenca' caracteres.
            """
            
            nome_arquivo = f"{self.diretorio_base}/tam_dif_strings_parciais_{tamanho_inicial}_a_{tamanho_final}.txt"
            arquivo = txt.Arquivo_txt(nome_arquivo)
            #Caso base
            s1 = 'a' * tamanho_inicial
            conteudo = f"{s1}\n"
            arquivo.escrever_no_arquivo(conteudo)
            
            for tamanho in range(tamanho_inicial, tamanho_final + 1):
                


                s2 = 'a' * (tamanho // 2) + ('b' * (tamanho // 2) if tamanho % 2 == 0 else 'b' * (tamanho // 2 + 1))
                conteudo = f"{s2}\n"
                arquivo.escrever_no_arquivo(conteudo)
            
        def gerar_testes_strings_aleatorias(self, tamanho_inicial:int, tamanho_final:int):
            """
            Gera um arquivo de teste com duas strings aleatórias de tamanho 'tamanho'.
            """
            import random
            import string
            
            nome_arquivo = f"{self.diretorio_base}/tam_dif_strings_aleatorias_{tamanho_inicial}_a_{tamanho_final}.txt"
            arquivo = txt.Arquivo_txt(nome_arquivo)

            #Caso base
            s1 = ''.join(random.choices(string.ascii_lowercase, k=tamanho_inicial))
            conteudo = f"{s1}\n"
            arquivo.escrever_no_arquivo(conteudo)
            
            for tamanho in range(tamanho_inicial, tamanho_final + 1):
                

                s2 = ''.join(random.choices(string.ascii_lowercase, k=tamanho))
                conteudo = f"{s2}\n"
                arquivo.escrever_no_arquivo(conteudo)
                
        gerar_testes_strings_iguais(self, tamanho1_inicial, tamanho1_final)
        gerar_testes_strings_diferentes(self, tamanho1_inicial, tamanho1_final)
        gerar_testes_strings_parciais(self, tamanho1_inicial, tamanho1_final)
        gerar_testes_strings_aleatorias(self, tamanho1_inicial, tamanho1_final)

    def deletar_all_testes(self):
        import os
        for arquivo in os.listdir(self.diretorio_base):
            if arquivo.startswith("tam_"):
                caminho_arquivo = os.path.join(self.diretorio_base, arquivo)
                arquivo_txt = txt.Arquivo_txt(caminho_arquivo)
                arquivo_txt.apagar_arquivo()
                
    def verificar_testes_existentes(self):
        import os
        arquivos_existentes = []
        for arquivo in os.listdir(self.diretorio_base):
            if arquivo.startswith("tam_"):
                arquivos_existentes.append(arquivo)
        return arquivos_existentes