# 1189A
# Keanu Reeves

stringlen = int(input())
string = str(input())
if len(string)%2==1 or len(string.split('0'))!= len(string.split('1')):
    print('1')
    print(string)
else:
    print('2')
    print(string[0]+' '+string[1:])