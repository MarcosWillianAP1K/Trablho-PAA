import matplotlib.pyplot as plt
import re
import os
import numpy as np

def extrair_dados_arquivo(nome_arquivo):
    """
    Extrai os dados de tempo de execução de um arquivo de resultados.
    
    Args:
        nome_arquivo (str): Caminho para o arquivo de resultados
        
    Returns:
        dict: Dicionário com os tempos para cada tamanho e tipo de lista
    """
    dados = {}
    
    try:
        with open(nome_arquivo, 'r') as f:
            conteudo = f.read()
            
        # Expressão regular para extrair os dados
        pattern = r"Resultados do .+ Sort para listas com (\d+) elementos:\s+\n\s*Lista crescente: ([\d\.e-]+) segundos\s*\n\s*Lista decrescente: ([\d\.e-]+) segundos\s*\n\s*Lista aleatoria: ([\d\.e-]+) segundos"
        
        matches = re.finditer(pattern, conteudo)
        
        for match in matches:
            tamanho = int(match.group(1))
            tempo_crescente = float(match.group(2))
            tempo_decrescente = float(match.group(3))
            tempo_aleatorio = float(match.group(4))
            
            dados[tamanho] = {
                'crescente': tempo_crescente,
                'decrescente': tempo_decrescente,
                'aleatorio': tempo_aleatorio
            }
    
    except Exception as e:
        print(f"Erro ao ler o arquivo {nome_arquivo}: {e}")
        return {}
        
    return dados

def gerar_grafico_comparativo_algoritmos():
    """
    Gera um gráfico comparando o desempenho dos algoritmos Cocktail Sort e Radix Sort
    para diferentes tamanhos e tipos de listas.
    """
    # Use absolute paths to ensure correct file location
    import os
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dados_cocktail = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_coktail.txt'))
    dados_radix = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_radix.txt'))
    
    # Verificar se foram extraídos dados
    if not dados_cocktail or not dados_radix:
        print("Erro: Não foi possível extrair dados dos arquivos de resultado")
        return
    
    # Garantir que estamos comparando os mesmos tamanhos
    tamanhos_comuns = sorted(set(dados_cocktail.keys()) & set(dados_radix.keys()))
    
    if not tamanhos_comuns:
        print("Erro: Não há tamanhos de lista comuns entre os algoritmos")
        return
    
    # Preparar os dados para o gráfico
    tipos_lista = ['crescente', 'decrescente', 'aleatorio']
    rotulos_tipos = ['Crescente', 'Decrescente', 'Aleatória']
    
    # Configurar o gráfico
    plt.figure(figsize=(15, 10))
    
    # Para cada tipo de lista (crescente, decrescente, aleatória)
    for i, (tipo, rotulo) in enumerate(zip(tipos_lista, rotulos_tipos)):
        plt.subplot(1, 3, i+1)
        
        x = tamanhos_comuns
        y_cocktail = [dados_cocktail[tamanho][tipo] for tamanho in tamanhos_comuns]
        y_radix = [dados_radix[tamanho][tipo] for tamanho in tamanhos_comuns]
        
        plt.plot(x, y_cocktail, 'b-o', label='Cocktail Sort')
        plt.plot(x, y_radix, 'r-s', label='Radix Sort')
        
        plt.title(f'Comparação para Lista {rotulo}')
        plt.xlabel('Tamanho da Lista')
        plt.ylabel('Tempo de Execução (segundos)')
        plt.grid(True)
        plt.legend()
        plt.xticks(tamanhos_comuns)
        
    plt.tight_layout()
    save_path = os.path.join(base_dir, 'Resultados', 'comparacao_algoritmos.png')
    plt.savefig(save_path)
    print(f"Gráfico de comparação gerado com sucesso: '{save_path}'")
    
