import matplotlib.pyplot as plt
import re
import os
import numpy as np

def extrair_dados_arquivo(nome_arquivo:str):
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

def formatar_valor(valor):
    """
    Formata um valor numérico para exibição nos gráficos,
    adaptando a precisão de acordo com a magnitude do valor.
    """
    if valor < 0.001:  # Notação científica para valores muito pequenos
        return f"{valor:.2e}"
    elif valor >= 1000:  # Para valores muito grandes, arredondar para inteiro
        return f"{int(valor)}"
    elif valor >= 100:  # Para valores grandes, apenas uma casa decimal
        return f"{valor:.1f}"
    elif valor >= 10:   # Para valores médios, duas casas decimais
        return f"{valor:.2f}"
    else:                # Para valores pequenos, até 4 casas decimais
        return f"{valor:.4f}"

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
        
        # Adicionar os valores em cada ponto
        for j, (xval, yval) in enumerate(zip(x, y_cocktail)):
            texto = formatar_valor(yval)
            plt.annotate(texto, (xval, yval), xytext=(0, 10), 
                         textcoords='offset points', ha='center', fontsize=8)
        
        # Adicionar os valores para o Radix Sort (abaixo dos pontos para evitar sobreposição)
        for j, (xval, yval) in enumerate(zip(x, y_radix)):
            texto = formatar_valor(yval)
            plt.annotate(texto, (xval, yval), xytext=(0, -15), 
                         textcoords='offset points', ha='center', fontsize=8)
        
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
        
        # Adicionar os valores em cada ponto
        for j, (xval, yval) in enumerate(zip(tamanhos, y_crescente)):
            texto = formatar_valor(yval)
            plt.annotate(texto, (xval, yval), xytext=(0, 10), 
                         textcoords='offset points', ha='center', fontsize=8)
                         
        for j, (xval, yval) in enumerate(zip(tamanhos, y_decrescente)):
            texto = formatar_valor(yval)
            plt.annotate(texto, (xval, yval), xytext=(0, 10), 
                         textcoords='offset points', ha='center', fontsize=8)
                         
        for j, (xval, yval) in enumerate(zip(tamanhos, y_aleatorio)):
            texto = formatar_valor(yval)
            plt.annotate(texto, (xval, yval), xytext=(0, 10), 
                         textcoords='offset points', ha='center', fontsize=8)
        
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
    Gera dois gráficos de barras separados, um para cada algoritmo (Cocktail e Radix),
    mostrando o desempenho para cada tamanho e tipo de lista.
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
    
    # Definição das cores para os diferentes tipos de lista
    cores = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Azul, Laranja, Verde
    
    # Tipos de lista e seus rótulos
    tipos_lista = ['crescente', 'decrescente', 'aleatorio']
    rotulos_tipos = ['Crescente', 'Decrescente', 'Aleatória']
    
    # Largura da barra e posicionamento
    n_tamanhos = len(tamanhos_comuns)
    n_tipos = len(tipos_lista)
    largura_total = 0.8  # Largura total disponível para cada tamanho
    largura_barra = largura_total / n_tipos  # Largura de cada barra individual
    
    # Posições no eixo X
    x_pos = np.arange(n_tamanhos)
    
    # ----------------------- Gráfico para o Cocktail Sort -----------------------
    plt.figure(figsize=(12, 8))
    
    for i, (tipo, rotulo) in enumerate(zip(tipos_lista, rotulos_tipos)):
        # Offset para posicionar as barras lado a lado em cada tamanho
        offset = -largura_total/2 + largura_barra/2 + i * largura_barra
        
        # Extrair os dados de tempo para cada tamanho
        tempos = [dados_cocktail[tamanho][tipo] for tamanho in tamanhos_comuns]
        
        # Plotar as barras
        barras = plt.bar(x_pos + offset, tempos, largura_barra, 
                color=cores[i], label=f'Lista {rotulo}')
        
        # Adicionar os valores em cima de cada barra
        for j, barra in enumerate(barras):
            altura = barra.get_height()
            texto = formatar_valor(altura)
            plt.text(barra.get_x() + barra.get_width()/2., altura + 0.01*max(tempos),
                    texto, ha='center', va='bottom', fontsize=8, rotation=45)
    
    # Configurações do gráfico
    plt.title('Desempenho do Cocktail Sort por Tamanho e Tipo de Lista')
    plt.xlabel('Tamanho da Lista')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.xticks(x_pos, tamanhos_comuns)
    plt.grid(True, axis='y')
    plt.legend()
    
    plt.tight_layout()
    save_path = os.path.join(base_dir, 'Resultados', 'barras_cocktail.png')
    plt.savefig(save_path)
    print(f"Gráfico de barras para Cocktail Sort gerado: '{save_path}'")
    
    # ----------------------- Gráfico para o Radix Sort -----------------------
    plt.figure(figsize=(12, 8))
    
    for i, (tipo, rotulo) in enumerate(zip(tipos_lista, rotulos_tipos)):
        # Offset para posicionar as barras lado a lado em cada tamanho
        offset = -largura_total/2 + largura_barra/2 + i * largura_barra
        
        # Extrair os dados de tempo para cada tamanho
        tempos = [dados_radix[tamanho][tipo] for tamanho in tamanhos_comuns]
        
        # Plotar as barras
        barras = plt.bar(x_pos + offset, tempos, largura_barra, 
                color=cores[i], label=f'Lista {rotulo}')
        
        # Adicionar os valores em cima de cada barra
        for j, barra in enumerate(barras):
            altura = barra.get_height()
            texto = formatar_valor(altura)
            plt.text(barra.get_x() + barra.get_width()/2., altura + 0.01*max(tempos),
                    texto, ha='center', va='bottom', fontsize=8, rotation=45)
    
    # Configurações do gráfico
    plt.title('Desempenho do Radix Sort por Tamanho e Tipo de Lista')
    plt.xlabel('Tamanho da Lista')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.xticks(x_pos, tamanhos_comuns)
    plt.grid(True, axis='y')
    plt.legend()
    
    plt.tight_layout()
    save_path = os.path.join(base_dir, 'Resultados', 'barras_radix.png')
    plt.savefig(save_path)
    print(f"Gráfico de barras para Radix Sort gerado: '{save_path}'")

