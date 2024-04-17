def get_elements():
    n = int(input("Enter number of elements(n): "))
    return n

def num(a):
    elements = []
    z = 1
    while z <= a:
        n = int(input("Enter number {}: ".format(z)))
        elements.append(n)
        z += 1
    return elements

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x * y) // gcd(x, y)

def lcm_of_list(numbers):
    lcm_value = numbers[0]
    for i in range(1, len(numbers)):
        lcm_value = lcm(lcm_value, numbers[i])
    return lcm_value

def main():
    number = get_elements()
    numbers_list = num(number)
    result = lcm_of_list(numbers_list)
    print("LCM of the given numbers:", result)

main()
