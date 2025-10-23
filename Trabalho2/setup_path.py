import sys
from pathlib import Path

def encontrar_raiz_projeto(nome_pasta:str) -> Path:
    """Encontra a pasta raiz do projeto subindo na hierarquia"""
    caminho_atual = Path(__file__).resolve()
    
    for pasta in caminho_atual.parents:
        if pasta.name == nome_pasta:
            return pasta
    
    return Path(__file__).parent

def configurar_path(nome_pasta:str= ""):
    
    if nome_pasta == "":
        return None
    
    """Configura o sys.path para permitir imports do projeto"""
    diretorio_projeto = encontrar_raiz_projeto(nome_pasta)
    if str(diretorio_projeto) not in sys.path:
        sys.path.insert(0, str(diretorio_projeto))
    
        return diretorio_projeto
    return None
    



