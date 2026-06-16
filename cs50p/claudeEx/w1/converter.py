def main():

    choice = input("What do you want to convert?\n   1. km -> mi\n   2. C -> F\n   3. kg -> lbs\nInsert your choice: ")
    
    match int(choice):
        case 1:
            km_mi(int(input("Km: ")))
        case 2:
            ce_fa(int(input("C: ")))
        case 3:
            kg_li(int(input("Kg: ")))
            
        case _:
            print("Choice not valid!")
    
def km_mi(km):    
    mi = km/1.609
    print(F"Mi: {mi}")

def ce_fa(ce):
    fa = (ce * (9/5)) + 32
    print(f"F: {fa}")
    
def kg_li(kg):
    li = kg * 2.205
    print(f"lbs: {li}")


main()
