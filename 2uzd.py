"""
Aprēķināt noteiktas skaitļu summu no 1 līdz n, kur n ir lietotāja ievadīts skaitlis.
"""
x = int(input("number: "))

sum = 0

for i in range(1, x+1):
    sum += i
print('sum =', sum)