# this is incomplete, done in Java by Rodrigo

aux = input()
l_games, l_score, r_games, r_score = 0, 0, 0 ,0
left_serve = True
for c in aux:
    if c == 'Q':
        ans = []
        ans.append(str(l_games))
        if l_games > 1:
            ans.append('(winner)')
        else:
            ans.append(str(l_score))
            if left_serve:
                ans.append('*)')
        continue
    if c == 'S':
        l_score += left_serve
        r_score += 1 - left_serve
    else:
        r_score += left_serve
        l_score += 1 - left_serve
        left_serve = bool(left_serve - 1)
    if (abs(l_score - r_score) > 1 and (l_score > 4 or r_score > 4)) or (l_score > 9 or r_score > 9):
        if l_score > r_score: l_games += 1
        else: r_games += 1
        l_score, r_score = 0, 0
