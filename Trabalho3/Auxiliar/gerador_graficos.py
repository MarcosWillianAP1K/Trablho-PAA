import matplotlib.pyplot as plt
import re
import os
import numpy as np

def extrair_dados_arquivo(nome_arquivo: str):
    """
    Extrai os dados de tempo de execução e memória de um arquivo de resultados.
    
    Args:
        nome_arquivo (str): Caminho para o arquivo de resultados
        
    Returns:
        dict: Dicionário com os tempos e memórias para cada tipo de string
    """
    dados = {}
    
    try:
        with open(nome_arquivo, 'r') as f:
            conteudo = f.read()
            
        # Determinar se é teste de tamanhos iguais ou diferentes
        tipo_teste = 'tam_iguais' if 'tam_iguais' in nome_arquivo else 'tam_diferentes'
        
        # Extrair o range de tamanhos do nome do arquivo
        pattern_nome = r"(\d+)_a_(\d+)"
        match_nome = re.search(pattern_nome, nome_arquivo)
        if match_nome:
            tamanho_inicial = int(match_nome.group(1))
            tamanho_final = int(match_nome.group(2))
        else:
            return {}
        
        # Extrair os dados
        pattern_tempo = r"Tempo medio strings (\w+): ([\d\.e\-\+]+)"
        pattern_memoria = r"Memoria media gasta strings (\w+): ([\d\.e\-\+]+)"
        
        tempos_matches = re.finditer(pattern_tempo, conteudo)
        memorias_matches = re.finditer(pattern_memoria, conteudo)
        
        # Armazenar os dados
        for match in tempos_matches:
            tipo = match.group(1)
            tempo = float(match.group(2))
            
            if tipo not in dados:
                dados[tipo] = {}
            dados[tipo]['tempo'] = tempo
            dados[tipo]['tamanho_inicial'] = tamanho_inicial
            dados[tipo]['tamanho_final'] = tamanho_final
            dados[tipo]['tipo_teste'] = tipo_teste
        
        for match in memorias_matches:
            tipo = match.group(1)
            memoria = float(match.group(2))
            
            if tipo not in dados:
                dados[tipo] = {}
            dados[tipo]['memoria'] = memoria
    
    except Exception as e:
        print(f"Erro ao ler o arquivo {nome_arquivo}: {e}")
        return {}
        
    return dados

def formatar_valor(valor):
    """
    Formata um valor numérico para exibição nos gráficos.
    """
    if valor < 0.00001:  # Notação científica para valores muito pequenos
        return f"{valor:.2e}"
    elif valor >= 1000:  # Para valores muito grandes
        return f"{int(valor)}"
    elif valor >= 100:
        return f"{valor:.1f}"
    elif valor >= 10:
        return f"{valor:.2f}"
    elif valor >= 0.1:
        return f"{valor:.3f}"
    else:
        return f"{valor:.4f}"

def listar_arquivos_resultados(diretorio_base: str, algoritmo: str):
    """
    Lista todos os arquivos de resultados para um algoritmo específico.
    
    Args:
        diretorio_base: Diretório base do projeto
        algoritmo: 'Prog_dinamica' ou 'Recursivo'
    
    Returns:
        dict: Dicionário organizado por tipo de teste e range de tamanhos
    """
    dir_resultados = os.path.join(diretorio_base, 'Resultados', algoritmo)
    
    if not os.path.exists(dir_resultados):
        return {}
    
    arquivos = {}
    
    for arquivo in os.listdir(dir_resultados):
        if arquivo.endswith('.txt') and arquivo.startswith('Resultados_string_'):
            caminho_completo = os.path.join(dir_resultados, arquivo)
            
            # Identificar tipo de teste
            if 'tam_iguais' in arquivo:
                tipo_teste = 'tam_iguais'
            elif 'tam_diferentes' in arquivo:
                tipo_teste = 'tam_diferentes'
            else:
                continue
            
            # Extrair range de tamanhos
            pattern = r"(\d+)_a_(\d+)"
            match = re.search(pattern, arquivo)
            if match:
                range_key = f"{match.group(1)}_a_{match.group(2)}"
                
                if tipo_teste not in arquivos:
                    arquivos[tipo_teste] = {}
                arquivos[tipo_teste][range_key] = caminho_completo
    
    return arquivos

