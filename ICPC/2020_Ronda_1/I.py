
numbers = {'1':1 , '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}
sym = {'.':1, '#':1, '$':1, '%':1, '/':1, '(':1, '&':1, ')':1}
low = {'a':'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f', 'g':'g', 'h':'h', 'i':'i',
        'j':'j', 'k':'k', 'l':'l', 'm':'m', 'n':'n', 'o':'o', 'p':'p', 'q':'q', 'r':'r',
        's':'s', 't':'t', 'u':'u', 'v':'v', 'w':'w', 'x':'x', 'y':'y', 'z':'z'}
upp = {'A':'A', 'B':'B', 'C':'C', 'D':'D', 'E':'E', 'F':'F', 'G':'G', 'H':'H', 'I':'I',
        'J':'J', 'K':'K', 'L':'L', 'M':'M', 'N':'N', 'O':'O', 'P':'P', 'Q':'Q', 'R':'R',
        'S':'S', 'T':'T', 'U':'U', 'V':'V', 'W':'W', 'X':'X', 'Y':'Y', 'Z':'Z'}
for a in range(int(input())):
    pswd = input()
    r_low, r_upp, r_num, r_2num, r_spc, r_10l = False, False, False, False, False, 9 < len(pswd)
    for c in range(len(pswd)):
        if sym.get(pswd[c]):
            r_spc = True
        elif numbers.get(pswd[c]) or pswd[c] == '0':
            r_num = True
            if (c+1 < len(pswd) and (numbers.get(pswd[c+1]) or pswd[c+1] == '0') and
                abs(numbers[pswd[c]]-numbers[pswd[c+1]]) == 1):
                r_2num = True
        elif upp.get(pswd[c]) and upp[pswd[c]] == pswd[c]:
            r_upp = True
        elif low.get(pswd[c]) and low[pswd[c]] == pswd[c]:
            r_low = True
    count = sum([r_low, r_upp, r_num and not r_2num, r_spc, r_10l])
    if count == 5:
        ans = 'Strong'
    elif count == 4:
        ans = 'Good'
    elif count == 3:
        ans = 'Weak'
    else:
        ans = 'Rejected'
    print('Assertion number #', a+1, ': ', ans, sep='')
