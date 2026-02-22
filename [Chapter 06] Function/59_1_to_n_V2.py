def count_n(n, current = 1):
    print(current)

    if current < n:
        count_n(n, current + 1)

count_n(int(input()))