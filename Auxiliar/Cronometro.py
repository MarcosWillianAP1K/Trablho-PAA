import time

class Cronometro:
    def __init__(self):
        self.tempo_inicial = 0.0
        self.tempo_total = 0.0

    def iniciar(self):
        self.tempo_inicial = time.perf_counter() 

    def parar(self):
        self.tempo_total += time.perf_counter() - self.tempo_inicial

    def resetar(self):
        self.tempo_inicial = 0.0
        self.tempo_total = 0.0

    def tempo_decorrido(self):
        return self.tempo_total * 1000