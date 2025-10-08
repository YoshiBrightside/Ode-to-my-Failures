# 2152B
# Catching the Krug
'''
We calculate the distance between Doran and the furthest walls in Krug's direction
If Krug and Doran share the same row or column, just check furthest wall in Krug's direction
'''

test_cases: int = int(input())
for _ in range(test_cases):
    map_size, krug_x, krug_y, dor_x, dor_y = list(map(int, input().split()))
    x_moves, y_moves = 1, 1
    if krug_x != dor_x:
        if krug_x < dor_x:
            # krug is to the left of dorian
            x_moves = dor_x
        else:
            # krug is to the right of dorian
            x_moves = map_size - dor_x
    if krug_y != dor_y:
        if krug_y < dor_y:
            # krug is north of dorian
            y_moves = dor_y
        else:
            # krug is south of dorian
            y_moves = map_size - dor_y
    print(max(x_moves, y_moves))

