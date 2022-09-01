def arb_args(*args):
    for arg in args:
        print(arg)

def inner_func(a, b):
    def mult(x, y):
        return x * y
    
    def sub(x, y):
        return x - y
    
    print(mult(a, b) + sub(a, b))

def lunch_lady(string1, string2 = 'Mystery Meat'):
    print(f"{string1} wants {string2}")

def sum_n_product(a, b):
    return a + b, a * b

alias_arb_args = arb_args

def arb_mean(*numbers):
    sum = 0

    for number in numbers:
        sum += number
    
    return sum / len(numbers)

def arb_longest_string(*strings):
    letters = 0
    longest = ''

    for string in strings:
        if len(string) > letters:
            letters = len(string)
            longest = string
    
    return longest

def arb_longest_string2(*strings):
    return max(strings)

arb_args('Hello', 23, True)
inner_func(1, 2)
lunch_lady('Casemiro', 'pasta')
lunch_lady('Casemiro')
print(sum_n_product(2, 3))
print(arb_mean(2, 5, 8, 11))
print(arb_longest_string('Hello', 'Hi', 'continiuos'))
print(arb_longest_string2('Hello', 'Hi', 'continiuos'))