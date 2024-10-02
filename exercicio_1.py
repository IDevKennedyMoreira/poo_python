"""
Crie uma classe Retangulo com os atributos largura e altura. 
Inclua um método que calcule a área do retângulo e outro método
 que calcule o perímetro.
"""
class Retangulo:
    def __init__(self, largura: float, altura:float) -> None:
        self._largura = largura
        self._altura = altura

    def calc_perimetro(self) -> float:
        return 2*(self._largura + self._altura)
    
    def calc_area(self) -> float:
        return self._largura * self._altura
    
    @property
    def altura(self) -> float:
        return self._altura
    
    @property
    def largura(self) -> float:
        return self._largura
    
    @altura.setter
    def altura(self, altura: float) -> None:
        if altura > 0:
            self._altura = altura
        else:
            raise ValueError("O valor de altura nao pode ser negativo")
        
    @largura.setter
    def largura(self, largura: float) -> float:
        if largura > 0:
            self._largura = largura
        else:
            raise ValueError("O valor de largura nao poder ser negativo")
