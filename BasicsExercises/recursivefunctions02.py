def fibonacci(n, diepte=0):
    indent = "  " * diepte
    print(f"{indent}fibonacci({n})")

    if n <= 1:
        resultaat = n
    else:
        resultaat = (
            fibonacci(n - 1, diepte + 1)
            + fibonacci(n - 2, diepte + 1)
        )

    print(f"{indent}retourneert {resultaat}")
    return resultaat


fibonacci(4)