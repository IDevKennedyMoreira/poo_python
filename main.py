"""
1. Classes e Objetos

Classe: Um modelo para criar objetos. Em Python, classes sao definidas usando a palavra-chave
class.

Objeto: Uma instancia de uma classe, que contem atributos e metodos definidos na classe
"""

class Pessoa:
     def __init__(self, nome, idade):
          self.nome = nome
          self.idade = idade

pessoa1 = Pessoa("Joao", 30)

"""
2. Atributos

Atributos de Instancia: Sao variaveis que pertencem a cada objeto (instancia) da classe

Atributos de Classe: Sao variaveis que pertencem a propria classe e sao compartilhados por todas as
instancias
"""

class Carro:
     rodas = 4 #Atributo de classe

     def __init__(self,cor):
          self.cor = cor #Atributo de instancia

"""
3. Metodos

Metodos de Instancia: Funcoes definidas dentro de uma classe que atuam sobre os atributos de
intancia

Metodo de Classe: Funcoes que atuam sobre os atributos de classe e utilizam o decorados @classmethod

Metodo Estaticos:Funcoes dentroi de uma classe que nao interagem com a isntancia nem com a classe
em si utilizando o decorador @staticmethod
"""

class Animal:
     @staticmethod
     def som():
          return "Algum som"
     
     @classmethod
     def especie(cls):
          return "Indefinido"
     
"""
4. Encapsulamento

Controle sobre o acesso aos dados. Em Python, utiliza-se convencoes para limitar o acesso a atributos
(ex.: usar um _ ou __ antes do nome da variavel para denotar atributos protegidos ou privados)
"""

class ContaBancaria:
     def __init__(self, saldo):
          self.__saldo = saldo # Atributo privado

"""
5. Heranca

Permite que uma classe herde atributos e metodos de outra. A classe que herda e chamada de de subclasse,
e a classe da qual ela herda e a superclasse.
"""

class Veiculo:
     def __init__(self, marca):
          self.marca = marca

class Carro(Veiculo):
     def __init__(self, marca, modelo):
          super().__init__(marca)
          self.modelo = modelo

"""
6. Polimorfismo

A capacidade de diferentes classes de implementarem metodos com o mesmo nome, mas comportamentos diferentes
"""

class Forma:
     def area(self):
          pass
     
class Retangulo(Forma):
     def area(self):
          return "Calculando a area do retangulo"
     
class Circulo(Forma):
     def area(self):
          return "Calculando a area do circulo"

"""
7. Abstracao

Focar nas funcionalidades essenciais de uum objeto sem revelar detalhes complexos. Em Python isso pode ser
implementado atraves dde classes abstratas usando o modulo abc
"""

from abc import ABC, abstractmethod

class Animal(ABC):
     @abstractmethod
     def som(self):
          pass
     
"""
8. Composicao
Relacionamento "tem um" entre classes. Em vez de herdar de uma classe, uma classe pode conter outra como
parte de sua estrutura
"""

class Motor:
     pass

class Carro:
     def __init__(self):
          self.motor = Motor() # Composicao

"""
9. Propriedades

As propriedades sao usadas pada encapsular o acesso a atributos privadois, permitindo controle sobre como esses
atributos sao acessados oui modificados.No Python isso e feito usando os decoradores @property e @<atributo>.setter.
"""

class Produto:
    def __init__(self, preco):
        self._preco = preco #Atributo privado
    
    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor > 0:
            self._preco = valor
        else:
             raise ValueError("O preco deve ser positivo")

p = Produto(100)
print(p.preco)
p.preco = 150

"""
10. Metodos Magicos (Dunder Methods)
Python oferece uma serie de metodos especiais, conhecidos como metodos magicos ou dunder methods
(double score), que permitem sobrecarregar operacoes para classes personalizadas. Eles geralmente comecam
e terminam, com 2 underscoores (__). Alfuns dos mais comuns sao:

__init__(self): Construtor da classe, inicializa objeto.
__str__(self): Define o comportamento da funcao str() e print()
__repr__(self): Define a respresentacao oficial da ionstancia, usada principalmente para depuracao
__eq__(self, other): Permite comparar dois objetos com ==
__lt__(self,other): Permite comparar dois objetos com <
__add__(self,other): Permite somat dois objetos com +
__len__(self): Define o comportamento da funcao len()
"""

class Retangulo:
    def __init__(self, largura, altura):
        self.argura = largura
        self.altura = altura
    
    def __str__(self):
        return f'Retangulo({self.largura}, {self.altura})'
    
    def __add__(self,outro):
         return Retangulo(self.largura + outro.largura, self.altura + outro.altura)

r1 = Retangulo(5, 10)
r2 = Retangulo(3,6)
r3 = r1 + r2
print(r3)

"""
11. Heranca Multipla

Python suporta heranca multipla, o que significa que uma classe pode herdar de varias classes ao mesmo tempo.
Isso permite combinar comprtamentos de difererntes superclasses, mas pode introduzir complexidade no design,
especialmente ao lidar com o problema do diamante de heranca
"""

class A:
     def falar(self):
          return "A esta falando"
     
class B:
     def falar(self):
          return "B esta falando"

class C(A,B):
     pass

c = C()

print(c.falar()) # A esta falando (a ordem de heranca importa)

"""
A resolucao de ordem de metodos (MRO) determina a prioridade das classes na heranca multipla. Em Python
pode ser visualizada usando o metodo C.mro()
"""

"""
12. Classes Abstratas e Interfaces

Embora Python nao tenha interfaces como em outras linguagens, usa-se classes abstratas para definir metodos que as
subclasses devem implementar. Isso fornece uma maneira de garantir que certas funcionalidades estejam presentes
na subclasse
"""

from abc import ABC, abstractmethod

class Forma(ABC):
     @abstractmethod
     def area(self):
          pass
class Quadrado(Forma):
    def __int__(self,lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2
q = Quadrado(5)
print(q.area()) #25
    