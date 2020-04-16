_ = raw_input()
string = raw_input()
ones, zeroes, ans = len(string.split('n'))-1, len(string.split('z'))-1, ''
for i in range(ones):
    ans+='1 '
for i in range(zeroes):
    ans+='0 '
if len(ans) > 0:
    print(ans[:-1])
else:
    print('0')