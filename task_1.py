# a, b, c = map(int, input().split(','))
# print(a * b * c)

a, b, c = [int(i) for i in input("Пожалуйста, введите 3 цифры: ").split(',')]
d = a * b * c
print(d)
