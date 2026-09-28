from lib import cuadrado, triangulo
print("Proyecto Figuras")
print(cuadrado.get_identificador())
lado=4
print(f"El area de un cuadrado de lado {lado} es: {cuadrado.area(lado)} y el perimetro es: {cuadrado.perimetro(lado)}")

base=4
altura=2
print(triangulo.get_identificador())
print(f"El area de un {triangulo.get_identificador()} de base {base} y altura {altura} es: {triangulo.get_area(base, altura)} y el perimetro es: {triangulo.get_perimetro(base, base, base)}")