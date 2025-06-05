n = int(input())
times = list(map(int, input().split()))
times.sort()
current_sum = 0
count = 0
for t in times:
    if current_sum <= t:
        count += 1
        current_sum += t
print(count)