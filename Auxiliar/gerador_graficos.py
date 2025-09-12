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
    Gera gráficos comparando o desempenho do Cocktail Sort com ambas as variações do Radix Sort
    para diferentes tamanhos e tipos de listas.
    """
    import os
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dados_cocktail = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_coktail.txt'))
    dados_radix_counting = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_radix_counting.txt'))
    dados_radix_bucket = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_radix_bucket.txt'))
    
    # Verificar se foram extraídos dados
    if not dados_cocktail:
        print("Erro: Não foi possível extrair dados do Cocktail Sort")
        return
        
    # Tipos de lista e seus rótulos
    tipos_lista = ['crescente', 'decrescente', 'aleatorio']
    rotulos_tipos = ['Crescente', 'Decrescente', 'Aleatória']
    
    # ----------------------- Comparação Cocktail vs Radix Counting -----------------------
    if dados_radix_counting:
        tamanhos_comuns = sorted(set(dados_cocktail.keys()) & set(dados_radix_counting.keys()))
        
        if tamanhos_comuns:
            plt.figure(figsize=(15, 10))
            
            for i, (tipo, rotulo) in enumerate(zip(tipos_lista, rotulos_tipos)):
                plt.subplot(1, 3, i+1)
                
                x = tamanhos_comuns
                y_cocktail = [dados_cocktail[tamanho][tipo] for tamanho in tamanhos_comuns]
                y_radix = [dados_radix_counting[tamanho][tipo] for tamanho in tamanhos_comuns]
                
                plt.plot(x, y_cocktail, 'b-o', label='Cocktail Sort')
                plt.plot(x, y_radix, 'r-s', label='Radix Sort (Counting)')
                
                # Adicionar os valores em cada ponto
                for j, (xval, yval) in enumerate(zip(x, y_cocktail)):
                    texto = formatar_valor(yval)
                    plt.annotate(texto, (xval, yval), xytext=(0, 10), 
                                 textcoords='offset points', ha='center', fontsize=8)
                
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
            save_path = os.path.join(base_dir, 'Resultados', 'comparacao_cocktail_radix_counting.png')
            plt.savefig(save_path)
            print(f"Gráfico de comparação Cocktail vs Radix Counting gerado: '{save_path}'")
    
    # ----------------------- Comparação Cocktail vs Radix Bucket -----------------------
    if dados_radix_bucket:
        tamanhos_comuns = sorted(set(dados_cocktail.keys()) & set(dados_radix_bucket.keys()))
        
        if tamanhos_comuns:
            plt.figure(figsize=(15, 10))
            
            for i, (tipo, rotulo) in enumerate(zip(tipos_lista, rotulos_tipos)):
                plt.subplot(1, 3, i+1)
                
                x = tamanhos_comuns
                y_cocktail = [dados_cocktail[tamanho][tipo] for tamanho in tamanhos_comuns]
                y_radix = [dados_radix_bucket[tamanho][tipo] for tamanho in tamanhos_comuns]
                
                plt.plot(x, y_cocktail, 'b-o', label='Cocktail Sort')
                plt.plot(x, y_radix, 'g-^', label='Radix Sort (Bucket)')
                
                # Adicionar os valores em cada ponto
                for j, (xval, yval) in enumerate(zip(x, y_cocktail)):
                    texto = formatar_valor(yval)
                    plt.annotate(texto, (xval, yval), xytext=(0, 10), 
                                 textcoords='offset points', ha='center', fontsize=8)
                
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
            save_path = os.path.join(base_dir, 'Resultados', 'comparacao_cocktail_radix_bucket.png')
            plt.savefig(save_path)
            print(f"Gráfico de comparação Cocktail vs Radix Bucket gerado: '{save_path}'")

    # ----------------------- Comparação das duas variações do Radix -----------------------
    if dados_radix_counting and dados_radix_bucket:
        tamanhos_comuns = sorted(set(dados_radix_counting.keys()) & set(dados_radix_bucket.keys()))
        
        if tamanhos_comuns:
            plt.figure(figsize=(15, 10))
            
            for i, (tipo, rotulo) in enumerate(zip(tipos_lista, rotulos_tipos)):
                plt.subplot(1, 3, i+1)
                
                x = tamanhos_comuns
                y_counting = [dados_radix_counting[tamanho][tipo] for tamanho in tamanhos_comuns]
                y_bucket = [dados_radix_bucket[tamanho][tipo] for tamanho in tamanhos_comuns]
                
                plt.plot(x, y_counting, 'r-s', label='Radix Sort (Counting)')
                plt.plot(x, y_bucket, 'g-^', label='Radix Sort (Bucket)')
                
                # Adicionar os valores em cada ponto
                for j, (xval, yval) in enumerate(zip(x, y_counting)):
                    texto = formatar_valor(yval)
                    plt.annotate(texto, (xval, yval), xytext=(0, 10), 
                                 textcoords='offset points', ha='center', fontsize=8)
                
                for j, (xval, yval) in enumerate(zip(x, y_bucket)):
                    texto = formatar_valor(yval)
                    plt.annotate(texto, (xval, yval), xytext=(0, -15), 
                                 textcoords='offset points', ha='center', fontsize=8)
                
                plt.title(f'Comparação Radix - Lista {rotulo}')
                plt.xlabel('Tamanho da Lista')
                plt.ylabel('Tempo de Execução (segundos)')
                plt.grid(True)
                plt.legend()
                plt.xticks(tamanhos_comuns)
                
            plt.tight_layout()
            save_path = os.path.join(base_dir, 'Resultados', 'comparacao_radix_counting_bucket.png')
            plt.savefig(save_path)
            print(f"Gráfico de comparação entre variações do Radix gerado: '{save_path}'")
    
def gerar_grafico_por_algoritmo():
    """
    Gera gráficos separados para cada algoritmo, mostrando o desempenho
    para diferentes tipos de lista.
    """
    import os
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dados_cocktail = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_coktail.txt'))
    dados_radix_counting = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_radix_counting.txt'))
    dados_radix_bucket = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_radix_bucket.txt'))
    
    algoritmos = [
        ('Cocktail Sort', dados_cocktail, 'cocktail'),
        ('Radix Sort (Counting)', dados_radix_counting, 'radix_counting'),
        ('Radix Sort (Bucket)', dados_radix_bucket, 'radix_bucket')
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
    Gera gráficos de barras separados para cada algoritmo,
    mostrando o desempenho para cada tamanho e tipo de lista.
    """
    import os
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dados_cocktail = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_coktail.txt'))
    dados_radix_counting = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_radix_counting.txt'))
    dados_radix_bucket = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_radix_bucket.txt'))
    
    algoritmos = [
        ('Cocktail Sort', dados_cocktail, 'cocktail'),
        ('Radix Sort (Counting)', dados_radix_counting, 'radix_counting'),
        ('Radix Sort (Bucket)', dados_radix_bucket, 'radix_bucket')
    ]
    
    cores = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Azul, Laranja, Verde
    tipos_lista = ['crescente', 'decrescente', 'aleatorio']
    rotulos_tipos = ['Crescente', 'Decrescente', 'Aleatória']
    
    for nome, dados, arquivo in algoritmos:
        if not dados:
            continue
            
        tamanhos = sorted(dados.keys())
        n_tamanhos = len(tamanhos)
        n_tipos = len(tipos_lista)
        largura_total = 0.8
        largura_barra = largura_total / n_tipos
        x_pos = np.arange(n_tamanhos)
        
        plt.figure(figsize=(12, 8))
        
        for i, (tipo, rotulo) in enumerate(zip(tipos_lista, rotulos_tipos)):
            offset = -largura_total/2 + largura_barra/2 + i * largura_barra
            tempos = [dados[tamanho][tipo] for tamanho in tamanhos]
            
            barras = plt.bar(x_pos + offset, tempos, largura_barra, 
                    color=cores[i], label=f'Lista {rotulo}')
            
            for j, barra in enumerate(barras):
                altura = barra.get_height()
                texto = formatar_valor(altura)
                plt.text(barra.get_x() + barra.get_width()/2., altura + 0.01*max(tempos),
                        texto, ha='center', va='bottom', fontsize=8, rotation=45)
        
        plt.title(f'Desempenho do {nome} por Tamanho e Tipo de Lista')
        plt.xlabel('Tamanho da Lista')
        plt.ylabel('Tempo de Execução (segundos)')
        plt.xticks(x_pos, tamanhos)
        plt.grid(True, axis='y')
        plt.legend()
        
        plt.tight_layout()
        save_path = os.path.join(base_dir, 'Resultados', f'barras_{arquivo}.png')
        plt.savefig(save_path)
        print(f"Gráfico de barras para {nome} gerado: '{save_path}'")

