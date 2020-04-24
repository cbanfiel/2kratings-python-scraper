def scaleBetween(unscaledNum, minAllowed, maxAllowed, min, max):
    return (
        ((maxAllowed - minAllowed) * (unscaledNum - min)) / (max - min) + minAllowed
    )



def main():
    print(scaleBetween(57,50,99,30,94))
    print(scaleBetween(57,50,99,42,96))


main()