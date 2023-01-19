mul = int(input('Ingresa el numero de tabla que quieres: '))

def tabla(mul):
    for x in range (1, 11):
        res = mul * x
        print('{} x {} = {}'.format(mul, x, res))

tabla(mul)