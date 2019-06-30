# 1187C
# Letters Shop

letteresLen = int(input())
letters = str(input())
friendsLen = int(input())
friends = [''] * friendsLen
for x in range(friendsLen):
    friends[x] = input()
lettersLeft = {}

for friend in friends:
    if friend+' total' not in lettersLeft:
        lettersLeft[friend+' total']=len(friend)
    for char in friend:
        if char not in lettersLeft:
            lettersLeft[char] = friend
        elif friend not in lettersLeft[char].split(' '):
            lettersLeft[char]+= ' '+friend
        if friend+' '+char in lettersLeft:
            lettersLeft[friend+' '+char]+=1
        else:
            lettersLeft[friend+' '+char]=1

for i in range(len(letters)):
    if letters[i] not in lettersLeft:
        continue
    words = lettersLeft[letters[i]].split(' ')
    # print(lettersLeft[letters[i]]+' '+str(i))
    for word in words:
        # print(word+' '+str(i))
        # Theres optimization here by removing the word from the dict
        if lettersLeft[word+' '+letters[i]]>0:
            lettersLeft[word+' '+letters[i]]-=1
            lettersLeft[word+' total']-=1
            if lettersLeft[word+' total']==0:
                lettersLeft[word+' ans']=i+1

for friend in friends:
    print(lettersLeft[friend+' ans'])
            
