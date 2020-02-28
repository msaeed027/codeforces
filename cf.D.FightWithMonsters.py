def calc_skip_val(a, b, h_i):
    r = h_i % (a + b)
    if 1 <= r <= a:
        return 0
    else:
        if r == 0:
            r = b
        else:
            r -= a
    return int(r / a) + (0 if r % a == 0 else 1)


def create_skip_table(a, b, h):
    return list(
        map(
            lambda h_i: calc_skip_val(a, b, h_i),
            h
        )
    )


def max_points_num(a, b, k, h):
    skip_table = create_skip_table(a, b, h)
    skip_table.sort()

    p = 0
    for s_i in skip_table:
        if s_i <= k:
            k -= s_i
            p += 1
        else:
            break

    return p


(n, a, b, k) = list(map(int, input().split()))
h = list(map(int, input().split()))

print(max_points_num(a, b, k, h))
