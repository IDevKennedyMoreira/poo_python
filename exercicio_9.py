"""
Aqui estão três exercícios de nível intermediário de Orientação a Objetos (OO) com Python, projetados para você praticar conceitos como herança, polimorfismo, encapsulamento e interação entre classes.

1. Sistema de Biblioteca
Implemente um sistema simples para gerenciar uma biblioteca, onde é possível adicionar livros, emprestá-los e devolvê-los.

Requisitos:
Crie uma classe Livro com os atributos: título, autor e disponibilidade (se está disponível ou emprestado).
Crie uma classe Biblioteca que mantém uma lista de livros e possui os métodos:
adicionar_livro(livro): para adicionar um livro à biblioteca.
emprestar_livro(titulo): para emprestar um livro, alterando sua disponibilidade.
devolver_livro(titulo): para devolver um livro, tornando-o disponível novamente.
listar_livros_disponiveis(): que lista apenas os livros disponíveis para empréstimo."""

class Livro:
    def __init__(self, titulo:str, autor: str, disponibilidade: bool = True) -> None:
        self._titulo = titulo
        self._autor = autor
        self._disponibilidade = disponibilidade

    @property
    def titulo(self) -> str:
        return self._titulo
    
    @property
    def autor(self) -> str:
        return self._autor
    
    @property
    def disponibilidade(self) -> bool:
        return self._disponibilidade
    
    @titulo.setter
    def titulo(self, titulo: str) -> None:
        if isinstance(titulo, str) and len(titulo) > 0:
            self._titulo = titulo
        else:
            raise ValueError("O nome do titulo deve ser um string nao vazia.")

    @autor.setter
    def autor(self, autor: str) -> None:
        if isinstance(autor, str) and len(autor) > 0:
            self._autor = autor
        else:
            raise ValueError("O nome do autor deve ser uma string nao vazia.")

    @disponibilidade.setter
    def disponibilidade(self, disponibilidade:bool) -> None:
        if isinstance(disponibilidade, bool):
            self._disponibilidade = disponibilidade
        else:
            raise ValueError("Disponibilidade deve ser um valor booleano.")
    
    def __str__(self) -> str:
        status = 'Disponível' if self._disponibilidade else 'Emprestado'
        return """Livro: {}
Autor: {}
Status: {}""".format(self._titulo, self._autor, status)

class Biblioteca:

    def __init__(self) -> None:
        self._livros: list[Livro] = []    

    def adicionar_livro(self, livro: Livro):
        self._livros.append(livro)

    def emprestar_livro(self, titulo: str):
        titulo = titulo.title()