def gerar_graficos_dados_pequenos():
    """
    Gera todos os gráficos (comparativo, por algoritmo e barras) utilizando
    apenas os dados dos testes com 100, 500 e 1000 elementos.
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
    
    # Filtrar apenas os tamanhos pequenos
    tamanhos_pequenos = [100, 500, 1000]
    
    # Filtrar os dados para conter apenas os tamanhos pequenos
    dados_cocktail_filtrados = {k: v for k, v in dados_cocktail.items() if k in tamanhos_pequenos}
    dados_radix_filtrados = {k: v for k, v in dados_radix.items() if k in tamanhos_pequenos}
    
    # Verificar se há dados para os tamanhos desejados
    tamanhos_comuns = sorted(set(dados_cocktail_filtrados.keys()) & set(dados_radix_filtrados.keys()))
    
    if not tamanhos_comuns:
        print("Erro: Não há dados para os tamanhos 100, 500 e 1000")
        return
    
    print(f"Gerando gráficos apenas para os tamanhos: {tamanhos_comuns}")
    
    # ---------------- Gráfico comparativo (linha) ----------------
    # Preparar os dados para o gráfico
    tipos_lista = ['crescente', 'decrescente', 'aleatorio']
    rotulos_tipos = ['Crescente', 'Decrescente', 'Aleatória']
    
    # Configurar o gráfico
    plt.figure(figsize=(15, 10))
    
    # Para cada tipo de lista (crescente, decrescente, aleatória)
    for i, (tipo, rotulo) in enumerate(zip(tipos_lista, rotulos_tipos)):
        plt.subplot(1, 3, i+1)
        
        x = tamanhos_comuns
        y_cocktail = [dados_cocktail_filtrados[tamanho][tipo] for tamanho in tamanhos_comuns]
        y_radix = [dados_radix_filtrados[tamanho][tipo] for tamanho in tamanhos_comuns]
        
        plt.plot(x, y_cocktail, 'b-o', label='Cocktail Sort')
        plt.plot(x, y_radix, 'r-s', label='Radix Sort')
        
        # Adicionar os valores em cada ponto para o Cocktail Sort
        for j, (xval, yval) in enumerate(zip(x, y_cocktail)):
            texto = formatar_valor(yval)
            plt.annotate(texto, (xval, yval), xytext=(0, 10), 
                         textcoords='offset points', ha='center', fontsize=8)
                         
        # Adicionar os valores em cada ponto para o Radix Sort
        for j, (xval, yval) in enumerate(zip(x, y_radix)):
            texto = formatar_valor(yval)
            plt.annotate(texto, (xval, yval), xytext=(0, -15), 
                         textcoords='offset points', ha='center', fontsize=8)
        
        plt.title(f'Comparação para Lista {rotulo} (Dados Pequenos)')
        plt.xlabel('Tamanho da Lista')
        plt.ylabel('Tempo de Execução (segundos)')
        plt.grid(True)
        plt.legend()
        plt.xticks(tamanhos_comuns)
        
    plt.tight_layout()
    save_path = os.path.join(base_dir, 'Resultados', 'comparacao_algoritmos_pequenos.png')
    plt.savefig(save_path)
    print(f"Gráfico de comparação (dados pequenos) gerado: '{save_path}'")
    
    # ---------------- Gráficos por algoritmo (linha) ----------------
    algoritmos = [
        ('Cocktail Sort', dados_cocktail_filtrados, 'cocktail'),
        ('Radix Sort', dados_radix_filtrados, 'radix')
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
        
        # Adicionar os valores em cada ponto
        for j, (xval, yval) in enumerate(zip(tamanhos, y_crescente)):
            texto = formatar_valor(yval)
            plt.annotate(texto, (xval, yval), xytext=(0, 10), 
                         textcoords='offset points', ha='center', fontsize=8)
                         
        for j, (xval, yval) in enumerate(zip(tamanhos, y_decrescente)):
            texto = formatar_valor(yval)
            plt.annotate(texto, (xval, yval), xytext=(0, 10), 
                         textcoords='offset points', ha='center', fontsize=8)
                         
        for j, (xval, yval) in enumerate(zip(tamanhos, y_aleatorio)):
            texto = formatar_valor(yval)
            plt.annotate(texto, (xval, yval), xytext=(0, 10), 
                         textcoords='offset points', ha='center', fontsize=8)
        
        plt.title(f'Desempenho do {nome} (Dados Pequenos)')
        plt.xlabel('Tamanho da Lista')
        plt.ylabel('Tempo de Execução (segundos)')
        plt.grid(True)
        plt.legend()
        plt.xticks(tamanhos)
        
        plt.tight_layout()
        save_path = os.path.join(base_dir, 'Resultados', f'desempenho_{arquivo}_pequenos.png')
        plt.savefig(save_path)
        print(f"Gráfico de desempenho para {nome} (dados pequenos) gerado: '{save_path}'")
    
    # ---------------- Gráficos de barras por algoritmo ----------------
    # Definição das cores para os diferentes tipos de lista
    cores = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Azul, Laranja, Verde
    
    # Largura da barra e posicionamento
    n_tamanhos = len(tamanhos_comuns)
    n_tipos = len(tipos_lista)
    largura_total = 0.8  # Largura total disponível para cada tamanho
    largura_barra = largura_total / n_tipos  # Largura de cada barra individual
    
    # Posições no eixo X
    x_pos = np.arange(n_tamanhos)
    
    # ----------------------- Gráfico para o Cocktail Sort -----------------------
    plt.figure(figsize=(12, 8))
    
    for i, (tipo, rotulo) in enumerate(zip(tipos_lista, rotulos_tipos)):
        # Offset para posicionar as barras lado a lado em cada tamanho
        offset = -largura_total/2 + largura_barra/2 + i * largura_barra
        
        # Extrair os dados de tempo para cada tamanho
        tempos = [dados_cocktail_filtrados[tamanho][tipo] for tamanho in tamanhos_comuns]
        
        # Plotar as barras
        barras = plt.bar(x_pos + offset, tempos, largura_barra, 
                color=cores[i], label=f'Lista {rotulo}')
        
        # Adicionar os valores em cima de cada barra
        for j, barra in enumerate(barras):
            altura = barra.get_height()
            texto = formatar_valor(altura)
            plt.text(barra.get_x() + barra.get_width()/2., altura + 0.01*max(tempos),
                    texto, ha='center', va='bottom', fontsize=8, rotation=45)
    
    # Configurações do gráfico
    plt.title('Desempenho do Cocktail Sort por Tamanho e Tipo de Lista (Dados Pequenos)')
    plt.xlabel('Tamanho da Lista')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.xticks(x_pos, tamanhos_comuns)
    plt.grid(True, axis='y')
    plt.legend()
    
    plt.tight_layout()
    save_path = os.path.join(base_dir, 'Resultados', 'barras_cocktail_pequenos.png')
    plt.savefig(save_path)
    print(f"Gráfico de barras para Cocktail Sort (dados pequenos) gerado: '{save_path}'")
    
    # ----------------------- Gráfico para o Radix Sort -----------------------
    plt.figure(figsize=(12, 8))
    
    for i, (tipo, rotulo) in enumerate(zip(tipos_lista, rotulos_tipos)):
        # Offset para posicionar as barras lado a lado em cada tamanho
        offset = -largura_total/2 + largura_barra/2 + i * largura_barra
        
        # Extrair os dados de tempo para cada tamanho
        tempos = [dados_radix_filtrados[tamanho][tipo] for tamanho in tamanhos_comuns]
        
        # Plotar as barras
        barras = plt.bar(x_pos + offset, tempos, largura_barra, 
                color=cores[i], label=f'Lista {rotulo}')
        
        # Adicionar os valores em cima de cada barra
        for j, barra in enumerate(barras):
            altura = barra.get_height()
            texto = formatar_valor(altura)
            plt.text(barra.get_x() + barra.get_width()/2., altura + 0.01*max(tempos),
                    texto, ha='center', va='bottom', fontsize=8, rotation=45)
    
    # Configurações do gráfico
    plt.title('Desempenho do Radix Sort por Tamanho e Tipo de Lista (Dados Pequenos)')
    plt.xlabel('Tamanho da Lista')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.xticks(x_pos, tamanhos_comuns)
    plt.grid(True, axis='y')
    plt.legend()
    
    plt.tight_layout()
    save_path = os.path.join(base_dir, 'Resultados', 'barras_radix_pequenos.png')
    plt.savefig(save_path)
    print(f"Gráfico de barras para Radix Sort (dados pequenos) gerado: '{save_path}'")
    
    print("\nTodos os gráficos com dados pequenos foram gerados com sucesso!")

# # Executar as funções de geração de gráficos
# if __name__ == "__main__":
#     # Verificar se o diretório de resultados existe
#     base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     resultados_dir = os.path.join(base_dir, 'Resultados')
#     if not os.path.exists(resultados_dir):
#         os.makedirs(resultados_dir)
        
#     print("Gerando gráficos de comparação...")
#     gerar_grafico_comparativo_algoritmos()
    
#     print("\nGerando gráficos de desempenho por algoritmo...")
#     gerar_grafico_por_algoritmo()
    
#     print("\nGerando gráficos de barras comparativos...")
#     gerar_grafico_barras_comparativo()
    
#     print("\nGerando gráficos para dados pequenos...")
#     gerar_graficos_dados_pequenos()
    
#     print("\nTodos os gráficos foram gerados com sucesso!")