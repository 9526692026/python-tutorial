from collections import Counter

s = "aabbbccde"
count = Counter(s)
top =count.most_common()
top.sort(key=lambda x: (-x[1], x[0]))
for char, count in top[:3]:
    print(f"{char} {count}")
