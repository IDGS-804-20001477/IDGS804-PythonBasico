import os
class Operasbas():
    
    #Propiedades de clase
    num1 = 0
    num2 = 0
    num3 = 0
    #Constructor de la clase
    #El "self" solo va cuando es dentro de la clase
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def suma(self):
        self.res = self.num1 + self.num2
    def resta(self):
        self.res = self.num1 - self.num2

def main():
    os.system('cls')
    obj = Operasbas(3, 4)
    obj.suma()
    print("La suma es: {}".format(obj.res))

if __name__ == '__main__':
    main()
    #Metodos de la clase
