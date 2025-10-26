import sys
from pathlib import Path

# Adiciona temporariamente o pai ao path para importar setup_path
sys.path.insert(0, str(Path(__file__).parent.parent))

import setup_path #configura o path automaticamente
DIRETORIO_BASE = setup_path.configurar_path("Trabalho2")
TAMANHO_INICIAL = 10
TAMANHO_FINAL = 100
    
import Trabalho2.Auxiliar.gerador_testes_resultados as gerador
import Trabalho2.Auxiliar.Cronometro as cronometro
import Trabalho2.Auxiliar.Medidor_memoria as medidor
import Trabalho2.Auxiliar.gerador_graficos as graficos

def gerar_testes():
    
    gerar = gerador.Gerador_testes(f"{DIRETORIO_BASE}/Arquivos_testes/", TAMANHO_INICIAL, TAMANHO_FINAL)
    
    # print(gerar.diretorio_base)
    
    gerar.gerar_testes_strings_tamanhos_iguais()
    gerar.gerar_testes_strings_tamanhos_diferentes()
    




if __name__ == "__main__":
    
    gerar_testes()
    