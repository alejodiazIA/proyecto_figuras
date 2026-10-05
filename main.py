from lib import cuadrado, triangulo, rectangulo, circunferencia
print("Proyecto Figuras")

#cuadrado
print(cuadrado.get_identificador())
lado=4
print(f"El area de un cuadrado de lado {lado} es: {cuadrado.area(lado)} y el perimetro es: {cuadrado.perimetro(lado)}")

base=4
altura=2

#triangulo
print(triangulo.get_identificador())
print(f"El area de un {triangulo.get_identificador()} de base {base} y altura {altura} es: {triangulo.get_area(base, altura)} y el perimetro es: {triangulo.get_perimetro(base, base, base)}")

#rectangulo
print(rectangulo.get_identificador())
print(f"El area de un {rectangulo.get_identificador()} de base {base} y altura {altura} es: {rectangulo.get_area(base, altura)} y el perimetro es: {rectangulo.get_perimetro(base, altura)}")

#circunferencia
radio = 3
print(f"El area de una circunferencia de radio {radio} es: {circunferencia.get_area(radio)}")