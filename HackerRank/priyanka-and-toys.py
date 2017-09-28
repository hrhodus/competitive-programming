ls = [0]*10001
length = input()
assert 1 <= length <= 10**5
costs = map(int,raw_input().split())
for i in costs:
    ls[i] += 1
    assert(0<= i <= 10**4)
i = 0
ans = 0
while (i < len(ls)):
    if ls[i] > 0:
        ans +=1
        i +=4
    i += 1
print ans    
