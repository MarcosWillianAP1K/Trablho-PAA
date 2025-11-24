import sys
from pathlib import Path

# Adiciona temporariamente o pai ao path para importar setup_path
sys.path.insert(0, str(Path(__file__).parent.parent))

import setup_path #configura o path automaticamente
DIRETORIO_BASE = setup_path.configurar_path("Trabalho2")
TAMANHO_INICIAL = 2
TAMANHO_FINAL = 10
NUMERO_DE_VEZES_EXECUTAR = 1


    
import Trabalho2.Auxiliar.gerador_testes_resultados as gerador
import Trabalho2.Auxiliar.Cronometro as cronometro
import Trabalho2.Auxiliar.Medidor_memoria as medidor
# import Trabalho2.Auxiliar.gerador_graficos as graficos
import Trabalho2.Algortimo.Distancia_de_edicao as algos

def gerar_testes():
    print("Gerando arquivos de teste...")
    gerar = gerador.Gerador_testes(f"{DIRETORIO_BASE}/Arquivos_testes/", TAMANHO_INICIAL, TAMANHO_FINAL)
    
    gerar.gerar_testes_strings_tamanhos_iguais()
    gerar.gerar_testes_strings_tamanhos_diferentes()
    print("✓ Arquivos de teste gerados com sucesso!\n")

# Funções para coletar strings dos arquivos de teste

def coletar_strings_de_arquivo(arquivo):
    linha1 = arquivo.readline().strip()
    linha2 = arquivo.readline().strip()
    return linha1, linha2

def coletar_1_string_de_arquivo(arquivo):
    linha = arquivo.readline().strip()
    return linha



# Funções auxiliares para executar testes em lote

def executar_testes_em_lote_tam_iguais(executar_teste_func, tamanho_inicial, tamanho_final, diretorio_base):
    """
    Executa testes para strings de tamanhos iguais em todos os tipos de teste.
    
    Args:
        executar_teste_func: Função que executa um teste individual (prog_dinamica ou recursivo)
        tamanho_inicial: Tamanho inicial das strings
        tamanho_final: Tamanho final das strings
        diretorio_base: Diretório onde estão os arquivos de teste
    
    Returns:
        Tupla com 8 listas: (tempos_iguais, mem_iguais, tempos_dif, mem_dif, tempos_parc, mem_parc, tempos_aleat, mem_aleat)
    """
    tipos_teste = ['iguais', 'diferentes', 'parciais', 'aleatorias']
    resultados = {tipo: {'tempos': [], 'memorias': []} for tipo in tipos_teste}
    
    for tipo in tipos_teste:
        nome_arquivo = f"{diretorio_base}/Arquivos_testes/tam_igual_strings_{tipo}_{tamanho_inicial}_a_{tamanho_final}.txt"
        
        with open(nome_arquivo, "r") as arquivo:
            for _ in range(tamanho_inicial, tamanho_final + 1):
                linha1, linha2 = coletar_strings_de_arquivo(arquivo)
                tempo, memoria = executar_teste_func(linha1, linha2)
                resultados[tipo]['tempos'].append(tempo)
                resultados[tipo]['memorias'].append(memoria)
    
    return (
        resultados['iguais']['tempos'], resultados['iguais']['memorias'],
        resultados['diferentes']['tempos'], resultados['diferentes']['memorias'],
        resultados['parciais']['tempos'], resultados['parciais']['memorias'],
        resultados['aleatorias']['tempos'], resultados['aleatorias']['memorias']
    )


def executar_testes_em_lote_tam_diferentes(executar_teste_func, tamanho_inicial, tamanho_final, diretorio_base):
    """
    Executa testes para strings de tamanhos diferentes em todos os tipos de teste.
    
    Args:
        executar_teste_func: Função que executa um teste individual (prog_dinamica ou recursivo)
        tamanho_inicial: Tamanho inicial da primeira string
        tamanho_final: Tamanho final das strings comparadas
        diretorio_base: Diretório onde estão os arquivos de teste
    
    Returns:
        Tupla com 8 listas: (tempos_iguais, mem_iguais, tempos_dif, mem_dif, tempos_parc, mem_parc, tempos_aleat, mem_aleat)
    """
    tipos_teste = ['iguais', 'diferentes', 'parciais', 'aleatorias']
    resultados = {tipo: {'tempos': [], 'memorias': []} for tipo in tipos_teste}
    
    for tipo in tipos_teste:
        nome_arquivo = f"{diretorio_base}/Arquivos_testes/tam_dif_strings_{tipo}_{tamanho_inicial}_a_{tamanho_final}.txt"
        
        with open(nome_arquivo, "r") as arquivo:
            linha1 = coletar_1_string_de_arquivo(arquivo)
            
            for _ in range(tamanho_inicial + 1, tamanho_final + 1):
                linha2 = coletar_1_string_de_arquivo(arquivo)
                tempo, memoria = executar_teste_func(linha1, linha2)
                resultados[tipo]['tempos'].append(tempo)
                resultados[tipo]['memorias'].append(memoria)
    
    return (
        resultados['iguais']['tempos'], resultados['iguais']['memorias'],
        resultados['diferentes']['tempos'], resultados['diferentes']['memorias'],
        resultados['parciais']['tempos'], resultados['parciais']['memorias'],
        resultados['aleatorias']['tempos'], resultados['aleatorias']['memorias']
    )

