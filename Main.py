from Auxiliar import Cronometro 
from Auxiliar import Manipulador_arquivos_txt
from Algoritmos import Coktail
from Algoritmos import Radix

#Defina na lista cada indice indicando a quantidade de numero do arquivo de teste, e a quantidade de indices indica quantos testes serao feitos
lista_quantidade_de_testes = ["100"]

def executar_testes_coktail():

    #Para cada quantidade ler o arquivo correspondente (Ja padronizado na funcao de gerar arquivos so mudando a quantidade)
    for i in lista_quantidade_de_testes:
        
        Manipulador_arquivos_txt.limpar_arquivo(f'Resultados/Resultados_coktail_{i}.txt')
        
        lista_crescente = Manipulador_arquivos_txt.ler_numeros_do_arquivo(f'Arquivos_testes/crescentes_{i}.txt')
        lista_decrescente = Manipulador_arquivos_txt.ler_numeros_do_arquivo(f'Arquivos_testes/decrescentes_{i}.txt')
        lista_aleatoria = Manipulador_arquivos_txt.ler_numeros_do_arquivo(f'Arquivos_testes/aleatorios_{i}.txt')
        
        print()
        
        def testar_lista(tipo_lista:str, lista:list[int]):
            cronometro = Cronometro.Cronometro()
            cronometro.iniciar()
            Coktail.cocktail_sort(lista)
            cronometro.parar()
            tempo_milisegundos = cronometro.tempo_milisegundos()
            print(f"Tempo de execução do Cocktail Sort para lista {tipo_lista} com {i} elementos: {tempo_milisegundos} milissegundos")
            cronometro.resetar()
            
            return tempo_milisegundos
        
        resultado_crescente = testar_lista("crescente", lista_crescente)
        resultado_decrescente = testar_lista("decrescente", lista_decrescente)
        resultado_aleatoria = testar_lista("aleatória", lista_aleatoria)
        
        print()

        Manipulador_arquivos_txt.escrever_no_arquivo(f'Resultados/Resultados_coktail_{i}.txt',
                                                     f"Resultados do Cocktail Sort para listas com {i} elementos:\n\n"
                                                     f"Lista crescente: {resultado_crescente} milissegundos\n"
                                                     f"Lista decrescente: {resultado_decrescente} milissegundos\n"
                                                     f"Lista aleatoria: {resultado_aleatoria} milissegundos\n\n"
                                                     f"---------------------------------\n\n")
        
        print()


def executar_testes_radix():
    
    #Para cada quantidade ler o arquivo correspondente (Ja padronizado na funcao de gerar arquivos so mudando a quantidade)
    for i in lista_quantidade_de_testes:
        
        Manipulador_arquivos_txt.limpar_arquivo(f'Resultados/Resultados_radix_{i}.txt')
        
        lista_crescente = Manipulador_arquivos_txt.ler_numeros_do_arquivo(f'Arquivos_testes/crescentes_{i}.txt')
        lista_decrescente = Manipulador_arquivos_txt.ler_numeros_do_arquivo(f'Arquivos_testes/decrescentes_{i}.txt')
        lista_aleatoria = Manipulador_arquivos_txt.ler_numeros_do_arquivo(f'Arquivos_testes/aleatorios_{i}.txt')
        
        print()
        
        def testar_lista(tipo_lista:str, lista:list[int]):
            cronometro = Cronometro.Cronometro()
            cronometro.iniciar()
            Radix.radix_sort(lista)
            cronometro.parar()
            tempo_milisegundos = cronometro.tempo_milisegundos()
            print(f"Tempo de execução do Radix Sort para lista {tipo_lista} com {i} elementos: {tempo_milisegundos} milissegundos")
            cronometro.resetar()
            
            return tempo_milisegundos

        resultado_crescente = testar_lista("crescente", lista_crescente)
        resultado_decrescente = testar_lista("decrescente", lista_decrescente)
        resultado_aleatoria = testar_lista("aleatória", lista_aleatoria)
        
        print()
        
        Manipulador_arquivos_txt.escrever_no_arquivo(f'Resultados/Resultados_radix_{i}.txt',
                                                     f"Resultados do Radix Sort para listas com {i} elementos:\n\n"
                                                     f"Lista crescente: {resultado_crescente} milissegundos\n"
                                                     f"Lista decrescente: {resultado_decrescente} milissegundos\n"
                                                     f"Lista aleatoria: {resultado_aleatoria} milissegundos\n\n"
                                                     f"---------------------------------\n\n")
        
        print()



if __name__ == '__main__':
    
    
    
    executar_testes_coktail()
    print("\n---------------------------------\n")
    executar_testes_radix()