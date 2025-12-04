import matplotlib.pyplot as plt
import re
import os
import numpy as np

# Constantes globais
ALGORITMOS = ['Guloso', 'Backtracking', 'Backtracking_poda']
VARIANTES = ['iguais', 'diferentes', 'parciais', 'aleatorias']
TIPOS_TAMANHO = [
    ('tam_iguais', 'Strings de Tamanhos Iguais'),
    ('tam_diferentes', 'Strings de Tamanhos Diferentes')
]
CORES_ALGORITMOS = {
    'Guloso': '#2ecc71',
    'Backtracking': '#e74c3c',
    'Backtracking_poda': '#3498db'
}


def limpar_graficos_existentes(diretorio_base):
    """
    Remove todos os gráficos existentes antes de gerar novos.
    
    Args:
        diretorio_base: Diretório base do projeto
    """
    # Limpar pasta de gráficos comparativos
    diretorio_graficos = f"{diretorio_base}/Graficos"
    if os.path.exists(diretorio_graficos):
        for arquivo in os.listdir(diretorio_graficos):
            caminho_arquivo = os.path.join(diretorio_graficos, arquivo)
            if os.path.isfile(caminho_arquivo) and arquivo.endswith('.png'):
                os.remove(caminho_arquivo)
        print("  ✓ Gráficos comparativos anteriores removidos")
    
    # Limpar pastas de gráficos individuais
    for algo in ALGORITMOS:
        diretorio_graficos_algo = f"{diretorio_graficos}/{algo}"
        if os.path.exists(diretorio_graficos_algo):
            for arquivo in os.listdir(diretorio_graficos_algo):
                if arquivo.endswith('.png'):
                    os.remove(os.path.join(diretorio_graficos_algo, arquivo))
            print(f"  ✓ Gráficos anteriores de {algo} removidos")


def ler_resultados_de_arquivo(caminho_arquivo):
    """
    Lê os dados de tempo e memória de um arquivo de resultados.
    
    Args:
        caminho_arquivo: Caminho completo do arquivo .txt
    
    Returns:
        Tupla (tempo_medio, memoria_media)
    """
    
    
    if not os.path.exists(caminho_arquivo):
        return 0.0, 0.0
    
    tempo_medio = 0.0
    memoria_media = 0.0
    
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        
        # Busca pelos valores médios diretamente (formato mais confiável)
        # Exemplo: "Tempo medio strings iguais: 3.0399999559449498e-05"
        
        # Tenta extrair tempos médios
        tempos_encontrados = re.findall(r'Tempo medio.*?:\s*([\d.e+-]+)', conteudo)
        if tempos_encontrados:
            valores_tempo = [float(v) for v in tempos_encontrados]
            tempo_medio = np.mean(valores_tempo)
        
        # Tenta extrair memórias médias
        memorias_encontradas = re.findall(r'Memoria media gasta.*?:\s*([\d.e+-]+)', conteudo)
        if memorias_encontradas:
            valores_memoria = [float(v) for v in memorias_encontradas]
            memoria_media = np.mean(valores_memoria)
    
    return tempo_medio, memoria_media


def criar_graficos_comparativos(diretorio_resultados, diretorio_graficos, tamanho_inicial, tamanho_final):
    """
    Cria gráficos comparativos entre os 3 algoritmos.
    Cada gráfico mostra as 4 variantes, com 3 barras (uma para cada algoritmo).
    """
    os.makedirs(diretorio_graficos, exist_ok=True)
    
    for tipo_tam, titulo_tam in TIPOS_TAMANHO:
        # Coleta dados para todas as variantes e algoritmos
        dados_tempo = {var: [] for var in VARIANTES}
        dados_memoria = {var: [] for var in VARIANTES}
        
        # Para cada algoritmo, coletar dados de TODAS as variantes
        for algo in ALGORITMOS:
            # Vetores temporários para armazenar dados deste algoritmo
            tempos_algo = []
            memorias_algo = []
            
            # Ler dados de cada variante
            for variante in VARIANTES:
                arquivo = f"{diretorio_resultados}/{algo}/Resultados_string_{tipo_tam}_{tamanho_inicial}_a_{tamanho_final}.txt"
                tempo_medio, memoria_media = ler_resultados_de_arquivo(arquivo)
                tempos_algo.append(tempo_medio)
                memorias_algo.append(memoria_media)
            
            # Armazenar no dicionário: cada variante recebe o valor correspondente deste algoritmo
            for i, variante in enumerate(VARIANTES):
                dados_tempo[variante].append(tempos_algo[i])
                dados_memoria[variante].append(memorias_algo[i])
        
        # Gráfico de Tempo
        criar_grafico_comparativo_barras(
            dados_tempo,
            VARIANTES,
            ALGORITMOS,
            CORES_ALGORITMOS,
            'Variantes de Strings',
            'Tempo Médio de Execução (s)',
            f'Comparação de Tempo - {titulo_tam}',
            f"{diretorio_graficos}/comparativo_tempo_{tipo_tam}.png",
            tipo_metrica='tempo'
        )
        
        # Gráfico de Memória
        criar_grafico_comparativo_barras(
            dados_memoria,
            VARIANTES,
            ALGORITMOS,
            CORES_ALGORITMOS,
            'Variantes de Strings',
            'Memória Média Utilizada (MB)',
            f'Comparação de Memória - {titulo_tam}',
            f"{diretorio_graficos}/comparativo_memoria_{tipo_tam}.png",
            tipo_metrica='memoria'
        )


