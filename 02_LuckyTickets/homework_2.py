def get_sum_nums(n):
    return sum(list(map(int, str(n))))

def get_last(n):
    return int(str(n)[-1])

def lucky(n):
    count = 0
    cols = 9 * n + 1
    table = [[0] * cols for i in range(10)]
    
    for i in range(10):
        # сколько чисел заканичвающихся на i сумма, которых дает k-ый элемент
        for j in range(10 ** n):
            if get_last(j) == i:
                table[i][get_sum_nums(j)] += 1

    for i in range(cols):
        in_count = 0
        for j in range(10):
            in_count += table[j][i]
        count += in_count ** 2
    
    return count

print(lucky(3))