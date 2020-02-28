def custom_sum(lst):
    lst_sum = 0
    contains_odd = False
    contains_even = False
    for num in lst:
        lst_sum += num
        if num % 2 == 0:
            contains_even = True
        else:
            contains_odd = True
    return lst_sum, contains_odd, contains_even


cases_count = int(input())

for i in range(0, cases_count):
    case_count = int(input())
    case = list(map(int, input().split()))

    case_sum = custom_sum(case)
    if case_sum[0] % 2 == 0:
        if case_sum[1] and case_sum[2]:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")


