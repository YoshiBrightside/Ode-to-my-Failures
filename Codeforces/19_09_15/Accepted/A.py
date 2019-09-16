#1215A
#Yellow Cards

team_players1 = int(raw_input())
team_players2 = int(raw_input())
max_cards1 = int(raw_input())
max_cards2 = int(raw_input())
cards = int(raw_input())
ans1 = cards - (team_players1*(max_cards1-1)+team_players2*(max_cards2-1))
ans1 = 0 if ans1 < 0 else ans1
if max_cards1 > max_cards2:
    aux = team_players1
    team_players1 = team_players2
    team_players2 = aux
    aux = max_cards1
    max_cards1 = max_cards2
    max_cards2 = aux
ans2 = min(team_players1, cards//max_cards1)
cards -= max_cards1*ans2
ans2 = min(ans2+team_players2, ans2+(cards//max_cards2))
print(str(ans1)+' '+str(ans2))