# a, b, c = map(int, input().split(','))
# print(a * b * c)

a, b, c = [int(x) for x in input("Пожалуйста, введите цифры: ").split(',')]
d = a * b * c
print(d)
