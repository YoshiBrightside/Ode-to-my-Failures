white = list(map(int, raw_input().split()))
black1 = list(map(int, raw_input().split()))
black2 = list(map(int, raw_input().split()))

bl_b1 = white[0]>=black1[0] and white[0]<=black1[2] and white[1]>=black1[1] and white[1]<=black1[3]
br_b1 = white[0]>=black1[0] and white[0]<=black1[2] and white[3]>=black1[1] and white[3]<=black1[3]
ul_b1 = white[2]>=black1[0] and white[2]<=black1[2] and white[1]>=black1[1] and white[1]<=black1[3]
ur_b1 = white[2]>=black1[0] and white[2]<=black1[2] and white[3]>=black1[1] and white[3]<=black1[3]

bl_b2 = white[0]>=black2[0] and white[0]<=black2[2] and white[1]>=black2[1] and white[1]<=black2[3]
br_b2 = white[0]>=black2[0] and white[0]<=black2[2] and white[3]>=black2[1] and white[3]<=black2[3]
ul_b2 = white[2]>=black2[0] and white[2]<=black2[2] and white[1]>=black2[1] and white[1]<=black2[3]
ur_b2 = white[2]>=black2[0] and white[2]<=black2[2] and white[3]>=black2[1] and white[3]<=black2[3]

pointsb1=int(bl_b1)+int(br_b1)+int(ul_b1)+int(ur_b1)
pointsb2=int(bl_b2)+int(br_b2)+int(ul_b2)+int(ur_b2)

if pointsb1>=3 or pointsb2>=3:
    print('NO')
    quit()
if not ((bl_b1 or bl_b2) and (br_b1 or br_b2) and (ul_b1 or ul_b2) and (ur_b1 or ur_b2)):
    #print((bl_b1 or bl_b2), (br_b1 or br_b2), (ul_b1 or ul_b2), (ur_b1 or ur_b2))
    print('YES')
    quit()
if bl_b1 and br_b1 and ul_b2 and ur_b2:
    print('NO') if black1[2]>=black2[0] else 'YES'
    quit()
if bl_b2 and br_b2 and ul_b1 and ur_b1:
    print('NO') if black2[2]>=black1[0] else 'YES'
    quit()
if bl_b1 and ul_b1 and br_b2 and ur_b2:
    print('NO') if black1[4]>=black2[1] else 'YES'
    quit()
if bl_b2 and ul_b2 and br_b1 and ur_b1:
    print('NO') if black1[4]>=black2[1] else 'YES'
    quit()



