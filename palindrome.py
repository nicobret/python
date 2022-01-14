x = -121
#   012345

def palindrome(x):
    x = str(x)
    for i in range(len(x) // 2):
        if x[i] != x[-i-1]:
            return False
    return True

print(palindrome(x))

def palindrome2(x):
    x = str(x)
    return x == x[::-1]

print(palindrome2(x))