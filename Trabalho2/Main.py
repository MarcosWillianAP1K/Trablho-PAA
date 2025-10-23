import sys
from pathlib import Path

# Adiciona temporariamente o pai ao path para importar setup_path
sys.path.insert(0, str(Path(__file__).parent.parent))

import setup_path #configura o path automaticamente
DIRETORIO_BASE = setup_path.configurar_path("Trabalho2")
TAMANHO_INICIAL = 10
TAMANHO_FINAL = 100
    
import Trabalho2.Auxiliar.gerador_testes_resultados as gerador



def gerar_testes():
    
    gerar = gerador.Gerador_testes(f"{DIRETORIO_BASE}/Arquivos_testes", TAMANHO_INICIAL, TAMANHO_FINAL)
    
    # print(gerar.diretorio_base)
    
    gerar.gerar_testes_strings_tamanhos_iguais()
    gerar.gerar_testes_strings_tamanhos_diferentes()
    
    #teste dos resultados
    
    lista = [10.0, 10.0, 10.0, 10.0, 10.0]
    
    resultados = gerador.gerador_resultados(f"{DIRETORIO_BASE}/Arquivos_testes", TAMANHO_INICIAL, TAMANHO_FINAL)
    
    resultados.escrever_resultado_tam_iguais(lista, lista, lista, lista)
    resultados.escrever_resultado_tam_diferentes(lista, lista, lista, lista)
    




if __name__ == "__main__":
    
    gerar_testes()
    