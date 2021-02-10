house = float(1000000.00)
good: float = float(.1)
bad = float(.2)
good_credit = True

if good_credit:
    print((house * good), "is required for down payment.")
else:
    print((house * bad), ' is required for down payment.')

