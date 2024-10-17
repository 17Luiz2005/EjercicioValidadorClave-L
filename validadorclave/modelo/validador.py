# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod


class ReglaValidacion(ABC):
    @abstractmethod
    def es_Valida(self, clave: str)->bool:
        pass

    def _validar_longitud(clave: str)->bool:
        pass