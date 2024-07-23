first_num = 0
second_num = 1

print(first_num)
print(second_num)

for _ in range(20):
    next_num = first_num + second_num

    print(next_num)

    second_num = first_num
    first_num = next_num




count = 2

def fibonacci(first_num, second_num):

    global count

    if count <= 19:
        next_num = first_num + second_num

        print(next_num)

        second_num = first_num
        first_num = next_num

        count += 1

        fibonacci(first_num, second_num)
    else:
        return

fibonacci(1, 0)


# find the nth value in a fibonacii using the iterative method

def f(n):

    if n <= 1:
        return n
    
    first_num, second_num = 0, 1

    for _ in range(2, n + 1):

        first_num, second_num = second_num, first_num + second_num

    return second_num
    
print(f(7))



def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(20):
    print(fibonacci(i))



def fibonacci(n, first_num=0, second_num=1):
    if n == 0:
        return first_num
    elif n == 1:
        return second_num
    else:
        return fibonacci(n - 1, second_num, first_num + second_num)

print(fibonacci(19))


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(19))