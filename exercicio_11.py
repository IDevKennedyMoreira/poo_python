"""
Exercício: Sistema de Cadastro de Veículos
Objetivo: Criar um sistema que represente diferentes tipos de veículos utilizando herança.

Especificações:
Classe Base: Veiculo

Atributos:
_marca (str): Marca do veículo.
_modelo (str): Modelo do veículo.
_ano (int): Ano de fabricação do veículo.
Métodos:
__init__(self, marca: str, modelo: str, ano: int): Construtor que inicializa os atributos.
def __str__(self): Método que retorna uma string formatada com as informações do veículo.
Classes Derivadas:

Carro

Atributo adicional:
_numero_de_portas (int): Número de portas do carro.
Métodos:
__init__(self, marca: str, modelo: str, ano: int, numero_de_portas: int): Construtor que chama o construtor da classe base e inicializa o novo atributo.
def __str__(self): Sobrescreve o método da classe base para incluir o número de portas.
Moto

Atributo adicional:
_tipo (str): Tipo da moto (por exemplo, "esportiva", "touring").
Métodos:
__init__(self, marca: str, modelo: str, ano: int, tipo: str): Construtor que chama o construtor da classe base e inicializa o novo atributo.
def __str__(self): Sobrescreve o método da classe base para incluir o tipo da moto.
Implementação:

Crie instâncias das classes Carro e Moto, e teste os métodos de impressão para verificar se a herança está funcionando corretamente.

"""
import enum

class Marca(enum.Enum):
    FORD = "FORD"
    FIAT = "FIAT"
    CHEVROLET = "CHEVROLET"
    CITROEN = "CITROEN"
    PEUGEOT = "PEUGEOT"

class Tipo(enum.Enum):
    ESPORTIVA = "ESPORTIVA"
    TOURING = "TOURING"

class Veiculo:
    def __init__(self, marca: Marca, modelo: str, ano: int):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano

    @property
    def marca(self) -> Marca:
        return self._marca
    
    @property
    def modelo(self) -> str:
        return self._modelo
    
    @property
    def ano(self) -> int:
        return self._ano
    
    @marca.setter
    def marca(self, marca: Marca) -> None:
        if isinstance(marca, Marca):
            self._marca = marca
        else:
            raise ValueError("Marca deve ser uma instância de Marca")

    @modelo.setter
    def modelo(self, modelo: str) -> None:
        if isinstance(modelo, str) and len(modelo) > 0:
            self._modelo = modelo
        else:
            raise ValueError("O valor do modelo deve ser diferente de nulo")

    @ano.setter
    def ano(self, ano: int) -> None:
        if ano >= 1920:
            self._ano = ano
        else:
            raise ValueError("O valor do ano deve ser maior ou igual a 1920") 
          
    def __str__(self):
        return "Marca: {}, Modelo: {}, Ano: {}".format(self._marca.value, self._modelo, self._ano)
    

class Carro(Veiculo):
    def __init__(self, marca: Marca, modelo: str, ano: int, numero_de_portas: int) -> None:
        super().__init__(marca, modelo, ano)
        self._numero_de_portas = numero_de_portas

    @property
    def numero_de_portas(self) -> int:
        return self._numero_de_portas
    
    @numero_de_portas.setter
    def numero_de_portas(self, numero_de_portas: int) -> None:
        if numero_de_portas > 0:
            self._numero_de_portas = numero_de_portas
        else:
            raise ValueError("Número de portas deve ser maior que zero.")
    
    def __str__(self) -> str:
        return super().__str__() + " | Número de Portas: {}".format(self._numero_de_portas)
    
class Moto(Veiculo):
    def __init__(self, marca: Marca, modelo: str, ano: int, tipo: Tipo) -> None:
        super().__init__(marca, modelo, ano)
        self._tipo = tipo

    @property
    def tipo(self) -> Tipo:
        return self._tipo
    
    @tipo.setter
    def tipo(self, tipo: Tipo) -> None:
        if isinstance(tipo, Tipo):
            self._tipo = tipo
        else:
            raise ValueError("Tipo deve ser uma instância da classe Tipo")
        
    def __str__(self) -> str:
        return super().__str__() + " | Tipo: {}".format(self._tipo.value)

# Testando as classes
carro = Carro(Marca.FORD, "Fiesta", 2020, 4)
moto = Moto(Marca.CHEVROLET, "Sport", 2021, Tipo.ESPORTIVA)

print(carro)  # Saída: Marca: FORD, Modelo: Fiesta, Ano: 2020 | Número de Portas: 4
print(moto)   # Saída: Marca: CHEVROLET, Modelo: Sport, Ano: 2021 | Tipo: ESPORTIVA


    