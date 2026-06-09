def f(n):

    if n == 0:
        return

    print("Before", n)

    f(n - 1)

    print("After", n)

f(3)