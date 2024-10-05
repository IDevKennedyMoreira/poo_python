"""

Você deve criar um sistema simples que permite cadastrar alunos em uma escola. O sistema deve ser capaz de armazenar informações como nome do aluno, idade e nota. Ele também deve permitir visualizar os alunos cadastrados e calcular a média das notas.

Requisitos:
Crie uma classe Aluno que tenha os seguintes atributos:

nome: o nome do aluno.
idade: a idade do aluno.
nota: a nota do aluno (um número entre 0 e 100).
A classe Aluno deve ter:

Um método __str__() que retorna as informações do aluno em uma string legível.
Um método que verifica se o aluno passou ou não. Um aluno passa se sua nota for maior ou igual a 60.
Crie uma classe Escola que tenha:

Um atributo alunos que armazena uma lista de objetos do tipo Aluno.
Um método adicionar_aluno() que permite adicionar um novo aluno à lista.
Um método listar_alunos() que imprime os dados de todos os alunos cadastrados.
Um método calcular_media() que retorna a média das notas dos alunos cadastrados.
Exemplo de Interação:
O sistema deve permitir adicionar alunos, listar alunos e calcular a média das notas.


"""

class Aluno:
    def __init__(self, nome: str, idade: int, nota: int) -> None:
        self._nome = nome
        self._idade = idade
        self._nota = nota
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def idade(self) -> int:
        return self._idade
    
    @property
    def nota(self) -> int:
        return self._nota
    
    @nome.setter
    def nome(self, nome: str) -> None:
        if len(nome) and isinstance(nome, str):
            self._nome = nome
        else:
            raise ValueError("O nome nao pode ser vazio.")
    
    @idade.setter
    def idade(self, idade: int) -> None:
        if idade > 0:
            self._idade = idade
        else:
            raise ValueError("O valor de idade nao pode ser negativo.")
        
    @nota.setter
    def nota(self, nota: int) -> None:
        if nota >= 0 and nota <= 100:
            self._nota = nota
        else:
            raise ValueError("O valor de nota deve ser um inteiro entre 0 e 100.")
        
    def __str__(self):
        return "Nome: {}, Idade:{}, Nota:{}".format(self._nome, self._idade, self.nota)

class Escola:
    def __init__(self) -> None:
        self._alunos: list[Aluno] = []

    @property
    def alunos(self) -> list[Aluno]:
        return self._alunos
    
    def adicionar_aluno(self, aluno: Aluno) -> None:
        self.alunos.append(aluno)

    def listar_alunos(self) -> None:
        for a in self._alunos:
            print(a.nome)

    def calcular_media(self) -> float:
        cont_alunos = len(self._alunos)
        if cont_alunos == 0:
            return 0.0
        total = 0
        for a in self._alunos:
            total += a.nota
        return total/len(self._alunos) 