def gerar_grafico_comparativo_algoritmos(diretorio_base: str):
    """
    Gera gráficos comparando Programação Dinâmica com Recursivo.
    """
    print("Gerando gráficos comparativos entre algoritmos...")
    
    # Listar arquivos de ambos os algoritmos
    arquivos_pd = listar_arquivos_resultados(diretorio_base, 'Prog_dinamica')
    arquivos_rec = listar_arquivos_resultados(diretorio_base, 'Recursivo')
    
    # Comparar para cada tipo de teste e range
    for tipo_teste in ['tam_iguais', 'tam_diferentes']:
        if tipo_teste not in arquivos_pd or tipo_teste not in arquivos_rec:
            continue
        
        # Encontrar ranges comuns
        ranges_pd = set(arquivos_pd[tipo_teste].keys())
        ranges_rec = set(arquivos_rec[tipo_teste].keys())
        ranges_comuns = sorted(ranges_pd & ranges_rec)
        
        for range_key in ranges_comuns:
            arquivo_pd = arquivos_pd[tipo_teste][range_key]
            arquivo_rec = arquivos_rec[tipo_teste][range_key]
            
            dados_pd = extrair_dados_arquivo(arquivo_pd)
            dados_rec = extrair_dados_arquivo(arquivo_rec)
            
            if not dados_pd or not dados_rec:
                continue
            
            # Gráfico de tempo
            _gerar_grafico_comparativo_tempo(dados_pd, dados_rec, tipo_teste, range_key, diretorio_base)
            
            # Gráfico de memória
            _gerar_grafico_comparativo_memoria(dados_pd, dados_rec, tipo_teste, range_key, diretorio_base)
    
    print("✓ Gráficos comparativos gerados!")

