A = int(input())
B = int(input())
C = int(input())

MaiorAB = (A + B + abs(A - B))/2
Maior_Total = (MaiorAB + C + abs(MaiorAB - C))/2

print(f"{Maior_Total} eh o maior")