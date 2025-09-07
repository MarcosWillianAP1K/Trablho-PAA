from Auxiliar import Cronometro 
from Auxiliar import Gerador_de_testes
from Algoritmos import Coktail
from Algoritmos import Radix



def executar_testes_coktail():
    
    lista_crescente = Gerador_de_testes.ler_numeros_do_arquivo('Arquivos_testes/crescentes_100.txt')
    lista_decrescente = Gerador_de_testes.ler_numeros_do_arquivo('Arquivos_testes/decrescentes_100.txt')
    lista_aleatoria = Gerador_de_testes.ler_numeros_do_arquivo('Arquivos_testes/aleatorios_100.txt')
    
    cronometro = Cronometro.Cronometro()
    
    cronometro.iniciar()
    
    Coktail.cocktail_sort(lista_crescente)
    
    cronometro.parar()

    print(f"\nTempo de execução do Cocktail Sort para lista crescente: {cronometro.tempo_milisegundos()} milissegundos")
    
    cronometro.resetar()
    
    
    
    cronometro.iniciar()
    
    Coktail.cocktail_sort(lista_decrescente)
    
    cronometro.parar()
    
    print(f"Tempo de execução do Cocktail Sort para lista decrescente: {cronometro.tempo_milisegundos()} milissegundos")
    
    cronometro.resetar()
    
    
    cronometro.iniciar()
    
    Coktail.cocktail_sort(lista_aleatoria)
    
    cronometro.parar()
    
    print(f"Tempo de execução do Cocktail Sort para lista aleatória: {cronometro.tempo_milisegundos()} milissegundos")

    cronometro.resetar()



def executar_testes_radix():
    
    lista_crescente = Gerador_de_testes.ler_numeros_do_arquivo('Arquivos_testes/crescentes_100.txt')
    lista_decrescente = Gerador_de_testes.ler_numeros_do_arquivo('Arquivos_testes/decrescentes_100.txt')
    lista_aleatoria = Gerador_de_testes.ler_numeros_do_arquivo('Arquivos_testes/aleatorios_100.txt')
    
    
    
    cronometro = Cronometro.Cronometro()
    
    cronometro.iniciar()
    
    Radix.radix_sort(lista_crescente)
    
    cronometro.parar()

    print(f"\nTempo de execução do Radix Sort para lista crescente: {cronometro.tempo_milisegundos()} milissegundos")
    
    cronometro.resetar()
    
    
    
    cronometro.iniciar()
    
    Radix.radix_sort(lista_decrescente)
    
    cronometro.parar()
    
    print(f"Tempo de execução do Radix Sort para lista decrescente: {cronometro.tempo_milisegundos()} milissegundos")
    
    cronometro.resetar()
    
    
    cronometro.iniciar()
    
    Radix.radix_sort(lista_aleatoria)
    
    cronometro.parar()
    
    print(f"Tempo de execução do Radix Sort para lista aleatória: {cronometro.tempo_milisegundos()} milissegundos")

    cronometro.resetar()
    
    


if __name__ == '__main__':
    executar_testes_coktail()
    print("\n---------------------------------\n")
    executar_testes_radix()