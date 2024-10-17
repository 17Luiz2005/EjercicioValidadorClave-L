# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod


class ReglaValidacion(ABC):
    def __init__(self, _longitud_esperada: int):
        self._longitud_esperada = _longitud_esperada

    def _validar_longitud(self, clave:str)->bool:
        return len(clave) > self._longitud_esperada
    
    def _contiene_mayuscula(self, clave: str)->bool:
        return any(c.isupper() for c in clave)

    def _contiene_mayusculas(self, clave: str)->bool:
        return any(c.islower() for c in clave)
    
    def _contiene_numero(self, clave: str)->bool:
        return any(c.isdigit() for c in clave)


    @abstractmethod
    def es_valida(self, clave: str)->bool:
        pass

