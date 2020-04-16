def faktoriyel(numara):
    carpim = 1
    while numara:
        carpim *= numara
        numara -= 1
    return carpim
