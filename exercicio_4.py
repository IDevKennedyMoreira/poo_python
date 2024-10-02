"""Crie uma classe Carro que tenha os atributos marca, modelo, ano, e velocidade_atual.
Adicione métodos para acelerar e frear o carro, 
alterando o valor da velocidade_atual."""

import enum

class Marca(enum.Enum):
    FORD = "FORD"
    CHEVROLET = "CHEVROLET"
    FIAT = "FIAT"
    CITROEN = "CITROEN"

class Carro:
    def __init__(self, marca:Marca, modelo: str, ano: int, velocidade_atual: int = 0):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._velocidade_atual = velocidade_atual

    @property
    def marca(self) -> Marca:
        return self._marca
    
    @property
    def modelo(self) -> str:
        return self._modelo
    
    @property
    def ano(self) -> int:
        return self._ano
    
    @property
    def velocidade_atual(self) -> int:
        return self._velocidade_atual
    
    @marca.setter
    def marca(self, marca: Marca) -> None:
        self._marca = marca

    @modelo.setter
    def modelo(self, modelo: str) -> None:
        self._modelo = modelo

    @ano.setter
    def ano(self, ano:int) -> None:
        if ano >= 1920:
            self._ano = ano
        else:
            raise ValueError("Nao sao permitidos carros abaixo de 1920")
        
    @velocidade_atual.setter
    def velocidade_atual(self, velocidade_atual: int) -> None:
        self._velocidade_atual = velocidade_atual

    def acelerar(self) -> None:
        self._velocidade_atual += 1 

    def frear(self) -> None:
        if self._velocidade_atual > 0:
            self._velocidade_atual -= 1 
        elif self._velocidade_atual == 0:
            return
        else:
            self._velocidade_atual += 1

