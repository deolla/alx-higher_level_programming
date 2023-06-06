for m in range(10):
    for n in range(m + 1, 10):
        print("{:d}{:d}".format(m, n), end="")
        if m != 8 or n != 9:
            print(", ", end="")
        else:
            print()
