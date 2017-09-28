ls = [0]*10001
length = input()
costs = map(int,raw_input().split())
for i in costs:
    ls[i] += 1
search = 0
ans = 0
while (len(ls) > search):
    if ls[search] > 0:
        ans +=1
        search +=4
    search += 1
print ans
