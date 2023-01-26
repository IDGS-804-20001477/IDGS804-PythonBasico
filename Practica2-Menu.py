import os
class Operasbas():

    num1 = 0
    num2 = 0

    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def suma(self, num1, num2):
        self.res = num1 + num2
        print('El resultado es: {}'.format(self.res))
    def resta(self, num1, num2):
        self.res = num1 - num2
        print('El resultado es: {}'.format(self.res))
    def multiplicacion(self, num1, num2):
        self.res = num1 * num2
        print('El resultado es: {}'.format(self.res))
    def division(self, num1, num2):
        self.res = num1 / num2
        print('El resultado es: {}'.format(self.res))

def main():
    obj = Operasbas()
    default = True
    while (default):
        opcion = int(input('\n1- Suma \n2- Resta \n3- Multiplicación \n4- División \n5- Salir \n Ingresa la operación que necesitas: '))
        match opcion:
            case (1):
                num1 = int(input('Ingresa un numero: '))
                num2 = int(input('Ingresa un numero: '))
                obj.suma(num1, num2)
            case (2):
                num1 = int(input('Ingresa un numero: '))
                num2 = int(input('Ingresa un numero: '))
                obj.resta(num1, num2)
            case (3):
                num1 = int(input('Ingresa un numero: '))
                num2 = int(input('Ingresa un numero: '))
                obj.multiplicacion(num1, num2)
            case (4):
                num1 = int(input('Ingresa un numero: '))
                num2 = int(input('Ingresa un numero: '))
                obj.division(num1, num2)
            case (5):
                os.system('cls')
                default = False
        
if __name__ == '__main__':
    main()