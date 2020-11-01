from itertools import permutations
if __name__ == '__main__':
	chain= str(input())
	validos=set()
	per= [''.join(p) for p in permutations(chain)]
	for e in per:
		if e[0]=="1":
			validos.add(e)
	print(int(len(validos)))


