def fibonacci(n):

    sequence = []

    a = 0
    b = 1

    for i in range(n):
        sequence.append(a)

        a, b = b, a + b

    return sequence


terms = int(input("Enter number of terms: "))

print("Fibonacci sequence:")
print(fibonacci(terms))
