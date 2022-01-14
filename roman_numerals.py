s = "MCMXCIV"
#    10, 1, 5

#i x
#0 10
#1 1
#2 5

ROMAN_NUMBERS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def roman_to_int(s):

    nombre = 0

    translations = [ROMAN_NUMBERS[c] for c in s]
    for i in range(len(translations)-1):
        if translations[i] >= translations[i+1]:
            nombre += translations[i]
        else:
            nombre -= translations[i]
    nombre += translations[-1]
    return nombre

print(roman_to_int(s))