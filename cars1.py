def triangle_area(a,b,c):
    """Find area of triange. If a,b,c not triangles sides returns False"""
    if a + b > c and a + c > b and c + b > a:
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 1./2.
        return s
    return False
print(triangle_area(28.5,37.7,47))

print("Механика машин")