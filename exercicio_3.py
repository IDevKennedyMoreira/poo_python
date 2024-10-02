"""Crie uma classe Pessoa que tenha os atributos nome, idade, e sexo. 
Adicione um método que exiba uma saudação personalizada,
 como "Olá, meu nome é [nome] e tenho [idade] anos."""

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def idade(self) -> int:
        return self._idade
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome
    
    @idade.setter
    def idade(self, idade: int) -> None:
        if idade >= 0:
            self._idade = idade
        else:
            raise ValueError("Valor negativo de idade não é permitido.")

    def saudacao(self) -> str:
        return f"Olá, meu nome é {self._nome} e tenho {self._idade} anos."
