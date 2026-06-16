def main():
    time = input("What time is it? ")

    time = convert(time)

    if 7 <= time <= 8:
        print("Breakfast time!")

    elif 12 <= time <= 13:
        print("Lunch time!")

    elif 18 <= time <= 19:
        print("Lunch time!")

    

def convert(time):
    h, m = time.split(":")

    h = int(h)
    m = int(m)
    
    timeCon = h + (((m*100)/60)/100)

    return timeCon


if __name__ == "__main__":
    main()
