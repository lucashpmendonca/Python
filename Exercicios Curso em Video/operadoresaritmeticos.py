import math

n1 = int(input('Digite um valor : '))
n2 = int(input('Digite outro valor : '))
# operadores padrao
s = n1 + n2
print('A soma é : ' , s)
s = n1 - n2
print('A substração é : ' , s)
s = n1 * n2
print('A multiplicação é : ' , s)
s = n1 / n2
print('A divisao é : ' , s)
s = n1 // n2
print('A parte intera da divisao é : ' , s)
s = n1 % n2
print('A o resto da divisao inteira é : ' , s)
s = n1 ** n2
print('A exponenciação é : ' , s)

#teste modulo math
print('teste modulo math')
n = int(input('Digite um valor : '))
r = math.factorial(n)
print(r)
r = math.log10(n)
print(r)
r = math.radians(n)
print(r)


