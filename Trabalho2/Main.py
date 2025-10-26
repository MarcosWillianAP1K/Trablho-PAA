import sys
from pathlib import Path

# Adiciona temporariamente o pai ao path para importar setup_path
sys.path.insert(0, str(Path(__file__).parent.parent))

import setup_path #configura o path automaticamente
DIRETORIO_BASE = setup_path.configurar_path("Trabalho2")
TAMANHO_INICIAL = 10
TAMANHO_FINAL = 100
NUMERO_DE_VEZES_EXECUTAR = 1
    
import Trabalho2.Auxiliar.gerador_testes_resultados as gerador
import Trabalho2.Auxiliar.Cronometro as cronometro
import Trabalho2.Auxiliar.Medidor_memoria as medidor
import Trabalho2.Auxiliar.gerador_graficos as graficos
import Trabalho2.Algortimo.Distancia_de_edicao as algos

def gerar_testes():
    
    gerar = gerador.Gerador_testes(f"{DIRETORIO_BASE}/Arquivos_testes/", TAMANHO_INICIAL, TAMANHO_FINAL)
    
    # print(gerar.diretorio_base)
    
    gerar.gerar_testes_strings_tamanhos_iguais()
    gerar.gerar_testes_strings_tamanhos_diferentes()
    

def coletar_strings_de_arquivo(arquivo):
    linha1 = arquivo.readline().strip()
    linha2 = arquivo.readline().strip()
    return linha1, linha2

def executar_testes_prog_dinamica():
    
    def executar_teste(string1:str, string2:str):
        cronometro_execucao = cronometro.Cronometro()
        medidor_memoria = medidor.MedidorMemoria()
        
        medidor_memoria.iniciar_medicao
        cronometro_execucao.iniciar()
        
        algos.distancia_edicao_prog_dinamica(string1, string2)
        
        cronometro_execucao.parar()
        medidor_memoria.parar_medicao()
        
        tempo_execucao = cronometro_execucao.tempo_segundos()
        memoria_usada_MB = medidor_memoria.obter_memoria_MB()
        
        return tempo_execucao, memoria_usada_MB
    
    lista_tempos_iguais = []
    lista_tempos_diferentes = []
    lista_tempos_parciais = []
    lista_tempos_aleatorias = []
    
    memoria_iguais = []
    memoria_diferentes = []
    memoria_parciais = []
    memoria_aleatorias = []
    
    try:   
        arquivo_tam_iguais = open(f"{DIRETORIO_BASE}/Arquivos_testes/tam_igual_strings_iguais_{TAMANHO_INICIAL}_a_{TAMANHO_FINAL}.txt", "r")


        for _ in range(TAMANHO_INICIAL, TAMANHO_FINAL + 1):
            linha1, linha2 = coletar_strings_de_arquivo(arquivo_tam_iguais)
            tempo, memoria = executar_teste(linha1, linha2)
            lista_tempos_iguais.append(tempo)
            memoria_iguais.append(memoria)

        arquivo_tam_iguais.close()

        arquivo_tam_diferentes = open(f"{DIRETORIO_BASE}/Arquivos_testes/tam_igual_strings_diferentes_{TAMANHO_INICIAL}_a_{TAMANHO_FINAL}.txt", "r")
        
        for _ in range(TAMANHO_INICIAL, TAMANHO_FINAL + 1):
            linha1, linha2 = coletar_strings_de_arquivo(arquivo_tam_diferentes)
            tempo, memoria = executar_teste(linha1, linha2)
            lista_tempos_diferentes.append(tempo)
            memoria_diferentes.append(memoria)
        arquivo_tam_diferentes.close()


        arquivo_tam_parciais = open(f"{DIRETORIO_BASE}/Arquivos_testes/tam_igual_strings_parciais_{TAMANHO_INICIAL}_a_{TAMANHO_FINAL}.txt", "r")

        for _ in range(TAMANHO_INICIAL, TAMANHO_FINAL + 1):
            linha1, linha2 = coletar_strings_de_arquivo(arquivo_tam_parciais)
            tempo, memoria = executar_teste(linha1, linha2)
            lista_tempos_parciais.append(tempo)
            memoria_parciais.append(memoria)
        arquivo_tam_parciais.close()

        arquivo_tam_aleatorias = open(f"{DIRETORIO_BASE}/Arquivos_testes/tam_igual_strings_aleatorias_{TAMANHO_INICIAL}_a_{TAMANHO_FINAL}.txt", "r")

        for _ in range(TAMANHO_INICIAL, TAMANHO_FINAL + 1):
            linha1, linha2 = coletar_strings_de_arquivo(arquivo_tam_aleatorias)
            tempo, memoria = executar_teste(linha1, linha2)
            lista_tempos_aleatorias.append(tempo)
            memoria_aleatorias.append(memoria)
        arquivo_tam_aleatorias.close()
        
        resultado = gerador.gerador_resultados(DIRETORIO_BASE + "/Resultados/", TAMANHO_INICIAL, TAMANHO_FINAL)
        resultado.escrever_resultado_tam_iguais(lista_tempos_iguais, memoria_iguais, lista_tempos_diferentes, memoria_diferentes, lista_tempos_parciais, memoria_parciais, lista_tempos_aleatorias, memoria_aleatorias)
        
    except Exception as e:
        print(f"Erro ao abrir arquivos de teste: {e}")
        return

    

def executar_testes_recursivo():
    pass

if __name__ == "__main__":
    
    # gerar_testes()
    executar_testes_prog_dinamica()
    