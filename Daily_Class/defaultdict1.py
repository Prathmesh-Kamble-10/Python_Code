from collections import defaultdict

n, m = map(int, input().split())
groupA = defaultdict(list)

for i in range(1, n + 1):
    word = input()
    groupA[word].append(i)

for _ in range(m):
    word = input()
    if word in groupA:
        print(*groupA[word])
    else:
        print(-1)


'''
STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b


Sample Output

1 2 4
3 5

'''