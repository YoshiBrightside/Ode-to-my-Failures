# 1191B
# Tokitsukaze and Mahjong

tiles = list(map(str,input().split(' ')))
repeated, sucesion = 0, 0
repeated+=1 if (tiles[0]==tiles[1]) else 0
repeated+=1 if (tiles[1]==tiles[2]) else 0
repeated+=1 if (tiles[2]==tiles[0]) else 0
sucesion+=1 if (abs(int(tiles[0][0])-int(tiles[1][0]))==1 and tiles[0][1]==tiles[1][1]) else 0
sucesion+=1 if (abs(int(tiles[1][0])-int(tiles[2][0]))==1 and tiles[1][1]==tiles[2][1]) else 0
sucesion+=1 if (abs(int(tiles[2][0])-int(tiles[0][0]))==1 and tiles[2][1]==tiles[0][1]) else 0
if ((sucesion == 0) and
    ((abs(int(tiles[0][0])-int(tiles[1][0]))==2 and tiles[0][1]==tiles[1][1])) or
    ((abs(int(tiles[1][0])-int(tiles[2][0]))==2 and tiles[1][1]==tiles[2][1])) or
    ((abs(int(tiles[2][0])-int(tiles[0][0]))==2 and tiles[2][1]==tiles[0][1]))):
    sucesion+=1
repeated = 2 if repeated==3 else repeated
sucesion = 1 if sucesion==2 and repeated==1 else sucesion
sucesion = 2 if sucesion==3 else sucesion
print(2-max(repeated,sucesion))
