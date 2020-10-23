aux = int(input())
while (aux != 0):
  list1 = [0] * aux
  list2 = [0] * len(list1)
  for i in range(len(list1)):
      list1[i] = int(input())
  for i in range(len(list2)):
      list2[i] = int(input())
  list1_2 = sorted(list1)
  list2.sort()
  correspondance = {}
  for i, v in enumerate(list1_2):
      correspondance[v] = list2[i]
  for i, v in enumerate(list1):
      print(correspondance[v])
  print()
  aux = int(input())
