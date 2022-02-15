def startswith_capital_counter(names):
    return sum(name.istitle() for name in names)
    # count = 0
    # for name in names:
    #     if name[0].isupper():
    #         count += 1
    # return count
