""" Crear una clase calculadora, con las siguientes características

-Dos atributos donde se guardaran los números, con los que se va a operar
-tendrá los siguientes métodos: Sumar,restar: devuelve la resta del mayor y el menor,
multiplicar, dividir: mayor entre menor """
class Calculadora:
    def __init__(self,op1,op2):
        self.operando_1=op1
        self.operando_2=op2
    def sumar(self):
        print("Sumando")
        return self.operando_1+self.operando_2
    def restar(self):
        print("Restando")
        return max(self.operando_1,self.operando_2)-min(self.operando_1,self.operando_2)
    def multiplicar(self):
        print("Multiplicando")
        return self.operando_1*self.operando_2
    def dividir(self):
        print("Dividiendo")
        return max(self.operando_1,self.operando_2)/min(self.operando_1,self.operando_2)