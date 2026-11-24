from abc import ABC, abstractmethod
class Paquete:
    def __init__(self, viajes): self.viajes = viajes
class ISolucionador(ABC):
    @abstractmethod
    def resolver(self, n): pass
