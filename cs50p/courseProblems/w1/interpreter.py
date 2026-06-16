x, y, z = input("Expression: ").split(" ")

x = float(x)
z = float(z)

match y:
    case "+":
        result = x+z

    case "-":
        result = x-z

    case "*":
        result = x*z

    case "/":
        result = x/z

print(result)
