"""
Izvadīt visus pirmsskaitļus no 1 līdz 100, izmantojot for un if.

"""
for n in range(1,101):
    nam = True
    if n == 1:
        nam = False
    else:
        for i in range(2,n):
            if n % i == 0:
                nam = False

        if nam:
            print(n)