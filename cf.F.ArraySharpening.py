def possible_sharpened_array(case_count, case):
    last_increasing_index, first_decreasing_index = -1, case_count
    for i in range(0, case_count):
        if case[i] < i:
            break
        last_increasing_index = i
    for i in range(case_count - 1, -1, -1):
        if case[i] < case_count - 1 - i:
            break
        first_decreasing_index = i
    print('=> ', case, last_increasing_index, first_decreasing_index)
    return 'YES' if first_decreasing_index <= last_increasing_index else 'NO'


cases_count = int(input())

for i in range(0, cases_count):
    case_count = int(input())
    case = list(map(int, input().split()))
    print(possible_sharpened_array(case_count, case))