'''
2155B
Abraham's Great Escape

You can make a maza with exactly k starting cells to escape, as lonmg as k is
different than n^2 - 1. This is because you can't loop with only 1 cell.
'''

test_cases: int = int(input())
for _ in range(test_cases):
    n, k =  list(map(int, input().split()))
    if k == n**2 - 1:
        print('NO')
        continue
    print('YES')

    # Now we build a sample maze
    bad_cells = n**2 - k
    for i in range(n):
        if bad_cells >= n:
            print('R'*(n-1), 'L', sep='')
            bad_cells -= n
        elif bad_cells:
            if i == 0:
                print('R'*(bad_cells-1), 'L', 'D'*(n-bad_cells), sep='')
            else:
                print('U'*bad_cells, 'D'*(n-bad_cells), sep='')
            bad_cells -= bad_cells
        else:
            print('D'*n)
