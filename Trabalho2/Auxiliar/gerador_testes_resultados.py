import Auxiliar.Manipulador_arquivos_txt as txt

class Gerador_testes:
    
    def __init__(self, diretorio_base:str = "",  tamanho_inicial:int = 0, tamanho_final:int = 0):

        self.diretorio_base = diretorio_base
        self.tamanho_inicial = tamanho_inicial
        self.tamanho_final = tamanho_final

    def gerar_testes_strings_tamanhos_iguais(self):
        
        def gerar_testes_strings_iguais(self):
            """
            Gera um arquivo de teste com duas strings iguais de tamanho 'tamanho'.
            """
            nome_arquivo = f"{self.diretorio_base}tam_igual_strings_iguais_{self.tamanho_inicial}_a_{self.tamanho_final}.txt"
            arquivo = txt.Arquivo_txt(nome_arquivo)
            
            arquivo.limpar_arquivo()

            for tamanho in range(self.tamanho_inicial, self.tamanho_final + 1):
                s = 'a' * tamanho
                conteudo = f"{s}\n{s}\n"
                arquivo.escrever_no_arquivo(conteudo)

        def gerar_testes_strings_diferentes(self):
            """
            Gera um arquivo de teste com duas strings diferentes de tamanho 'tamanho'.
            """
            nome_arquivo = f"{self.diretorio_base}tam_igual_strings_diferentes_{self.tamanho_inicial}_a_{self.tamanho_final}.txt"
            arquivo = txt.Arquivo_txt(nome_arquivo)
            arquivo.limpar_arquivo()

            for tamanho in range(self.tamanho_inicial, self.tamanho_final + 1):


                s1 = 'a' * tamanho
                s2 = 'b' * tamanho
                conteudo = f"{s1}\n{s2}\n"
                arquivo.escrever_no_arquivo(conteudo)

        def gerar_testes_strings_parciais(self):
            """
            Gera um arquivo de teste com duas strings que diferem em 'diferenca' caracteres.
            """
            nome_arquivo = f"{self.diretorio_base}tam_igual_strings_parciais_{self.tamanho_inicial}_a_{self.tamanho_final}.txt"
            arquivo = txt.Arquivo_txt(nome_arquivo)
            arquivo.limpar_arquivo()

            for tamanho in range(self.tamanho_inicial, self.tamanho_final + 1):

                s1 = 'a' * tamanho
                s2 = 'a' * (tamanho // 2) + ('b' * (tamanho // 2) if tamanho % 2 == 0 else 'b' * (tamanho // 2 + 1))
                conteudo = f"{s1}\n{s2}\n"
                arquivo.escrever_no_arquivo(conteudo)
            
        def gerar_testes_strings_aleatorias(self):
            """
            Gera um arquivo de teste com duas strings aleatórias de tamanho 'tamanho'.
            """
            import random
            import string

            nome_arquivo = f"{self.diretorio_base}/tam_igual_strings_aleatorias_{self.tamanho_inicial}_a_{self.tamanho_final}.txt"
            arquivo = txt.Arquivo_txt(nome_arquivo)
            arquivo.limpar_arquivo()

            for tamanho in range(self.tamanho_inicial, self.tamanho_final + 1):
                

                s1 = ''.join(random.choices(string.ascii_lowercase, k=tamanho))
                s2 = ''.join(random.choices(string.ascii_lowercase, k=tamanho))
                conteudo = f"{s1}\n{s2}\n"
                arquivo.escrever_no_arquivo(conteudo)

        gerar_testes_strings_iguais(self)
        gerar_testes_strings_diferentes(self)
        gerar_testes_strings_parciais(self)
        gerar_testes_strings_aleatorias(self)

    def gerar_testes_strings_tamanhos_diferentes(self):

        def gerar_testes_strings_iguais(self):
            """
            Gera um arquivo de teste com duas strings iguais de tamanho 'tamanho'.
            """
            nome_arquivo = f"{self.diretorio_base}/tam_dif_strings_iguais_{self.tamanho_inicial}_a_{self.tamanho_final}.txt"
            arquivo = txt.Arquivo_txt(nome_arquivo)
            arquivo.limpar_arquivo()

            for tamanho in range(self.tamanho_inicial + 1, self.tamanho_final + 1):
                s = 'a' * tamanho
                conteudo = f"{s}\n"
                arquivo.escrever_no_arquivo(conteudo)

        def gerar_testes_strings_diferentes(self):
            """
            Gera um arquivo de teste com duas strings diferentes de tamanho 'tamanho'.
            """

            nome_arquivo = f"{self.diretorio_base}/tam_dif_strings_diferentes_{self.tamanho_inicial}_a_{self.tamanho_final}.txt"
            arquivo = txt.Arquivo_txt(nome_arquivo)
            arquivo.limpar_arquivo()
            #Caso base
            s1 = 'a' * self.tamanho_inicial
            conteudo = f"{s1}\n"
            arquivo.escrever_no_arquivo(conteudo)
            
            #proximas strings a serem comparadas
            for tamanho in range(self.tamanho_inicial + 1, self.tamanho_final + 1):
                

                s2 = 'b' * tamanho
                conteudo = f"{s2}\n"
                arquivo.escrever_no_arquivo(conteudo)
            
        def gerar_testes_strings_parciais(self):
            """
            Gera um arquivo de teste com duas strings que diferem em 'diferenca' caracteres.
            """

            nome_arquivo = f"{self.diretorio_base}/tam_dif_strings_parciais_{self.tamanho_inicial}_a_{self.tamanho_final}.txt"
            arquivo = txt.Arquivo_txt(nome_arquivo)
            arquivo.limpar_arquivo()
            #Caso base
            s1 = 'a' * self.tamanho_inicial
            conteudo = f"{s1}\n"
            arquivo.escrever_no_arquivo(conteudo)

            for tamanho in range(self.tamanho_inicial + 1, self.tamanho_final + 1):



                s2 = 'a' * (tamanho // 2) + ('b' * (tamanho // 2) if tamanho % 2 == 0 else 'b' * (tamanho // 2 + 1))
                conteudo = f"{s2}\n"
                arquivo.escrever_no_arquivo(conteudo)

        def gerar_testes_strings_aleatorias(self):
            """
            Gera um arquivo de teste com duas strings aleatórias de tamanho 'tamanho'.
            """
            import random
            import string

            nome_arquivo = f"{self.diretorio_base}/tam_dif_strings_aleatorias_{self.tamanho_inicial}_a_{self.tamanho_final}.txt"
            arquivo = txt.Arquivo_txt(nome_arquivo)
            arquivo.limpar_arquivo()

            #Caso base
            s1 = ''.join(random.choices(string.ascii_lowercase, k=self.tamanho_inicial))
            conteudo = f"{s1}\n"
            arquivo.escrever_no_arquivo(conteudo)

            for tamanho in range(self.tamanho_inicial + 1, self.tamanho_final + 1):


                s2 = ''.join(random.choices(string.ascii_lowercase, k=tamanho))
                conteudo = f"{s2}\n"
                arquivo.escrever_no_arquivo(conteudo)

        gerar_testes_strings_iguais(self)
        gerar_testes_strings_diferentes(self)
        gerar_testes_strings_parciais(self)
        gerar_testes_strings_aleatorias(self)

    def deletar_all_testes(self):
        import os
        for arquivo in os.listdir(self.diretorio_base):
            if arquivo.startswith("tam_"):
                caminho_arquivo = os.path.join(self.diretorio_base, arquivo)
                arquivo_txt = txt.Arquivo_txt(caminho_arquivo)
                arquivo_txt.apagar_arquivo()
    
    
class gerador_resultados:
    
    def __init__(self, diretorio_base:str = "", tamanho_inicial:int = 0, tamanho_final:int = 0):
        self.diretorio_base = diretorio_base
        self.tamanho_inicial = tamanho_inicial
        self.tamanho_final = tamanho_final

    def escrever_resultado_tam_iguais(self, tempo_iguais:list[float], memoria_iguais:list[float], tempo_diferentes:list[float], memoria_diferentes:list[float],
                                      tempo_parciais:list[float], memoria_parciais:list[float], tempo_aleatorias:list[float], memoria_aleatorias:list[float]):

        if not tempo_iguais or not tempo_diferentes or not tempo_parciais or not tempo_aleatorias:
            return

        nome_arquivo = f"{self.diretorio_base}Resultados_string_tam_iguais_{self.tamanho_inicial}_a_{self.tamanho_final}.txt"
        arquivo = txt.Arquivo_txt(nome_arquivo)
        arquivo.limpar_arquivo()
        
        arquivo.escrever_no_arquivo(f"Resultados para strings de tamanhos iguais de {self.tamanho_inicial} a {self.tamanho_final}\n")
        arquivo.escrever_no_arquivo(f"Executado {len(tempo_iguais)} vezes para cada teste:\n\n")
        arquivo.escrever_no_arquivo("\n--------------------------------\n\n")
        
        tempo_medio = sum(tempo_iguais) / len(tempo_iguais)
        memoria_media_gasta = sum(memoria_iguais) / len(memoria_iguais)
        
        arquivo.escrever_no_arquivo(f"Tempo medio strings iguais: {tempo_medio}\n")
        arquivo.escrever_no_arquivo(f"Memoria media gasta strings iguais: {memoria_media_gasta}\n")

        tempo_medio = sum(tempo_diferentes) / len(tempo_diferentes)
        memoria_media_gasta = sum(memoria_diferentes) / len(memoria_diferentes)

        arquivo.escrever_no_arquivo(f"Tempo medio strings diferentes: {tempo_medio}\n")
        arquivo.escrever_no_arquivo(f"Memoria media gasta strings diferentes: {memoria_media_gasta}\n")

        tempo_medio = sum(tempo_parciais) / len(tempo_parciais)
        memoria_media_gasta = sum(memoria_parciais) / len(memoria_parciais)

        arquivo.escrever_no_arquivo(f"Tempo medio strings parciais: {tempo_medio}\n")
        arquivo.escrever_no_arquivo(f"Memoria media gasta strings parciais: {memoria_media_gasta}\n")

        tempo_medio = sum(tempo_aleatorias) / len(tempo_aleatorias)
        memoria_media_gasta = sum(memoria_aleatorias) / len(memoria_aleatorias)

        arquivo.escrever_no_arquivo(f"Tempo medio strings aleatorias: {tempo_medio}\n")
        arquivo.escrever_no_arquivo(f"Memoria media gasta strings aleatorias: {memoria_media_gasta}\n")

        arquivo.escrever_no_arquivo("\n--------------------------------")

    def escrever_resultado_tam_diferentes(self, tempo_iguais:list[float], memoria_iguais:list[float], tempo_diferentes:list[float], memoria_diferentes:list[float],
                                          tempo_parciais:list[float], memoria_parciais:list[float], tempo_aleatorias:list[float], memoria_aleatorias:list[float]):

        if not tempo_iguais or not tempo_diferentes or not tempo_parciais or not tempo_aleatorias:
            return
        
        nome_arquivo = f"{self.diretorio_base}Resultados_string_tam_diferentes_{self.tamanho_inicial}_a_{self.tamanho_final}.txt"
        arquivo = txt.Arquivo_txt(nome_arquivo)
        arquivo.limpar_arquivo()

        arquivo.escrever_no_arquivo(f"Resultados para strings de tamanhos diferentes de {self.tamanho_inicial} a {self.tamanho_final}\n")
        arquivo.escrever_no_arquivo(f"Executado {len(tempo_iguais)} vezes para cada teste:\n\n")
        arquivo.escrever_no_arquivo("\n--------------------------------\n\n")
        
        tempo_medio = sum(tempo_iguais) / len(tempo_iguais)
        memoria_media_gasta = sum(memoria_iguais) / len(memoria_iguais)

        arquivo.escrever_no_arquivo(f"Tempo medio strings iguais: {tempo_medio}\n")
        arquivo.escrever_no_arquivo(f"Memoria media gasta strings iguais: {memoria_media_gasta}\n")

        tempo_medio = sum(tempo_diferentes) / len(tempo_diferentes)
        memoria_media_gasta = sum(memoria_diferentes) / len(memoria_diferentes)

        arquivo.escrever_no_arquivo(f"Tempo medio strings diferentes: {tempo_medio}\n")
        arquivo.escrever_no_arquivo(f"Memoria media gasta strings diferentes: {memoria_media_gasta}\n")

        tempo_medio = sum(tempo_parciais) / len(tempo_parciais)
        memoria_media_gasta = sum(memoria_parciais) / len(memoria_parciais)

        arquivo.escrever_no_arquivo(f"Tempo medio strings parciais: {tempo_medio}\n")
        arquivo.escrever_no_arquivo(f"Memoria media gasta strings parciais: {memoria_media_gasta}\n")

        tempo_medio = sum(tempo_aleatorias) / len(tempo_aleatorias)
        memoria_media_gasta = sum(memoria_aleatorias) / len(memoria_aleatorias)

        arquivo.escrever_no_arquivo(f"Tempo medio strings aleatorias: {tempo_medio}\n")
        arquivo.escrever_no_arquivo(f"Memoria media gasta strings aleatorias: {memoria_media_gasta}\n")

        arquivo.escrever_no_arquivo("\n--------------------------------")
    
    
                                                                              
    def deletar_all_resultados(self):
        import os
        for arquivo in os.listdir(self.diretorio_base):
            if arquivo.startswith("Resultados_"):
                caminho_arquivo = os.path.join(self.diretorio_base, arquivo)
                arquivo_txt = txt.Arquivo_txt(caminho_arquivo)
                arquivo_txt.apagar_arquivo()
    