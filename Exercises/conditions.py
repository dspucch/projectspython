good_credit = True
house = 1000000
good: float = float(.1)
bad = float(.2)


if good_credit:
    print((house * good) +  "is required for down payment.")
else:
    print((house * bad) + ' is required for down payment.')

