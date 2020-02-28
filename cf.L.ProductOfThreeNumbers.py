cases_count = int(input())

for i in range(0, cases_count):
    n = case = int(input())

    exists = set()
    i = 1
    while i * i < n:
        i += 1
        if len(exists) == 2:
            break
        if n % i == 0 and i not in exists:
            n /= i
            exists.add(i)
            i = 1  # reset i

    if len(exists) == 2 and n not in exists:
        exists.add(n)
        print("YES")
        print(" ".join(map(lambda i: str(int(i)), exists)))
    else:
        print("NO")