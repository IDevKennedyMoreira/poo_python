"""Crie uma classe Circulo que tenha um atributo raio. 
Adicione métodos para calcular a área e a circunferência 
do círculo."""

from math import pi

class Circulo:
    def __init__(self,raio: float) -> None:
        self._raio = raio

    @property
    def raio(self) -> float:
        return self._raio
    
    @raio.setter
    def raio(self, raio) -> None:
        if raio > 0:
            self._raio = raio
        else:
            raise ValueError("O valor de raio nao pode ser negativo")
        
    def calc_perimetro(self) -> float:
        return 2*pi*self._raio
    
    def calc_area(self) -> float:
        return pi*(self._raio**2)
        