'''
2145A
Candies for Nephews
'''

test_cases: int = int(input())
for _ in range(test_cases):
    candy = int(input())
    if candy%3==0:
        print(0)
    else:
        print(3-candy%3)