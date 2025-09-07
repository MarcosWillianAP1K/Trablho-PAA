from Auxiliar import Cronometro 

cronometro = Cronometro.Cronometro()

cronometro.iniciar()

cronometro.parar()

print("Tempo decorrido:", cronometro.tempo_decorrido(), "ms")