def _gerar_grafico_comparativo_tempo(dados_pd, dados_rec, tipo_teste, range_key, diretorio_base):
    """Gera gráficos comparativos de tempo entre PD e Recursivo (barras e linhas)."""
    tipos_string = ['iguais', 'diferentes', 'parciais', 'aleatorias']
    rotulos = ['Iguais', 'Diferentes', 'Parciais', 'Aleatórias']
    
    # Filtrar apenas tipos que existem em ambos
    tipos_disponiveis = [t for t in tipos_string if t in dados_pd and t in dados_rec]
    rotulos_disponiveis = [rotulos[tipos_string.index(t)] for t in tipos_disponiveis]
    
    if not tipos_disponiveis:
        return
    
    tempos_pd = [dados_pd[t]['tempo'] for t in tipos_disponiveis]
    tempos_rec = [dados_rec[t]['tempo'] for t in tipos_disponiveis]
    
    # GRÁFICO DE BARRAS
    fig, ax = plt.subplots(figsize=(12, 6))
    
    x = np.arange(len(tipos_disponiveis))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, tempos_pd, width, label='Programação Dinâmica', color='#2ca02c')
    bars2 = ax.bar(x + width/2, tempos_rec, width, label='Recursivo', color='#ff7f0e')
    
    # Adicionar valores nas barras
    for bar in bars1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                formatar_valor(height), ha='center', va='bottom', fontsize=9)
    
    for bar in bars2:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                formatar_valor(height), ha='center', va='bottom', fontsize=9)
    
    ax.set_xlabel('Tipo de String', fontsize=12)
    ax.set_ylabel('Tempo Médio (segundos)', fontsize=12)
    tipo_label = 'Tamanhos Iguais' if tipo_teste == 'tam_iguais' else 'Tamanhos Diferentes'
    ax.set_title(f'Comparação de Tempo (Barras) - {tipo_label} ({range_key.replace("_", " ")})', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(rotulos_disponiveis)
    ax.legend()
    ax.grid(True, axis='y', alpha=0.3)
    
    plt.tight_layout()
    graficos_dir = os.path.join(diretorio_base, 'Graficos')
    os.makedirs(graficos_dir, exist_ok=True)
    save_path = os.path.join(graficos_dir, f'comparacao_tempo_barras_{tipo_teste}_{range_key}.png')
    plt.savefig(save_path, dpi=200)
    plt.close()
    print(f"  → {os.path.basename(save_path)}")
    
    # GRÁFICO DE LINHAS
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(rotulos_disponiveis, tempos_pd, marker='o', linewidth=2, markersize=8, 
            label='Programação Dinâmica', color='#2ca02c')
    ax.plot(rotulos_disponiveis, tempos_rec, marker='s', linewidth=2, markersize=8,
            label='Recursivo', color='#ff7f0e')
    
    # Adicionar valores nos pontos
    for i, (rotulo, tempo_pd, tempo_rec) in enumerate(zip(rotulos_disponiveis, tempos_pd, tempos_rec)):
        ax.annotate(formatar_valor(tempo_pd), (i, tempo_pd), 
                   textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
        ax.annotate(formatar_valor(tempo_rec), (i, tempo_rec),
                   textcoords="offset points", xytext=(0,-15), ha='center', fontsize=9)
    
    ax.set_xlabel('Tipo de String', fontsize=12)
    ax.set_ylabel('Tempo Médio (segundos)', fontsize=12)
    ax.set_title(f'Comparação de Tempo (Linhas) - {tipo_label} ({range_key.replace("_", " ")})', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    save_path = os.path.join(graficos_dir, f'comparacao_tempo_linhas_{tipo_teste}_{range_key}.png')
    plt.savefig(save_path, dpi=200)
    plt.close()
    print(f"  → {os.path.basename(save_path)}")

def _gerar_grafico_comparativo_memoria(dados_pd, dados_rec, tipo_teste, range_key, diretorio_base):
    """Gera gráficos comparativos de memória entre PD e Recursivo (barras e linhas)."""
    tipos_string = ['iguais', 'diferentes', 'parciais', 'aleatorias']
    rotulos = ['Iguais', 'Diferentes', 'Parciais', 'Aleatórias']
    
    tipos_disponiveis = [t for t in tipos_string if t in dados_pd and t in dados_rec]
    rotulos_disponiveis = [rotulos[tipos_string.index(t)] for t in tipos_disponiveis]
    
    if not tipos_disponiveis:
        return
    
    mems_pd = [dados_pd[t]['memoria'] for t in tipos_disponiveis]
    mems_rec = [dados_rec[t]['memoria'] for t in tipos_disponiveis]
    
    # GRÁFICO DE BARRAS
    fig, ax = plt.subplots(figsize=(12, 6))
    
    x = np.arange(len(tipos_disponiveis))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, mems_pd, width, label='Programação Dinâmica', color='#1f77b4')
    bars2 = ax.bar(x + width/2, mems_rec, width, label='Recursivo', color='#d62728')
    
    # Adicionar valores nas barras
    for bar in bars1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                formatar_valor(height), ha='center', va='bottom', fontsize=9)
    
    for bar in bars2:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                formatar_valor(height), ha='center', va='bottom', fontsize=9)
    
    ax.set_xlabel('Tipo de String', fontsize=12)
    ax.set_ylabel('Memória Média (MB)', fontsize=12)
    tipo_label = 'Tamanhos Iguais' if tipo_teste == 'tam_iguais' else 'Tamanhos Diferentes'
    ax.set_title(f'Comparação de Memória (Barras) - {tipo_label} ({range_key.replace("_", " ")})', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(rotulos_disponiveis)
    ax.legend()
    ax.grid(True, axis='y', alpha=0.3)
    
    plt.tight_layout()
    graficos_dir = os.path.join(diretorio_base, 'Graficos')
    os.makedirs(graficos_dir, exist_ok=True)
    save_path = os.path.join(graficos_dir, f'comparacao_memoria_barras_{tipo_teste}_{range_key}.png')
    plt.savefig(save_path, dpi=200)
    plt.close()
    print(f"  → {os.path.basename(save_path)}")
    
    # GRÁFICO DE LINHAS
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(rotulos_disponiveis, mems_pd, marker='o', linewidth=2, markersize=8,
            label='Programação Dinâmica', color='#1f77b4')
    ax.plot(rotulos_disponiveis, mems_rec, marker='s', linewidth=2, markersize=8,
            label='Recursivo', color='#d62728')
    
    # Adicionar valores nos pontos
    for i, (rotulo, mem_pd, mem_rec) in enumerate(zip(rotulos_disponiveis, mems_pd, mems_rec)):
        ax.annotate(formatar_valor(mem_pd), (i, mem_pd),
                   textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
        ax.annotate(formatar_valor(mem_rec), (i, mem_rec),
                   textcoords="offset points", xytext=(0,-15), ha='center', fontsize=9)
    
    ax.set_xlabel('Tipo de String', fontsize=12)
    ax.set_ylabel('Memória Média (MB)', fontsize=12)
    ax.set_title(f'Comparação de Memória (Linhas) - {tipo_label} ({range_key.replace("_", " ")})', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    save_path = os.path.join(graficos_dir, f'comparacao_memoria_linhas_{tipo_teste}_{range_key}.png')
    plt.savefig(save_path, dpi=200)
    plt.close()
    print(f"  → {os.path.basename(save_path)}")

def gerar_graficos_por_algoritmo(diretorio_base: str):
    """
    Gera gráficos separados para cada algoritmo mostrando desempenho
    para diferentes tipos de strings.
    """
    print("\nGerando gráficos por algoritmo...")
    
    for algoritmo in ['Prog_dinamica', 'Recursivo']:
        print(f"\n  Processando {algoritmo}...")
        arquivos = listar_arquivos_resultados(diretorio_base, algoritmo)
        
        for tipo_teste in ['tam_iguais', 'tam_diferentes']:
            if tipo_teste not in arquivos:
                continue
            
            for range_key, arquivo in arquivos[tipo_teste].items():
                dados = extrair_dados_arquivo(arquivo)
                
                if not dados:
                    continue
                
                # Gráfico de tempo
                _gerar_grafico_individual_tempo(dados, algoritmo, tipo_teste, range_key, diretorio_base)
                
                # Gráfico de memória
                _gerar_grafico_individual_memoria(dados, algoritmo, tipo_teste, range_key, diretorio_base)
    
    print("\n✓ Gráficos por algoritmo gerados!")

def _gerar_grafico_individual_tempo(dados, algoritmo, tipo_teste, range_key, diretorio_base):
    """Gera gráfico de tempo para um algoritmo específico."""
    tipos_string = ['iguais', 'diferentes', 'parciais', 'aleatorias']
    rotulos = ['Iguais', 'Diferentes', 'Parciais', 'Aleatórias']
    cores = ['#2ca02c', '#d62728', '#ff7f0e', '#9467bd']
    
    tipos_disponiveis = [t for t in tipos_string if t in dados]
    rotulos_disponiveis = [rotulos[tipos_string.index(t)] for t in tipos_disponiveis]
    cores_disponiveis = [cores[tipos_string.index(t)] for t in tipos_disponiveis]
    
    if not tipos_disponiveis:
        return
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    x = np.arange(len(tipos_disponiveis))
    tempos = [dados[t]['tempo'] for t in tipos_disponiveis]
    
    bars = ax.bar(x, tempos, color=cores_disponiveis, alpha=0.8, edgecolor='black')
    
    # Adicionar valores nas barras
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                formatar_valor(height), ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    ax.set_xlabel('Tipo de String', fontsize=12)
    ax.set_ylabel('Tempo Médio (segundos)', fontsize=12)
    tipo_label = 'Tamanhos Iguais' if tipo_teste == 'tam_iguais' else 'Tamanhos Diferentes'
    alg_label = 'Programação Dinâmica' if algoritmo == 'Prog_dinamica' else 'Recursivo'
    ax.set_title(f'Desempenho de Tempo - {alg_label}\n{tipo_label} ({range_key.replace("_", " ")})', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(rotulos_disponiveis)
    ax.grid(True, axis='y', alpha=0.3)
    
    plt.tight_layout()
    graficos_dir = os.path.join(diretorio_base, 'Graficos', algoritmo)
    os.makedirs(graficos_dir, exist_ok=True)
    save_path = os.path.join(graficos_dir, f'tempo_{tipo_teste}_{range_key}.png')
    plt.savefig(save_path, dpi=200)
    plt.close()
    print(f"    → {os.path.basename(save_path)}")

def _gerar_grafico_individual_memoria(dados, algoritmo, tipo_teste, range_key, diretorio_base):
    """Gera gráfico de memória para um algoritmo específico."""
    tipos_string = ['iguais', 'diferentes', 'parciais', 'aleatorias']
    rotulos = ['Iguais', 'Diferentes', 'Parciais', 'Aleatórias']
    cores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    
    tipos_disponiveis = [t for t in tipos_string if t in dados]
    rotulos_disponiveis = [rotulos[tipos_string.index(t)] for t in tipos_disponiveis]
    cores_disponiveis = [cores[tipos_string.index(t)] for t in tipos_disponiveis]
    
    if not tipos_disponiveis:
        return
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    x = np.arange(len(tipos_disponiveis))
    memorias = [dados[t]['memoria'] for t in tipos_disponiveis]
    
    bars = ax.bar(x, memorias, color=cores_disponiveis, alpha=0.8, edgecolor='black')
    
    # Adicionar valores nas barras
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                formatar_valor(height), ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    ax.set_xlabel('Tipo de String', fontsize=12)
    ax.set_ylabel('Memória Média (MB)', fontsize=12)
    tipo_label = 'Tamanhos Iguais' if tipo_teste == 'tam_iguais' else 'Tamanhos Diferentes'
    alg_label = 'Programação Dinâmica' if algoritmo == 'Prog_dinamica' else 'Recursivo'
    ax.set_title(f'Desempenho de Memória - {alg_label}\n{tipo_label} ({range_key.replace("_", " ")})', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(rotulos_disponiveis)
    ax.grid(True, axis='y', alpha=0.3)
    
    plt.tight_layout()
    graficos_dir = os.path.join(diretorio_base, 'Graficos', algoritmo)
    os.makedirs(graficos_dir, exist_ok=True)
    save_path = os.path.join(graficos_dir, f'memoria_{tipo_teste}_{range_key}.png')
    plt.savefig(save_path, dpi=200)
    plt.close()
    print(f"    → {os.path.basename(save_path)}")

def gerar_todos_graficos(diretorio_base: str = None):
    """
    Função principal que gera todos os gráficos e tabelas.
    """
    if diretorio_base is None:
        diretorio_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    print("="*60)
    print("GERADOR DE GRÁFICOS - TRABALHO 2")
    print("Análise de Distância de Edição")
    print("="*60)
    
    # Verificar se o diretório de resultados existe
    resultados_dir = os.path.join(diretorio_base, 'Resultados')
    if not os.path.exists(resultados_dir):
        print(f"Erro: Diretório de resultados não encontrado: {resultados_dir}")
        return
    
    try:
        gerar_grafico_comparativo_algoritmos(diretorio_base)
        gerar_graficos_por_algoritmo(diretorio_base)
        
        print("\n" + "="*60)
        print("✓ TODOS OS GRÁFICOS FORAM GERADOS COM SUCESSO!")
        print("="*60)
        
    except Exception as e:
        print(f"\n✗ Erro durante a geração dos gráficos: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    gerar_todos_graficos()