#Função para executar o teste do algoritmo guloso


def executar_testes_guloso():
    """Executa todos os testes usando abordagem gulosa."""
    
    def executar_teste_guloso(string1:str, string2:str):
        cronometro_execucao = cronometro.Cronometro()
        medidor_memoria = medidor.MedidorMemoria()
            
        medidor_memoria.iniciar_medicao()  
        cronometro_execucao.iniciar()
            
        algos.distancia_edicao_gulosa(string1, string2)
            
        cronometro_execucao.parar()
        medidor_memoria.parar_medicao()
            
        tempo_execucao = cronometro_execucao.tempo_segundos()
        memoria_usada = medidor_memoria.obter_memoria_MB()
            
        return tempo_execucao, memoria_usada
    
    
    print("Iniciando testes - Algoritmo Guloso...")
    
    try:
        
        print("  Executando testes com tamanhos iguais...")
        # Testes para tamanhos iguais
        tempo_ig, mem_ig, tempo_dif, mem_dif, tempo_parc, mem_parc, tempo_aleat, mem_aleat = \
            executar_testes_em_lote_tam_iguais(executar_teste_guloso, TAMANHO_INICIAL, TAMANHO_FINAL, DIRETORIO_BASE)
        
        print("  Escrevendo resultados...")
        resultado = gerador.gerador_resultados(DIRETORIO_BASE + "/Resultados/Guloso/", TAMANHO_INICIAL, TAMANHO_FINAL)
        resultado.escrever_resultado_tam_iguais(tempo_ig, mem_ig, tempo_dif, mem_dif, tempo_parc, mem_parc, tempo_aleat, mem_aleat)
        print("  ✓ Testes com tamanhos iguais concluídos!")
        
    except Exception as e:
        print(f"  ✗ Erro ao executar testes gulosos de tamanhos iguais: {e}")
        return
    
    try:
        print("  Executando testes com tamanhos diferentes...")
        # Testes para tamanhos diferentes
        tempo_ig, mem_ig, tempo_dif, mem_dif, tempo_parc, mem_parc, tempo_aleat, mem_aleat = \
            executar_testes_em_lote_tam_diferentes(executar_teste_guloso, TAMANHO_INICIAL, TAMANHO_FINAL, DIRETORIO_BASE)
        
        print("  Escrevendo resultados...")
        resultado = gerador.gerador_resultados(DIRETORIO_BASE + "/Resultados/Guloso/", TAMANHO_INICIAL, TAMANHO_FINAL)
        resultado.escrever_resultado_tam_diferentes(tempo_ig, mem_ig, tempo_dif, mem_dif, tempo_parc, mem_parc, tempo_aleat, mem_aleat)
        print("  ✓ Testes com tamanhos diferentes concluídos!")
        
    except Exception as e:
        print(f"  ✗ Erro ao executar testes gulosos de tamanhos diferentes: {e}")
        return
    
    print("✓ Testes do Algoritmo Guloso finalizados!\n")


#Função para executar o teste do algoritmo backtracking

