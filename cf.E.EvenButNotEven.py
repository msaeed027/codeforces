def ebne(case_count, case):
    odd_indices = list(
        filter(
            lambda i: int(case[i]) % 2 != 0,
            range(0, case_count)
        )
    )
    odd_indices_len = len(odd_indices)
    return '-1' if odd_indices_len < 2 else case[odd_indices[odd_indices_len - 2]:odd_indices[odd_indices_len - 1] + 1]


cases_count = int(input())

for i in range(0, cases_count):
    case_count = int(input())
    case = str(input())
    print(ebne(case_count, case))