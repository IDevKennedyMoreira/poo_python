"""Crie uma classe chamada Temperatura que tenha métodos estáticos
 para converter Celsius em Fahrenheit e vice-versa."""

class Tempereratura:

    @staticmethod
    def celsius_para_farenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_para_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9