def criar_grafico_comparativo_barras(dados, variantes, algoritmos, cores, xlabel, ylabel, titulo, caminho_saida, tipo_metrica='tempo'):
    """
    Cria um gráfico de barras comparativo.
    
    Args:
        dados: Dicionário {variante: [valor_algo1, valor_algo2, valor_algo3]}
        variantes: Lista de nomes das variantes
        algoritmos: Lista de nomes dos algoritmos
        cores: Dicionário {algoritmo: cor}
        xlabel, ylabel, titulo: Rótulos do gráfico
        caminho_saida: Caminho para salvar
        tipo_metrica: 'tempo' ou 'memoria' para formatação adequada
    """
    # Remove arquivo existente se houver
    if os.path.exists(caminho_saida):
        os.remove(caminho_saida)
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    n_variantes = len(variantes)
    n_algoritmos = len(algoritmos)
    largura_barra = 0.25
    
    indices = np.arange(n_variantes)
    
    # Coletar todos os valores para análise
    todos_valores = []
    for var in variantes:
        todos_valores.extend(dados[var])
    
    valores_nao_zero = [v for v in todos_valores if v > 0]
    max_valor = max(valores_nao_zero) if valores_nao_zero else 0
    min_valor = min(valores_nao_zero) if valores_nao_zero else 0
    
    # Plotar barras para cada algoritmo
    for i, algo in enumerate(algoritmos):
        valores = [dados[var][i] for var in variantes]
        offset = (i - 1) * largura_barra
        
        # Formatar nome do algoritmo para legenda
        nome_legenda = algo.replace('_', ' ').title()
        if 'Poda' in nome_legenda:
            nome_legenda = 'Backtracking com Poda'
        
        ax.bar(indices + offset, valores, largura_barra,
               label=nome_legenda, color=cores.get(algo, f'C{i}'),
               alpha=0.85, edgecolor='black', linewidth=1)
    
    # Ajustar escala do eixo Y
    if max_valor > 0:
        # Define margem superior (10% acima do valor máximo)
        margem_superior = max_valor * 1.1
        ax.set_ylim(bottom=0, top=margem_superior)
        
        # Usar notação científica se os valores forem muito pequenos OU muito grandes
        if max_valor < 0.001:
            ax.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))
        elif max_valor > 10000:
            ax.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))
    else:
        ax.set_ylim(bottom=0, top=1)
    
    # Configurações
    ax.set_xlabel(xlabel, fontsize=13, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=13, fontweight='bold')
    ax.set_title(titulo, fontsize=15, fontweight='bold', pad=20)
    ax.set_xticks(indices)
    ax.set_xticklabels([v.capitalize() for v in variantes], fontsize=11)
    ax.legend(loc='upper left', fontsize=11, framealpha=0.9)
    ax.grid(True, alpha=0.3, axis='y', linestyle='--')
    
    plt.tight_layout()
    plt.savefig(caminho_saida, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"  ✓ Gráfico comparativo salvo: {os.path.basename(caminho_saida)}")


def criar_graficos_individuais(diretorio_resultados, diretorio_graficos, tamanho_inicial, tamanho_final):
    """
    Cria gráficos individuais para cada algoritmo.
    Cada gráfico mostra tempo e memória para cada variante.
    """
    for algo in ALGORITMOS:
        diretorio_graficos_algo = f"{diretorio_graficos}/{algo}"
        os.makedirs(diretorio_graficos_algo, exist_ok=True)
        
        for tipo_tam, titulo_tam in TIPOS_TAMANHO:
            # Coleta dados para todas as variantes
            tempos = []
            memorias = []
            
            for variante in VARIANTES:
                arquivo = f"{diretorio_resultados}/{algo}/Resultados_string_{tipo_tam}_{tamanho_inicial}_a_{tamanho_final}.txt"
                tempo_medio, memoria_media = ler_resultados_de_arquivo(arquivo)
                tempos.append(tempo_medio)
                memorias.append(memoria_media)
            
            # Criar gráfico individual
            criar_grafico_individual_barras(
                tempos,
                memorias,
                VARIANTES,
                algo,
                titulo_tam,
                f"{diretorio_graficos_algo}/{tipo_tam}.png"
            )


