def triangle_area(a,b,c):
    """Find area of triange. If a,b,c not triangles sides returns False"""
    if a + b > c and a + c > b and c + b > a:
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 1./2.
        return s
    return False
print(triangle_area(28.5,37.7,47))

a = 143
b = 43
d = divmod(a,b)
d1 = (a // b, a % b)
print(d, d1)

def caesar_cipher(string):
    a = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    b = a[::-1]
    k = 0
    c = {}
    for elem in a:
        c[elem] = b[k]
        k = k + 1
    return "".join([c[letter] for letter in list(string.lower()) if letter in a])

def not_caesar_cipher(string):
    b = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    a = b[::-1]
    k = 0
    c = {}
    for elem in a:
        c[elem] = b[k]
        k = k + 1
    return "".join([c[letter] for letter in list(string.lower()) if letter in a])

print(caesar_cipher("поцэъм"))

def array_add(array, *args):
    global a
    a = list(args)
    return array + a
print(array_add([11,2,3,4,5,7], 11,12,13, None))

def args_sum(*args):
    return sum(list(args))
