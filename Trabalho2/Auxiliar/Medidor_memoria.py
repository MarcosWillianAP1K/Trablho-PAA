import tracemalloc as tm
import inspect as ins
import sys
import gc


class MedidorMemoria:
    def __init__(self):
        self.memoria_atual = 0.0  # Inicializa com 0

    def iniciar_medicao(self):
        if tm.is_tracing():
            tm.stop()  # Para a medição anterior antes de iniciar nova
        gc.collect()  # Coleta lixo antes de iniciar a medição
        tm.start()

    def parar_medicao(self):
        if not tm.is_tracing():
            return  # Evita erro se não estiver medindo
        self.memoria_atual, _ = tm.get_traced_memory()
        tm.stop()

    def obter_memoria_MB(self) -> float:
        return self.memoria_atual / (1024 ** 2)  # Converte para MB
    
    def obter_memoria_kB(self) -> float:
        return self.memoria_atual / 1024  # Converte para kB
    
    def limpar_medicao(self):
        """Reseta a medição atual."""
        if tm.is_tracing():
            tm.stop()
        self.memoria_atual = 0
        tm.clear_traces()

    def estimar_memoria_total(self, profundidade_maxima):
        """
        Estima a memória total utilizada por funções RECURSIVAS, 
        somando a heap (memória dinâmica) com a stack (pilha de chamadas recursivas).
        
        Args:
            profundidade_maxima: Profundidade máxima da recursão (número máximo de chamadas empilhadas)
        
        Returns:
            float: Memória total estimada em MB (heap + stack da recursão)
        """
        
        def medir_memoria_frame_MB():
            """Mede o tamanho de um frame da pilha de chamadas em MB."""
            frame = ins.currentframe()
            tamanho = sys.getsizeof(frame) / (1024 ** 2)
            del frame
            return tamanho
        
        # Soma o uso da heap (medido) com o da stack recursiva (estimado)
        memoria_heap_mb = self.obter_memoria_MB()
        return memoria_heap_mb + (profundidade_maxima * medir_memoria_frame_MB())