def gerar_grafico_por_algoritmo():
    """
    Gera gráficos separados para cada algoritmo, mostrando o desempenho
    para diferentes tipos de lista.
    """
    # Use absolute paths to ensure correct file location
    import os
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dados_cocktail = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_coktail.txt'))
    dados_radix = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_radix.txt'))
    
    algoritmos = [
        ('Cocktail Sort', dados_cocktail, 'cocktail'),
        ('Radix Sort', dados_radix, 'radix')
    ]
    
    for nome, dados, arquivo in algoritmos:
        if not dados:
            continue
            
        tamanhos = sorted(dados.keys())
        
        plt.figure(figsize=(10, 6))
        
        y_crescente = [dados[tamanho]['crescente'] for tamanho in tamanhos]
        y_decrescente = [dados[tamanho]['decrescente'] for tamanho in tamanhos]
        y_aleatorio = [dados[tamanho]['aleatorio'] for tamanho in tamanhos]
        
        plt.plot(tamanhos, y_crescente, 'g-o', label='Lista Crescente')
        plt.plot(tamanhos, y_decrescente, 'r-s', label='Lista Decrescente')
        plt.plot(tamanhos, y_aleatorio, 'b-^', label='Lista Aleatória')
        
        plt.title(f'Desempenho do {nome}')
        plt.xlabel('Tamanho da Lista')
        plt.ylabel('Tempo de Execução (segundos)')
        plt.grid(True)
        plt.legend()
        plt.xticks(tamanhos)
        
        plt.tight_layout()
        save_path = os.path.join(base_dir, 'Resultados', f'desempenho_{arquivo}.png')
        plt.savefig(save_path)
        print(f"Gráfico de desempenho para {nome} gerado: '{save_path}'")

def gerar_grafico_barras_comparativo():
    """
    Gera um gráfico de barras comparando o desempenho dos algoritmos
    para cada tipo de lista e tamanho.
    """
    # Use absolute paths to ensure correct file location
    import os
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dados_cocktail = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_coktail.txt'))
    dados_radix = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_radix.txt'))
    
    # Verificar se foram extraídos dados
    if not dados_cocktail or not dados_radix:
        print("Erro: Não foi possível extrair dados dos arquivos de resultado")
        return
    
    # Garantir que estamos comparando os mesmos tamanhos
    tamanhos_comuns = sorted(set(dados_cocktail.keys()) & set(dados_radix.keys()))
    
    if not tamanhos_comuns:
        print("Erro: Não há tamanhos de lista comuns entre os algoritmos")
        return
    
    # Para cada tamanho de lista, criar um gráfico de barras
    for tamanho in tamanhos_comuns:
        plt.figure(figsize=(10, 6))
        
        tipos_lista = ['crescente', 'decrescente', 'aleatorio']
        rotulos = ['Crescente', 'Decrescente', 'Aleatória']
        
        x = np.arange(len(tipos_lista))
        largura = 0.35
        
        tempos_cocktail = [dados_cocktail[tamanho][tipo] for tipo in tipos_lista]
        tempos_radix = [dados_radix[tamanho][tipo] for tipo in tipos_lista]
        
        plt.bar(x - largura/2, tempos_cocktail, largura, label='Cocktail Sort')
        plt.bar(x + largura/2, tempos_radix, largura, label='Radix Sort')
        
        plt.title(f'Comparação de Algoritmos para Lista de Tamanho {tamanho}')
        plt.xlabel('Tipo de Lista')
        plt.ylabel('Tempo de Execução (segundos)')
        plt.xticks(x, rotulos)
        plt.grid(True, axis='y')
        plt.legend()
        
        plt.tight_layout()
        save_path = os.path.join(base_dir, 'Resultados', f'comparacao_barras_{tamanho}.png')
        plt.savefig(save_path)
        print(f"Gráfico de barras para tamanho {tamanho} gerado: '{save_path}'")

# Executar as funções de geração de gráficos
if __name__ == "__main__":
    # Verificar se o diretório de resultados existe
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    resultados_dir = os.path.join(base_dir, 'Resultados')
    if not os.path.exists(resultados_dir):
        os.makedirs(resultados_dir)
        
    print("Gerando gráficos de comparação...")
    gerar_grafico_comparativo_algoritmos()
    
    print("\nGerando gráficos de desempenho por algoritmo...")
    gerar_grafico_por_algoritmo()
    
    print("\nGerando gráficos de barras comparativos...")
    gerar_grafico_barras_comparativo()
    
    print("\nTodos os gráficos foram gerados com sucesso!")