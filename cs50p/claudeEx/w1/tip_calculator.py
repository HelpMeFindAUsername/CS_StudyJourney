print("**TIP CALCULATOR**\n\n")

subtotal = float(input("Insert the subtotal of the bill: "))

tip_percent = int(input("Insert tip %: "))

def calc(tot:float, perc:int):

    tip:float = (tot*perc)/100

    return tip

def printBill():
    tip = calc(subtotal, tip_percent)
    total = subtotal + tip
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Tip ({tip_percent}): {tip:.2f}")
    print(f"Total: {total:.2f}")

printBill()