def executar_testes_backtracking():
    """Executa todos os testes usando abordagem backtracking."""
    
    def executar_teste_backtracking(string1:str, string2:str):
        cronometro_execucao = cronometro.Cronometro()
        medidor_memoria = medidor.MedidorMemoria()
            
        medidor_memoria.iniciar_medicao()  
        cronometro_execucao.iniciar()
            
        algos.distancia_edicao_backtracking(string1, string2)
            
        cronometro_execucao.parar()
        medidor_memoria.parar_medicao()
            
        tempo_execucao = cronometro_execucao.tempo_segundos()
        medidor_memoria.memoria_atual = medidor_memoria.estimar_memoria_total(max(len(string1), len(string2)))
        memoria_usada = medidor_memoria.obter_memoria_MB()
            
        return tempo_execucao, memoria_usada
    
    print("Iniciando testes - Backtracking...")
    
    try:
        
        print("  Executando testes com tamanhos iguais...")
        # Testes para tamanhos iguais
        tempo_ig, mem_ig, tempo_dif, mem_dif, tempo_parc, mem_parc, tempo_aleat, mem_aleat = \
            executar_testes_em_lote_tam_iguais(executar_teste_backtracking, TAMANHO_INICIAL, TAMANHO_FINAL, DIRETORIO_BASE)
        
        print("  Escrevendo resultados...")
        resultado = gerador.gerador_resultados(DIRETORIO_BASE + "/Resultados/Backtracking/", TAMANHO_INICIAL, TAMANHO_FINAL)
        resultado.escrever_resultado_tam_iguais(tempo_ig, mem_ig, tempo_dif, mem_dif, tempo_parc, mem_parc, tempo_aleat, mem_aleat)
        print("  ✓ Testes com tamanhos iguais concluídos!")
        
    except Exception as e:
        print(f"  ✗ Erro ao executar testes backtracking de tamanhos iguais: {e}")
        return
    
    try:
        print("  Executando testes com tamanhos diferentes...")
        # Testes para tamanhos diferentes
        tempo_ig, mem_ig, tempo_dif, mem_dif, tempo_parc, mem_parc, tempo_aleat, mem_aleat = \
            executar_testes_em_lote_tam_diferentes(executar_teste_backtracking, TAMANHO_INICIAL, TAMANHO_FINAL, DIRETORIO_BASE)
        
        print("  Escrevendo resultados...")
        resultado = gerador.gerador_resultados(DIRETORIO_BASE + "/Resultados/Backtracking/", TAMANHO_INICIAL, TAMANHO_FINAL)
        resultado.escrever_resultado_tam_diferentes(tempo_ig, mem_ig, tempo_dif, mem_dif, tempo_parc, mem_parc, tempo_aleat, mem_aleat)
        print("  ✓ Testes com tamanhos diferentes concluídos!")
        
    except Exception as e:
        print(f"  ✗ Erro ao executar testes backtracking de tamanhos diferentes: {e}")
        return
    
    print("✓ Testes de Backtracking finalizados!\n")


#Função para executar o teste do algoritmo backtracking com poda

def executar_testes_backtracking_poda():
    """Executa todos os testes usando backtracking com poda."""
    
    def executar_teste_backtracking_poda(string1:str, string2:str):
        cronometro_execucao = cronometro.Cronometro()
        medidor_memoria = medidor.MedidorMemoria()
                
        medidor_memoria.iniciar_medicao()  
        cronometro_execucao.iniciar()
                
        algos.distancia_edicao_backtracking_com_poda(string1, string2)
                
        cronometro_execucao.parar()
        medidor_memoria.parar_medicao()
                
        tempo_execucao = cronometro_execucao.tempo_segundos()
        medidor_memoria.memoria_atual = medidor_memoria.estimar_memoria_total(max(len(string1), len(string2)))
        memoria_usada = medidor_memoria.obter_memoria_MB()
                
        return tempo_execucao, memoria_usada
    
    print("Iniciando testes - Backtracking com Poda...")
    
    try:
        
        print("  Executando testes com tamanhos iguais...")
        # Testes para tamanhos iguais
        tempo_ig, mem_ig, tempo_dif, mem_dif, tempo_parc, mem_parc, tempo_aleat, mem_aleat = \
            executar_testes_em_lote_tam_iguais(executar_teste_backtracking_poda, TAMANHO_INICIAL, TAMANHO_FINAL, DIRETORIO_BASE)
        
        print("  Escrevendo resultados...")
        resultado = gerador.gerador_resultados(DIRETORIO_BASE + "/Resultados/Backtracking_poda/", TAMANHO_INICIAL, TAMANHO_FINAL)
        resultado.escrever_resultado_tam_iguais(tempo_ig, mem_ig, tempo_dif, mem_dif, tempo_parc, mem_parc, tempo_aleat, mem_aleat)
        print("  ✓ Testes com tamanhos iguais concluídos!")
        
    except Exception as e:
        print(f"  ✗ Erro ao executar testes backtracking com poda de tamanhos iguais: {e}")
        return
    
    try:
        print("  Executando testes com tamanhos diferentes...")
        # Testes para tamanhos diferentes
        tempo_ig, mem_ig, tempo_dif, mem_dif, tempo_parc, mem_parc, tempo_aleat, mem_aleat = \
            executar_testes_em_lote_tam_diferentes(executar_teste_backtracking_poda, TAMANHO_INICIAL, TAMANHO_FINAL, DIRETORIO_BASE)
        
        print("  Escrevendo resultados...")
        resultado = gerador.gerador_resultados(DIRETORIO_BASE + "/Resultados/Backtracking_poda/", TAMANHO_INICIAL, TAMANHO_FINAL)
        resultado.escrever_resultado_tam_diferentes(tempo_ig, mem_ig, tempo_dif, mem_dif, tempo_parc, mem_parc, tempo_aleat, mem_aleat)
        print("  ✓ Testes com tamanhos diferentes concluídos!")
        
    except Exception as e:
        print(f"  ✗ Erro ao executar testes backtracking com poda de tamanhos diferentes: {e}")
        return
    
    print("✓ Testes de Backtracking com Poda finalizados!\n")


if __name__ == "__main__":
    
    gerar_testes()
    executar_testes_guloso()
    executar_testes_backtracking()
    executar_testes_backtracking_poda()
    print("\n" + "="*50)
    print("Todos os testes foram concluídos com sucesso!")
    print("="*50)
