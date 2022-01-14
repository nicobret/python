digits = [1,2,9]
#         0 1 2

def plusOne(digits):
    digits.reverse()

    digits[0] += 1

    for i in range(len(digits)):
        if digits[i] == 10:
            digits[i] = 0
            if i+1<len(digits):
                digits[i+1] += 1
            else:
                digits += [1]
        else:
            break

    digits.reverse()
    return digits

def plusOne2(digits):
    digits.reverse()
    myinteger = 1
    for i, d in enumerate(digits):
        myinteger += d*10**i
    resultat = []
    while myinteger > 0:
        resultat = [myinteger%10] + resultat
        myinteger = myinteger//10
    return resultat

def plusOne3(digits):
    myinteger = 1 + sum([d*10**i for i, d in enumerate(reversed(digits))])
    resultat = []
    while myinteger > 0:
        resultat = [myinteger%10] + resultat
        myinteger = myinteger//10
    return resultat

print(plusOne3(digits))