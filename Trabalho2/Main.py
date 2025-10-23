import sys
from pathlib import Path

# Adiciona temporariamente o pai ao path para importar setup_path
sys.path.insert(0, str(Path(__file__).parent.parent))

import setup_path #configura o path automaticamente
DIRETORIO_BASE = setup_path.configurar_path("Trabalho2")
    
import Arquivos_testes.gerador_testes as gerador



def gerar_testes():
    
    TAMANHO_INICIAL = 10
    TAMANHO_FINAL = 100

    gerar = gerador.Gerador_testes(f"{DIRETORIO_BASE}/Arquivos_testes")
    
    # print(gerar.diretorio_base)
    if len(gerar.verificar_testes_existentes()) < 8:
        gerar.gerar_testes_strings_tamanhos_iguais(TAMANHO_INICIAL, TAMANHO_FINAL)
        gerar.gerar_testes_strings_tamanhos_diferentes(TAMANHO_INICIAL, TAMANHO_FINAL)
    

if __name__ == "__main__":
    
    gerar_testes()
    