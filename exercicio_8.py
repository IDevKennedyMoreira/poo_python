"""Crie uma classe chamada Email que tenha um método de classe para validar se um endereço de e-mail é válido."""
import re 

class Email:

    _email: str
    _patern: str = "r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'"

    @classmethod
    def email(cls, email) -> None:
        if re.match(cls._patern, cls._email) is not None:
            cls._email = email
        else:
            raise ValueError("Valor de Email nao obedece ao padrao")
