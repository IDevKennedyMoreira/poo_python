"""Crie uma classe chamada Contador que mantenha um contador de quantas instâncias da classe foram criadas.
 Use um método de classe para obter o número de instâncias."""

class Contador:

    _contador: int = 0

    @classmethod
    def inc_contador(cls):
        cls._contador +=1

    @classmethod
    def contador(cls):
        return cls._contador

    def __init__(self):
        Contador.inc_contador()
        