def criar_grafico_individual_barras(tempos, memorias, variantes, algoritmo, titulo_tipo, caminho_saida):
    """
    Cria um gráfico individual mostrando tempo e memória para cada variante.
    
    Args:
        tempos: Lista de tempos médios para cada variante
        memorias: Lista de memórias médias para cada variante
        variantes: Lista de nomes das variantes
        algoritmo: Nome do algoritmo
        titulo_tipo: Tipo de tamanho (iguais ou diferentes)
        caminho_saida: Caminho para salvar
    """
    # Remove arquivo existente se houver
    if os.path.exists(caminho_saida):
        os.remove(caminho_saida)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    n_variantes = len(variantes)
    largura_barra = 0.35
    indices = np.arange(n_variantes)
    
    # Analisar valores
    tempos_nao_zero = [t for t in tempos if t > 0]
    memorias_nao_zero = [m for m in memorias if m > 0]
    
    max_tempo = max(tempos_nao_zero) if tempos_nao_zero else 0
    max_memoria = max(memorias_nao_zero) if memorias_nao_zero else 0
    
    # Criar eixo secundário para memória
    ax2 = ax.twinx()
    
    # Barras de tempo (eixo primário - esquerdo)
    barras_tempo = ax.bar(indices - largura_barra/2, tempos, largura_barra,
                          label='Tempo de Execução', color='#3498db',
                          alpha=0.85, edgecolor='black', linewidth=1)
    
    # Barras de memória (eixo secundário - direito)
    barras_memoria = ax2.bar(indices + largura_barra/2, memorias, largura_barra,
                            label='Memória Utilizada', color='#e74c3c',
                            alpha=0.85, edgecolor='black', linewidth=1)
    
    # Ajustar escalas com margem superior
    if max_tempo > 0:
        ax.set_ylim(bottom=0, top=max_tempo * 1.1)
        # Notação científica para valores muito pequenos ou muito grandes
        if max_tempo < 0.001 or max_tempo > 10000:
            ax.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))
    else:
        ax.set_ylim(bottom=0, top=1)
    
    if max_memoria > 0:
        ax2.set_ylim(bottom=0, top=max_memoria * 1.1)
        # Notação científica para valores muito pequenos ou muito grandes
        if max_memoria < 0.001 or max_memoria > 10000:
            ax2.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))
    else:
        ax2.set_ylim(bottom=0, top=1)
    
    # Configurações eixo primário (Tempo - Esquerdo)
    ax.set_xlabel('Variantes de Strings', fontsize=12, fontweight='bold')
    ax.set_ylabel('Tempo Médio de Execução (s)', fontsize=12, fontweight='bold', color='#2874a6')
    ax.tick_params(axis='y', labelcolor='#2874a6', labelsize=10)
    ax.set_xticks(indices)
    ax.set_xticklabels([v.capitalize() for v in variantes], fontsize=10)
    ax.grid(True, alpha=0.3, axis='y', linestyle='--', color='#3498db')
    
    # Configurações eixo secundário (Memória - Direito)
    ax2.set_ylabel('Memória Média Utilizada (MB)', fontsize=12, fontweight='bold', color='#a93226')
    ax2.tick_params(axis='y', labelcolor='#a93226', labelsize=10)
    ax2.grid(False)
    
    # Formatar nome do algoritmo
    nome_algoritmo = algoritmo.replace('_', ' ').title()
    if 'Poda' in nome_algoritmo:
        nome_algoritmo = 'Backtracking com Poda'
    
    # Título
    ax.set_title(f'{nome_algoritmo} - {titulo_tipo}', fontsize=14, fontweight='bold', pad=20)
    
    # Legenda combinada
    linhas1, labels1 = ax.get_legend_handles_labels()
    linhas2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(linhas1 + linhas2, labels1 + labels2, loc='upper left', fontsize=10, framealpha=0.9)
    
    plt.tight_layout()
    plt.savefig(caminho_saida, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"  ✓ Gráfico individual salvo: {nome_algoritmo}/{os.path.basename(caminho_saida)}")


def gerar_todos_graficos(diretorio_base, tamanho_inicial, tamanho_final):
    """
    Gera todos os gráficos automaticamente.
    
    Args:
        diretorio_base: Diretório base do projeto
        tamanho_inicial: Tamanho inicial dos testes
        tamanho_final: Tamanho final dos testes
    """

    diretorio_resultados = f"{diretorio_base}/Resultados"
    diretorio_graficos = f"{diretorio_base}/Graficos"
    
    print("\nGerando gráficos...")
    
    # Limpar gráficos existentes
    print("  Removendo gráficos anteriores...")
    limpar_graficos_existentes(diretorio_base)
    
    print("\n  Criando gráficos comparativos entre algoritmos...")
    criar_graficos_comparativos(diretorio_resultados, diretorio_graficos, tamanho_inicial, tamanho_final)
    
    print("\n  Criando gráficos individuais para cada algoritmo...")
    criar_graficos_individuais(diretorio_resultados, diretorio_graficos, tamanho_inicial, tamanho_final)
    
    print("\n✓ Todos os gráficos foram gerados com sucesso!\n")
