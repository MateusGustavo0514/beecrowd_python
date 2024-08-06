pi = 3.14159
A = float(input())
B = float(input())
C = float(input())

triangle = ((A*C)/2)
circle = ((C**2)*pi)
trapeze = (((A+B)*C)/2)
quadrate = (B**2)
rectangle = (A*B)

print(f"TRIANGULO: {triangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapeze:.3f}")
print(f"QUADRADO: {quadrate:.3f}")
print(f"RETANGULO: {rectangle:.3f}")