"""Crie uma classe ContaBancaria que tenha atributos como titular e saldo.
 Adicione métodos para depositar, sacar e consultar saldo."""

class ContaBancaria:
    def __init__(self, titular: str, saldo:float =0) -> None:
        self._titular = titular 
        self._saldo = saldo

    @property
    def saldo(self) -> float:
        return self._saldo
    
    @property
    def titular(self) -> str:
        return self._titular
    
    @saldo.setter
    def saldo(self,saldo: float):
        if saldo > 0:
            self._saldo = saldo
        else:
            raise ValueError("O valor de saldo nao pode ser negativo")
    
    @titular.setter
    def titular(self, titular: str)->None:
        self._titular = titular

    def depositar(self, valor:float)-> None:
        if valor > 0:
            self._saldo += valor 
        else:
            raise ValueError("Nao e permitido depositar um valor negativo")
        
    def sacar(self, valor:float) -> None:
        if (self._saldo - valor) >= 0:
            self._saldo -= valor
        else: 
            raise ValueError("Nao e possivel sacar acima do limite da conta")
    