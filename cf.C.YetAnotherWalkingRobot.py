# example:  L   L   R   U   D
# x: 0     -1  -2  -1  -1  -1
# y: 0      0   0   0   1   0


def char_resolution(char):
    if char == 'L':
        return -1, 0
    elif char == 'R':
        return 1, 0
    elif char == 'U':
        return 0, 1
    else:  # D
        return 0, -1


cases_count = int(input())

for i in range(0, cases_count):
    case_count = int(input())
    case = str(input())

    x = 0
    y = 0
    answer_store = {(0,0): 0}

    p_start = -1
    p_end = -1

    for char_index in range(0, case_count):
        delta_x, delta_y = char_resolution(case[char_index])
        x += delta_x
        y += delta_y

        if (x, y) in answer_store and (p_start == -1 or char_index - answer_store[(x, y)] < p_end - p_start):
            p_start = answer_store[(x, y)] + 1
            p_end = char_index + 1

        answer_store[(x, y)] = char_index + 1

    print('-1' if p_start == -1 else f'{p_start} {p_end}')