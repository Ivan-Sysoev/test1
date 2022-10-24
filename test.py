def args_sum(*args):
    a = list(args)
    try: 
        return sum(a)
    except:
        return "Все аргументы должны являться числами"
print(args_sum(1,2,3,4,5.3, None))

def if_palindrom(string):
    if isinstance(string, str):
        if string == string[::-1]:
            return True
        return False
    return "Аргумент должен быть строкой"
print(if_palindrom("1234321"))