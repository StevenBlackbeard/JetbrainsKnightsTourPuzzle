def rec_sum(n):
    if n == 1:
        return n

    return n + rec_sum(n - 1)