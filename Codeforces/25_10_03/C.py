# 2152C
# Triple Removal

test_cases: int = int(input())
for _ in range(test_cases):
    _, queries = list(map(int, input().split()))
    array = list(map(int, input().split()))
    # Sums from left and from right, to fetch subarray totals without parsing twice
    zero_sum_l, zero_sum_r = [], []
    one_sum_l, one_sum_r = [], []
    # Closest index where two same numbers are adyacent, to calculate extra costs
    closest_ady_num_l, closest_ady_num_r = [], []

    cur_zeroes, cur_ones, cur_closest_ady = 0, 0, -1
    for i, val in enumerate(array):
        zero_sum_l.append(cur_zeroes)
        one_sum_l.append(cur_ones)
        if val:
            cur_ones += 1
        else:
            cur_zeroes += 1
        if i > 0 and array[i-1] == array[i]:
            cur_closest_ady = i
        closest_ady_num_l.append(cur_closest_ady)

    cur_zeroes, cur_ones, cur_closest_ady = 0, 0, -1
    for i in reversed(range(len(array))):
        zero_sum_r.append(cur_zeroes)
        one_sum_r.append(cur_ones)
        if array[i]:
            cur_ones += 1
        else:
            cur_zeroes += 1
        if i < len(array)-1 and array[i+1] == array[i]:
            cur_closest_ady = i
        closest_ady_num_r.append(cur_closest_ady)
    zero_sum_r.reverse()
    one_sum_r.reverse()
    closest_ady_num_r.reverse()

    # Total number of 0's and 1's
    zeroes, ones = cur_zeroes, cur_ones

    for _ in range(queries):
        i, j = list(map(int, input().split()))
        subarr_zeroes = zeroes - zero_sum_l[i-1] - zero_sum_r[j-1]
        subarr_ones = ones - one_sum_l[i-1] - one_sum_r[j-1]
        if closest_ady_num_r[i-1] < j-1 or closest_ady_num_l[j-1] >= i-1:
            extra_cost = 0
        else:
            extra_cost = 1
        
        if subarr_zeroes % 3 != 0 or subarr_ones % 3 != 0:
            print(-1)
        else:
            print((j-i+1)//3 + extra_cost)