def gerar_graficos_dados_pequenos():
    """
    Gera todos os gráficos (comparativo, por algoritmo e barras) utilizando
    apenas os dados dos testes com 100, 500 e 1000 elementos.
    """
    import os
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dados_cocktail = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_coktail.txt'))
    dados_radix_counting = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_radix_counting.txt'))
    dados_radix_bucket = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_radix_bucket.txt'))
    
    # Verificar se foram extraídos dados
    if not dados_cocktail:
        print("Erro: Não foi possível extrair dados do Cocktail Sort")
        return
    
    # Filtrar apenas os tamanhos pequenos
    tamanhos_pequenos = [100, 500, 1000]
    
    # Filtrar os dados para conter apenas os tamanhos pequenos
    dados_cocktail_filtrados = {k: v for k, v in dados_cocktail.items() if k in tamanhos_pequenos}
    dados_radix_counting_filtrados = {k: v for k, v in dados_radix_counting.items() if k in tamanhos_pequenos} if dados_radix_counting else {}
    dados_radix_bucket_filtrados = {k: v for k, v in dados_radix_bucket.items() if k in tamanhos_pequenos} if dados_radix_bucket else {}
    
    tipos_lista = ['crescente', 'decrescente', 'aleatorio']
    rotulos_tipos = ['Crescente', 'Decrescente', 'Aleatória']
    
    # ----------------------- Comparação Cocktail vs Radix Counting (pequenos) -----------------------
    if dados_radix_counting_filtrados:
        tamanhos_comuns = sorted(set(dados_cocktail_filtrados.keys()) & set(dados_radix_counting_filtrados.keys()))
        
        if tamanhos_comuns:
            plt.figure(figsize=(15, 10))
            
            for i, (tipo, rotulo) in enumerate(zip(tipos_lista, rotulos_tipos)):
                plt.subplot(1, 3, i+1)
                
                x = tamanhos_comuns
                y_cocktail = [dados_cocktail_filtrados[tamanho][tipo] for tamanho in tamanhos_comuns]
                y_radix = [dados_radix_counting_filtrados[tamanho][tipo] for tamanho in tamanhos_comuns]
                
                plt.plot(x, y_cocktail, 'b-o', label='Cocktail Sort')
                plt.plot(x, y_radix, 'r-s', label='Radix Sort (Counting)')
                
                # Adicionar os valores em cada ponto
                for j, (xval, yval) in enumerate(zip(x, y_cocktail)):
                    texto = formatar_valor(yval)
                    plt.annotate(texto, (xval, yval), xytext=(0, 10), 
                                 textcoords='offset points', ha='center', fontsize=8)
                                 
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
            save_path = os.path.join(base_dir, 'Resultados', 'comparacao_cocktail_radix_counting_pequenos.png')
            plt.savefig(save_path)
            print(f"Gráfico de comparação Cocktail vs Radix Counting (dados pequenos) gerado: '{save_path}'")
    
    # ----------------------- Comparação Cocktail vs Radix Bucket (pequenos) -----------------------
    if dados_radix_bucket_filtrados:
        tamanhos_comuns = sorted(set(dados_cocktail_filtrados.keys()) & set(dados_radix_bucket_filtrados.keys()))
        
        if tamanhos_comuns:
            plt.figure(figsize=(15, 10))
            
            for i, (tipo, rotulo) in enumerate(zip(tipos_lista, rotulos_tipos)):
                plt.subplot(1, 3, i+1)
                
                x = tamanhos_comuns
                y_cocktail = [dados_cocktail_filtrados[tamanho][tipo] for tamanho in tamanhos_comuns]
                y_radix = [dados_radix_bucket_filtrados[tamanho][tipo] for tamanho in tamanhos_comuns]
                
                plt.plot(x, y_cocktail, 'b-o', label='Cocktail Sort')
                plt.plot(x, y_radix, 'g-^', label='Radix Sort (Bucket)')
                
                # Adicionar os valores em cada ponto
                for j, (xval, yval) in enumerate(zip(x, y_cocktail)):
                    texto = formatar_valor(yval)
                    plt.annotate(texto, (xval, yval), xytext=(0, 10), 
                                 textcoords='offset points', ha='center', fontsize=8)
                                 
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
            save_path = os.path.join(base_dir, 'Resultados', 'comparacao_cocktail_radix_bucket_pequenos.png')
            plt.savefig(save_path)
            print(f"Gráfico de comparação Cocktail vs Radix Bucket (dados pequenos) gerado: '{save_path}'")
    
    # ---------------- Gráficos por algoritmo (linha) ----------------
    algoritmos = [
        ('Cocktail Sort', dados_cocktail_filtrados, 'cocktail'),
        ('Radix Sort (Counting)', dados_radix_counting_filtrados, 'radix_counting'),
        ('Radix Sort (Bucket)', dados_radix_bucket_filtrados, 'radix_bucket')
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
    
    # ----------------------- Gráfico para o Radix Sort (Counting) -----------------------
    plt.figure(figsize=(12, 8))
    
    for i, (tipo, rotulo) in enumerate(zip(tipos_lista, rotulos_tipos)):
        # Offset para posicionar as barras lado a lado em cada tamanho
        offset = -largura_total/2 + largura_barra/2 + i * largura_barra
        
        # Extrair os dados de tempo para cada tamanho
        tempos = [dados_radix_counting_filtrados[tamanho][tipo] for tamanho in tamanhos_comuns]
        
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
    plt.title('Desempenho do Radix Sort (Counting) por Tamanho e Tipo de Lista (Dados Pequenos)')
    plt.xlabel('Tamanho da Lista')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.xticks(x_pos, tamanhos_comuns)
    plt.grid(True, axis='y')
    plt.legend()
    
    plt.tight_layout()
    save_path = os.path.join(base_dir, 'Resultados', 'barras_radix_counting_pequenos.png')
    plt.savefig(save_path)
    print(f"Gráfico de barras para Radix Sort (Counting) (dados pequenos) gerado: '{save_path}'")
    
    # ----------------------- Gráfico para o Radix Sort (Bucket) -----------------------
    plt.figure(figsize=(12, 8))
    
    for i, (tipo, rotulo) in enumerate(zip(tipos_lista, rotulos_tipos)):
        # Offset para posicionar as barras lado a lado em cada tamanho
        offset = -largura_total/2 + largura_barra/2 + i * largura_barra
        
        # Extrair os dados de tempo para cada tamanho
        tempos = [dados_radix_bucket_filtrados[tamanho][tipo] for tamanho in tamanhos_comuns]
        
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
    plt.title('Desempenho do Radix Sort (Bucket) por Tamanho e Tipo de Lista (Dados Pequenos)')
    plt.xlabel('Tamanho da Lista')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.xticks(x_pos, tamanhos_comuns)
    plt.grid(True, axis='y')
    plt.legend()
    
    plt.tight_layout()
    save_path = os.path.join(base_dir, 'Resultados', 'barras_radix_bucket_pequenos.png')
    plt.savefig(save_path)
    print(f"Gráfico de barras para Radix Sort (Bucket) (dados pequenos) gerado: '{save_path}'")
    
    print("\nTodos os gráficos com dados pequenos foram gerados com sucesso!")

def gerar_tabelas_html():
    """
    Gera tabelas HTML com os resultados dos algoritmos, com os tamanhos das listas
    na primeira coluna e os tipos de lista (crescente, decrescente, aleatória) nas colunas.
    Salva as tabelas em arquivos HTML na pasta de Resultados.
    """
    # Use absolute paths to ensure correct file location
    import os
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dados_cocktail = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_coktail.txt'))
    dados_radix_counting = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_radix_counting.txt'))
    dados_radix_bucket = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_radix_bucket.txt'))
    
    # Verificar se foram extraídos dados
    if not dados_cocktail:
        print("Erro: Não foi possível extrair dados do Cocktail Sort")
        return
    
    algoritmos = [
        ('Cocktail Sort', dados_cocktail, 'cocktail'),
        ('Radix Sort (Counting)', dados_radix_counting, 'radix_counting'),
        ('Radix Sort (Bucket)', dados_radix_bucket, 'radix_bucket')
    ]
    
    # Estilos CSS para a tabela
    estilos_css = """
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
            font-family: Arial, sans-serif;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }
        th {
            padding-top: 12px;
            padding-bottom: 12px;
            background-color: #4CAF50;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        tr:hover {
            background-color: #ddd;
        }
        .header {
            text-align: center;
            padding: 20px 0;
            font-family: Arial, sans-serif;
        }
    </style>
    """
    
    # Para cada algoritmo, gerar uma tabela
    for nome, dados, arquivo in algoritmos:
        if not dados:
            continue
            
        tamanhos = sorted(dados.keys())
        
        # Criar o conteúdo HTML
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Resultados do {nome}</title>
            {estilos_css}
        </head>
        <body>
            <div class="header">
                <h1>Resultados do {nome}</h1>
                <p>Tempos de execução para diferentes tamanhos de lista e tipos de entrada</p>
            </div>
            
            <table>
                <tr>
                    <th>Tamanho da Lista</th>
                    <th>Lista Crescente (s)</th>
                    <th>Lista Decrescente (s)</th>
                    <th>Lista Aleatória (s)</th>
                </tr>
        """
        
        # Adicionar os dados para cada tamanho de lista
        for tamanho in tamanhos:
            tempo_crescente = formatar_valor(dados[tamanho]['crescente'])
            tempo_decrescente = formatar_valor(dados[tamanho]['decrescente'])
            tempo_aleatorio = formatar_valor(dados[tamanho]['aleatorio'])
            
            html_content += f"""
                <tr>
                    <td>{tamanho}</td>
                    <td>{tempo_crescente}</td>
                    <td>{tempo_decrescente}</td>
                    <td>{tempo_aleatorio}</td>
                </tr>
            """
        
        html_content += """
            </table>
        </body>
        </html>
        """
        
        # Salvar o arquivo HTML
        save_path = os.path.join(base_dir, 'Resultados', f'tabela_{arquivo}.html')
        with open(save_path, 'w') as f:
            f.write(html_content)
        
        print(f"Tabela HTML para {nome} gerada: '{save_path}'")
    
    # Criar uma tabela comparativa
    html_comparativo = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Comparação de Algoritmos</title>
        {estilos_css}
    </head>
    <body>
        <div class="header">
            <h1>Comparação entre Cocktail Sort e Radix Sort</h1>
            <p>Comparação dos tempos de execução para diferentes tamanhos e tipos de lista</p>
        </div>
    """
    
    # Lista de tamanhos comuns para comparação
    tamanhos_comuns = sorted(set(dados_cocktail.keys()) & set(dados_radix_counting.keys()) & set(dados_radix_bucket.keys()))
    
    # Para cada tipo de lista, criar uma tabela separada
    tipos = [('crescente', 'Lista Crescente'), ('decrescente', 'Lista Decrescente'), ('aleatorio', 'Lista Aleatória')]
    
    for tipo, titulo in tipos:
        html_comparativo += f"""
        <h2>{titulo}</h2>
        <table>
            <tr>
                <th>Tamanho da Lista</th>
                <th>Cocktail Sort (s)</th>
                <th>Radix Sort (Counting) (s)</th>
                <th>Radix Sort (Bucket) (s)</th>
                <th>Diferença (s)</th>
                <th>Cocktail/Radix Counting</th>
                <th>Cocktail/Radix Bucket</th>
            </tr>
        """
        
        for tamanho in tamanhos_comuns:
            tempo_cocktail = dados_cocktail[tamanho][tipo]
            tempo_radix_counting = dados_radix_counting[tamanho][tipo]
            tempo_radix_bucket = dados_radix_bucket[tamanho][tipo]
            diferenca_counting = tempo_cocktail - tempo_radix_counting
            diferenca_bucket = tempo_cocktail - tempo_radix_bucket
            razao_counting = tempo_cocktail / tempo_radix_counting if tempo_radix_counting > 0 else float('inf')
            razao_bucket = tempo_cocktail / tempo_radix_bucket if tempo_radix_bucket > 0 else float('inf')
            
            html_comparativo += f"""
            <tr>
                <td>{tamanho}</td>
                <td>{formatar_valor(tempo_cocktail)}</td>
                <td>{formatar_valor(tempo_radix_counting)}</td>
                <td>{formatar_valor(tempo_radix_bucket)}</td>
                <td>{formatar_valor(diferenca_counting)}</td>
                <td>{formatar_valor(razao_counting)}</td>
                <td>{formatar_valor(razao_bucket)}</td>
            </tr>
            """
        
        html_comparativo += """
        </table>
        """
    
    html_comparativo += """
    </body>
    </html>
    """
    
    # Salvar o arquivo HTML comparativo
    save_path_comp = os.path.join(base_dir, 'Resultados', 'tabela_comparativa.html')
    with open(save_path_comp, 'w') as f:
        f.write(html_comparativo)
    
    print(f"Tabela HTML comparativa gerada: '{save_path_comp}'")

def gerar_tabelas_png():
    """
    Gera tabelas como imagens PNG com os resultados dos algoritmos, mostrando o tamanho
    das listas na primeira coluna e os tipos de listas nas colunas.
    """
    import os
    from matplotlib.table import Table
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dados_cocktail = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_coktail.txt'))
    dados_radix_counting = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_radix_counting.txt'))
    dados_radix_bucket = extrair_dados_arquivo(os.path.join(base_dir, 'Resultados', 'Resultados_radix_bucket.txt'))
    
    algoritmos = [
        ('Cocktail Sort', dados_cocktail, 'cocktail'),
        ('Radix Sort (Counting)', dados_radix_counting, 'radix_counting'),
        ('Radix Sort (Bucket)', dados_radix_bucket, 'radix_bucket')
    ]
    
    # Gerar uma tabela para cada algoritmo
    for nome, dados, arquivo in algoritmos:
        if not dados:
            continue
            
        tamanhos = sorted(dados.keys())
        
        # Definir o tamanho da figura baseado no número de linhas (tamanhos)
        fig_height = max(6, 3 + len(tamanhos) * 0.4)
        plt.figure(figsize=(10, fig_height))
        ax = plt.subplot(111, frame_on=False)
        ax.xaxis.set_visible(False)  # Esconder eixo x
        ax.yaxis.set_visible(False)  # Esconder eixo y
        
        # Criar cabeçalho com os títulos das colunas
        cell_text = []
        for tamanho in tamanhos:
            # Formatar os valores para cada tipo de lista
            row = [
                f"{tamanho}",
                formatar_valor(dados[tamanho]['crescente']),
                formatar_valor(dados[tamanho]['decrescente']),
                formatar_valor(dados[tamanho]['aleatorio'])
            ]
            cell_text.append(row)
        
        # Definir cabeçalhos de coluna
        column_headers = [
            'Tamanho da Lista', 
            'Lista Crescente (s)', 
            'Lista Decrescente (s)', 
            'Lista Aleatória (s)'
        ]
        
        # Criar a tabela
        table = ax.table(
            cellText=cell_text,
            colLabels=column_headers,
            loc='center',
            cellLoc='center'
        )
        
        # Estilizar a tabela
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1, 1.5)  # Tornar células um pouco mais altas
        
        # Estilizar cabeçalho
        for k, cell in table.get_celld().items():
            if k[0] == 0:  # Cabeçalho (primeira linha)
                cell.set_text_props(weight='bold', color='white')
                cell.set_facecolor('#4CAF50')  # Verde
            else:  # Corpo da tabela
                if k[0] % 2 == 0:  # Linhas pares
                    cell.set_facecolor('#f2f2f2')  # Cinza claro
        
        plt.title(f'Resultados do {nome}', fontsize=16, pad=20)
        plt.tight_layout()
        
        # Salvar a tabela como imagem
        save_path = os.path.join(base_dir, 'Resultados', f'tabela_{arquivo}.png')
        plt.savefig(save_path, bbox_inches='tight', dpi=200)
        print(f"Tabela PNG para {nome} gerada: '{save_path}'")
        plt.close()
    
    # Criar tabelas comparativas separadas por tipo de lista
    tipos = [('crescente', 'Lista Crescente'), ('decrescente', 'Lista Decrescente'), ('aleatorio', 'Lista Aleatória')]
    tamanhos_comuns = sorted(set(dados_cocktail.keys()) & set(dados_radix_counting.keys()) & set(dados_radix_bucket.keys()))
    
    for tipo, titulo in tipos:
        fig_height = max(6, 3 + len(tamanhos_comuns) * 0.4)
        plt.figure(figsize=(12, fig_height))
        ax = plt.subplot(111, frame_on=False)
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        
        # Criar dados para a tabela
        cell_text = []
        for tamanho in tamanhos_comuns:
            tempo_cocktail = dados_cocktail[tamanho][tipo]
            tempo_radix_counting = dados_radix_counting[tamanho][tipo]
            tempo_radix_bucket = dados_radix_bucket[tamanho][tipo]
            diferenca_counting = tempo_cocktail - tempo_radix_counting
            diferenca_bucket = tempo_cocktail - tempo_radix_bucket
            razao_counting = tempo_cocktail / tempo_radix_counting if tempo_radix_counting > 0 else float('inf')
            razao_bucket = tempo_cocktail / tempo_radix_bucket if tempo_radix_bucket > 0 else float('inf')
            
            row = [
                f"{tamanho}",
                formatar_valor(tempo_cocktail),
                formatar_valor(tempo_radix_counting),
                formatar_valor(tempo_radix_bucket),
                formatar_valor(diferenca_counting),
                formatar_valor(razao_counting),
                formatar_valor(razao_bucket)
            ]
            cell_text.append(row)
        
        # Definir cabeçalhos de coluna
        comp_headers = [
            'Tamanho da Lista',
            'Cocktail Sort (s)',
            'Radix Sort (Counting) (s)',
            'Radix Sort (Bucket) (s)',
            'Diferença (s)',
            'Cocktail/Radix Counting',
            'Cocktail/Radix Bucket'
        ]
        
        # Criar a tabela
        table = ax.table(
            cellText=cell_text,
            colLabels=comp_headers,
            loc='center',
            cellLoc='center'
        )
        
        # Estilizar a tabela
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1, 1.5)  # Tornar células um pouco mais altas
        
        # Estilizar cabeçalho e alternar cores de linhas
        for k, cell in table.get_celld().items():
            if k[0] == 0:  # Cabeçalho (primeira linha)
                cell.set_text_props(weight='bold', color='white')
                cell.set_facecolor('#4CAF50')  # Verde
            else:  # Corpo da tabela
                if k[0] % 2 == 0:  # Linhas pares
                    cell.set_facecolor('#f2f2f2')  # Cinza claro
        
        plt.title(f'Comparação - {titulo}', fontsize=16, pad=20)
        plt.tight_layout()
        
        # Salvar a tabela como imagem
        save_path = os.path.join(base_dir, 'Resultados', f'tabela_comparativa_{tipo}.png')
        plt.savefig(save_path, bbox_inches='tight', dpi=200)
        print(f"Tabela comparativa PNG para {titulo} gerada: '{save_path}'")
        plt.close()

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
    
#     print("\nGerando tabelas HTML...")
#     gerar_tabelas_html()
    
#     print("\nGerando tabelas PNG...")
#     gerar_tabelas_png()
    
#     print("\nTodos os gráficos e tabelas foram gerados com sucesso!")