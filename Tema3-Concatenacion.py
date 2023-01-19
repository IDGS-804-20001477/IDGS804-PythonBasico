dato1 = "Hola"
dato2 = "Mundo"
saludo = dato1 + " " + dato2

print(saludo)

print("El saludo es: %s %s" % (dato1, dato2))

SaludoFinal = "Saludo {1} {0}".format(dato1, dato2)
print(SaludoFinal)

SaludoFinal = "Saludo {a} {b}".format(a = dato1, b = dato2)
print(SaludoFinal)