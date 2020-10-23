universities = {}
for _ in range(int(input())):
  if len(universities) > 11:
    break
  uni_and_team = input().split()
  if not universities.get(uni_and_team[0]):
    universities[uni_and_team[0]] = 1
    print(uni_and_team[0], uni_and_team[1])
    