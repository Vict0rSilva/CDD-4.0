a = [0] * 10
m = [0] * 10
for i in range(10):
    a[i] = int(input(f"Digite {i+1}° valor: "))

x = int(input("Digite um valor para multiplicar: "))

for y in range(10):
    m[y] = a[y]*x

print(m)